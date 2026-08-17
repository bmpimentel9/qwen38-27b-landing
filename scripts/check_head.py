#!/usr/bin/env python3
"""
scripts/check_head.py — Gate anti-regressão de head (RF2 do PRD t_5ce82346)

Varre HTMLs publicáveis e verifica:
  C1 google-site-verification presente com content = token do index.html
  C2 nenhum placeholder SEU_TOKEN_DE_VERIFICACAO_AQUI
  C3 G-016TVX8LEE (GA4) presente (exceto 404.html)
  C4 rel=canonical presente
  C5 sitemap ↔ arquivos: todo <loc> resolve em arquivo, todo HTML (exceto 404) está no sitemap

Exit 1 se qualquer check falhar.
--json para saída parseável (CI futuro).

Uso:
  python3 scripts/check_head.py
  python3 scripts/check_head.py --json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree

REPO = Path(__file__).resolve().parent.parent

SKIP_PREFIXES = ('.git/', '.claude/', 'templates/')

META_GSC_RE = re.compile(
    r'<meta\s+name="google-site-verification"\s+content="([A-Za-z0-9_-]{40,60})"\s*/?>'
)
PLACEHOLDER_RE = re.compile(r'SEU_TOKEN_DE_VERIFICACAO_AQUI')
GA4_RE = re.compile(r'G-016TVX8LEE')
CANONICAL_RE = re.compile(r'rel="canonical"')


def find_html_files() -> list[Path]:
    htmls = []
    for f in sorted(REPO.rglob('*.html')):
        rel = f.relative_to(REPO).as_posix()
        if any(rel.startswith(p) for p in SKIP_PREFIXES):
            continue
        htmls.append(f)
    return htmls


def get_reference_token(htmls: list[Path]) -> str | None:
    """Extrai o token do index.html (fonte da verdade — D6)."""
    index = REPO / 'index.html'
    if index not in htmls:
        return None
    m = META_GSC_RE.search(index.read_text(encoding='utf-8'))
    return m.group(1) if m else None


def parse_sitemap() -> set[str]:
    """Retorna set de caminhos normalizados (ex: /guia/faq, /modelos) do sitemap."""
    sitemap = REPO / 'sitemap.xml'
    if not sitemap.exists():
        return set()
    tree = ElementTree.parse(sitemap)
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    locs: set[str] = set()
    for loc in tree.findall('.//sm:loc', ns):
        if not loc.text:
            continue
        url = loc.text.strip()
        # Extrai path da URL
        path = url.replace('https://qwen38-27b-landing.vercel.app', '')
        path = '/' + path.lstrip('/')
        locs.add(path)
    return locs


def html_path_to_url_path(html_path: Path) -> str:
    """Converte path de arquivo para URL (cleanUrls: / → index.html, .html → sem extensão)."""
    rel = html_path.relative_to(REPO).as_posix()
    if rel == 'index.html':
        return '/'
    if rel.endswith('/index.html'):
        return '/' + rel[:-len('/index.html')]
    if rel.endswith('.html'):
        return '/' + rel[:-len('.html')]
    return '/' + rel


def run_checks(htmls: list[Path], json_output: bool) -> dict:
    """Executa C1-C5 e retorna dict de resultados."""
    results = {
        'files_checked': len(htmls),
        'checks': {},
        'files': {},
        'passed': True,
    }

    token = get_reference_token(htmls)
    sitemap_urls = parse_sitemap()

    # C1 — GSC meta
    c1_fails = []
    for html in htmls:
        text = html.read_text(encoding='utf-8')
        m = META_GSC_RE.search(text)
        rel = html.relative_to(REPO).as_posix()
        if not m:
            c1_fails.append(f'{rel}: sem meta google-site-verification')
        elif token and m.group(1) != token:
            c1_fails.append(f'{rel}: token diverge do index.html ({m.group(1)[:6]}…)')

    results['checks']['C1_gsc_meta'] = {
        'desc': 'google-site-verification com content = token do index.html',
        'status': 'PASS' if not c1_fails else 'FAIL',
        'failures': c1_fails,
    }
    if c1_fails:
        results['passed'] = False

    # C2 — placeholder
    c2_fails = []
    for html in htmls:
        text = html.read_text(encoding='utf-8')
        if PLACEHOLDER_RE.search(text):
            rel = html.relative_to(REPO).as_posix()
            c2_fails.append(rel)

    results['checks']['C2_no_placeholder'] = {
        'desc': 'nenhum SEU_TOKEN_DE_VERIFICACAO_AQUI em *.html',
        'status': 'PASS' if not c2_fails else 'FAIL',
        'failures': c2_fails,
    }
    if c2_fails:
        results['passed'] = False

    # C3 — GA4 (exceto 404.html)
    c3_fails = []
    for html in htmls:
        rel = html.relative_to(REPO).as_posix()
        if rel == '404.html':
            continue  # 404 não tem gtag por design
        text = html.read_text(encoding='utf-8')
        if not GA4_RE.search(text):
            c3_fails.append(rel)

    results['checks']['C3_ga4'] = {
        'desc': 'G-016TVX8LEE presente (exceto 404.html)',
        'status': 'PASS' if not c3_fails else 'FAIL',
        'failures': c3_fails,
    }
    if c3_fails:
        results['passed'] = False

    # C4 — canonical
    c4_fails = []
    for html in htmls:
        text = html.read_text(encoding='utf-8')
        if not CANONICAL_RE.search(text):
            rel = html.relative_to(REPO).as_posix()
            c4_fails.append(rel)

    results['checks']['C4_canonical'] = {
        'desc': 'rel=canonical presente',
        'status': 'PASS' if not c4_fails else 'FAIL',
        'failures': c4_fails,
    }
    if c4_fails:
        results['passed'] = False

    # C5 — sitemap ↔ arquivos
    c5_fails = []
    # Todo <loc> resolve em arquivo?
    for url_path in sitemap_urls:
        # Converte URL path para arquivo no repo
        if url_path == '/':
            file_path = REPO / 'index.html'
        elif url_path.endswith('/'):
            file_path = REPO / url_path.lstrip('/') / 'index.html'
        else:
            # Pode ser /modelos -> modelos.html, ou /guia/faq -> guia/faq/index.html
            candidate1 = REPO / (url_path.lstrip('/') + '.html')
            candidate2 = REPO / url_path.lstrip('/') / 'index.html'
            if candidate1.exists():
                file_path = candidate1
            else:
                file_path = candidate2

        if not file_path or not file_path.exists():
            c5_fails.append(f'sitemap:{url_path} → nenhum arquivo encontrado')

    # Todo HTML (exceto 404) está no sitemap?
    for html in htmls:
        rel = html.relative_to(REPO).as_posix()
        if rel == '404.html':
            continue
        url_path = html_path_to_url_path(html)
        if url_path not in sitemap_urls:
            c5_fails.append(f'arquivo:{rel} → URL {url_path} não está no sitemap')

    results['checks']['C5_sitemap_files'] = {
        'desc': 'sitemap ↔ arquivos: todo <loc> resolve, todo HTML (exceto 404) no sitemap',
        'status': 'PASS' if not c5_fails else 'FAIL',
        'failures': c5_fails,
    }
    if c5_fails:
        results['passed'] = False

    return results


def main():
    parser = argparse.ArgumentParser(description='Gate anti-regressão de head')
    parser.add_argument('--json', action='store_true', help='saída JSON')
    args = parser.parse_args()

    htmls = find_html_files()
    results = run_checks(htmls, json_output=args.json)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(f'check_head.py — Gate anti-regressão (t_d36048c1)')
        print(f'Arquivos verificados: {results["files_checked"]}')
        print()
        for ck, data in results['checks'].items():
            icon = '✅' if data['status'] == 'PASS' else '❌'
            print(f'  {icon} {ck}: {data["desc"]}')
            print(f'      Status: {data["status"]}')
            if data['failures']:
                for f in data['failures'][:5]:
                    print(f'      → {f}')
                if len(data['failures']) > 5:
                    print(f'      … e mais {len(data["failures"]) - 5}')
            print()
        print(f'Resultado: {"✅ TODOS PASS" if results["passed"] else "❌ FALHAS ENCONTRADAS"}')
        print()

    sys.exit(0 if results['passed'] else 1)


if __name__ == '__main__':
    main()