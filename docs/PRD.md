# PRD — Blog de Modelos Locais: Arquitetura de Informação + Design Spec

> **Tarefa:** `t_e35424ef` · **Perfil:** discovery · **Data:** 23/08/2026
> **Pré-requisitos consumidos:** [discovery-report.md](./discovery-report.md) (benchmark de mercado) + [PLANO-BLOG.md](./PLANO-BLOG.md) (plano diretor).
> **ADRs vigentes:** [DECISIONS.md](./DECISIONS.md) — ADR-001 (estático zero-build), ADR-002 (Geist), ADR-003 (font stack de sistema), ADR-005 (Vercel auto-deploy), ADR-007 (GA4 `G-016TVX8LEE`), ADR-008 (`AIModel` no schema).

---

## 1. Objetivo e escopo

Transformar a landing `qwen38-27b-landing.vercel.app` em um **blog profissional de modelos locais (≤30B)**: feed de artigos na home, navegação por categoria, template único de artigo, design system compartilhado e trilhas de monetização instaladas — **sem quebrar nenhuma URL, canonical, sitemap, robots.txt, llms.txt nem o SEO conquistado**.

Este PRD é a **autoridade de decisão** para as fases de Design (Fase 3) e Dev (Fase 4). Todo item é acionável por quem implementa.

### Fora do escopo desta fase
- Ads de rede (EthicalAds/Carbon) — **explicitamente adiados** (gate de tráfego, ver §8.3).
- Patrocínio direto e produto pago (fases 3-4 do roadmap).
- Conteúdo novo (o blog publica via job diário; o redesenho não cria artigo).
- Migração para framework/CMS (ADR-001: HTML estático, zero build).

---

## 2. Estado atual (baseline verificado — 23/08/2026)

| Área | Hoje | Gap |
|---|---|---|
| **Home** | Landing institucional do Qwen3.8-27B (specs, benchmarks, multimodal, timeline) | Não é feed de blog; sem recência/categoria/tempo de leitura |
| **Artigos** | 26 páginas `/guia/*` (21 artigos + 5 hubs + 1 EN) com **CSS inline duplicado** por página | Sem design system compartilhado, sem template único |
| **Header/nav** | Repetido manualmente em cada artigo (Home, Guia, Benchmarks, Hardware, Como Rodar, Comunidade, FAQ) | Sem header/footer globais centralizados |
| **Cabeçalho de artigo** | `<h1>` + lead + badges | Sem **data visível**, sem tempo de leitura, sem thumbnail |
| **TOC** | `<div class="toc">` estático | Não é sticky, sem scrollspy |
| **Prev/next** | Links manuais "Continue por aqui" | Sem nav automatizada prev/next + relacionados |
| **Categorias** | Tags por cor no `/guia/` (tag-guide/bench/hw/community/faq) | Sem arquitetura de 5 categorias navegáveis |
| **JSON-LD** | TechArticle + HowTo + FAQPage por página | Pode ganhar `BlogPosting` + `BreadcrumbList` padronizado |
| **SEO** | Canonical, sitemap (31 URLs), robots, llms.txt OK | Regerar após mudanças; **não quebrar** |
| **GA4** | `G-016TVX8LEE` + `qwenTrackSearch()` definido no GA4 (helper de busca planejado) | Busca ainda não implementada no site |
| **Tráfego** | ~350 visitas/mês, bounce 71%, tempo 1m40s (GA4) | Metas ROADMAP: 1k (30d) → 5k (90d) |
| **Monetização** | Nenhuma | Newsletter + affiliate a instalar |

**Leitura:** o ativo é **conteúdo + SEO técnico**. A transformação é majoritariamente **arquitetura de informação + design system + template**, não conteúdo novo.

---

## 3. Arquitetura de Informação (nova IA)

### 3.1 Árvore do site (após redesenho)

