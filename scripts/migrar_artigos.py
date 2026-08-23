#!/usr/bin/env python3
"""
scripts/migrar_artigos.py — Migra os artigos de guia/* para o template único
(templates/artigo.html) + design system compartilhado (assets/css/blog.css).

Card t_0a2d3a4f · PRD §5/§10.3.

O QUE FAZ por artigo:
  1. Preserva o <head> EXATO: title, description, keywords, canonical, OG,
     twitter, article:*, JSON-LD, GA4. Remove apenas o <style> inline.
  2. Injeta <link blog.css> + <script blog.js defer>.
  3. Substitui header/nav manual pelo HEADER GLOBAL (templates/header.html).
  4. Substitui footer manual pelo FOOTER GLOBAL (templates/footer.html).
  5. Monta o esqueleto do template: breadcrumb → article-head (h1+meta+lead)
     → TOC sticky → corpo preservado → prev/next → relacionados → compartilhar.
  6. Preserva a URL /guia/<slug> e o canonical (assert de igualdade).
  7. Adiciona BlogPosting + BreadcrumbList no JSON-LD (aditivo, sem remover
     FAQPage/HowTo/TechArticle existentes).
  8. Normaliza classes legadas: callout-warn → callout warn.

O corpo é preservado por fatiamento de STRING (não re-serialização do bs4),
garantindo que o conteúdo original não sofra normalização de formatação.

NÃO FAZ (outras cards): newsletter/affiliate/ad (t_8dd9a051),
home/archive/header-footer-sync (t_c3a93c3e).

Uso:
  python3 scripts/migrar_artigos.py            # migra todos
  python3 scripts/migrar_artigos.py --check    # só valida, não escreve
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
GUIAS = ROOT / "guia"
HEADER = (ROOT / "templates" / "header.html").read_text(encoding="utf-8")
FOOTER = (ROOT / "templates" / "footer.html").read_text(encoding="utf-8")
INDEX = json.loads((ROOT / "assets" / "js" / "blog-index.json").read_text(encoding="utf-8"))

CAT_ANCHOR = {
    "Guias": "guias", "Benchmarks": "benchmarks", "Hardware": "hardware",
    "Releases": "releases", "Comunidade": "comunidade",
}
CAT_BADGE = {
    "Guias": "guides", "Benchmarks": "bench", "Hardware": "hw",
    "Releases": "releases", "Comunidade": "community",
}
CAT_COLOR = {
    "Guias": "#A78BFA", "Benchmarks": "#2DD4BF", "Hardware": "#4ADE80",
    "Releases": "#F5B841", "Comunidade": "#3B82F6",
}
AUTHOR = "Bruno Pimentel"
SITE = "https://qwen38-27b-landing.vercel.app"

INDEX_BY_SLUG = {e["slug"]: e for e in INDEX}

CANON_RE = re.compile(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']')
CANON_RE2 = re.compile(r'<link[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']')


def get_canonical(html: str) -> str | None:
    m = CANON_RE.search(html) or CANON_RE2.search(html)
    return m.group(1) if m else None


def readtime_words(html_body: str) -> int:
    text = re.sub(r"<[^>]+>", " ", html_body)
    text = re.sub(r"\s+", " ", text)
    words = len(text.split())
    return max(1, round(words / 200))


def get_meta(soup: BeautifulSoup, prop_or_name: str) -> str | None:
    m = soup.find("meta", attrs={"property": prop_or_name}) or soup.find(
        "meta", attrs={"name": prop_or_name}
    )
    if m and m.get("content") is not None:
        return str(m["content"])
    return None


def build_toc(body: str) -> str:
    """Gera <nav class=toc> a partir dos h2/h3 com id do corpo (string bruta)."""
    items = []
    for m in re.finditer(r"<h([23])([^>]*)>(.*?)</h\1>", body, re.S):
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        idm = re.search(r'id=["\']([^"\']+)["\']', attrs)
        if not idm:
            continue
        label = re.sub(r"<[^>]+>", " ", inner)
        label = re.sub(r"\s+", " ", label).strip()
        cls = ' class="sub"' if tag == "3" else ""
        items.append(f'<li{cls}><a href="#{idm.group(1)}">{label}</a></li>')
    if not items:
        return ""
    lis = "\n            ".join(items)
    return (
        '<nav class="toc" aria-label="Nesta página">\n'
        "          <h4>Nesta página</h4>\n"
        f"          <ul>\n            {lis}\n          </ul>\n"
        "        </nav>"
    )


def prev_next(slug: str, all_sorted: list[dict]) -> tuple[dict | None, dict | None]:
    idx = next((i for i, e in enumerate(all_sorted) if e["slug"] == slug), None)
    if idx is None:
        return None, None
    return (all_sorted[idx - 1] if idx > 0 else None,
            all_sorted[idx + 1] if idx < len(all_sorted) - 1 else None)


def related(slug: str, category: str, all_sorted: list[dict], n: int = 3) -> list[dict]:
    same = [e for e in all_sorted if e["slug"] != slug and e.get("category") == category]
    others = [e for e in all_sorted if e["slug"] != slug and e.get("category") != category]
    return (same + others)[:n]


def pn_html(pn: dict | None, direction: str) -> str:
    if not pn:
        return ""
    label = "← Anterior" if direction == "prev" else "Próximo →"
    cls = "pn-card" + ("" if direction == "prev" else " next")
    return (
        f'<a class="{cls}" href="/guia/{pn["slug"]}">'
        f'<div class="dir">{label}</div><div class="t">{pn["title"]}</div></a>'
    )


def related_card_html(e: dict) -> str:
    cat = e.get("category") or "Guias"
    badge = CAT_BADGE[cat]
    color = CAT_COLOR[cat]
    mono = re.sub(r"[^A-Za-z0-9]", "", e["slug"])[:6].upper() or "ART"
    title = e["title"]
    return (
        f'<a class="post-card" href="/guia/{e["slug"]}">\n'
        f'  <div class="post-thumb-fallback" style="background:linear-gradient(135deg,{color}33,{color}11);color:{color};font-size:1rem"><span>{mono}</span></div>\n'
        f'  <div class="post-body"><div class="post-meta"><span class="badge-cat {badge}">{cat}</span></div><h3>{title}</h3></div>\n'
        "</a>"
    )


def blogposting_jsonld(slug: str, title: str, date_iso: str, desc: str) -> str:
    data: dict = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": desc,
        "author": {"@type": "Person", "name": AUTHOR},
        "publisher": {"@type": "Organization", "name": AUTHOR},
        "mainEntityOfPage": f"{SITE}/guia/{slug}",
        "image": f"{SITE}/og-image.png",
        "inLanguage": "pt-BR",
    }
    if date_iso:
        date = date_iso[:10]
        data["datePublished"] = date
        data["dateModified"] = date
    return json.dumps(data, ensure_ascii=False)


def breadcrumb_jsonld(cat: str, slug: str, title: str) -> str:
    anchor = CAT_ANCHOR.get(cat, "guias")
    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": cat, "item": f"{SITE}/guia/#{anchor}"},
                {"@type": "ListItem", "position": 3, "name": title, "item": f"{SITE}/guia/{slug}"},
            ],
        },
        ensure_ascii=False,
    )


def extract_block(txt: str, start_marker: str, end_tag: str) -> tuple[str, int, int]:
    """Extrai bloco de <start_marker...> até o </end_tag> correspondente (sem aninhamento de tag)."""
    start = txt.find(start_marker)
    if start == -1:
        return "", -1, -1
    end_m = re.search(rf"</{end_tag}>", txt[start:])
    if not end_m:
        return "", -1, -1
    end = start + end_m.end()
    return txt[start:end], start, end


def find_top_tables(body: str) -> list[tuple[int, int]]:
    """Ranges [start,end) das <table> de nível superior (não aninhadas)."""
    ranges: list[tuple[int, int]] = []
    depth = 0
    open_pos = -1
    i = 0
    n = len(body)
    while i < n:
        if body.startswith("<table", i):
            if depth == 0:
                open_pos = i
            depth += 1
            i += 6
        elif body.startswith("</table>", i):
            depth -= 1
            if depth == 0 and open_pos != -1:
                ranges.append((open_pos, i + 8))
                open_pos = -1
            i += 8
        else:
            i += 1
    return ranges


def wrap_tables(body: str) -> str:
    """Envolve tabelas cruas em <div class=\"table-wrap\"> (PRD §5.4: scroll
    horizontal em mobile). Pula tabelas já dentro de .table-wrap. Só a tabela
    mais externa recebe o wrapper (aninhadas seguem intactas)."""
    ranges = find_top_tables(body)
    if not ranges:
        return body
    out: list[str] = []
    prev = 0
    for s, e in ranges:
        out.append(body[prev:s])
        chunk = body[s:e]
        prefix = body[:s]
        already = (
            "class=\"table-wrap\"" in prefix
            and prefix.rfind("class=\"table-wrap\"") > prefix.rfind("</div>")
        )
        out.append(chunk if already else '<div class="table-wrap">' + chunk + "</div>")
        prev = e
    out.append(body[prev:])
    return "".join(out)


def migrate(path: Path, dry: bool, verbose: bool = False) -> list[str]:
    problems = []
    rel = path.relative_to(ROOT).as_posix()
    slug = rel.split("/")[1]
    html = path.read_text(encoding="utf-8")
    canonical = get_canonical(html)
    if not canonical:
        problems.append(f"{rel}: SEM canonical")
        return problems

    # ---------- parse leve (head + metadata) ----------
    soup = BeautifulSoup(html, "html.parser")
    head = soup.head
    title = (soup.title.get_text(strip=True) if soup.title else "") or slug
    title = re.sub(r"\s*\|\s*Blog Modelos Locais\s*$", "", title).strip()
    desc = get_meta(soup, "description") or ""
    date_iso = get_meta(soup, "article:published_time") or get_meta(soup, "datePublished") or ""
    lang = (soup.html.get("lang") if soup.html else None) or "pt-BR"
    idx = INDEX_BY_SLUG.get(slug)
    # data: meta do artigo primeiro; fallback índice; nunca inventar data.
    if not date_iso and idx and idx.get("date"):
        date_iso = idx["date"]
    category = (idx or {}).get("category") or get_meta(soup, "article:section") or "Guias"

    # h1 do header antigo
    h1_el = soup.body.find("h1") if soup.body else None
    h1_text = h1_el.get_text(" ", strip=True) if h1_el else title
    lead_el = soup.body.find("p", class_="lead") if soup.body else None
    lead = lead_el.get_text(" ", strip=True) if lead_el else (idx or {}).get("lead", "")

    # ---------- CORPO preservado por fatiamento de string ----------
    body_open = html.find("<body")
    body_close = html.rfind("</body>")
    if body_open == -1 or body_close == -1:
        problems.append(f"{rel}: sem <body>")
        return problems
    body_inner = html[body_open:body_close]

    # remove o <header>...</header> antigo (header + nav + h1 + lead)
    _, hs, he = extract_block(body_inner, "<header", "header")
    if hs == -1:
        problems.append(f"{rel}: sem <header> antigo")
        return problems
    body_inner = body_inner[:hs] + body_inner[he:]

    # remove o <div class="toc">...</div> antigo
    toc_start = body_inner.find('<div class="toc">')
    if toc_start == -1:
        m = re.search(r'<div class=["\']toc["\']>', body_inner)
        toc_start = m.start() if m else -1
    if toc_start != -1:
        depth = 0
        i = toc_start
        while i < len(body_inner):
            if body_inner.startswith("<div", i):
                depth += 1
                i += 4
            elif body_inner.startswith("</div>", i):
                depth -= 1
                if depth == 0:
                    body_inner = body_inner[:toc_start] + body_inner[i + 6:]
                    break
                i += 6
            else:
                i += 1

    # remove o <footer>...</footer> antigo
    _, fs, fe = extract_block(body_inner, "<footer", "footer")
    if fs != -1:
        body_inner = body_inner[:fs] + body_inner[fe:]

    # remove <nav> remanescente (nav manual que sobrou fora do header)
    body_inner = re.sub(r"<nav[^>]*>.*?</nav>", "", body_inner, flags=re.S)

    # remove comentários de borda do doctype
    body_inner = body_inner.replace("<body>", "").replace("<body ", "")

    # normaliza classes legadas
    body_inner = body_inner.replace('class="callout-warn"', 'class="callout warn"')
    body_inner = body_inner.replace("class=callout-warn", 'class="callout warn"')

    body_html = body_inner.strip()
    # PRD §5.4: tabelas cruas → .table-wrap (scroll horizontal em mobile)
    body_html = wrap_tables(body_html)

    # ---------- head novo por cirurgia de STRING (preserva bytes EXATOS) ----------
    head_open = html.find("<head")
    head_close = html.find("</head>")
    if head_open == -1 or head_close == -1:
        problems.append(f"{rel}: sem <head>")
        return problems
    raw_head = html[head_open:head_close]
    raw_head = re.sub(r"<style.*?</style>", "", raw_head, flags=re.S)
    # injeta css + js antes de </head>
    raw_head += (
        '\n  <link rel="stylesheet" href="/assets/css/blog.css">\n'
        '  <script src="/assets/js/blog.js" defer></script>'
    )
    # PRD §5.1: garante article:modified_time quando há published_time (aditivo)
    if date_iso and "article:modified_time" not in raw_head:
        raw_head += f'\n  <meta property="article:modified_time" content="{date_iso[:10]}">'
    existing_types = " ".join(
        s.get_text() for s in head.find_all("script", type="application/ld+json")
    )
    add = ""
    if "BlogPosting" not in existing_types:
        add += f'\n  <script type="application/ld+json">\n  {blogposting_jsonld(slug, h1_text or title, date_iso, desc)}\n  </script>'
    if "BreadcrumbList" not in existing_types:
        add += f'\n  <script type="application/ld+json">\n  {breadcrumb_jsonld(category, slug, h1_text or title)}\n  </script>'
    raw_head += add
    head_html = raw_head + "</head>"

    # ---------- TOC / prevnext / related / share ----------
    toc_html = build_toc(body_html)

    all_entries = [
        {**e, "date": e.get("date") or e.get("datePublished") or ""}
        for e in INDEX_BY_SLUG.values()
    ]
    all_entries.sort(key=lambda e: (e["date"] or "", e["slug"]))
    prev, nxt = prev_next(slug, all_entries)
    rels = related(slug, category, all_entries)

    readtime = (idx or {}).get("readTime") or readtime_words(body_html)

    date_vis = ""
    if date_iso:
        try:
            d = datetime.fromisoformat(date_iso[:10])
            meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
            date_vis = f"{d.day} {meses[d.month - 1]} {d.year}"
        except Exception:
            date_vis = date_iso[:10]
    else:
        date_vis = "ago 2026"
    badge = CAT_BADGE.get(category, "guides")
    anchor = CAT_ANCHOR.get(category, "guias")

    prev_html = pn_html(prev, "prev")
    nxt_html = pn_html(nxt, "next")
    prevnext_html = ""
    if prev or nxt:
        prevnext_html = (
            '        <h2 id="prevnext">Continue por aqui</h2>\n'
            f'        <div class="prevnext">\n          {prev_html}\n          {nxt_html}\n        </div>'
        )
    related_html = ""
    if rels:
        cards = "\n          ".join(related_card_html(r) for r in rels)
        related_html = (
            '        <section aria-labelledby="rel-title">\n'
            '          <h2 class="section-title" id="rel-title" style="margin-top:var(--space-7)">Artigos relacionados</h2>\n'
            f'          <div class="related-grid">\n            {cards}\n          </div>\n'
            "        </section>"
        )
    copy_url = f"{SITE}/guia/{slug}"
    copy_html = (
        f'<a href="{copy_url}" data-copy-link '
        "onclick=\"if(navigator.clipboard){event.preventDefault();var b=this;"
        "navigator.clipboard.writeText(this.href).then(function(){"
        "b.textContent='Copiado!';setTimeout(function(){b.textContent='Copiar link';},2000);});}\">"
        "Copiar link</a>"
    )
    share_html = (
        '        <div class="share">\n'
        "          <span>Compartilhar:</span>\n"
        f'          <a href="https://twitter.com/intent/tweet?url={SITE}/guia/{slug}">X</a>\n'
        f'          <a href="https://www.linkedin.com/sharing/share-offsite/?url={SITE}/guia/{slug}">LinkedIn</a>\n'
        f'          <a href="https://wa.me/?text={SITE}/guia/{slug}">WhatsApp</a>\n'
        f"          {copy_html}\n"
        "        </div>"
    )

    header_frag = HEADER.strip()
    footer_frag = FOOTER.strip()

    new_html = f"""<!DOCTYPE html>
