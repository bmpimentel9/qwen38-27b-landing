# 📜 CHANGELOG — Projeto SEO Local Models 30B

> Formato baseado em [Keep a Changelog](https://keepachangelog.com/).
> Este projeto segue [Versionamento Semântico](https://semver.org/).

---

## [0.1.0] — 2026-08-15

### Added
- Projeto `seo-local-models-30b` criado no Hermes
- Board kanban vinculado ao projeto
- Repositório clonado em `~/qwen38-27b-landing`
- Seções do portal: Modelos, Hardware, Benchmarks, Guia Rápido
- CSS compartilhado em `assets/css/portal.css`
- Template de artigo em `templates/template-artigo.md`
- Navegação responsiva com hamburguer menu
- GA4 tracking real (G-016TVX8LEE) instalado
- Pipeline de evolução diária: cron 7h pesquisa → card kanban → artigo → deploy
- Agente Arquivista (`arquivista`) criado para documentação

### Changed
- Index.html: título atualizado para "Portal de Modelos Locais de 30B"
- Nav da home: links corrigidos para cleanUrls (`/modelos`, `/hardware`, `/guia`)
- Meta tags e OG tags melhoradas
- Vercel.json: cleanUrls true, headers de segurança e cache
- Integração com PRs do time SEO (guia completo, sitemap, robôs, FAQ)

### Fixed
- Menu sumia em telas <900px → hamburguer com dropdown adicionado
- Links `modelos.html` → `modelos` (redirect 308 do cleanUrls)

### Removed
- GA4 placeholder G-QWEN3827B → substituído pelo ID real

---

[0.1.0]: https://qwen38-27b-landing.vercel.app
## [2026-08-15]


### Added
- [Correção R1] Performance Lighthouse + a11y — Portal 30B (QA FAIL) (seo-tech)
- [Correção R2] JS quebrado na home (querySelector('/guia')) + meta desc + README — Portal 30B (seo-tech)
- Correção [QA FAIL]: re-target Qwen3.8-27B + integrar/publishar artigos no portal (seo-content)
- Correção QA: remover aggregateRating fabricado + completar 9 benchmarks no llms.txt (seo)
- [QA] Validar: Content Strategy & Artigos — Portal 30B (qa)
- [QA] Validar: Tech SEO & Performance — Portal 30B (qa)
- [QA] Validar: [Correção R1] Performance Lighthouse + a11y — Portal 30B (QA (qa)
- [QA] Validar: Correção [QA FAIL]: re-target Qwen3.8-27B + integrar/publish (qa)
- [QA] Validar: SEO Audit & Schema — Qwen3.8-27B Landing (qa)
- [QA] Validar: [Correção R2] JS quebrado na home (querySelector('/guia')) + (qa)
- [QA] Validar: Correção QA: remover aggregateRating fabricado + completar 9 (qa)
- SEO Audit & Schema — Qwen3.8-27B Landing (seo)
- Content Strategy & Artigos — Portal 30B (seo-content)
- Tech SEO & Performance — Portal 30B (seo-tech)
- 📊 GA4: Analytics & Dashboard — Qwen3.8 Landing (atlas)
- 🌅 Daily Content 15/08 — modelos locais ≤30B (discovery)
- GA4: instala tag real G-016TVX8LEE (propriedade QWEN38-27B-LANDING 549987691)
- Merge remote-tracking branch 'origin/main'

### Fixed
- fix(nav): menu responsivo com hamburguer + corrige links para cleanUrls
- fix(seo): remover aggregateRating fabricado do JSON-LD + completar 26 benchmarks no llms.txt (QA t_251e9f6c)
- fix(R2): scrollspy SyntaxError (/guia nao-hash), meta desc 152 chars, README GA4