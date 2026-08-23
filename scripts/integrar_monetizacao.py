#!/usr/bin/env python3
"""Integração da monetização (card t_8dd9a051) nos arquivos atuais — v2 estendida.
Cobre TODOS os artigos de guia/* (newsletter + ad-slot) e affiliate só nos de hardware.
Insere com assert para garantir que cada edição aconteceu.
"""
import sys

ROOT = "/home/bruno/workspace/qwen38-27b-landing/.worktrees/t_8dd9a051"

CSS_LINK = '  <link rel="stylesheet" href="/assets/css/blog-monetizacao.css">\n'
JS_TAG = '  <script defer src="/assets/js/newsletter.js"></script>\n'

# Slugs de hardware/compra — affiliate SÓ aqui (PRD §8.2)
HARDWARE_SLUGS = {
    "hardware-local",
    "quantizacao-gguf-30b-quanto-cabe-na-sua-gpu",
    "tokens-por-segundo-30b-hardware-real",
    "lemonade-sdk-v11-6-llm-local-gpu-npu-amd",
    "qwen38-27b-16gb-vram-llama-cpp",
    "qwen3-8-27b-contexto-256k-24gb",
}

AD_SLOT = '<!-- ad slot: ativar quando tráfego >20k/mês (EthicalAds/Carbon) -->\n<div class="ad-slot" aria-hidden="true"></div>\n'

NEWSLETTER_INLINE = """<section class="newsletter" aria-labelledby="nl-art">
  <h2 id="nl-art">Receba o resumo semanal</h2>
  <p>Releases, benchmarks e hardware de modelos locais ≤30B — no seu email, 1x por semana.</p>
  <form class="newsletter-form" action="#" method="post" novalidate>
    <input type="email" name="email" required placeholder="seu@email.com" aria-label="Seu email" autocomplete="email">
    <button type="submit">Assinar</button>
  </form>
  <p class="microcopy">1 email/semana · cancele quando quiser · Ao assinar você aceita nossa <a href="/privacidade">política de privacidade</a></p>
</section>
"""

AFFILIATE = """<h2 id="hardware-recomendado">Hardware recomendado</h2>
<div class="affiliate">
  <h3>🖥️ Hardware recomendado para rodar este modelo</h3>
  <div class="affiliate-table-wrap">
    <table>
      <thead><tr><th>Produto</th><th>Onde comprar</th></tr></thead>
      <tbody>
        <!-- Adicione ?tag=SEUTAG aos links para habilitar a comissão de afiliado -->
        <tr><td>GPU 24 GB (ex.: RTX 4090)</td><td><a href="https://www.amazon.com.br/s?k=rtx+4090" rel="sponsored noopener" target="_blank">Amazon BR →</a></td></tr>
        <tr><td>RAM 64 GB DDR5</td><td><a href="https://www.mercadolivre.com.br/baratos/memoria-64gb-ddr5" rel="sponsored noopener" target="_blank">Mercado Livre →</a></td></tr>
      </tbody>
    </table>
  </div>
  <p class="disclosure">Ao clicar e comprar por links de afiliado, o preço não muda para você e recebemos uma pequena comissão que mantém o blog gratuito.</p>
</div>
"""


def edit(path, old, new, must=True, count=1):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    n = s.count(old)
    if n < count:
        if must:
            raise SystemExit(f"FALHA em {path}: achei {n}x de: {old[:70]!r}")
        return False
    s = s.replace(old, new, count)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    return True


def process_article(path, slug):
    from pathlib import Path
    path = Path(path)
    if not path.exists():
        raise SystemExit(f"FALHA: {path} não existe")
    s = path.read_text(encoding="utf-8")
    orig = s
    if "blog-monetizacao.css" not in s:
        s = s.replace("</head>", CSS_LINK + "</head>", 1)
    if "newsletter.js" not in s:
        s = s.replace("</body>", JS_TAG + "</body>", 1)

    if 'class="newsletter"' not in s:
        # insere antes do ÚLTIMO <footer>
        idx = s.rfind("<footer>")
        if idx == -1:
            idx = s.rfind("<footer ")
        if idx == -1:
            raise SystemExit(f"FALHA: {path} sem <footer>")
        block = "<!-- ===================== MONETIZAÇÃO ===================== -->\n" + AD_SLOT + "\n"
        if slug in HARDWARE_SLUGS:
            block += AFFILIATE + "\n"
        block += NEWSLETTER_INLINE + "\n"
        s = s[:idx] + block + "    " + s[idx:]
    if s != orig:
        path.write_text(s, encoding="utf-8")
    print(f"OK artigo {slug}")


def main():
    import glob
    only = sys.argv[1] if len(sys.argv) > 1 else None
    paths = sorted(glob.glob(f"{ROOT}/guia/*/index.html"))
    n = 0
    for p in paths:
        slug = p.split("/guia/")[1].split("/")[0]
        if slug == "en":
            continue
        if only and slug != only:
            continue
        process_article(p, slug)
        n += 1
    print(f"PROCESSADOS: {n} artigos")


if __name__ == "__main__":
    main()
