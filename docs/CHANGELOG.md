# Changelog

Registro de mudanças do projeto **Qwen3.8-27B landing page / Portal de
Modelos Locais de 30B**.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
ordem reversa (mais recente primeiro). Datas em ISO `YYYY-MM-DD`.

---


## [2026-08-15] — Atualização diária

### Added
- `docs/team/PLAYBOOK.md` — metodologia de operação do time Hermes
  (`f14a0e0`, arquivista).
- Compilação do board `seo-local-models-30b`: 24 tasks concluídas em
  2026-08-15 — correções R1/R2 (performance, a11y, SEO), 2 artigos do dia,
  nav consistente com cleanUrls, GSC e as respectivas validações QA.
  Detalhes nas entradas "[2026-08-15]" acima; registro completo no board.

*(Entry gerada automaticamente pelo job das 20h e curada pelo Arquivista.)*

---

## [2026-08-15] — Fix: referências de benchmark sem fonte oficial substituídas pelas colunas reais do model card

### Fixed
- **Landing, guia de benchmarks, llms.txt e FAQ** (`t_6dd8d927` — seo-content):
  referências de "fronteira" que citavam modelos/valores inexistentes no model
  card (GPT-5.6 Sol, Opus 4.8, Opus 5, Qwen3.8-Max 86,1/74,8) substituídas pelas
  colunas oficiais do card: **Qwen3.7-Plus · Muse Glimmer-30B · Opus 4.6 Max**.
- `index.html`: barras dos gráficos (Opus 4.8→4.6 Max 78,2; GPT-5.6 Sol→Qwen3.7-Plus
  64,0/57,6/14,2; Opus 5→Opus 4.6 Max 53,4; + barra OSWorld Opus 4.6 Max 72,7);
  tabela de 26 benchmarks com colunas v3.6 preenchidas (36,2/70,3/87,8/24,0/69,1/
  85,1/89,4/78,4/84,1/28,9/62,5/45,0/42,6) e referências reais nas 26 linhas;
  legendas e caption atualizados ("Referências do model card").
- `guia/benchmarks-comparativos/`: 3 tabelas + parágrafos narrativos recalculados
  (GPQA "próximo de" → distâncias reais 1,1/2,1 pts; OSWorld/CoWorkBench claims).
- `llms.txt` (l.49 e resumo) e `guia/faq/` (pergunta vs ChatGPT) realinhados.
- Regra do projeto reafirmada: toda referência de benchmark deve ter linha
  correspondente no model card — zero termos proibidos, 26/26 refs verificadas,
  deltas aritméticos conferidos (26 no index, 40 no guia).

---

## [2026-08-15] — Artigos do dia: Muse Glimmer 30B + tabela GGUF, e navegação consistente

### Added
- **2 artigos do dia** (`188ba96`, task `t_7ab9d2fd` — seo-content + discovery):
  - *Muse Glimmer 30B* (`/guia/muse-glimmer-30b-agente-local`) — 29,6B denso
    Apache 2.0 multimodal para agentes locais 24/7; benchmarks oficiais vs
    Gemma4-31B/Qwen3.6-27B + cruzamento honesto com o Qwen3.8-27B nos 4
    benchmarks comuns.
  - *Tabela real de quantização GGUF ≤30B*
    (`/guia/quantizacao-gguf-30b-quanto-cabe-na-sua-gpu`) — GB medidos via
    HF API (Qwen3.8-27B vs Muse Glimmer), IQ2 a Q8, mmproj, drafter, GPU
    por tier.
  - GA4 (`G-016TVX8LEE`) + `scroll_depth` nas 2 novas páginas; JSON-LD
    (TechArticle + SoftwareApplication/FAQPage + BreadcrumbList); 2 cards
    no índice do `/guia`; 2 URLs no sitemap; seções novas no `llms.txt`.
- **Links dos 5 artigos do `/guia` na home** (`40cef50`).
- **Página 404 com links internos** para modelos, hardware, benchmarks e
  guia (`5b462e7`).

