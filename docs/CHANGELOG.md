# Changelog

Registro de mudanças do projeto **Qwen3.8-27B landing page**.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
ordem reversa (mais recente primeiro). Datas em ISO `YYYY-MM-DD`.

---

## [Não publicado]

### Added
- Pasta `docs/` com documentação estruturada do projeto: `README.md`,
  `CHANGELOG.md`, `HISTORICO.md`, `DECISIONS.md`, `ROADMAP.md`.
  *(Arquivista — task kanban `t_f56140db`)*

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
- `preconnect` para `googletagmanager.com`.

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
- **GA4** removido (ID placeholder `G-QWEN3827B` era falso, não coletava dados;
  reativar apenas com ID válido).

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
