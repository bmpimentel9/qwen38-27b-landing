#!/usr/bin/env python3
"""
scripts/inject_gsc_token.py — RF1 do PRD t_5ce82346

Substitui/insere a meta google-site-verification com token real nos 17 HTMLs
publicáveis e atualiza <lastmod> no sitemap.xml.

Idempotente: re-run = no-op se token já presente e igual.
Exit 1 se ao final algum HTML publicável ficar sem meta válida.

Uso:
  python3 scripts/inject_gsc_token.py --token TOKEN
  python3 scripts/inject_gsc_token.py                  # lê env GSC_TOKEN
"""

import argparse
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Diretórios/prefixos a pular (D9 do PRD)
SKIP_PREFIXES = ('.git/', '.claude/', 'templates/')

# Meta tag template (4 espaços de indentação, mesma do repo)
META_TPL = '    <meta name="google-site-verification" content="{token}" />'

# Âncora para inserção nos arquivos sem meta
INSERT_AFTER = '<meta charset="UTF-8">'

# Placeholder a substituir — linha completa
PLACEHOLDER_RE = re.compile(
    r'<meta\s+name="google-site-verification"\s+content="SEU_TOKEN_DE_VERIFICACAO_AQUI"\s*/>'
)

# Regex para detectar meta já presente (idempotência)
META_RE = re.compile(
    r'<meta\s+name="google-site-verification"\s+content="([A-Za-z0-9_-]{40,60})"\s*/?>'
)

# Regex para <lastmod> no sitemap
LASTMOD_RE = re.compile(r'(<lastmod>)(\d{4}-\d{2}-\d{2})(</lastmod>)')


def find_html_files() -> list[Path]:
    """Todos os *.html publicáveis, excluindo SKIP_PREFIXES."""
    htmls = []
    for f in sorted(REPO.rglob('*.html')):
        rel = f.relative_to(REPO).as_posix()
        if any(rel.startswith(p) for p in SKIP_PREFIXES):
            continue
        htmls.append(f)
    return htmls


def inject_token(html: Path, token: str) -> str | None:
    """Aplica a substituição/inserção. Retorna descrição da ação ou None se pulou."""
    text = html.read_text(encoding='utf-8')

    # Já tem meta com token igual? Idempotente — pula
    existing = META_RE.search(text)
    if existing:
        if existing.group(1) == token:
            return None  # já ok, no-op
        # Token diferente — substitui no lugar
        old_full = existing.group(0)
        new_full = META_TPL.format(token=token)
        text = text.replace(old_full, new_full)
        html.write_text(text, encoding='utf-8')
        return f'substituído token (era {existing.group(1)[:6]}…)'

    # Placeholder (13 arquivos)
    if PLACEHOLDER_RE.search(text):
        text = PLACEHOLDER_RE.sub(META_TPL.format(token=token), text)
        html.write_text(text, encoding='utf-8')
        return 'placeholder substituído'

    # Sem meta alguma — insere após <meta charset> (4 artigos novos)
    anchor = INSERT_AFTER
    if anchor in text:
        new_line = META_TPL.format(token=token)
        text = text.replace(anchor, anchor + '\n' + new_line)
        html.write_text(text, encoding='utf-8')
        return 'inserido após <meta charset>'

    # Não encontrou nem meta, nem placeholder, nem âncora
    return 'ERRO: sem meta, placeholder ou âncora <meta charset>'


def check_all_htmls(htmls: list[Path], token: str) -> int:
    """Exit 1 se algum HTML publicável ficou sem meta válida."""
    failures = 0
    for html in htmls:
        text = html.read_text(encoding='utf-8')
        m = META_RE.search(text)
        if not m:
            rel = html.relative_to(REPO)
            print(f'  FAIL: {rel} — sem google-site-verification')
            failures += 1
        elif m.group(1) != token:
            rel = html.relative_to(REPO)
            print(f'  FAIL: {rel} — token diverge ({m.group(1)[:6]}…)')
            failures += 1
    return failures


def update_sitemap_lastmod(token: str) -> str | None:
    """Atualiza <lastmod> para 2026-08-17 no sitemap.xml. Retorna ação."""
    sitemap = REPO / 'sitemap.xml'
    if not sitemap.exists():
        return 'sitemap.xml não encontrado'
    text = sitemap.read_text(encoding='utf-8')

    def replace_lm(m: re.Match) -> str:
        return m.group(1) + '2026-08-17' + m.group(3)

    new = LASTMOD_RE.sub(replace_lm, text)
    if new == text:
        return 'lastmod já é 2026-08-17 (no-op)'
    sitemap.write_text(new, encoding='utf-8')
    return 'lastmod atualizado para 2026-08-17'


def main():
    parser = argparse.ArgumentParser(description='Injetar token GSC real nos HTMLs')
    parser.add_argument('--token', help='Token GSC (~43 chars)')
    args = parser.parse_args()

    token = args.token or os.environ.get('GSC_TOKEN')
    if not token:
        print('ERRO: informe --token ou env GSC_TOKEN')
        sys.exit(1)

    if not re.match(r'^[A-Za-z0-9_-]{40,60}$', token):
        print(f'ERRO: token não passa validação (40-60 chars, alfanumérico+_-): {token[:10]}…')
        sys.exit(1)

    print(f'Token: {token}')
    print(f'Repositório: {REPO}')
    print()

    # 1. Injetar nos HTMLs
    htmls = find_html_files()
    print(f'HTMLs encontrados: {len(htmls)}')
    print()
    print(f'{"Arquivo":<60} {"Ação"}')
    print('-' * 75)
    actions = {}
    for html in htmls:
        rel = html.relative_to(REPO).as_posix()
        action = inject_token(html, token)
        if action:
            actions[rel] = action
            print(f'{rel:<60} {action}')
        else:
            print(f'{rel:<60} já ok (no-op)')

    print()
    print(f'Modificados: {len(actions)}')

    # 2. Verificar consistência pós-injeção
    print()
    print('Verificação pós-injeção…')
    fails = check_all_htmls(htmls, token)
    print(f'OK: {len(htmls) - fails}, FAIL: {fails}')
    if fails:
        sys.exit(1)

    # 3. Sitemap lastmod
    print()
    sm_action = update_sitemap_lastmod(token)
    print(f'Sitemap: {sm_action}')

    print()
    print('✓ Concluído.')


if __name__ == '__main__':
    main()