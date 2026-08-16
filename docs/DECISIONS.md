# Decision Records (ADRs)

Architecture Decision Records leves do projeto **Qwen3.8-27B landing page**.
Cada registro documenta uma decisão arquitetural: contexto, decisão e
consequências. Narrativa estendida em `HISTORICO.md`.

Formato inspirado em [Michael Nygard's ADR template](https://github.com/joelparkerhenderson/architecture_decision_record).

---

## ADR-001 — Página estática única, sem build e sem dependências de runtime

**Data:** 2026-08-14  
**Status:** Aceito

**Contexto.** A página é documentação técnica de produto sobre um lançamento
de modelo. Precisa ser rápida, indexável, cacheável e hospedável em qualquer
CDN estático. Não há conteúdo dinâmico, autenticação ou backend.

**Decisão.** `index.html` único, sem framework, sem build step, sem
dependências de runtime. Todo CSS e JS inline ou em arquivos estáticos
servidos do mesmo domínio.

**Consequências.**
- LCP mínimo, zero requisições externas bloqueantes.
- Deploy é só copiar arquivos — funciona em qualquer CDN (Vercel, Netlify,
  GitHub Pages, S3).
- Sem reatividade de framework: interatividade via JS vanilla
  (`IntersectionObserver`, `localStorage`, filtros de tabela).
- Sem TypeScript, sem bundler, sem `node_modules`. O repo é legível por
  qualquer pessoa que saiba HTML/CSS/JS.

---

## ADR-002 — Geist como design system de referência

**Data:** 2026-08-14  
**Status:** Aceito

**Contexto.** A página precisava de um registro visual de documentação
técnica de produto, não de marketing. O design anterior (gradiente roxo,
glow, emojis) competia com a densidade de dados.

**Decisão.** Adotar o **Geist** (design system open-source da Vercel) como
referência: superfícies neutras quase monocromáticas, hairlines de 1px,
font stack de sistema, raio 8/12px, densidade de documentação.

**Consequências.**
- Estética neutra que não compete com os dados.
- Tema claro e escuro completos com alternância manual.
- Paleta de gráficos por função (violeta/laranja/cinza), validada por script
  para daltonismo e contraste.
- Sem dependência de npm/pacote Geist — a referência é interpretada em CSS
  vanilla, não importada como biblioteca.

---

## ADR-003 — Font stack de sistema em vez de Google Fonts

**Data:** 2026-08-15  
**Status:** Aceito  
**Supera:** implícito no redesign Geist (que carregava Inter via Google Fonts)

**Contexto.** Google Fonts era render-blocking e segurava o LCP em 4,8s. A
página é estática e sem dependências externas por princípio.

**Decisão.** Substituir Google Fonts por font stack de sistema:
`system-ui` para texto, `ui-monospace` para números e código.

**Consequências.**
- Zero requisições externas de fonte. LCP cai de 4,8s para < 1s.
- Aparência varia ligeiramente entre plataformas, sempre dentro do espírito Geist.
- Removida a dependência de `fonts.googleapis.com`.

---

## ADR-004 — Sem analytics até decisão explícita

**Data:** 2026-08-15  
**Status:** Superceded por ADR-007 (GA4 real `G-016TVX8LEE`, commit `7afed08`)

**Contexto.** O snippet GA4 existente usava um ID placeholder (`G-QWEN3827B`)
que não coletava dados. Carregava script à toa, adicionando requisição externa
e footprint de privacidade.

**Decisão.** Remover GA4. Não incluir nenhum analytics até que haja um ID
válido e uma decisão explícita de medir tráfego.

**Consequências.**
- Zero medição de tráfego até decisão deliberada. *(A decisão veio no mesmo
  dia — ver ADR-007.)*
- Quando reativar, avaliar alternativas privacy-first (Plausible, Umami)
  antes de voltar ao GA4. *(Avaliadas no ADR-007; GA4 venceu pela integração
  com Search Console/Looker Studio e `anonymize_ip`.)*
- O `preconnect` para `googletagmanager.com` em `0fc7b79` tornou-se órfão —
  *deixou de ser problema: a tag gtag async do `7afed08` o substituiu; hoje
  não existe nenhum `preconnect` no `index.html`.*

---

## ADR-005 — Deploy automático via Vercel conectada ao repositório

**Data:** 2026-08-15  
**Status:** Aceito

**Contexto.** Deploy por upload manual permitia que site e repositório
divergissem silenciosamente — já tinha acontecido.

**Decisão.** Conectar o repositório à Vercel. `main` = produção; cada PR
ganha deploy de pré-visualização.

**Consequências.**
- Elimina a classe de bugs "site não reflete o repo".
- `vercel.json` ganha caching headers (assets imutáveis 1 ano), security
  headers e redirects.
- Cada push em `main` publica automaticamente.

---

## ADR-006 — Documentação centralizada em `docs/`

**Data:** 2026-08-15  
**Status:** Aceito

**Contexto.** A documentação do projeto estava apenas no `README.md` da raiz,
sem registro contínuo de mudanças, decisões ou roadmap. O projeto cresceu
em complexidade (SEO técnico, acessibilidade, design system) e precisa de
memória institucional.

**Decisão.** Criar pasta `docs/` com documentação estruturada:
`CHANGELOG.md` (mudanças), `HISTORICO.md` (narrativa de decisões),
`DECISIONS.md` (ADRs), `ROADMAP.md` (próximos passos) e `README.md` (guia
da documentação). O `README.md` da raiz mantém-se como introdução ao projeto
e aponta para `docs/`. Os documentos iniciados na raiz (`CHANGELOG.md`,
`HISTORICO.md`, `ROADMAP.md`) foram consolidados em `docs/`; a raiz ficou
apenas com stubs de redirecionamento (task `t_2e42bec9`).

**Consequências.**
- Documentação viva, mantida pelo Arquivista (job diário às 20h no perfil
  do Arquivista executa `~/.hermes/scripts/daily_doc.py`).
- `README.md` da raiz não é duplicado — é a porta de entrada; `docs/` é o
  registro contínuo.
- Mudanças futuras devem ser refletidas no CHANGELOG antes do commit.

---

## ADR-007 — GA4 real com IP anonimizado

**Data:** 2026-08-15  
**Status:** Aceito  
**Supera:** ADR-004

**Contexto.** O ADR-004 removeu o snippet GA4 porque o ID era um placeholder
falso (`d554f7c`, 16:36). Horas depois o Bruno decidiu medir o tráfego de
verdade: o agente atlas criou a propriedade real **QWEN38-27B-LANDING**
(ID 549987691) na conta Google do projeto, e o commit `7afed08` (17:04)
instalou o Measurement ID **G-016TVX8LEE**. A "decisão explícita" que o
ADR-004 exigia foi tomada.

**Decisão.** Usar GA4 com o ID real: tag assíncrona com
`anonymize_ip: true`. O enhanced measurement do stream cobre `page_view`,
`scroll`, `click_outbound`, `file_download`, `site_search` e `video_*`;
eventos custom: `scroll_depth` (25/50/75/100%) e helper `qwenTrackSearch()`.

**Alternativas consideradas.**
1. *Manter sem analytics (ADR-004).* Zero dados — mas o projeto passou a ter
   metas de tráfego explícitas (ver ROADMAP) e não se gerencia o que não se
   mede.
2. *Plausible/Umami (privacy-first).* Exigiriam serviço/conta adicional;
   descartados por enquanto — o Bruno já opera o ecossistema Google
   (Search Console, Looker Studio).
3. *GA4 com IP anonimizado.* Gratuito, integra nativamente com Search
   Console e Looker Studio; `anonymize_ip` mitiga o custo de privacidade.

**Consequências.**
- Tráfego mensurável desde 2026-08-15; as metas do ROADMAP passam a ter
  denominador.
- O `preconnect` órfão de `googletagmanager.com` (consequência pendente do
  ADR-004) deixou de existir: a tag async o substituiu — nenhuma limpeza
  pendente.
- Uma requisição externa a `googletagmanager.com` volta a existir — é a
  única dependência externa da página, aceitável pelo valor da medição.

---

## ADR-008 — `applicationCategory: "AIModel"` como extensão consciente de schema

**Status.** Aceita (2026-08-16) · **Task:** t_11224bcd

**Contexto.** A enumeração oficial de `applicationCategory` (schema.org) não tem
valor para "modelo de linguagem". O projeto usa `SoftwareApplication` para as
entidades de modelo (Qwen3.8-27B na home, Muse Glimmer 30B no artigo) e precisa
de uma categoria que diga o que a coisa é — para rich results clássicos e,
principalmente, para crawlers de IA (GEO/AEO), objetivo declarado do site.

**Decisão.** Manter `applicationCategory: "AIModel"` — extensão consciente do
vocabulário: schema.org aceita texto livre no campo, e o alvo é compreensão de
entidade por LLMs/crawlers de IA, não apenas elegibilidade de rich result
clássico do Google.

**Alternativas consideradas.**
1. *`BusinessApplication` / `EducationalSoftware`* (valores da enum) — errados:
   nenhum descreve modelo de linguagem.
2. *Omitir o campo* — perde o sinal semântico mais forte para consumidores de IA.
3. *`AIModel` como texto livre* — não-padrão porém válido; risco limitado a
   warnings de vocabulário em validadores estritos.

**Consequências.**
- Entidades ficam auto-descritivas para crawlers de IA (llms.txt + JSON-LD
  coerentes).
- Rich Results Test pode exibir warning de categoria fora da enum — aceito e
  documentado aqui.
- Se schema.org incorporar categoria de modelo de IA no futuro, migrar é
  busca-e-substituição em 2 nodes (`#software` da home, `#software` do Muse).