```
/                      Home = feed do blog (+ hero compacto Qwen3.8-27B)
├── /guia/             Índice/arquivo de todos os artigos, agrupado pelas 5 categorias  ← URL preservada
│   ├── /guia/como-rodar/               Hub "Guias"            (URL preservada)
│   ├── /guia/benchmarks-comparativos/  Hub "Benchmarks"       (URL preservada)
│   ├── /guia/hardware-local/           Hub "Hardware"         (URL preservada)
│   ├── /guia/comunidade-casos-uso/     Hub "Comunidade"       (URL preservada)
│   ├── /guia/faq/                      Página utilitária FAQ  (URL preservada)
│   └── /guia/<slug>/...                21 artigos + 1 EN      (URLs preservadas)
├── /modelos           Página de modelos (existente)
├── /hardware          Página de hardware (existente)
├── /benchmarks        Página de benchmarks (existente)
├── /guia-rapido       Página guia rápido (existente)
├── /404.html, /manifest.json, /og-image.* (existentes)
└── /guia/en/...       Variante EN existente (preservada)
```

### 3.2 Decisões BIND de IA

**BIND-01 — Home vira feed de blog.** A home deixa de ser landing única do Qwen e passa a ter esta estrutura de blocos, em ordem:
1. **Nav global** (ver §4.1).
2. **Hero compacto** do Qwen3.8-27B: marca, uma linha de value prop, 4 stats-chave (27B · 262K ctx · Apache 2.0 · 52 AAI), 2 CTAs (Hugging Face, Guia). — *Preserva a identidade e o SEO da palavra-chave "Qwen3.8-27B" sem dominar a página.*
3. **"Em destaque"** — 1 card hero editorial (artigo escolhido manualmente via `data-featured` no feed JSON).
4. **"Últimos artigos"** — grid de até 6 cards recentes (por data de publicação).
5. **"Explorar por categoria"** — 5 blocos (Guias · Benchmarks · Hardware · Releases · Comunidade) com contagem de artigos e 2-3 links internos cada.
6. **Newsletter CTA** (seção completa, ver §8.1).
7. **Footer global** (ver §4.2).

As seções profundas da landing atual (specs completas, 26 benchmarks, multimodal, timeline) **saem da home** e continuam acessíveis pelas páginas existentes `/modelos`, `/benchmarks`, `/hardware`, `/guia`. O `index.html` mantém `<title>`/`description` otimizados para "Qwen3.8-27B" **e** passa a mencionar "blog de modelos locais" para capturar a segunda intenção.

**BIND-02 — Categorias canônicas = 5.** `Guias · Benchmarks · Hardware · Releases · Comunidade`. A FAQ é **página utilitária** (link no footer e no `/guia/`), **não é categoria**.

**BIND-03 — `/guia/` é o arquivo central por categoria.** O índice `/guia/` vira um único arquivo com 5 seções (uma por categoria), cada uma com seus cards. A navegação por categoria usa **âncoras** (`/guia/#guias`, `/guia/#benchmarks`, `/guia/#hardware`, `/guia/#releases`, `/guia/#comunidade`) — **sem criar URLs novas de categoria**, mantendo tudo estático, crawlável e zero-build. *Nota: quando o acervo passar de ~60 artigos, avaliar páginas de categoria dedicadas `/guia/categoria/*` — decisão adiada, não bloqueante.*

**BIND-04 — Mapeamento canônico dos 26 artigos para as 5 categorias** (autoridade; o card de cada artigo exibe a categoria + tags secundárias):

