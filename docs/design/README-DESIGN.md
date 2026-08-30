# Design System + Mockups — Blog Modelos Locais ≤30B

> Fase 3 (Design) · task `t_38013a68` · diretordearte · 23/08/2026
> Autoridade: `docs/PRD.md` (§6 design tokens, §7 home, §5 template artigo, BIND-03 categorias)
> **Status: pronto para aprovação do Bruno ANTES do Dev (Fase 4).**

---

## Como revisar

Abra os HTML direto no navegador (usam `blog.css` local, zero dependência externa):

| Arquivo | O que mostra | Verificar |
|---|---|---|
| `mockup-home.html` | Home-feed: hero compacto Qwen3.8-27B → destaque → últimos 6 → 5 categorias → newsletter → footer | Hierarquia, ritmo do grid, hero não domina |
| `mockup-artigo.html` | Template de artigo: breadcrumb → h1+meta+lead → thumbnail → TOC sticky (240px) → corpo 720px → affiliate → prev/next → relacionados → compartilhar → newsletter | TOC acompanha o scroll, medida de linha, legibilidade |
| `mockup-guia.html` | Arquivo `/guia/`: H1+stats → 5 seções de categoria (âncoras) → FAQ link → newsletter | Cada categoria com cor própria + cards |
| `preview-home-desktop.png` | Screenshot renderizado (1440px) | Atalho visual sem abrir HTML |
| `preview-artigo-desktop.png` | Screenshot renderizado (1440px) | Atalho visual |
| `preview-guia-desktop.png` | Screenshot renderizado (1440px) | Atalho visual |

Dica: use o botão ☾ no header para alternar o tema claro/escuro e estreite a janela
(<900px) para ver o hambúrguer e o layout mobile (1 coluna).

---

## Como "página de categoria" foi resolvida

O PRD define na **BIND-03**: páginas de categoria dedicadas são **adiadas** (avaliar
quando o acervo passar de ~60 artigos). Hoje a navegação por categoria usa **âncoras**
no arquivo único `/guia/#guias · /guia/#benchmarks · /guia/#hardware · /guia/#releases ·
/guia/#comunidade` — zero URLs novas, tudo estático e crawlável.

O `mockup-guia.html` é exatamente essa peça: cada categoria é uma seção com header
colorido (chip + título + contagem) + grid de cards. A home e a nav global apontam
para essas âncoras. **Nenhum mockup de URL de categoria separada foi criado de propósito**
— seguiria na contramão do PRD e quebraria a restrição SEO.

Quando o acervo crescer, a página de categoria vira um template de 5 linhas de CSS
reutilizando os componentes já existentes (`.cat-section` + `.post-card`).

---

## QA realizado (23/08/2026 — evidência estrutural)

Validação programática (Playwright/Chromium) nos 3 mockups × 3 viewports
(1440 desktop · 768 tablet · 390 mobile):

- **Overflow horizontal:** 0 (corrigido 1 bug: barra `.share` sem `flex-wrap` estourava
  8px em mobile no `mockup-artigo` → `flex-wrap: wrap` no `blog.css`).
- **Texto cortado/clipado:** 0 (headings, cards, TOC, links checam `scrollWidth`).
- **Âncoras quebradas:** 0 (todo `href="#..."` resolve para um `id` real).
- **Contraste (WCAG AA):** text/bg 16.4:1 · muted/surface 5.8:1 · muted/bg 6.5:1 ·
  accent/bg 10.4:1 — todas ≥ 4.5:1.
- **Tema claro:** toggle ☾ funciona (`--bg` → `#FAFAFA`, corpo re-mapeia tokens).
- **Footer corrigido:** o `mockup-home.html` tinha um resquício de f-string
  (`<function footer at …>`) no lugar do footer — substituído pelo footer global real.

Contraste das 5 cores de categoria sobre superfície escura (badges usam 16% de alpha
sobre o fundo — legíveis, validado visualmente na renderização).

---

## Cobertura dos itens da task

- [x] **Design tokens** — paleta dark-first (12 cores + 5 categorias), tipografia
      (stack sistema ADR-003 + escala), spacing (grid 8px), radius (6/8/12), shadows
      (só overlay) → `DESIGN-SYSTEM.md` §2 + `blog.css` `:root`
- [x] **Mockup home-blog** (feed de cards) — `mockup-home.html`
- [x] **Mockup artigo** (TOC sticky + legibilidade) — `mockup-artigo.html`
- [x] **Mockup página de categoria** — `mockup-guia.html` (arquivo com 5 seções/âncoras,
      conforme BIND-03)
- [x] **Componentes** — card de artigo (thumbnail/fallback, título, lead, data,
      categoria, tempo) · header/footer globais idênticos nos 3 mockups · newsletter
      (home + fim de artigo + footer) · + TOC, breadcrumb, affiliate, prev/next,
      relacionados, compartilhar, busca, FAQ link
- [x] **Visual dark-first profissional** — estética Geist (ADR-002), densidade de
      documentação, hairline 1px, raio 8/12, medida de linha 65-75ch
- [x] **Mobile** — 3→2→1 colunas, hambúrguer <900px, tabelas com scroll, TOC vira
      "Nesta página" (mockup usa lista estática; scrollspy entra no Dev com blog.js)

---

## Próximo passo (Fase 4 — Dev)

Quando aprovado: copiar `blog.css` → `assets/css/blog.css`, implementar
`templates/header.html` + `footer.html` + `template-artigo.html`, `sync_layout.py`,
`build_index.py`, `blog.js` (scrollspy/menu/busca/tema/newsletter) e migrar os 26
artigos preservando URLs. Ver PRD §10.
