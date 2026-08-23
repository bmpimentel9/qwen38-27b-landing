# PLANO-BLOG.md — Transformar qwen38-27b-landing em Blog de Modelos Locais

> Plano diretor. Escrito por Dani em 23/08/2026 a pedido do Bruno.
> Objetivo final: **layout totalmente remodelado, estilo blog profissional, amigável para o fã de modelos locais — e monetizável.**

## Contexto

- **Hoje**: landing single-page 100% focada no Qwen3.8-27B (index.html + 26 artigos em `/guia/`). HTML estático puro, Vercel, deploy auto da main.
- **Board**: `seo-local-models-30b` (181 done, limpo). Pipeline padrão Discovery→PRD→Dev→QA.
- **Oportunidade**: o site já atrai impressões orgânicas e tem 26 artigos de qualidade. Falta o formato: virar **blog de referência da comunidade de modelos locais** — não mais só "landing do Qwen".
- **Trunfo**: posicionar como o blog que o fã de modelos locais consulta — guias, benchmarks, hardware, releases. Conteúdo amigável de ler, organizado por categoria, com caminhos de monetização embutidos sem poluir a leitura.

## Princípios do redesenho

1. **Conteúdo amigável primeiro**: tipografia confortável, tempo de leitura, TOC sticky, breadcrumbs, prev/next, legibilidade em mobile.
2. **Blog de verdade**: home vira feed de artigos (cards com data/categoria/tempo de leitura), não landing institucional.
3. **Navegação por categoria**: Guias, Benchmarks, Hardware, Releases, Comunidade — o leitor encontra o que procura em 2 cliques.
4. **Não quebrar SEO**: URLs atuais `/guia/*` permanecem, canonical, sitemap, robots, llms.txt intactos.
5. **Monetização sem poluir**: newsletter + affiliate de hardware + ads dev-friendly posicionados sem atrapalhar leitura.
6. **Um design system só**: hoje cada artigo tem CSS próprio duplicado. Unificar em CSS compartilhado + template único.

## Fases e tarefas (pipeline kanban)

### Fase 1 — Discovery (benchmark)
**Tarefa**: pesquisar blogs de modelos locais / dev blogs que monetizam bem (Hugging Face blog, Simon Willison, r/LocalLLaMA digests, blogs de hardware, exemplos de newsletter/affiliate/ads dev-friendly). Extrair padrões de layout profissional de blog técnico. Entregar `discovery-report.md`.

### Fase 2 — PRD (arquitetura de informação + design spec)
**Tarefa**: definir a nova IA do site:
- Home = feed de artigos (destaque + recentes + por categoria)
- Template único de artigo (header com título/meta/thumbnail, TOC sticky, corpo legível, prev/next, artigos relacionados)
- Header/footer globais com navegação por categoria
- Categorias: Guias · Benchmarks · Hardware · Releases · Comunidade
- Design tokens (cores, tipografia, spacing, dark-first)
- Requisitos de monetização (onde entram newsletter, affiliate, ads)
- Restrição: não quebrar URLs/SEO atuais. Entregar `PRD.md`.

### Fase 3 — Design (design system + mockups)
**Tarefa**: diretordearte produz design system (tokens) + mockups: home-blog, página de artigo, página de categoria. Aprovação do Bruno antes de codar.

### Fase 4 — Dev (implementação)
**Tarefas**:
1. Design system implementado: CSS compartilhado + JS global + header/footer.
2. Home remodelada em blog (feed de cards, destaque, categorias).
3. Template de artigo novo + migração dos 26 artigos existentes (sem quebrar URLs).
4. Monetização: formulário de newsletter + blocos affiliate + slots de ads dev-friendly.

### Fase 5 — QA
**Tarefa**: validação completa — mobile (<900px, hamburguer), links vivos, SEO (canonical/sitemap/robots), performance, acessibilidade, aderência ao PRD.

## Entregável final
Layout novo 100% remodelado no ar (Vercel), blog amigável de modelos locais, SEO preservado, com trilhas de monetização instaladas.