| Categoria | Artigos (`/guia/<slug>`) |
|---|---|
| **Guias** (10) | `como-rodar` (hub) · `como-rodar-sglang-qwen3-8-27b` · `como-rodar-vllm-qwen3-8-27b` · `qwen3-8-27b-contexto-256k-24gb` · `qwen3-8-27b-lento-causas-fixes` · `qwen3-8-27b-reasoning-configuracao-ideal` · `qwen3-8-27b-uncensored-abliterated` · `qwen3-8-27b-visao-videos-local` · `minimax-music3-musica-local` · `ltx-2-5-video-local-comfyui` |
| **Benchmarks** (7) | `benchmarks-comparativos` (hub) · `qwen3.8-vs-qwen3.6-27b` · `qwen3.8-vs-qwen3-coder-30b-a3b` · `qwen3-8-27b-benchmark-artificial-analysis` · `quantizacao-multilingue-portugues` · `agent-memory-leaderboard-resultados` · `melhores-modelos-locais-30b` |
| **Hardware** (5) | `hardware-local` (hub) · `quantizacao-gguf-30b-quanto-cabe-na-sua-gpu` · `tokens-por-segundo-30b-hardware-real` · `lemonade-sdk-v11-6-llm-local-gpu-npu-amd` · `qwen38-27b-16gb-vram-llama-cpp` |
| **Releases** (2) | `muse-glimmer-30b-agente-local` · `1-ano-gpt-oss-modelos-locais-2026` |
| **Comunidade** (1+FAQ) | `comunidade-casos-uso` (hub) · *(FAQ como utilitária, no footer)* |

*(A categoria Releases nasce fina — 2 artigos — e cresce organicamente com o job diário de conteúdo, que cobre lançamentos. Isso é esperado e saudável.)*

**BIND-05 — Cada artigo tem UMA categoria primária + tags secundárias livres.** A categoria primária dirige o agrupamento no `/guia/`, a cor do card e os "artigos relacionados". Tags secundárias (existentes hoje: tag-guide/bench/hw/community/faq) continuam como metadado de card e filtro futuro.

**BIND-06 — Template único de artigo (obrigatório para TODO artigo novo e migração dos existentes).** Ver §5.

**BIND-07 — Busca simples, sem backend.** Modal de busca (botão na nav global) com **índice estático** `assets/blog-index.json` (título, slug, categoria, tags, lead, data) carregado via `fetch`, filtro client-side em JS vanilla, e disparo de `qwenTrackSearch(term)` (helper já previsto no GA4). Fallback sem-JS: link "Ver todos os artigos" → `/guia/`. *Pagefind foi considerado mas descartado (gera build/artefatos — contraria ADR-001); reavaliar quando o acervo passar de ~100 artigos.*

**BIND-08 — Header/footer globais por sincronização (não por JS fetch).** Como não há build nem server-side include (ADR-001), header e footer são mantidos como **fragmentos canônicos** em `templates/header.html` e `templates/footer.html` e sincronizados por um script `scripts/sync_layout.py` (no padrão do `inject_gsc_token.py` já existente) que reescreve o bloco em todas as páginas. O `check_head.py` ganha um check extra de hash do bloco para impedir drift (ver §10). *Motivo: nav/footer são navegação primária; renderizar por JS pioraria crawlabilidade e acessibilidade.*

---

## 4. Header/footer globais

### 4.1 Header (nav) — template `templates/header.html`
- **Desktop:** `brand` (Q · Blog Modelos Locais) à esquerda; links de categoria: `Guias · Benchmarks · Hardware · Releases · Comunidade` (→ âncoras em `/guia/`) + `Modelos` + `FAQ`; à direita: botão **busca** (🔍, abre modal), botão **tema** (claro/escuro, preservar lógica atual) e CTA "Hugging Face".
- **Mobile (<900px):** hambúrguer (preservar padrão atual `.nav-toggle`), menu colapsável.
- **Sticky** no topo (padrão atual), `aria-label="Navegação principal"`, item ativo com `aria-current="true"`.
- `id="topo"` para âncoras de "voltar ao topo".

### 4.2 Footer — template `templates/footer.html`
- Coluna 1: marca + uma linha de descrição + selo "feito sem build, HTML estático".
- Coluna 2: **Navegação** (categorias + Modelos + Benchmarks + Hardware + Guia Rápido + FAQ).
- Coluna 3: **Recursos** (llms.txt · sitemap.xml · robots.txt · RSS futuro).
- Coluna 4: **Newsletter** (mini-form, ver §8.1).
- Linha final: © ano, "Portal de modelos locais de 30B", disclosure padrão de affiliate (§8.2) e link "Política de privacidade" (página nova `privacidade.html`, simples, LGPD).
- Breadcrumbs (artigos/categorias): migrar para estrutura semântica `<nav aria-label="breadcrumb">` + JSON-LD `BreadcrumbList`.

