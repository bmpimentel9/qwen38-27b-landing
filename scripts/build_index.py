#!/usr/bin/env python3
"""
scripts/build_index.py — Gera assets/js/blog-index.json (fonte de dados do blog)
e os blocos HTML de cards do feed (home + /guia/) a partir dos artigos reais.

Fonte de verdade: guia/*/index.html (og:title, meta description, published_time, tags).
Sem build, sem dependência externa (ADR-001). Zero-build: roda na hora do PR.

Saídas:
  assets/js/blog-index.json   — índice completo (busca + prev/next + relacionados)
  assets/js/feed-home.html    — cards HTML dos 6 recentes + destaque + 5 categorias
                                (importado manualmente no index.html; crawlable, sem JS)

Mapeamento categoria (BIND-04 do PRD):
  Guias · Benchmarks · Hardware · Releases · Comunidade
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GUIA = REPO / "guia"
OUT_JSON = REPO / "assets" / "js" / "blog-index.json"
# Fragmento dos cards da home vai para templates/ (SKIP_PREFIXES do check_head/sync_layout)
OUT_FEED = REPO / "templates" / "feed-home.html"

# slug -> categoria (BIND-04, autoridade do PRD)
CATEGORIA = {
    # Guias (10)
    "como-rodar": "Guias",
    "como-rodar-sglang-qwen3-8-27b": "Guias",
    "como-rodar-vllm-qwen3-8-27b": "Guias",
    "qwen3-8-27b-contexto-256k-24gb": "Guias",
    "qwen3-8-27b-lento-causas-fixes": "Guias",
    "qwen3-8-27b-reasoning-configuracao-ideal": "Guias",
    "qwen3-8-27b-uncensored-abliterated": "Guias",
    "qwen3-8-27b-visao-videos-local": "Guias",
    "minimax-music3-musica-local": "Guias",
    "ltx-2-5-video-local-comfyui": "Guias",
    "ollama": "Guias",
    # Benchmarks (7)
    "benchmarks-comparativos": "Benchmarks",
    "qwen3.8-vs-qwen3.6-27b": "Benchmarks",
    "qwen3.8-vs-qwen3-coder-30b-a3b": "Benchmarks",
    "qwen3.8-vs-ornith-1-5-35b-a3b": "Benchmarks",
    "qwen3-8-27b-benchmark-artificial-analysis": "Benchmarks",
    "quantizacao-multilingue-portugues": "Benchmarks",
    "agent-memory-leaderboard-resultados": "Benchmarks",
    "melhores-modelos-locais-30b": "Benchmarks",
    # Hardware (5)
    "hardware-local": "Hardware",
    "quantizacao-gguf-30b-quanto-cabe-na-sua-gpu": "Hardware",
    "tokens-por-segundo-30b-hardware-real": "Hardware",
    "lemonade-sdk-v11-6-llm-local-gpu-npu-amd": "Hardware",
    "qwen38-27b-16gb-vram-llama-cpp": "Hardware",
    # Releases (2)
    "muse-glimmer-30b-agente-local": "Releases",
    "1-ano-gpt-oss-modelos-locais-2026": "Releases",
    # Comunidade (2)
    "comunidade-casos-uso": "Comunidade",
    "qwen3-8-27b-veredito-comunidade-semana": "Comunidade",
}

# slug -> data manual para hubs sem article:published_time (datas de criação reais)
FALLBACK_DATE = {
    "como-rodar": "2026-08-14",
    "benchmarks-comparativos": "2026-08-15",
    "hardware-local": "2026-08-15",
    "comunidade-casos-uso": "2026-08-16",
    "qwen3.8-vs-qwen3.6-27b": "2026-08-17",
    "qwen3.8-vs-qwen3-coder-30b-a3b": "2026-08-18",
}

# slug marcado como destaque editorial (manual)
FEATURED = "qwen3-8-27b-uncensored-abliterated"

MONOGRAMAS = {
    "1-ano-gpt-oss-modelos-locais-2026": "1",
    "qwen3-8-27b-uncensored-abliterated": "UNCENSORED",
    "quantizacao-multilingue-portugues": "QU",
    "qwen3.8-vs-qwen3-coder-30b-a3b": "QW",
    "qwen3.8-vs-qwen3.6-27b": "VS",
    "melhores-modelos-locais-30b": "TOP",
    "muse-glimmer-30b-agente-local": "MG",
    "ltx-2-5-video-local-comfyui": "LTX",
    "minimax-music3-musica-local": "M3",
    "lemonade-sdk-v11-6-llm-local-gpu-npu-amd": "LM",
    "como-rodar-sglang-qwen3-8-27b": "SG",
    "como-rodar-vllm-qwen3-8-27b": "VL",
    "qwen3-8-27b-contexto-256k-24gb": "CTX",
    "qwen3-8-27b-lento-causas-fixes": "QW",
    "qwen3-8-27b-reasoning-configuracao-ideal": "RS",
    "qwen3-8-27b-visao-videos-local": "VI",
    "qwen3-8-27b-benchmark-artificial-analysis": "AA",
    "quantizacao-gguf-30b-quanto-cabe-na-sua-gpu": "GGUF",
    "tokens-por-segundo-30b-hardware-real": "t/s",
    "qwen38-27b-16gb-vram-llama-cpp": "16G",
    "agent-memory-leaderboard-resultados": "AML",
    "comunidade-casos-uso": "CC",
    "qwen3-8-27b-veredito-comunidade-semana": "VCD",
    "como-rodar": "CR",
    "benchmarks-comparativos": "BC",
    "hardware-local": "HW",
}

# slug-artigo -> slug-imagem (o nome do arquivo webp/avif em /images/).
# A maioria coincide com o slug do artigo; os dois casos abaixo têm sufixo
# -qwen3-8-27b no slug do artigo mas a imagem usa o prefixo (t_0a2d3a4f).
IMAGE_SLUG = {
    "como-rodar-sglang-qwen3-8-27b": "como-rodar-sglang",
    "como-rodar-vllm-qwen3-8-27b": "como-rodar-vllm",
}

CAT_CSS = {
    "Guias": "guides",
    "Benchmarks": "bench",
    "Hardware": "hw",
    "Releases": "releases",
    "Comunidade": "community",
}

CAT_COLOR = {
    "Guias": "#A78BFA",
    "Benchmarks": "#2DD4BF",
    "Hardware": "#4ADE80",
    "Releases": "#F5B841",
    "Comunidade": "#3B82F6",
}


def extract(path: Path) -> dict | None:
    txt = path.read_text(encoding="utf-8")
    slug = path.parent.name

    def grab(pattern: str) -> str | None:
        m = re.search(pattern, txt)
        return m.group(1).strip() if m else None

    title = grab(r'<meta property="og:title" content="([^"]+)"') or grab(r"<title>([^<]+)</title>")
    desc = grab(r'<meta name="description" content="([^"]+)"')
    pub = grab(r'<meta property="article:published_time" content="([^"]+)"')
    tags = re.findall(r'<meta property="article:tag" content="([^"]+)"', txt)

    # corpo: texto entre <main>...</main> (ou <body> como fallback p/ artigos sem <main>)
    # para estimar tempo de leitura. Remove nav/header/footer/script/style.
    mbody = re.search(r"<main[^>]*>(.*?)</main>", txt, re.S)
    if not mbody:
        mbody = re.search(r"<body[^>]*>(.*?)</body>", txt, re.S)
    body_text = mbody.group(1) if mbody else txt
    body_text = re.sub(r"<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", body_text, flags=re.S)
    body_text = re.sub(r"<[^>]+>", " ", body_text)
    words = len(body_text.split())
    read_min = max(1, round(words / 200))  # ~200 wpm pt-BR

    if not title:
        return None

    date_str = (pub or FALLBACK_DATE.get(slug) or "2026-08-14")[:10]
    return {
        "slug": slug,
        "title": title,
        "category": CATEGORIA.get(slug, "Guias"),
        "tags": tags[:6],
        "date": date_str,
        "lead": desc or "",
        "readTime": read_min,
        "featured": slug == FEATURED,
        "url": "/guia/" + slug,
    }


def rel_date(iso: str) -> str:
    d = datetime.strptime(iso, "%Y-%m-%d").date()
    delta = (date.today() - d).days
    if delta <= 0:
        return "hoje"
    if delta == 1:
        return "ontem"
    if delta < 30:
        return f"há {delta} dias"
    return d.strftime("%d %b %Y").lstrip("0").replace(" 0", " ")


def card_html(a: dict) -> str:
    """Card de artigo (.post-card) com imagem real do pack (fallback de categoria se ausente)."""
    cat_css = CAT_CSS[a["category"]]
    color = CAT_COLOR[a["category"]]
    mono = MONOGRAMAS.get(a["slug"], a["slug"][:2].upper())
    img_slug = IMAGE_SLUG.get(a["slug"], a["slug"])
    thumb = (
        f'<div class="post-thumb-wrap">'
        f'<picture class="post-thumb">'
        f'<source type="image/avif" srcset="/images/{img_slug}.avif" width="1200" height="675">'
        f'<img src="/images/{img_slug}.webp" alt="{a["title"]}" width="1200" height="675" '
        f'loading="lazy" decoding="async">'
        f'</picture>'
        f'<span class="post-thumb-fallback" style="background:linear-gradient(135deg,{color}33,{color}11);'
        f'color:{color}"><span>{mono}</span></span>'
        f'</div>'
    )
    return (
        f'<a class="post-card" href="{a["url"]}">\n'
        f"  {thumb}\n"
        f"  <div class=\"post-body\">\n"
        f"    <div class=\"post-meta\">\n"
        f'      <span class="badge-cat {cat_css}">{a["category"]}</span><span class="dot">·</span>'
        f"<time>{rel_date(a['date'])}</time><span class=\"dot\">·</span><span>{a['readTime']} min</span>\n"
        f"    </div>\n"
        f"    <h3>{a['title']}</h3>\n"
        f"    <p>{a['lead']}</p>\n"
        f"  </div>\n"
        f"</a>"
    )


def featured_html(a: dict) -> str:
    color = CAT_COLOR[a["category"]]
    cat_css = CAT_CSS[a["category"]]
    img_slug = IMAGE_SLUG.get(a["slug"], a["slug"])
    return (
        f'<a class="featured-card" href="{a["url"]}">\n'
        f'  <div class="fc-media-wrap">'
        f'<picture class="fc-media">'
        f'<source type="image/avif" srcset="/images/{img_slug}.avif" width="1200" height="675">'
        f'<img src="/images/{img_slug}.webp" alt="{a["title"]}" width="1200" height="675" '
        f'loading="eager" fetchpriority="high" decoding="async">'
        f'</picture>'
        f'<div class="post-thumb-fallback" style="background:linear-gradient(135deg,{color}33,{color}11);'
        f'color:{color};min-height:100%;border-radius:0"><span>{MONOGRAMAS.get(a["slug"], "QW")}</span></div>'
        f'</div>\n'
        f"  <div class=\"fc-body\">\n"
        f'    <div class="post-meta"><span class="badge-cat {cat_css}">{a["category"]}</span>'
        f'<span class="dot">·</span><time>{rel_date(a["date"])}</time><span class="dot">·</span>'
        f'<span>{a["readTime"]} min de leitura</span></div>\n'
        f"    <h2>{a['title']}</h2>\n"
        f"    <p>{a['lead']}</p>\n"
        f'    <span class="fc-link">Ler artigo →</span>\n'
        f"  </div>\n"
        f"</a>"
    )


def main() -> int:
    articles = []
    for d in sorted(GUIA.iterdir()):
        idx = d / "index.html"
        if not idx.exists() or d.name == "en" or d.name == "faq":
            # faq = página utilitária (BIND-02), não é artigo do feed
            continue
        a = extract(idx)
        if a:
            articles.append(a)

    if not articles:
        print("ERRO: nenhum artigo encontrado em guia/", file=sys.stderr)
        return 1

    # ordena por data desc
    articles.sort(key=lambda x: x["date"], reverse=True)
    total = len(articles)

    # --- blog-index.json ---
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(articles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # --- feed-home.html (blocos para a home) ---
    featured = next((a for a in articles if a["featured"]), articles[0])
    recentes = [a for a in articles if a["slug"] != featured["slug"]][:6]
    cats_order = ["Guias", "Benchmarks", "Hardware", "Releases", "Comunidade"]

    parts = []
    parts.append("<!-- BLOCO: Destaque (gerado por scripts/build_index.py — não editar à mão) -->")
    parts.append(featured_html(featured))
    parts.append("<!-- BLOCO: Últimos artigos -->")
    parts.append('<div class="post-grid">')
    parts.append("\n".join(card_html(a) for a in recentes))
    parts.append("</div>")
    parts.append("<!-- BLOCO: Explorar por categoria -->")
    parts.append('<div class="cat-blocks">')
    for cat in cats_order:
        items = [a for a in articles if a["category"] == cat]
        color = CAT_COLOR[cat]
        anchor = {
            "Guias": "topicos", "Benchmarks": "benchmarks-resumo", "Hardware": "memoria",
            "Releases": "topicos", "Comunidade": "topicos",
        }[cat]
        links = "".join(f'<li><a href="{a["url"]}">{a["title"]}</a></li>' for a in items[:3])
        parts.append(
            f'<div class="cat-block">\n'
            f'  <span class="cat-chip" style="background:{color}"></span>'
            f'<span class="cat-count">{len(items)} artigos</span>\n'
            f"  <h3>{cat}</h3>\n"
            f"  <ul>{links}</ul>\n"
            f'  <a href="/guia/#{anchor}" style="font-size:.8rem;font-weight:700;color:{color}">Ver todos →</a>\n'
            f"</div>"
        )
    parts.append("</div>")
    OUT_FEED.parent.mkdir(parents=True, exist_ok=True)
    OUT_FEED.write_text("\n".join(parts) + "\n", encoding="utf-8")

    counts = ", ".join(f"{c}={sum(1 for a in articles if a['category'] == c)}" for c in cats_order)
    print(f"OK: {total} artigos indexados")
    print(f"  JSON → {OUT_JSON.relative_to(REPO)}")
    print(f"  Feed → {OUT_FEED.relative_to(REPO)}")
    print(f"  Destaque: {featured['slug']} ({featured['title'][:50]}…)")
    print(f"  Categorias: {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