<html lang="{lang}" data-theme="dark">
{head_html}
<body>
<!-- @@HEADER@@ -->
{header_frag}
<!-- @@/HEADER@@ -->

  <main id="topo" class="container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="/">Home</a><span class="sep">›</span><a href="/guia/#{anchor}">{category}</a><span class="sep">›</span><span aria-current="page">{h1_text}</span>
    </nav>

    <article>
      <header class="article-head">
        <h1>{h1_text}</h1>
        <div class="article-meta">
          <span class="badge-cat {badge}">{category}</span>
          <span class="sep">·</span><span class="author">{AUTHOR}</span>
          <span class="sep">·</span><time datetime="{date_iso[:10]}">{date_vis}</time>
          <span class="sep">·</span><span>{readtime} min de leitura</span>
        </div>
        <p class="article-lead">{lead}</p>
      </header>

      <div class="article-layout">
        {toc_html}

        <div class="article-body">
          <img class="article-thumb" src="/og-image.png" alt="{h1_text}" width="1200" height="630" loading="eager">

{body_html}

          {prevnext_html}

          {related_html}

          {share_html}
        </div><!-- /.article-body -->
      </div><!-- /.article-layout -->
    </article>
  </main>

<!-- @@FOOTER@@ -->
{footer_frag}
<!-- @@/FOOTER@@ -->
</body>
</html>
"""

    new_canonical = get_canonical(new_html)
    if not new_canonical or new_canonical != canonical:
        problems.append(f"{rel}: canonical mudou ({canonical} → {new_canonical})")
    if "<style" in new_html:
        problems.append(f"{rel}: ainda contém <style>")

    if not dry:
        path.write_text(new_html, encoding="utf-8")
    if verbose:
        print(f"  {rel}: ok (cat={category}, rt={readtime}, prev={prev and prev['slug']}, next={nxt and nxt['slug']})")
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="só valida, não escreve")
    ap.add_argument("--only", help="migra apenas este slug")
    args = ap.parse_args()

    targets = []
    for idx_html in sorted(GUIAS.glob("*/index.html")):
        rel = idx_html.relative_to(ROOT).as_posix()
        if rel == "guia/index.html" or "guia/en/" in rel:
            continue
        targets.append(idx_html)
    if args.only:
        targets = [t for t in targets if t.relative_to(ROOT).as_posix().split("/")[1] == args.only]

    all_problems = []
    ok_count = 0
    for t in targets:
        problems = migrate(t, dry=args.check, verbose=True)
        if problems:
            all_problems.extend(problems)
        else:
            ok_count += 1

    print(f"\nMigrados OK: {ok_count}/{len(targets)}  (dry={'SIM' if args.check else 'não'})")
    if all_problems:
        print("PROBLEMAS:")
        for p in all_problems:
            print("  ✗", p)
        sys.exit(1)
    print("TODOS OK")


if __name__ == "__main__":
    main()