---

## 5. Template único de artigo

Arquivo de referência: `templates/template-artigo.html` (novo). **Todo artigo novo copia o template; a migração dos 26 existentes preserva o conteúdo e troca o esqueleto.** Estrutura obrigatória de cima a baixo:

### 5.1 `<head>` (idêntico em todas as páginas — gate `check_head.py`)
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="google-site-verification" content="tfpagcfTcW5Dv8rv3Rwa1rxtkKJ9qO1LCMu1zsGZdYQ">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<title>…</title>  <!-- padronizar: "Título | Blog Modelos Locais" -->
<meta name="description" content="…(≤155 chars, com dado citável)">
<link rel="canonical" href="https://qwen38-27b-landing.vercel.app/guia/<slug>">  <!-- PRESERVAR URL -->
<!-- OG/Twitter: og:type=article, og:locale=pt_BR, og:title/description/url, og:image=/og-image.png -->
<meta property="article:published_time" content="…">
<meta property="article:modified_time" content="…">
<meta property="article:section" content="<Categoria>">
<meta property="article:tag" content="…">
<link rel="stylesheet" href="/assets/css/blog.css">
<script src="/assets/js/blog.js" defer></script>
<!-- gtag GA4 G-016TVX8LEE (preservar) -->
```

### 5.2 JSON-LD (por página — padronizar para o grafo completo)
- `BlogPosting` (novo; substitui/estende `TechArticle` mantendo os campos ricos atuais: `headline`, `description`, `datePublished`, `dateModified`, `author`/`publisher` (Bruno Pimentel), `mainEntityOfPage`, `image`, `inLanguage=pt-BR`, `keywords`).
- `BreadcrumbList` (novo, padronizado: Home › Categoria › Artigo).
- `FAQPage` — **manter** nos artigos que já têm FAQ; `HowTo` — manter onde existir.
- Schema de modelo (`applicationCategory: "AIModel"` — ADR-008) preservado nos artigos de modelo.

### 5.3 Corpo visível (ordem obrigatória)

| Bloco | Conteúdo | Notas |
|---|---|---|
| **Breadcrumb** | Home › Guias › Título | `<nav aria-label="breadcrumb">` |
| **Header do artigo** | `<h1>` (único) · meta (data ISO visível + autor + categoria + **tempo de leitura**) · lead (1-2 frases) · thumbnail (imagem 1200×630, `og-image.png` por padrão, alt descritivo) | Data: `article:published_time`; exibir "19 ago 2026" |
| **Corpo** | Conteúdo original preservado | Medida ~65-75ch (ver §7.4) |
| **TOC sticky** | Lateral esquerda em desktop (≥1024px); colapsável/oculto em mobile com "Nesta página" fixo | Scrollspy (IntersectionObserver), link âncora com `scroll-margin-top` p/ nav sticky |
| **Bloco affiliate** | "Hardware recomendado para rodar este modelo" — **só** em artigos de hardware/compra | Ver §8.2 |
| **Newsletter inline** | Form compacto "Receba os lançamentos no seu email" | Ver §8.1 |
| **Prev/next** | Navegação por data/categoria: card anterior + card seguinte (título + seta) | Automatizado via índice JSON |
| **Relacionados** | 3 cards (mesma categoria primeiro, depois tags) | Automatizado via índice JSON |
| **Compartilhar** | Links X / LinkedIn / WhatsApp / copiar link (sem tracking extra) | Pequenos, no fim |
| **Footer** | Global (ver §4.2) | |

### 5.4 Elementos de corpo reutilizáveis (componentes do design system)
- `callout` (destaque com borda lateral — preservar) · `leader` ("Dado citável", já usado) · `stat-card`/`stat-row` (preservar) · `table` (com scroll horizontal em mobile) · `pre/code` (com header de linguagem opcional) · `faq-item` (acordeão leve com JS, ou estático) · `toc` · `related` · `prevnext`.

---

## 6. Design System / Design Tokens

### 6.1 Direção
**Dark-first, público dev/entusiasta, estética Geist** (ADR-002) — superfícies quase monocromáticas, hairlines de 1px, raio 8/12px, densidade de documentação. **Consolidar** os dois sistemas atuais (tokens do `index.html` + `portal.css`) em **um único** `assets/css/blog.css` com tokens por CSS custom properties. Tema claro via `[data-theme="light"]` (alternância manual preservada).

### 6.2 Tokens de cor (dark — paleta de referência)

| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#0B0E14` | Fundo da página |
| `--surface` | `#151B27` | Cards, nav, footer |
| `--surface-2` | `#1C2433` | Hover, headers de tabela |
| `--border` | `#2A3446` | Hairlines |
| `--text` | `#E8EDF6` | Texto primário |
| `--muted` | `#8C96AB` | Metadados, leads |
| `--accent` | `#2DD4BF` (cyan) | Links, CTAs, foco — *accent primário* |
| `--accent-2` | `#4ADE80` (green) | Sucesso, confirmação, "novo" |
| `--accent-3` | `#F5B841` (amber) | Avisos, badges "recente" |
| `--accent-4` | `#A78BFA` (violet) | Guias, destaque |
| `--accent-5` | `#F87171` (red) | Erro, perigo |
| `--code-bg` | `#1C2128` | Blocos de código |

