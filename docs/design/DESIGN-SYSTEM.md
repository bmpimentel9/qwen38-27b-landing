# Design System — Blog Modelos Locais ≤30B

> Fase 3 (Design) · task `t_38013a68` · diretordearte · 23/08/2026
> Autoridade: docs/PRD.md §6 + ADR-002 (Geist) + ADR-003 (font stack) + ADR-001 (zero-build).
> Entrega para aprovação do Bruno ANTES do Dev. Mockups: `mockup-home.html` · `mockup-artigo.html` · `mockup-guia.html`.

---

## 1. Princípios (por que é assim)

1. **Dark-first, densidade de documentação, estética Geist** — superfícies quase monocromáticas, hairlines de 1px, raio 8/12. O conteúdo (dados, benchmarks) é o protagonista; o chrome compete com nada.
2. **Legibilidade sobre decoração** — medida de linha ~65-75ch no corpo, `line-height 1.6-1.7`, hierarquia por peso/tamanho, não por cor chamativa.
3. **Zero dependência externa** (ADR-001/003) — font stack de sistema, sem Google Fonts, sem framework. Tema claro via `[data-theme="light"]` (alternância manual preservada).
4. **Categoria = cor**. As 5 categorias têm acentos próprios, mas sempre sobre fundo escuro neutro, em baixa saturação — cor é sinal, não enfeite.
5. **Mobile-first de verdade**: 3 colunas ≥1024px → 2 colunas 640-1024 → 1 coluna <640. Tabelas com scroll horizontal. TOC vira "Nesta página" fixo.

---

## 2. Design tokens

### 2.1 Cor (dark — tema padrão)

| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#0B0E14` | Fundo da página |
| `--surface` | `#151B27` | Cards, nav, footer, TOC |
| `--surface-2` | `#1C2433` | Hover, headers de tabela, campos |
| `--border` | `#2A3446` | Hairlines (1px) |
| `--text` | `#E8EDF6` | Texto primário |
| `--muted` | `#8C96AB` | Metadados, leads, captions |
| `--accent` | `#2DD4BF` (cyan) | Links, CTAs, foco, itens ativos |
| `--accent-2` | `#4ADE80` (green) | Sucesso, badge "novo" |
| `--accent-3` | `#F5B841` (amber) | Avisos, "recente" |
| `--accent-4` | `#A78BFA` (violet) | Categoria Guias, destaque editorial |
| `--accent-5` | `#F87171` (red) | Erro, perigo |
| `--code-bg` | `#1C2128` | Blocos de código |

**Mapeamento categoria → cor do card/badge:**

| Categoria | Acento | Badge |
|---|---|---|
| Guias | `--accent-4` (violet) | `--cat-guides` |
| Benchmarks | `--accent` (cyan) | `--cat-bench` |
| Hardware | `--accent-2` (green) | `--cat-hw` |
| Releases | `--accent-3` (amber) | `--cat-releases` |
| Comunidade | `--blue #3B82F6` | `--cat-community` |

Tema claro (`[data-theme="light"]`): fundos invertem com contraste mantido — bg `#FAFAFA`, surface `#FFFFFF`, text `#17191C`, border `#E4E7EC`, acentos iguais escurecidos em 1 passo. Contraste validado ≥ AA (4.5:1 normal, 3:1 grande) pelo script do ADR-002.

### 2.2 Tipografia

- **Stack texto (ADR-003):** `system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`
- **Stack mono (números, código, data):** `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`
- **Escala (desktop → mobile):**

| Role | Desktop | Mobile |
|---|---|---|
| H1 (artigo) | `2rem` / lh 1.25 | `1.6rem` |
| H2 (seção) | `1.4rem` | `1.25rem` |
| H3 (card/sub) | `1.1rem` | `1.05rem` |
| Corpo | `1rem` (16px) / lh 1.7 | `1rem` / lh 1.7 |
| Meta / card | `0.85-0.92rem` | `0.85rem` |
| Caption | `0.78rem` | `0.78rem` |

- Título de card em `font-weight: 700`; leads em `--muted`. Números de benchmark sempre `ui-monospace`.

### 2.3 Espaçamento (grid de 8px)

`--space-1:4px · --space-2:8px · --space-3:12px · --space-4:16px · --space-5:24px · --space-6:32px · --space-7:48px`

- Card: padding `--space-5` (24px); gap de grid `--space-5`.
- Container: `max-width:1120px`; artigo `max-width:720px`; TOC coluna `240px` (grid `240px 1fr` ≥1024px).

### 2.4 Raio e sombra

- `--radius-sm:6px` (badges, code) · `--radius-md:8px` (botões, inputs, tables) · `--radius-lg:12px` (cards, hero, TOC).
- Sombras: **apenas overlays** (modal, dropdown) — `0 8px 24px rgba(0,0,0,.4)`. Sem glow, sem gradiente decorativo.

---

## 3. Componentes

### 3.1 Card de artigo (feed) — `.post-card`

```
┌────────────────────────────────┐
│ ▓▓▓▓ thumbnail 16:9 ▓▓▓▓▓▓▓▓▓ │  ← ratio 16:9, objeto cover, overlay sutil
│  [Cat·badge]  ·  há 3 dias  ·  8 min │
│  Título do artigo (H3, link)      │
│  Lead em 1-2 linhas (muted)      │
└────────────────────────────────┘
```
- Inteiro é um `<a>` (link grande, área clicável). Hover: `translateY(-2px)` + borda acento da categoria.
- Thumbnail: imagem real (`og-image` ou custom 1200×630); fallback = gradiente de categoria + monograma do slug (para artigos sem imagem dedicada).
- Meta usa `--muted`, mono para data relativa.
- **Regra inviolável:** título e lead nunca sobrepõem a thumbnail; tipografia vive na própria área do card (zona limpa).

