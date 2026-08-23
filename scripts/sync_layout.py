#!/usr/bin/env python3
"""
scripts/sync_layout.py — Sincroniza header/footer globais (PRD BIND-08)

Lê os fragmentos canônicos templates/header.html e templates/footer.html e
injeta/atualiza o bloco correspondente em todas as páginas publicáveis.

Padrão de marcação (a mesma dos templates — NÃO duplicar à mão):
  <!-- @@HEADER@@ --> ... <!-- @@/HEADER@@ -->
  <!-- @@FOOTER@@ --> ... <!-- @@/FOOTER@@ -->

O script substitui o conteúdo ENTRE os marcadores. Se a página não tem
marcadores, insere header após <body...> e footer antes de </body>.

Idempotente: re-run = no-op se o bloco já está idêntico ao template.
Exit 1 se alguma página ficar sem header/footer válido.

Uso:
  python3 scripts/sync_layout.py              # todas as páginas
  python3 scripts/sync_layout.py --dry-run    # mostra o que faria
"""

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HEADER_TPL = REPO / "templates" / "header.html"
FOOTER_TPL = REPO / "templates" / "footer.html"

SKIP_PREFIXES = (".git/", ".claude/", "templates/")

# Marcadores de bloco
HDR_OPEN = "<!-- @@HEADER@@ -->"
HDR_CLOSE = "<!-- @@/HEADER@@ -->"
FTR_OPEN = "<!-- @@FOOTER@@ -->"
FTR_CLOSE = "<!-- @@/FOOTER@@ -->"


def find_html_files() -> list[Path]:
    htmls = []
    for f in sorted(REPO.rglob("*.html")):
        rel = f.relative_to(REPO).as_posix()
        if any(rel.startswith(p) for p in SKIP_PREFIXES):
            continue
        htmls.append(f)
    return htmls


def replace_block(text: str, open_m: str, close_m: str, block: str) -> tuple[str, str]:
    """Substitui o conteúdo entre marcadores. Retorna (novo_texto, ação)."""
    pat = re.compile(re.escape(open_m) + r".*?" + re.escape(close_m), re.S)
    m = pat.search(text)
    if m:
        if m.group(0) == open_m + "\n" + block + "\n" + close_m:
            return text, "no-op"
        return pat.sub(open_m + "\n" + block + "\n" + close_m, text), "atualizado"
    return text, "ausente"


def insert_header(text: str, block: str) -> tuple[str, str]:
    """Insere header logo após <body...>."""
    m = re.search(r"<body[^>]*>", text)
    if not m:
        return text, "ERRO: sem <body>"
    if HDR_OPEN in text:
        return text, "no-op"
    pos = m.end()
    return text[:pos] + "\n" + HDR_OPEN + "\n" + block + "\n" + HDR_CLOSE + text[pos:], "inserido"


def insert_footer(text: str, block: str) -> tuple[str, str]:
    """Insere footer antes de </body>."""
    if FTR_OPEN in text:
        return text, "no-op"
    m = re.search(r"</body>", text)
    if not m:
        return text, "ERRO: sem </body>"
    pos = m.start()
    return text[:pos] + FTR_OPEN + "\n" + block + "\n" + FTR_CLOSE + "\n" + text[pos:], "inserido"


def main():
    parser = argparse.ArgumentParser(description="Sincronizar header/footer globais")
    parser.add_argument("--dry-run", action="store_true", help="apenas mostra o que faria")
    args = parser.parse_args()

    header_block = HEADER_TPL.read_text(encoding="utf-8").strip()
    footer_block = FOOTER_TPL.read_text(encoding="utf-8").strip()
    htmls = find_html_files()

    print(f"Header: {HEADER_TPL.relative_to(REPO)}")
    print(f"Footer: {FOOTER_TPL.relative_to(REPO)}")
    print(f"Páginas: {len(htmls)}")
    print()
    print(f"{'Arquivo':<52} {'Header':<11} {'Footer':<11}")
    print("-" * 76)

    changed = 0
    failures = 0
    for html in htmls:
        text = html.read_text(encoding="utf-8")
        text, h_act = replace_block(text, HDR_OPEN, HDR_CLOSE, header_block)
        text, f_act = replace_block(text, FTR_OPEN, FTR_CLOSE, footer_block)
        if h_act == "ausente":
            text, h_act = insert_header(text, header_block)
        if f_act == "ausente":
            text, f_act = insert_footer(text, footer_block)
        rel = html.relative_to(REPO).as_posix()
        if "ERRO" in h_act or "ERRO" in f_act:
            failures += 1
        if h_act != "no-op" or f_act != "no-op":
            changed += 1
            if not args.dry_run:
                html.write_text(text, encoding="utf-8")
        print(f"{rel:<52} {h_act:<11} {f_act:<11}")

    print("-" * 76)
    print(f"Alteradas: {changed} · Failures: {failures}")
    if args.dry_run:
        print("(dry-run — nada escrito)")
    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