- **Contraste:** todas as combinações texto/fundo ≥ AA (4.5:1 normal, 3:1 grande). Manter script de validação de contraste/daltonismo citado no ADR-002.

### 6.3 Tipografia
- **Font stack (ADR-003 — zero font externa):** `system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` para texto; `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` para números/código.
- Escala (desktop): H1 `2rem`/`2.2rem` · H2 `1.4rem` · H3 `1.1rem` · corpo `1rem` (16px) · meta/cards `0.85-0.92rem` · caption `0.78rem`. `line-height: 1.6-1.7` no corpo.

### 6.4 Espaçamento e forma
- **Escala de espaço:** `--space-1: 4px · --space-2: 8px · --space-3: 12px · --space-4: 16px · --space-5: 24px · --space-6: 32px · --space-7: 48px`. Grid de 8px.
- **Raios:** `--radius-sm: 6px · --radius-md: 8px · --radius-lg: 12px` (cards/hero).
- **Sombras:** sutis, apenas para overlays (modal, dropdown) — sem glow.
- **Layout:** container central `max-width: 1120px`; corpo de artigo `max-width: 720px` (≈65-75ch) com TOC em coluna lateral (`grid-template-columns: 240px 1fr` em ≥1024px).

### 6.5 Card de artigo (componente do feed)
```
[thumbnail 16:9]
Categoria (badge colorida) · Data relativa ("há 3 dias") · Tempo de leitura ("8 min")
Título (H3, link)
Lead (1-2 linhas, muted)
```
Grid responsivo: 3 colunas ≥1024px · 2 colunas 640-1024px · 1 coluna <640px.

### 6.6 Acessibilidade (não negociável)
Contraste AA · `prefers-reduced-motion` · skip-link (`#topo`) · foco visível (`:focus-visible`) · labels em inputs e aria em modal/menu · ordenação lógica de leitura.

---

## 7. Home — feed de blog (detalhe de implementação)

- **Destaque (featured):** 1 card grande (thumbnail grande, categoria, data, título, lead, CTA "Ler artigo"). Escolha manual: o artigo marcado `"featured": true` no índice JSON. *Sem rotação automática nesta fase.*
- **Últimos artigos:** até 6 cards, ordem por `datePublished` desc. Exibir sempre data ISO + tempo de leitura.
- **Por categoria:** 5 seções compactas (título + contagem + 2-3 links). Ao clicar na categoria, leva a `/guia/#<categoria>`.
- **Índice de dados:** `assets/blog-index.json` — array de objetos `{slug, title, category, tags[], date, lead, readTime, featured}`. **Fonte de verdade única** para home, `/guia/`, prev/next, relacionados e busca. Atualizado por script `scripts/build_index.py` (ou manual no PR) — gate `check_head.py` valida que `sitemap.xml` e `blog-index.json` não divergem dos arquivos.

