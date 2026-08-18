# PROJECT.md — seo-local-models-30b

> Documento mestre do projeto. Tudo 100% explicado. Atualizado: 18/08/2026.

## O que é
Portal de conteúdo sobre **LLMs locais <30B** — guias, benchmarks e comparativos para rodar modelos de linguagem em máquina própria (foco hardware AMD/Strix Halo e VRAM limitada). Dois produtos: o **portal Qwen3.8-27B** (qwen38-27b-landing) e o site **RodaLocal**.

## Status atual (18/08/2026)
- ✅ Portal no ar com guias + benchmarks completos (26 resultados oficiais publicados 18/08, PR #21)
- ✅ RodaLocal público (18/08)
- 🔄 Redações em curso: "Qwen3.8-27B no Artificial Analysis" + "guia visão/vídeo local"
- ⏳ 1 QA bloqueado (validação artigo 16GB VRAM)

## Stack
- Portal: HTML estático + assets (sem framework), Vercel serve
- RodaLocal: Astro, deploy Vercel

## Links
| O quê | URL |
|-------|-----|
| **Portal Qwen (produção)** | https://qwen38-27b-landing.vercel.app |
| **/benchmarks (novo)** | https://qwen38-27b-landing.vercel.app/benchmarks |
| **RodaLocal (produção)** | https://rodalocal.vercel.app |
| Repo portal | https://github.com/bmpimentel9/qwen38-27b-landing (privado) |
| Worktrees | `~/qwen38-27b-landing/.worktrees/` (5 branches de cards) |

## Infra Vercel
- **Portal**: projeto `qwen38-27b-landing`, deploy auto da main, GSC verificado (meta google-site-verification)
- **RodaLocal**: deploy manual via Composio 18/08 10:33, commit `fb27e635`, SSO preview-only (público desde 18/08)
- SEO: cleanUrls (sem .html), canonical, sitemap, robots

## Integrações
- GitHub ↔ Vercel (deploy contínuo)
- Google Search Console (site verification)
- Fontes de benchmarks: Qwen README HF, arXiv 2503.19786, arXiv 2508.10925 (ver SOURCES-BENCHMARKS.md)

## Dono e time
- **Decisão**: Bruno · **Operação**: Dani
- Agentes: seo-content (redação), qa (validação), growth, discovery

## Board kanban
- Board: `seo-local-models-30b` (86 done) · Projeto: `seo-local-models-30b` (1 folder)
- Pipeline padrão Discovery→PRD→Dev→QA

## Como rodar local
Portal: abrir HTML direto ou `python3 -m http.server` na raiz do clone.

## Decisões importantes
| Data | Decisão |
|------|---------|
| 18/08 | Benchmarks publicado via PR #21 (rebase limpo, QA 26/26 validado antes) |
| 18/08 | RodaLocal liberado público (SSO preview-only) |
| 18/08 | Benchmarks.html: manter TODOS os hunks da tabela em conflitos; nav/canonical padrão cleanUrls |