### Fixed
- **Navegação consistente em todo o portal** — cleanUrls em todas as páginas
  do portal e menu hambúrguer mobile (<900px) nas 4 páginas do portal
  (`40cef50`, `da6a636`; PRs #5 e #6, task `t_72542ef7`).
- **Acessibilidade do menu hambúrguer** — `aria-expanded`, `aria-label` e
  `type="button"` no `nav-toggle` das 4 páginas do portal (`0f2fa61`).

---

## [2026-08-15] — Consolidação da documentação em `docs/`

### Changed
- Documentação consolidada em `docs/`: os `CHANGELOG.md`, `HISTORICO.md` e
  `ROADMAP.md` da raiz foram mesclados para cá (conteúdo único preservado) e
  substituídos na raiz por stubs de redirecionamento. ADR-004 marcado como
  superado pelo ADR-007 (GA4 real). CHANGELOG completado com os commits que
  faltavam de 2026-08-15. A versão `0.1.0` que vivia na raiz foi absorvida
  pelas entradas por data.
  *(Arquivista — task kanban `t_2e42bec9`)*

---

## [2026-08-15] — Correções R1/R2, GA4 real, portal e Search Console

### Added
- **GA4 real instalado** — Measurement ID `G-016TVX8LEE` (propriedade
  QWEN38-27B-LANDING, ID 549987691), substituindo o ID placeholder
  `G-QWEN3827B` que tinha sido removido no `d554f7c`. Tag async com
  `anonymize_ip:true`; enhanced measurement do stream (page_view, scroll,
  click_outbound, file_download, site_search, video_*) + eventos custom
  `scroll_depth` (25/50/75/100%) e helper `qwenTrackSearch()`.
  (`7afed08` — task "GA4: Analytics & Dashboard", agente atlas)
- **Verificação do Google Search Console** — meta tag
  `google-site-verification` em todas as páginas + `GSC_SETUP.md` com o
  passo a passo; sitemap expandido com as 6 URLs do guia como entradas
  individuais. (`d256ec3`, PR #4 — task kanban `t_65295f98`)
- **Portal de modelos locais** — seções Modelos, Hardware, Benchmarks e
  Guia Rápido; CSS compartilhado em `assets/css/portal.css`; template de
  artigo em `templates/template-artigo.md`. (`45dcb1a`)
- **Menu responsivo com hambúrguer** para telas <900px. (`0bbb4a8`)
- Agente **Arquivista** (Hermes) responsável pela documentação contínua, e
  rotina `~/.hermes/scripts/daily_doc.py` que compila tasks concluídas no
  CHANGELOG (agendada diariamente às 20h no perfil do Arquivista).

### Fixed
- **Scrollspy `SyntaxError` na home** — `document.querySelector('/guia')`
  usava seletor inválido (href com barra); navegação destacava seção errada
  e gerava erro no console. (`ffb0c3c`)
- **`aggregateRating` fabricado removido do JSON-LD** — reviewCount 397 e
  ratingValue 4,8 não correspondiam a fonte real (risco de penalização
  manual do Google por rich snippet enganoso). `llms.txt` completado com os
  26 benchmarks do model card. (`4f4dbb5` — QA `t_251e9f6c`)
- **Menu sumia em telas <900px** — o CSS escondia o nav sem alternativa;
  adicionado botão ☰ com dropdown flutuante, e links corrigidos para
  cleanUrls (`/modelos` em vez de `modelos.html`, que sofria redirect 308).
  (`0bbb4a8`)
- Meta description da home encurtada para 152 caracteres (limite 155 do
  Google). (`ffb0c3c`)

### Changed
- Título da home atualizado para "Portal de Modelos Locais de 30B";
  `vercel.json` com `cleanUrls: true` e headers de segurança/cache.
  (`45dcb1a`, `0bbb4a8`)

---

## [2026-08-15] — Estrutura de documentação inicial

### Changed
- **PLAYBOOK.md 0.1.0 → 0.2.0** (revisão semanal do Arquivista, com base em
  dados reais do sistema): seção 2.1 agora lista `Sentinela` e nomeia os perfis
  reais (`product-owner`, `qa`, …) com os crons que os acionam
  (`product-owner-morning` 06:00, `daily-research-30b` 07:00,
  `arquivista-daily-doc` 20:00, `sentinel-audit`, `auto-cura-hermes`);
  seção 4.1 corrige o caminho do playbook (`docs/team/PLAYBOOK.md`, não
  `docs/TEAM-PLAYBOOK.md`) e o mantenedor (Arquivista, semanal); seção 5.1
  corrige a sintaxe do `hermes cron create` (schedule e prompt são posicionais);
  seção 7 ganha snapshot real de 2026-08-15 (24 tasks/dia, retrabalho QA 37,5%,
  2 cards bloqueados <24h).
  *(Arquivista — task kanban `t_158f6aba`)*

### Added
- Pasta `docs/` com documentação estruturada do projeto: `README.md`,
  `CHANGELOG.md`, `HISTORICO.md`, `DECISIONS.md`, `ROADMAP.md`.
  `README.md` da raiz atualizado com seção "Documentação" apontando para
  `docs/`. *(Arquivista — task kanban `t_f56140db`, commit `17d8439`)*

---

## [2026-08-15] — Performance, acessibilidade e SEO finos

### Changed
- **Font stack de sistema** substitui Google Fonts (render-blocking). Antes o
  LCP ficava em 4,8s por causa do carregamento síncrono das fontes Inter e
  JetBrains Mono; agora zero requisições externas de fonte, stack
  `system-ui` + `ui-monospace`.
- Contraste de texto melhorado para WCAG AA: `--fg-3` dark `#6f6f6f` → `#8b8b8b`
  (3,94:1 → 5,81:1); `--fg-3` light `#8f8f8f` → `#767676` (3,23:1 → 4,54:1).
- Ordem de headings corrigida: `h4` no rodapé → `p.foot-title` (não quebra a
  sequência `h1`–`h3`).
- Meta description encurtada: 239 → 152 caracteres (≤ 155, limite do Google).

### Added
- `og-image.png` 1200×630 gerado do `og-image.svg` para Open Graph/Twitter Card.
- `robots.txt` com allowlist explícita para GPTBot, ClaudeBot, PerplexityBot e
  20+ crawlers de IA.
- `sitemap.xml` com URL principal, `lastmod` e `changefreq`.
- `llms.txt` com conteúdo estruturado para crawlers de LLM (GEO).
- `manifest.json` — PWA manifest com ícone SVG, theme color e categorias.
- `404.html` — página 404 customizada com design consistente.
- `vercel.json` — caching headers (assets imutáveis 1 ano), security headers,
  8 redirects.
- JSON-LD enriquecido: `TechArticle` + `BreadcrumbList` + `FAQPage` (4 Q&As).
- `noscript` — fallback acessível para usuários sem JS.

### Fixed
- Mojibake corrigido no relatório anexado.
- Três trechos residuais em inglês traduzidos para pt-BR: "Quantizações
  day-zero" → "no lançamento"; "GGUF de 4 bits (Unsloth, day-zero)" → "no dia do
  lançamento"; meta description "open-weight" → "de pesos abertos".
- Três citações da comunidade perdidas no redesign restauradas, agora
  traduzidas. Página volta a ter as 15 originais.
- `IFBench` exibia seta "↑" como placeholder — valor real 79,5 preenchido.
- Classe CSS `hero` (cabeçalho) colidia com `td.n.hero` (células de destaque),
  herdando `padding:76px` e desalinhando colunas. Renomeada para `n lead`.

### Removed
- **GA4 placeholder removido** (ID `G-QWEN3827B` era falso, não coletava
  dados). *Reinstalado horas depois com ID real — ver a entrada
  "[2026-08-15] — Correções R1/R2..." acima e o ADR-007.* (`d554f7c`)

---

## [2026-08-14] — Landing page inicial e redesign Geist

### Added
- Página informativa (não oficial) sobre o lançamento dos pesos abertos do
  **Qwen3.8-27B** (14/08/2026): especificações, 26 benchmarks do model card,
  requisitos de hardware, throughput medido em máquina real e recepção da
  comunidade.
- Seção "Medido nesta máquina": decode em platô térmico (400 tokens/rodada,
  9 rodadas) no ASUS ROG Flow Z13 (Strix Halo, Radeon 8060S, 128 GB unificados)
  com Ollama sobre Vulkan — 10,6 tok/s no Qwen3.8-27B denso (Q5_K_M) contra
  56,6 tok/s no Qwen3.6-35B MoE.
- Redesign sobre o design system **Geist** (Vercel): superfícies neutras,
  hairlines de 1px, raio 8/12px, tema claro e escuro com alternância manual
  persistida em `localStorage`.
- Barra de navegação fixa com destaque da seção atual via `IntersectionObserver`.
- Paleta de gráficos validada por script: cor por função (violeta = Qwen3.8,
  laranja = fronteira proprietária, cinza = geração anterior), ΔE CVD ≥ 8,
  contraste ≥ 3:1.
- Marcos semânticos, link de pular para o conteúdo, foco visível, `aria-pressed`
  nos filtros, `aria-current` na navegação, `prefers-reduced-motion` respeitado.
- Meta tags Open Graph e Twitter, canonical, `theme-color` por esquema,
  JSON-LD `schema.org/TechArticle`.
- Comandos prontos para Ollama, llama.cpp e vLLM, cada um com botão de copiar.
- Deploy automático na Vercel conectado ao repositório (`main` = produção).

### Changed
- De 11 para 26 benchmarks na tabela — todos os resultados do model card oficial.
- Arquitetura detalhada: 64 camadas no padrão 16 × (3 × Gated DeltaNet →
  1 × Gated Attention), contagem de heads e dimensões.
- Nova seção multimodal com nove métricas próprias da torre de visão.
- Página afirmava "thinking-only" — corrigido para documentar os dois modos
  (thinking: temp 1.0 / top_p 0.95; instruct: temp 0.7 / top_p 0.80 /
  presence_penalty 1.5).