---

## 8. Monetização (sem poluir a leitura)

### 8.1 Newsletter — FASE 1 (implementar agora) · plataforma: Buttondown
- **Formato:** resumo semanal "o que rolou nos modelos locais ≤30B" (releases, benchmarks, hardware). Em pt-BR; futuro EN.
- **Plataforma:** Buttondown (API-first, Markdown, grátis até 100 subs — alinhado ao espírito zero-build/OSS). Migração futura para Beehiiv se escalar (documentada no discovery, §5.1).
- **Placements (3, sem roubar o foco da leitura):**
  1. **Fim de artigo** — form inline após prev/next: título curto ("Receba o resumo semanal") + campo email + botão "Assinar" + microcopy "1 email/semana · cancele quando quiser".
  2. **Rodapé global** — mini-form na coluna 4.
  3. **Home** — seção própria entre "Por categoria" e o footer.
- **Implementação:** embed do Buttondown (`<form action="https://buttondown.com/api/emails/embed-subscribe/<user>" method="post">` + hidden `tag`) OU wrapper JS `fetch` para a API com mensagem de sucesso/erro inline. Decidir no Dev; exigência: **sem redirecionar** o leitor para fora do artigo, sem popup, sem dark pattern.
- **Privacidade (LGPD):** microcopy "Ao assinar você aceita nossa política de privacidade" + link para `privacidade.html`.

### 8.2 Affiliate de hardware — FASE 2 (implementar agora) · com disclosure
- **Onde:** fim de artigos de **Hardware** e de guias de compra/roundup (alta intenção): bloco "Hardware recomendado para rodar este modelo" com tabela curta (produto · onde comprar · link de afiliado). **Não** em artigo informativo genérico (cookie curto da Amazon 24h — só converte em intenção de compra).
- **Programas:** Amazon BR (Associates) + Mercado Livre Afiliados (padrão hardware.com.br) como início; Amazon.com/Newegg/B&H quando houver audiência global EN.
- **Disclosure obrigatório** (estilo Tecnoblog), sempre visível no bloco: *"Ao clicar e comprar por links de afiliado, o preço não muda para você e recebemos uma pequena comissão que mantém o blog gratuito."* Repetir no footer (§4.2) e na página `privacidade.html`.
- **CSS:** componente `.affiliate` no design system; `rel="sponsored noopener"` nos links (SEO/trust).

### 8.3 Ads dev-friendly — FASE 3 (NÃO implementar agora) · gate de tráfego
- **Decisão explícita:** ads fora do escopo desta fase. O tráfego atual (~350/mês) está ~140× abaixo do mínimo da EthicalAds (50k pageviews/mês) e a monetização por newsletter+affiliate cobre 100% das necessidades sem poluir.
- **Preparação mínima (custou ~zero):** definir **slots reservados em CSS** — `article .ad-slot`, `aside .ad-slot`, `home .ad-slot` — como placeholders vazios/desligados (`display:none` por padrão) com comentário HTML `<!-- ad slot: ativar quando tráfego >20k/mês (EthicalAds/Carbon) -->`. Assim, ativar ads na Fase 3 é só CSS + 1 script, sem mexer no template.
- **Política de ads:** 1 ad por página, sem tracking extra, sem interromper leitura (ÉthicalAds quando ativar).

### 8.4 Matriz de decisão (resumo)
| Canal | Nesta fase? | Quando | Onde |
|---|---|---|---|
| Newsletter (Buttondown) | ✅ Sim | Agora | Fim de artigo + footer + home |
| Affiliate Amazon/ML | ✅ Sim | Agora | Fim de artigos de hardware/compra |
| Ads (EthicalAds/Carbon) | ⛔ Não (só slots CSS) | >20-50k/mês | Slots reservados |

---