### 3.2 Header global (nav) — `site-header`

- Sticky top, `--surface`, hairline inferior.
- Desktop: brand (`Q` mark + "Blog Modelos Locais") · nav categorias (Guias, Benchmarks, Hardware, Releases, Comunidade → `/guia/#ancora`) · Modelos · FAQ · busca (🔍 modal) · tema (☀/🌙) · CTA "Hugging Face".
- Mobile <900px: hambúrguer (`.nav-toggle`), menu colapsável vertical.
- Item ativo: `aria-current="true"` + acento cyan.

### 3.3 Footer global — `site-footer`

4 colunas (≥768px; empilha abaixo):
1. Marca + 1 linha de descrição + selo "feito sem build, HTML estático".
2. Navegação (categorias + Modelos + Benchmarks + Hardware + Guia Rápido + FAQ).
3. Recursos (llms.txt · sitemap.xml · robots.txt · RSS futuro).
4. Newsletter mini-form.
Linha final: © ano · "Portal de modelos locais de 30B" · disclosure affiliate · Política de privacidade.

### 3.4 TOC sticky (artigo)

- Desktop ≥1024px: coluna `240px` à esquerda, `position:sticky; top:96px`. Scrollspy com `IntersectionObserver` (item ativo = `--accent` + barra lateral).
- Mobile <1024px: oculto na lateral; vira botão "Nesta página" fixo (fab) que abre o TOC em overlay.
- Links âncora com `scroll-margin-top: 96px` (compensa nav sticky).
- Sem JS: o TOC continua renderizado como lista estática de âncoras.

### 3.5 Newsletter — `.newsletter`

- 3 placements: fim de artigo (form inline), footer (mini), home (seção).
- Buttondown embed (`<form action="https://buttondown.com/api/emails/embed-subscribe/<user>" method="post">`), sem redirect — sucesso/erro inline via JS.
- Microcopy obrigatória: "1 email/semana · cancele quando quiser" + "Ao assinar você aceita nossa [política de privacidade]".

### 3.6 Affiliate — `.affiliate` (só hardware/compra)

- Bloco `--surface-2` com hairline, título "Hardware recomendado para rodar este modelo", tabela curta (produto · onde comprar · link).
- Disclosure sempre visível (estilo Tecnoblog): *"Ao clicar e comprar por links de afiliado, o preço não muda para você e recebemos uma pequena comissão que mantém o blog gratuito."*
- Links `rel="sponsored noopener"`.

### 3.7 Slots de ad (desligados)

`.ad-slot` em `article`, `aside`, `home` — `display:none` por padrão + comentário `<!-- ad slot: ativar quando tráfego >20k/mês -->`. Ativar na Fase 3 = CSS + 1 script.

### 3.8 Elementos de corpo (preservados do acervo)

- `.callout` (borda lateral 3px, `--surface`) · `.leader` (dado citável, big text muted) · `.stat-card`/`.stat-row` (mono value) · `table` (scroll horizontal mobile) · `pre/code` (header de linguagem opcional) · `faq-item` (acordeão leve).

---

## 4. Layout

### 4.1 Home (feed)

```
[Header global]
[Hero compacto Qwen3.8-27B]  ← 1 linha value prop + 4 stats + 2 CTAs (compacto!)
[Em destaque — 1 card hero editorial]
[Últimos artigos — grid 6 cards]
[Explorar por categoria — 5 blocos]
[Newsletter CTA]
[Footer global]
```

### 4.2 Artigo

```
[Header global]
[Breadcrumb: Home › Categoria › Título]
[Header artigo: h1 · meta (data/autor/cat/tempo) · lead · thumbnail]
[TOC sticky 240px] [Corpo 720px]   ← grid ≥1024
[Affiliate (se hardware)]
[Newsletter inline]
[Prev/Next]
[Relacionados — 3 cards]
[Compartilhar]
[Footer global]
```

### 4.3 /guia/ (arquivo)

```
[Header global]
[H1 "Guias e artigos" + lead + stats de acervo]
[5 seções com âncora: #guias #benchmarks #hardware #releases #comunidade]
   — cada seção: header categoria (badge + título + contagem) + grid de cards
[FAQ link destacado]
[Newsletter]
[Footer global]
```

---

## 5. Acessibilidade (não negociável)

- Contraste AA em todas as combinações texto/fundo (validado por script ADR-002).
- `prefers-reduced-motion`: desliga translate/hover animations.
- Skip-link (`#topo`), `:focus-visible` ring (2px accent), labels em inputs, `aria-*` em modal/menu.
- Ordenação lógica de leitura: h1 → h2 → h3 sem saltos.

---

## 6. Performance (Lighthouse alvo)

- 100/100 · LCP < 1,5s · zero requisição externa de fonte.
- Nenhum JS bloqueante no head; `blog.js` com `defer`.
- Imagens: `loading="lazy"` no feed (hero/featured eager).

---

## 7. Arquivos

| Arquivo | Papel |
|---|---|
| `blog.css` | Design system em CSS (copiar → `assets/css/blog.css`) |
| `mockup-home.html` | Home-feed aprovável |
| `mockup-artigo.html` | Template de artigo (TOC sticky) aprovável |
| `mockup-guia.html` | Arquivo `/guia/` por categoria aprovável (BIND-03) |
| `README-DESIGN.md` | Índice de revisão + como "categoria" foi resolvida + QA |
| `preview-*.png` | Screenshots desktop dos 3 mockups (atalho visual) |
| `DESIGN-SYSTEM.md` | Este documento |
