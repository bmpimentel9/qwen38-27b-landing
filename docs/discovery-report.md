# Discovery Report — Blog de Modelos Locais: Benchmark de Layout + Monetização

> **Tarefa:** `t_55aa3541` · **Perfil:** discovery · **Data:** 23/08/2026
> **Objetivo:** transformar a landing `qwen38-27b-landing` em um blog de modelos locais, profissional, amigável e monetizável.
> **Base:** [PLANO-BLOG.md](./PLANO-BLOG.md) (plano diretor escrito pela Dani) + estado real do repo `~/workspace/qwen38-27b-landing`.

---

## 1. Contexto

O site `qwen38-27b-landing.vercel.app` começou como landing page single-page do Qwen3.8-27B e evoluiu para um **portal de modelos locais de 30B** com 26 artigos em `/guia/`. Hoje ele tem bom SEO técnico (canonical, sitemap, llms.txt, schema.org, GA4 real) e conteúdo de qualidade, mas **não tem formato de blog** — não há home em feed, nem categorias navegáveis, nem tempo de leitura, nem TOC sticky, nem qualquer trilha de monetização.

O plano diretor define que o site deve virar o **blog de referência do fã de modelos locais** (BR + global), com layout profissional e monetização embutida sem poluir a leitura. Este relatório entrega o benchmark de mercado para fundamentar o PRD (Fase 2).

---

## 2. Estado atual (verificado no repo e no GA4)

| Item | Situação hoje | Gap para blog profissional |
|---|---|---|
| **Home (`/`)** | Landing institucional focada no Qwen3.8-27B: seções specs, benchmarks, multimodal, comunidade, timeline, guia-artigos | Não é feed de cards; não mostra recência/categoria/tempo de leitura |
| **Artigos (`/guia/*`)** | 26 artigos em diretórios próprios com `index.html`; cada um com **CSS inline duplicado** (~1 `<style>` por página) | Sem design system compartilhado; sem template único |
| **Header/nav** | Repetido manualmente em cada artigo (Home, Guia, Benchmarks, Hardware, Como Rodar, Comunidade, FAQ) | Sem header/footer globais centralizados |
| **Cabeçalho de artigo** | Já tem `<h1>`, `lead`, badges de specs | **Sem data visível**, sem autor, sem tempo de leitura, sem thumbnail |
| **TOC** | Existe `<div class="toc">` com links de âncora, mas **não é sticky** (`position` estático) | Falta TOC sticky + scrollspy |
| **Prev/next** | Só links manuais de "Leia mais" no fim | Sem navegação prev/next automatizada nem "artigos relacionados" |
| **Categorias** | Tags por cor no card-grid do `/guia/` (tag-guide, tag-bench) | Sem páginas de categoria dedicadas |
| **JSON-LD** | TechArticle + BreadcrumbList + FAQPage por página — forte | Pode ganhar `Blog`/`BlogPosting` + `NewsArticle` |
| **SEO** | Canonical, sitemap (33 URLs), robots, llms.txt intactos | **Não quebrar** — restrição dura do plano |
| **Tráfego (GA4 `G-016TVX8LEE`)** | ~350 visitas/mês, bounce 71%, tempo médio 1min40s | Meta 30d: 1.000; meta 90d: 5.000 (ROADMAP.md) |
| **Monetização** | Nenhuma | Newsletter, affiliate, ads — todos a instalar |

**Leitura do estado:** o site tem **conteúdo e SEO**, mas não tem **formato nem monetização**. A transformação para blog é majoritariamente de **arquitetura de informação + template único + design system**, não de conteúdo novo.

---

## 3. Benchmark — Blogs/Dev blogs que monetizam bem