## 9. SEO — RESTRIÇÃO CRÍTICA (não quebrar)

1. **URLs intactas:** todo caminho `/guia/*`, `/modelos`, `/hardware`, `/benchmarks`, `/guia-rapido`, `/guia/en/*` permanece **exatamente** o mesmo. **Nenhum redirect necessário, nenhum 301.** Se algo precisar mudar (ex.: título de artigo), a URL fica; só o conteúdo/template muda.
2. **Canonical:** `rel="canonical"` aponta para a URL atual em **todas** as páginas (sem `www`, sem trailing slash inconsistente — manter o padrão atual).
3. **Sitemap.xml:** regerar **após** a migração incluindo todas as páginas novas (se houver) e `lastmod` atualizado. Gate: `check_head.py` C5 já valida sitemap↔arquivos; manter.
4. **Robots.txt:** inalterado (já permite crawlers de busca e de IA — GEO/AEO).
5. **llms.txt:** regerar — refletir novo título/descrição do site, manter as "citações prontas" e links de todos os artigos; adicionar seção de categorias.
6. **JSON-LD:** padronizar para `BlogPosting` + `BreadcrumbList` (mantendo FAQPage/HowTo/AIModel onde existem). **Não** remover schema existente sem substituição equivalente.
7. **GA4 `G-016TVX8LEE`:** preservar tag em todas as páginas; eventos `scroll_depth` e `qwenTrackSearch` continuam.
8. **hreflang:** o site tem variante EN (`/guia/en/`). Registrar no PRD: adicionar `<link rel="alternate" hreflang>` quando houver mais de 1 página traduzida — **decisão de escopo**: não bloquear esta fase.
9. **Meta descriptions:** padronizar ≤155 chars com dado citável (padrão já adotado).
10. **Verificação pós-deploy:** re-submeter sitemap no Search Console e validar Core Web Vitals (Lighthouse lab) — meta: manter 100/100 e LCP < 1,5s.

---

## 10. Arquitetura técnica (implementação)

### 10.1 Estrutura de arquivos (alvo)

```
assets/
  css/blog.css          ← NOVO: design system unificado (substitui portal.css e CSS inline)
  js/blog.js            ← NOVO: TOC sticky+scrollspy, menu, busca, tema, newsletter
  js/blog-index.json    ← NOVO: índice de artigos (fonte de dados)
templates/
  header.html           ← NOVO: fragmento nav global
  footer.html           ← NOVO: fragmento footer global
  template-artigo.html  ← NOVO: esqueleto de artigo único
  template-artigo.md    ← manter (referência editorial)
scripts/
  build_index.py        ← NOVO: gera blog-index.json a partir dos artigos (ou atualização manual)
  sync_layout.py        ← NOVO: injeta header/footer nas páginas (padrão inject_gsc_token.py)
  check_head.py         ← EXTENDER: + check de hash header/footer + validar blog-index ↔ sitemap
index.html              ← REMODELAR (home-feed, manter hero compacto)
guia/index.html         ← REMODELAR (arquivo por 5 categorias)
guia/*/index.html       ← MIGRAR 26 (trocar esqueleto, preservar conteúdo/URL/head gate)
privacidade.html        ← NOVO (LGPD + disclosure)
```

### 10.2 Restrições de implementação
- **Zero build, zero framework, zero dependência de runtime** (ADR-001): JS vanilla (IntersectionObserver, fetch, localStorage).
- **Nenhuma requisição externa de fonte** (ADR-003). Única dependência externa: gtag GA4 (ADR-007) + API Buttondown (newsletter).
- **Deploy:** Vercel via push em `main` (ADR-005). `vercel.json` caching/security headers inalterados.

### 10.3 Migração dos 26 artigos (procedimento)
1. Congelar o `<style>` inline de cada artigo e removê-lo (passa a usar `blog.css`).
2. Substituir nav/footer manuais pelos fragmentos globais.
3. Injetar header de artigo (data/autor/categoria/tempo de leitura) + TOC sticky + prev/next + relacionados.
4. Manter conteúdo, JSON-LD e canonical intactos.
5. Rodar `check_head.py` (gate) + verificação visual em amostra (QA cobre os 26).

