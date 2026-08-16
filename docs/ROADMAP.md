# Roadmap

Próximos passos do projeto **Qwen3.8-27B landing page / Portal de Modelos
Locais de 30B**. A seção "Concluído" registra o que já foi entregue.

**Board kanban:** `seo-local-models-30b`  
**Produção:** https://qwen38-27b-landing.vercel.app (GA4 `G-016TVX8LEE` ativo)  
**Última atualização:** 2026-08-15

---

## Concluído

- ✅ Landing page inicial (2026-08-14)
- ✅ Redesign Geist + 26 benchmarks (2026-08-14)
- ✅ Seção "Medido nesta máquina" — decode em platô térmico no Strix Halo (2026-08-14)
- ✅ Tradução pt-BR completa (2026-08-15)
- ✅ Deploy automático Vercel (2026-08-15)
- ✅ Tech SEO & Performance — robots, sitemap, llms.txt, PWA, 404 (2026-08-15)
- ✅ Fix performance/acessibilidade/SEO — font stack, contraste AA, headings (2026-08-15)
- ✅ Portal 30B — seções Modelos, Hardware, Benchmarks, Guia Rápido (2026-08-15)
- ✅ Menu responsivo com hambúrguer + links cleanUrls (2026-08-15)
- ✅ Remoção do `aggregateRating` fabricado do JSON-LD + 26 benchmarks no llms.txt (2026-08-15)
- ✅ Fix scrollspy `SyntaxError` (`querySelector('/guia')`) + meta description 152 chars (2026-08-15)
- ✅ GA4 real `G-016TVX8LEE` instalado, com `anonymize_ip` (2026-08-15, `7afed08` — decisão de
  analytics resolvida pelo Bruno; ver ADR-007)
- ✅ Google Search Console — sitemap expandido (2026-08-15, `d256ec3`). **Meta
  de verificação voltou a pendente** (2026-08-16): a meta em produção é
  placeholder (`SEU_TOKEN_DE_VERIFICACAO_AQUI`) em 12 páginas e ausente nas 2
  novas — resolver via GA4 (`GSC_SETUP.md`, card `t_65295f98`).
- ✅ Estruturar documentação inicial em `docs/` (2026-08-15, task `t_f56140db`)
- ✅ Consolidar docs da raiz em `docs/` + stubs + ADR-007 (2026-08-15, task `t_2e42bec9`)

---

## Curto prazo (próximos 7 dias)

- [ ] **Dashboard Looker Studio** — conectar o GA4 (`G-016TVX8LEE`) e criar
  visualização de tráfego (tentativa anterior do atlas travou na UI).
- [ ] **Configurar metas no GA4** — 1k visitas/mês, bounce < 50%, tempo
  médio > 2 min.
- ✅ 2 artigos publicados: Muse Glimmer 30B + quantização GGUF (2026-08-15) — *removido do curto prazo*
- [ ] **Submeter o sitemap no Search Console** — verificação instalada
  (`d256ec3`); falta concluir o processo no console (`GSC_SETUP.md`).
- ✅ **Validar Core Web Vitals pós-font-stack** — Lighthouse lab (mobile,
  16/08): home 100/100 com LCP 1,1 s; artigo Muse 100/100 com LCP 0,8 s. Nota
  lab×field: field data (CrUX) só existe com tráfego real — medir novamente
  quando o GA4 (`G-016TVX8LEE`) mostrar tráfego.
- ✅ **Grafo JSON-LD completo** (2026-08-16, task `t_11224bcd`): ItemList em
  `/modelos`, `offers`+`softwareRequirements` no Muse, FAQPage em
  `/guia/faq`, WebPage+Breadcrumb nas 4 páginas do portal — ver ADR-008 e
  `HISTORICO.md`.

## Médio prazo (30 dias)

- [ ] **1.000 visitas/mês** no portal (GA4).
- [ ] **15+ artigos publicados** (1 a cada 2 dias úteis).
- [ ] **Top 10 no Google** para "modelos locais 30B" e variações.
- [ ] **Benchmarks reais** — medir o Qwen3.8-27B no Strix Halo com script
  reproduzível.
- [ ] **Página de comparação** — tabela interativa de modelos ≤ 30B.

## Longo prazo (90 dias)

- [ ] **5.000 visitas/mês**.
- [ ] **Newsletter** — assinantes recebem resumo semanal dos artigos.
- [ ] **Comunidade** — seção de contribuições (benchmarks enviados por
  usuários).
- [ ] **Domínio próprio** (modelos30b.com.br ou similar).

---

## Métricas de sucesso

| Métrica            | Atual | Meta 30d | Meta 90d |
|--------------------|-------|----------|----------|
| Visitas/mês        | —     | 1.000    | 5.000    |
| Artigos publicados | 0     | 15       | 60       |
| Bounce rate        | —     | < 50%    | < 40%    |
| Tempo médio        | —     | > 2 min  | > 3 min  |
| GitHub stars       | —     | 50       | 200      |

*Fonte de dados: GA4 `G-016TVX8LEE` (ativo desde 2026-08-15).*

---

## Backlog (ideias sem prioridade)

- **Internacionalização (i18n):** versão em inglês da página. O conteúdo é
  em pt-BR; uma versão EN ampliaria alcance. Depende de decisão de escopo.
- **Modo de comparação lado a lado:** permitir comparar o Qwen3.8-27B com
  modelos de fronteira selecionados pelo usuário.
- **Gráficos interativos:** os gráficos são SVG estático. Adicionar
  interatividade (hover detalhado, toggle de séries) sem quebrar o princípio
  de "zero dependências de runtime" exigiria JS vanilla — avaliar.
- **Testes automatizados:** a página é HTML estático, mas testes de
  regressão visual (Playwright/Percy) poderiam proteger contra quebras de
  layout em mudanças futuras.
- **Analytics privacy-first (Plausible/Umami):** reapreciar se as metas de
  privacidade mudarem (hoje GA4 com `anonymize_ip` — ADR-007).