### 3.1 Simon Willison's Weblog — o modelo canônico de dev blog monetizado
Fonte: [simonwillison.net](https://simonwillison.net/) (extraído ao vivo em 23/08/2026) + [How I blog](https://simonwillison.net/series/blogging/) + [mtlynch.io notes](https://mtlynch.io/notes/simon-willison-software-misadventures/)

- **O que é:** blog de 22 anos de um desenvolvedor influente (criador do Datasette/LLM CLI). Referência máxima de dev blog de IA.
- **Monetização:**
  - **Patrocínio fixo no topo** ("Sponsored by: Teleport") — um único sponsor por página, rotativo.
  - **GitHub Sponsors** — "Sponsor me for **$10/month** and get a curated email digest of the month's most important LLM developments" (Newsletter mensal paga como *benefício de patrocínio*, não paywall).
  - **~6.000 assinantes de newsletter** (via Substack/RSS), usada como distribuição, não como produto principal.
- **Padrões de layout:** feed por data com **tags massivas** (cada post taggeado: `llm-reasoning 101`, `sqlite 484`...), seções separadas (Entries / Links / Quotes / Notes / Guides), arquivo por ano, Atom feed. **Disclosure público** de conflitos na página About.
- **Lições para nós:** (1) sponsor único discreto é aceitável em dev blog; (2) newsletter paga como *add-on* de quem já lê; (3) tags + arquivo por ano = navegação de blog de verdade; (4) transparência de disclosure é obrigatória.

### 3.2 Hugging Face Blog — a vitrine da comunidade
Fonte: [huggingface.co/blog](https://huggingface.co/blog) (extraído ao vivo em 23/08/2026)

- **O que é:** blog da HF (corporativo + community articles). Não é monetizado por ads — é inbound marketing do ecossistema, mas é a **referência de IA que o público já conhece**.
- **Padrões de layout:** card grid com **thumbnail, autor, "X days ago", contagem de likes**; tabs "Community" vs oficial; ordenação por trending. Posts longos usam TOC e "progressive disclosure" (crítico no topo, profundidade abaixo — [HF docs](https://huggingface.co/docs/course/chapter4/4)).
- **Lições:** cards com data relativa + autor + engagement; categorização por tags; estrutura de artigo com "TL;DR no topo".

### 3.3 ModelFit Blog — dev blog de modelos locais com newsletter semanal
Fonte: [modelfit.io/blog](https://modelfit.io/blog) (search, 23/08/2026)

- **O que é:** blog focado em rodar local LLM em Apple Silicon + GPU (mesmíssima audiência-alvo do nosso portal).
- **Padrões:** cada post com **TL;DR**, data, guias por RAM tier, comparativos; **newsletter semanal gratuita** ("The weekly local-AI refresh — free, one email a week") embutida no blog.
- **Lições:** newsletter é o canal padrão da audiência local-LLM; conteúdo por tier de hardware é o formato que converte.

### 3.4 ServeTheHome — hardware blog que vive de ads + affiliate
Fonte: [servethehome.com/about/editorial-copyright-policies](http://servethehome.com/about/editorial-copyright-policies) (extraído ao vivo)

- **O que é:** um dos maiores blogs de hardware/server do mundo.
- **Monetização:** **ads de terceiros (Google AdSense, agências) + affiliate links (Amazon, eBay, Skimlinks)** + produtos de review emprestados (sem pagamento por opinião). Divulga lista pública de conflitos.
- **Lições:** affiliate + ads coexistem em hardware blog, com **política editorial explícita** ("não aceitamos dinheiro por resultado de review").

### 3.5 Hardware.com.br / Tecnoblog — o padrão BR de affiliate
Fonte: [hardware.com.br](https://www.hardware.com.br/) e [Tecnoblog](https://tecnoblog.net/) (extraído ao vivo)

- **hardware.com.br:** blog BR de hardware com seção **"Hardware Indica"** — artigos de oferta/recomendação ("5 mini projetores 4K", "lâmpada com 73% OFF") que são puro affiliate. Padrão maduro no BR.
- **Tecnoblog:** usa **links de afiliado com disclosure** ("Aviso de ética: ao clicar em um link de afiliado, o preço não muda para você e recebemos uma comissão"), breadcrumbs, seções por tema.
- **Lições:** no BR, affiliate de hardware é viável e normalizado; **disclosure é requisito legal/ético** (FTC no US, prática consolidada no BR).

### 3.6 Newsletter "Last Week in r/LocalLLaMA" — o digest da comunidade
Fonte: [Spotify](https://open.spotify.com/show/4BLUo6W1IBxFnlIOG2apT6) + [agentsindex](https://agentsindex.ai/r-localllama) + [reddtrends](https://reddtrends.com/r/localllama)

- **r/LocalLLaMA tem ~796 mil membros** (reddtrends, 23/08/2026) — a maior comunidade de local LLM do mundo. Cresceu de ~50k (2024) para ~796k (2026).
- Existe **podcast semanal "Last Week in r/LocalLLaMA"** + monthly threads de top models — prova de demanda por **digest semanal de modelos locais**, exatamente o que nossa newsletter seria.
- **Tio digest** ([tio.ist/newsletter](https://tio.ist/newsletter)) é outro exemplo de newsletter semanal de tech/AI "sem sponsors" — mostra que curadoria semanal é formato consolidado.

### 3.7 Newsletters de IA que faturam (referência de teto)
Fontes: [newsletterinsights.io — Ben's Bites](https://newsletterinsights.io/newsletter/bensbites-com/investor-report), [emailbreakdown — 2 AI Newsletter Playbooks](https://emailbreakdown.beehiiv.com/p/inside-2-ai-newsletter-playbooks), [newslettergrowthmemo — The Rundown $10M/yr](https://www.newslettergrowthmemo.com/p/the-1st-ai-newsletter-to-hit-10m-yr)

| Newsletter | Modelo | Números |
|---|---|---|
| **Ben's Bites** | Educação/community-driven: Pro Membership ($175/ano) + Lifetime ($228), 20k+ membros pagantes | $79k/mês est. receita, ~7,2k paid subs (substack, $25/mo ou $80/ano) |
| **The Rundown AI** | Media-driven: ads + sponsorships + AI University ($999/ano, 5k membros) | 900k-1,4M subs, ~$10M run-rate, margem 25-50% |

**Lições:** nenhum blog solto chega lá; mas o **caminho comprovado é: conteúdo grátis (SEO) → newsletter → camada paga (produto educacional)**. Para nós, uma newsletter semanal gratuita primeiro, com **patrocínio de slot** depois, é o caminho realista.

---

## 4. Padrões de layout profissional de blog técnico

Fonte consolidada: [optimizepress — 18 best blog designs](https://www.optimizepress.com/best-blog-designs), [fifteen4 — best practices blog](https://fifteen4.com/best-practices-for-designing-a-blog), [webflow — blog layouts](https://webflow.com/blog/7-beautiful-blog-layouts), [exclusiveaddons — card grid](https://exclusiveaddons.com/blog-layout-ideas), HF docs (3.2), análise ao vivo de simonwillison.net e huggingface.co/blog.

### 4.1 Home como feed de cards
- **Card grid responsivo** (2-3 colunas desktop, 1 mobile) — o padrão de blogs modernos e do HF Blog.
- **Card mínimo:** thumbnail, título, **data, categoria, tempo de leitura** — para o leitor decidir o clique em 1 segundo.
- **Featured/hero no topo:** artigo em destaque maior (Webflow, Strive/Lattice) — dá destaque editorial sem quebrar o grid.
- **Ordem por recência + "Editor's Picks"** (Riverside/Ramp usam seção de curadoria no topo).

### 4.2 Página de artigo
- **Header de artigo:** breadcrumbs → H1 → meta (autor, data, categoria, tempo de leitura) → lead → thumbnail.
- **TOC sticky** na lateral esquerda (Ramp, Riverside) que acompanha o scroll + scrollspy — o plano pede explicitamente.
- **Tipografia confortável:** linha de ~65-75 chars, line-height 1.6-1.7, contraste AA, dark-first.
- **Prev/next + relacionados** no fim — estende a sessão e melhora SEO interno.
- **Social share** no topo e rodapé (ou floating) — Fifteen4 recomenda; mobile pode ser bottom-anchored.
- **Newsletter CTA** após o artigo (Fifteen4 item #9).

### 4.3 Navegação
- **Categorias no header** (Guias · Benchmarks · Hardware · Releases · Comunidade — do plano) com **páginas de categoria dedicadas**.
- **Breadcrumbs** em artigo.
- **Busca** (já existe helper `qwenTrackSearch()` no GA4 — sinal de que busca foi planejada).

### 4.4 Design system
- **CSS compartilhado** + template único (hoje cada artigo duplica CSS — custo de manutenção alto, risco de drift). O plano pede "um design system só".
- Dark-first com tema claro (o site já tem `data-theme` e tokens Geist — reutilizar).

---

## 5. Modelos de monetização viáveis (BR + global)

Análise de viabilidade contra o tráfego atual (~350/mês) e as metas (1k → 5k/mês). **Ordem importa: nada funciona sem audiência; monetização cresce em camadas.**

### 5.1 Newsletter (Fase 1 — sem tração ainda, custo ~zero) ✅ PRIORIDADE ALTA
- **Formato:** resumo semanal "o que rolou nos modelos locais" (novos releases ≤30B, benchmarks, hardware) — o digest que a comunidade r/LocalLLaMA já consome (3.6).
- **Plataforma (comparativo pesquisado):** [PickLogic dev newsletter platforms](https://picklogic.co/newsletter-platforms/best-for-developers/) + [youngju.dev deep dive](https://www.youngju.dev/blog/culture/2026-05-16-newsletter-platforms-2026-substack-beehiiv-kit-convertkit-buttondown-ghost-maven-deep-dive.en) + [emailfordevelopers](https://emailfordevelopers.com/providers/buttondown/):
  - **Buttondown** — API-first, Markdown, webhooks, dados exportáveis, grátis até 100 subs. **Melhor para dev-flavored.**
  - **Beehiiv** — growth tools (referrals, ad network, boosts), free até 2.500 subs. Melhor para escalar rápido.
  - **Substack** — mais fácil, mas taxa de 10% sobre receita e lock-in.
  - **Recomendação:** **Buttondown** (filosofia OSS/indie + API, encaixa no espírito do projeto "zero build") com possibilidade de migrar para Beehiiv quando escalar. Alternativa leve: form HTML próprio + planilha, mas perde entregabilidade.
- **Monetização futura:** slot de patrocínio por edição (padrão The Rundown: $30 CPM × 40% open; deep dives 4-6× o preço de slot — [newslettergrowthmemo](https://www.newslettergrowthmemo.com/p/the-1st-ai-newsletter-to-hit-10m-yr)). Realista só a partir de ~5-10k subs.

### 5.2 Affiliate de hardware (Fase 2 — converte com audiência tech) ✅ PRIORIDADE ALTA
- **O que anunciar:** GPUs (RTX 4090/5090, Radeon), Macs/Strix Halo, minis, RAM, eGPU, docks — exatamente o que os guias `/guia/hardware-local` e `/guia/quantizacao-gguf-30b-quanto-cabe-na-sua-gpu` recomendam.
- **Números:** Amazon Associates ~2,5-4,5% em eletrônicos (cookie 24h); Newegg 1-5% (30d); B&H até 8% (30d) — [youfiliate](https://youfiliate.com/blog/best-affiliate-programs-tech-reviewers), [findaffiliates](https://findaffiliates.online/blog/amazon-affiliate-program-tech-review-bloggers). No BR, **Amazon BR** + Mercado Livre Afiliados (padrão hardware.com.br — seção "Hardware Indica", 3.5).
- **Forma:** bloco "Hardware recomendado para rodar este modelo" no fim de cada artigo + tabela de VRAM com links de compra no guia de hardware. **Disclosure obrigatório** (estilo Tecnoblog).
- **Cuidado:** cookie curto (Amazon 24h), então affiliate funciona em *roundups de compra* de alta intenção, não em artigo informativo genérico.

### 5.3 Ads dev-friendly (Fase 3 — só com volume) ⏳ GATILHO DE TRÁFEGO
- **EthicalAds** (privacy-first, 70/30 publisher, ~$2,50 CPM EU/NA, **mínimo 50k pageviews/mês**, invite-only, 1 ad por página) — [ethicalads.io/publishers](https://www.ethicalads.io/publishers/). Perfeito filosoficamente (open source, sem tracking, sem cookie banner), mas **nossa audiência atual (~350/mês) está 140× abaixo do mínimo**.
- **Carbon Ads** (BuySellAds): ~10k pageviews/dia, CPM alto, fila de espera — [wmtips](https://www.wmtips.com/technologies/compare/carbon-ads-vs-ethicalads/).
- **Conclusão:** ads **não são para agora**. Registrar como **fase 3**, quando o tráfego passar de ~20-50k/mês. Enquanto isso, **newsletter + affiliate cobrem 100% das necessidades** e não poluem.

### 5.4 Patrocínio direto / produto (Fase 3-4 — teto)
- Sponsor fixo no topo (modelo Simon Willison) ou "powered by" — viável quando houver audiência.
- Produto educacional pago (ex: "Guia completo de rodar LLM local no Brasil") — o caminho Ben's Bites. **Longo prazo**, não escopo do PRD.

### 5.5 Matriz de decisão (resumo executivo)

| Canal | Custo | Esforço | Receita potencial | Quando |
|---|---|---|---|---|
| Newsletter (Buttondown) | R$0 | Baixo | Média (via sponsors) | **Agora** |
| Affiliate Amazon/ML | R$0 | Baixo | Média (alta intenção) | **Agora** |
| Ads (EthicalAds) | R$0 | Baixo | Baixa até 50k/mês | >20k visitas/mês |
| Sponsor direto | R$0 | Médio | Alta | >10k visitas/mês |
| Produto pago | R$0 | Alto | Alta | >50k visitas/mês |

---

## 6. Recomendação técnica (para o PRD)

1. **Arquitetura do blog (sem framework, zero build — respeita ADR-001):**
   - `index.html` vira **feed de cards** (featured hero + grid por categoria), mantendo as seções de specs do Qwen como conteúdo, não como única face.
   - **Template único de artigo** (`templates/template-artigo.html`) com header de artigo (data/autor/categoria/tempo de leitura), TOC sticky + scrollspy, corpo legível, prev/next, relacionados.
   - **CSS compartilhado** (`assets/blog.css`) substituindo os CSS inline duplicados; **JS global** (`assets/blog.js`) para TOC, scrollspy, menu.
   - **Header/footer globais** com navegação por categoria.
2. **Categorias (do plano):** Guias · Benchmarks · Hardware · Releases · Comunidade — como **páginas de categoria** (`/guia/<categoria>/` ou filtro na home). Mapear os 26 artigos existentes para as 5 categorias.
3. **Não quebrar SEO:** manter URLs `/guia/*`, canonical, sitemap (regerar), robots, llms.txt (regerar). Migrar JSON-LD para `Blog` + `BlogPosting`.
4. **Monetização instalada:** form de newsletter (Buttondown embed) no fim de artigo + rodapé + home; blocos affiliate no guia de hardware e nos artigos com disclosure; **sem ads ainda** (decisão explícita de fase).
5. **Tempo de leitura:** calcular por contagem de palavras (JS simples, sem dependência) e exibir no card e no header do artigo.

---

## 7. Riscos

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| **Quebrar SEO ao remodelar** | Média | Alto | Congelar URLs; regerar sitemap/llms.txt; teste de 301/404; verificação GSC pós-deploy |
| **Tráfego atual baixo (~350/mês)** | Alta | Alto | Monetização não paga as contas no início; tratar como investimento; newsletter cresce por SEO orgânico |
| **Drift entre artigos (CSS duplicado)** | Alta | Médio | Design system único; script de validação (estilo `check_head.py`) |
| **Affiliate sem disclosure / baixa intenção** | Média | Médio | Disclosure visível; affiliate só em roundups de compra |
| **Ad network rejeitada por tráfego baixo** | Alta | Baixo | Não depender de ads; gate de 20-50k/mês |
| **Migração manual dos 26 artigos** | Média | Médio | Template único + script de migração; QA valida os 26 |

---

## 8. Próximos passos (escopo sugerido para o PRD — Fase 2)

1. **IA do site:** home-feed, template único, categorias, header/footer globais, TOC sticky, prev/next, relacionados, tempo de leitura, busca.
2. **Design spec:** design tokens (reusar Geist + dark-first existentes), mockup home-blog, página de artigo, página de categoria.
3. **Monetização (MVP):** form de newsletter (Buttondown) + blocos affiliate com disclosure no guia de hardware. **Decidir explicitamente: ads fora do escopo desta fase** (gatilho de tráfego).
4. **SEO preservation:** URLs intactas, canonical, sitemap/llms.txt regenerados, JSON-LD `Blog`/`BlogPosting`, hreflang (o site já tem variante EN em `/guia/en/`).
5. **Não quebrar:** GA4 `G-016TVX8LEE`, PWA, acessibilidade (contraste AA, reduced-motion, skip link), zero build.

---

## Fontes

- [PLANO-BLOG.md](https://github.com/bmpimentel9/qwen38-27b-landing/blob/main/docs/PLANO-BLOG.md) — plano diretor
- [ROADMAP.md](https://github.com/bmpimentel9/qwen38-27b-landing/blob/main/docs/ROADMAP.md) — metas de tráfego
- Simon Willison: [blog](https://simonwillison.net/) · [How I blog](https://simonwillison.net/series/blogging/) · [notes mtlynch](https://mtlynch.io/notes/simon-willison-software-misadventures/)
- Hugging Face: [blog](https://huggingface.co/blog) · [model card best practices](https://huggingface.co/docs/hub/model-cards) · [course ch4](https://huggingface.co/docs/course/chapter4/4)
- ModelFit: [modelfit.io/blog](https://modelfit.io/blog)
- ServeTheHome: [editorial policy](http://servethehome.com/about/editorial-copyright-policies)
- Hardware.com.br: [site](https://www.hardware.com.br/) · Tecnoblog: [site](https://tecnoblog.net/)
- Ad networks: [EthicalAds publishers](https://www.ethicalads.io/publishers/) · [wmtips Carbon vs Ethical](https://www.wmtips.com/technologies/compare/carbon-ads-vs-ethicalads/) · [Sponsoric 2026](https://sponsoric.com/compare/best-ad-networks-for-developer-sites) · [idlen playbook](https://www.idlen.io/blog/developer-ad-network-playbook/)
- Newsletters: [Ben's Bites report](https://newsletterinsights.io/newsletter/bensbites-com/investor-report) · [emailbreakdown](https://emailbreakdown.beehiiv.com/p/inside-2-ai-newsletter-playbooks) · [newslettergrowthmemo TRAI](https://www.newslettergrowthmemo.com/p/the-1st-ai-newsletter-to-hit-10m-yr) · [tio digest](https://tio.ist/newsletter)
- Platforms: [PickLogic](https://picklogic.co/newsletter-platforms/best-for-developers/) · [youngju.dev](https://www.youngju.dev/blog/culture/2026-05-16-newsletter-platforms-2026-substack-beehiiv-kit-convertkit-buttondown-ghost-maven-deep-dive.en) · [emailfordevelopers/buttondown](https://emailfordevelopers.com/providers/buttondown/) · [revenuerulebreaker](https://www.revenuerulebreaker.com/which-platform-should-i-use-for-my-newsletter-business/)
- Affiliate: [youfiliate](https://youfiliate.com/blog/best-affiliate-programs-tech-reviewers) · [findaffiliates](https://findaffiliates.online/blog/amazon-affiliate-program-tech-review-bloggers)
- Layout: [optimizepress](https://www.optimizepress.com/best-blog-designs) · [fifteen4](https://fifteen4.com/best-practices-for-designing-a-blog) · [webflow](https://webflow.com/blog/7-beautiful-blog-layouts) · [exclusiveaddons](https://exclusiveaddons.com/blog-layout-ideas)
- Comunidade: [reddtrends r/LocalLLaMA](https://reddtrends.com/r/localllama) · [Last Week in r/LocalLLaMA (Spotify)](https://open.spotify.com/show/4BLUo6W1IBxFnlIOG2apT6) · [agentsindex](https://agentsindex.ai/r-localllama)