---

## 11. Critérios de aceite (para QA — Fase 5)

1. **Home é feed:** destaque + recentes (com data/tempo de leitura) + 5 categorias visíveis em 1 viewport.
2. **URLs intactas:** 26/26 `/guia/*` + `/modelos` + `/hardware` + `/benchmarks` + `/guia-rapido` + EN retornam 200 com canonical próprio; nenhum redirect novo.
3. **Template único:** 26/26 artigos usam `blog.css` + esqueleto do template; zero `<style>` inline remanescente.
4. **TOC sticky** com scrollspy funcional em desktop; colapsável em mobile.
5. **Header/footer globais** idênticos em todas as páginas (hash validado pelo gate).
6. **Busca** funciona (filtra por título/categoria/tag), dispara `qwenTrackSearch`, fallback sem-JS.
7. **Newsletter** (Buttondown): form presente no fim de artigo + footer + home; assinatura não redireciona para fora.
8. **Affiliate** com disclosure visível nos artigos de hardware mapeados.
9. **Slots de ads** presentes mas desligados (`display:none`) com comentário de fase.
10. **SEO:** sitemap regerado e válido (0 erros no GSC), llms.txt regerado, robots inalterado, JSON-LD `BlogPosting`+`BreadcrumbList` presentes, GA4 tag em todas.
11. **Acessibilidade:** contraste AA, `prefers-reduced-motion`, skip-link, labels, foco visível — Lighthouse a11y ≥ 95.
12. **Performance:** Lighthouse 100/100, LCP < 1,5s (lab), zero requisição externa de fonte.
13. **Mobile (<900px):** menu hambúrguer, cards 1 coluna, tabelas com scroll.

---

## 12. Riscos e mitigação

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Quebrar SEO ao remodelar | Média | Alto | Congelar URLs; regerar sitemap/llms.txt; re-submeter GSC; gate check_head.py |
| Drift entre artigos (CSS duplicado volta) | Alta | Médio | Design system único + gate de hash header/footer + check de `<style>` inline |
| Busca/índice JSON desatualizado | Média | Médio | `build_index.py` + gate valida índice↔sitemap↔arquivos |
| Newsletter com entregabilidade baixa | Média | Médio | Buttondown (API, boas práticas); form legítimo, sem dark pattern |
| Affiliate sem intenção de compra = pouco retorno | Alta | Baixo | Aplicar só em artigos de hardware/compra; disclosure obrigatório |
| Releases nasce com 2 artigos | Alta | Baixo | Esperado; job diário alimenta; seção comunica "novos lançamentos" |
| Migração manual dos 26 quebra conteúdo | Média | Médio | Template + sync_layout + QA valida os 26 |

---

## 13. Próximos passos (para o pipeline)

1. **Fase 3 — Design** (diretordearte): executar este design spec → mockups (home-feed, artigo, `/guia/`) para aprovação do Bruno antes de codar.
2. **Fase 4 — Dev:** implementar por ordem (design system → header/footer → home-feed → template artigo → migração → busca → monetização → SEO regen).
3. **Fase 5 — QA:** validar os 13 critérios de aceite (§11) contra o site em staging/preview Vercel.

---

## Fontes / referências

- [discovery-report.md](./discovery-report.md) — benchmark completo (Simon Willison, HF Blog, ModelFit, ServeTheHome, hardware.com.br, EthicalAds, Buttondown vs Beehiiv vs Substack, Ben's Bites/The Rundown) com 28 links.
- [PLANO-BLOG.md](./PLANO-BLOG.md) — plano diretor (princípios + fases).
- [DECISIONS.md](./DECISIONS.md) — ADRs 001-008.
- [ROADMAP.md](./ROADMAP.md) — metas de tráfego e métricas de sucesso.
- [SEO-STRATEGY.md](../SEO-STRATEGY.md) — estratégia SEO/GEO existente.
