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
**Status:** Aceito

**Contexto.** O snippet GA4 existente usava um ID placeholder (`G-QWEN3827B`)
que não coletava dados. Carregava script à toa, adicionando requisição externa
e footprint de privacidade.

**Decisão.** Remover GA4. Não incluir nenhum analytics até que haja um ID
válido e uma decisão explícita de medir tráfego.

**Consequências.**
- Zero medição de tráfego até decisão deliberada.
- Quando reativar, avaliar alternativas privacy-first (Plausible, Umami)
  antes de voltar ao GA4.
- O `preconnect` para `googletagmanager.com` em `0fc7b79` tornou-se órfão e
  deve ser removido na próxima limpeza.

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
e aponta para `docs/`.

**Consequências.**
- Documentação viva, mantida pelo Arquivista (cron job diário 20h).
- `README.md` da raiz não é duplicado — é a porta de entrada; `docs/` é o
  registro contínuo.
- Mudanças futuras devem ser refletidas no CHANGELOG antes do commit.
