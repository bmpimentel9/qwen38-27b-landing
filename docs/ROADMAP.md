# Roadmap

Próximos passos do projeto **Qwen3.8-27B landing page**, ordenados por
prioridade. Atualizado semanalmente ou quando o board do kanban muda.

**Board kanban:** `seo-local-models-30b`  
**Última atualização:** 2026-08-15

---

## Em andamento

### 📚 Estruturar documentação inicial — `t_f56140db`
- **Origem:** task kanban (Arquivista)
- **Estado:** em execução
- **Descrição:** Criar `docs/` com CHANGELOG, HISTORICO, DECISIONS, ROADMAP e
  README explicativo. Mover documentação da raiz para `docs/`.
- **Assignee:** arquivista

---

## Próximos passos (planejados)

### 1. Remover `preconnect` órfão de `googletagmanager.com`
- **Origem:** ADR-004 (consequência da remoção do GA4)
- **Prioridade:** baixa
- **Descrição:** O commit `0fc7b79` adicionou `preconnect` para
  `googletagmanager.com`, mas o GA4 foi removido no commit `d554f7c`. O
  `preconnect` tornou-se órfão — não pré-conecta a nada que a página use.
  Remover do `index.html`.

### 2. Decidir sobre analytics de tráfego
- **Origem:** ADR-004
- **Prioridade:** média
- **Descrição:** Decidir se o projeto terá analytics e qual ferramenta.
  Avaliar alternativas privacy-first (Plausible self-hosted, Umami) antes
  de voltar ao GA4. Bloqueado em decisão do Bruno.

### 3. Validar Core Web Vitals pós-font-stack
- **Origem:** commit `d554f7c` (troca de font stack)
- **Prioridade:** média
- **Descrição:** A troca de Google Fonts para font stack de sistema deveria
  ter baixado o LCP de 4,8s para < 1s. Validar com Lighthouse ou PageSpeed
  Insights na URL de produção. Registrar resultado no HISTORICO.

### 4. Consolidar métricas do projeto
- **Origem:** responsabilidade semanal do Arquivista
- **Prioridade:** baixa
- **Descrição:** Quando houver analytics configurado (depende do item 2),
  consolidar métricas de tráfego (GA4/Plausible), GitHub stars e engajamento
  em um relatório semanal em `docs/`.

---

## Backlog (ideias sem prioridade)

- **Internacionalização (i18n):** versão em inglês da página. O conteúdo é
  em pt-BR; uma versão EN ampliaria alcance. Depende de decisão de escopo.
- **Modo de comparação lado-a-side:** permitir comparar Qwen3.8-27B com
  modelos de fronteira selecionados pelo usuário.
- **Gráficos interativos:** os gráficos são SVG estático. Adicionar
  interatividade (hover detalhado, toggle de séries) sem quebrar o princípio
  de "zero dependências de runtime" exigiria JS vanilla — avaliar.
- **Testes automatizados:** a página é HTML estático, mas testes de
  regressão visual (Playwright/Percy) poderiam proteger contra quebras de
  layout em mudanças futuras.

---

## Concluído (referência)

- ✅ Landing page inicial (2026-08-14)
- ✅ Redesign Geist + 26 benchmarks (2026-08-14)
- ✅ Tradução pt-BR completa (2026-08-15)
- ✅ Deploy automático Vercel (2026-08-15)
- ✅ Tech SEO & Performance (2026-08-15)
- ✅ Fix performance/acessibilidade/SEO (2026-08-15)
- ✅ Estruturar documentação inicial (2026-08-15) — *este task*
