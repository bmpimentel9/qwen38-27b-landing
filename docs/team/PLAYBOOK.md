# 🏗️ PLAYBOOK — Time Hermes: Metodologia de Operação

> Este documento é o **manual vivo** de como times de agentes autônomos operam.
> Criado a partir do projeto piloto `seo-local-models-30b` (Qwen3.8-27B Landing).
> Versão: 0.1.0 | Data: 2026-08-15

---

## 1. Filosofia

> *"Agentes fazem, humanos decidem."*

O time Hermes opera em **camadas de autonomia progressiva**:

| Nível | O que acontece | Quem valida |
|---|---|---|
| **1. Automático** | Crons, scripts, coleta de dados, deploy | Ninguém — execução segura e reversível |
| **2. Supervisionado** | Criação de cards, sugestões, artigos | QA automatizado + Arquivista documenta |
| **3. Gate humano** | Publicação de conteúdo, mudanças irreversíveis, decisões estratégicas | Bruno aprova explicitamente |

---

## 2. Arquitetura do Time

### 2.1 Perfis de Agentes

| Perfil | Tipo | Função | Acionado por |
|---|---|---|---|
| **Product Owner** | Headless | Sugere melhorias SEO/GEO, analisa concorrência, cria cards | Cron 6h |
| **Arquivista** | Headless | Documenta tasks, mantém CHANGELOG, organiza repo | Cron 20h + Kanban |
| **Daily Research** | Script | Coleta modelos, papers, concorrentes | Cron 7h |
| **Discovery** | Headless | Valida temas de pesquisa, curadoria | Kanban dispatcher |
| **SEO Content** | Headless | Escreve artigos PT-BR | Kanban dispatcher |
| **Redator** | Headless | Revisa tom e clareza | Kanban dispatcher |
| **SEO Tech** | Headless | Publica, configura infra, SEO técnico | Kanban dispatcher |
| **SEO** | Headless | Estratégia de busca, GEO, Search Console | Kanban dispatcher |
| **Atlas** | Headless | Métricas, GA4, dashboards | Kanban dispatcher |
| **QA** | Headless | Valida qualidade de entregas | Kanban dispatcher (automático) |
| **Programadora** | Headless | Correções técnicas, auto-cura | Kanban dispatcher |
| **Dani** | Conversacional | Interface única com Bruno, orquestradora | Mensagem do Bruno |

### 2.2 Como criar um novo agente

**Pré-requisitos:**
- Propósito definido em 1 frase
- Nome em lowercase (≤20 chars)
- Tipo: headless (kanban worker) ou conversacional (com Telegram)

**Passo a passo:**
```bash
# 1. Criar perfil (headless)
hermes profile create <nome> --clone-from seo --description "<propósito>"

# 2. Escrever SOUL.md (personalidade, sistema de trabalho, regras)
#    Local: ~/.hermes/profiles/<nome>/SOUL.md

# 3. Profile.yaml com description (essencial pro dispatcher rotear)
#    Local: ~/.hermes/profiles/<nome>/profile.yaml

# 4. Testar:
hermes -p <nome> chat -q "Teste de fumaça"
```

**Para adicionar ao time de um projeto:**
1. Criar kanban card com assignee=<nome>
2. Dispatcher encontra pelo profile.yaml description
3. Cron pode ser configurado se necessário

### 2.3 Como criar um novo projeto

```bash
# 1. Criar projeto Hermes
hermes project create <nome-projeto> --description "<descrição>"

# 2. Clonar/clonar repositório
gh repo clone <org>/<repo> ~/<repo>

# 3. Adicionar pasta ao projeto
hermes project add-folder <nome-projeto> ~/<repo> --primary

# 4. Criar board kanban
hermes kanban boards create <nome-projeto>
hermes project bind-board <nome-projeto> <nome-projeto>

# 5. Inicializar documentação (Arquivista)
#    Criar CHANGELOG.md, HISTORICO.md, ROADMAP.md, DECISIONS.md

# 6. Configurar time padrão:
#    - Product Owner (cron 6h) — se aplicável
#    - Arquivista (cron 20h)
#    - Tasks iniciais no kanban

# 7. Verificar:
#    - hermes project show <nome-projeto>
#    - hermes kanban stats
```

---

## 3. Ciclo de Evolução Diária

### 3.1 Linha do tempo

```
 06:00 ─ PO acorda ──────────────────────────────────────────────
         │ Lê: CHANGELOG, ROADMAP, kanban, llms.txt, sitemap, robots
         │ Analisa: keywords, concorrência, GEO, gaps de conteúdo
         │ Cria: 1-3 cards de melhoria (SEO/GEO/conteúdo)
         │ Saída: Cards [PO] no board
         ─────────────────────────────────────────────────────────

 07:00 ─ Research acorda ─────────────────────────────────────────
         │ Coleta: HF Trending, arXiv papers, blogs concorrentes
         │ Cria: 1 card daily-content com temas candidatos
         │ Saída: Card discovery
         ─────────────────────────────────────────────────────────

 07h-18h ─ Dispatcher (a cada 30min) ─────────────────────────────
         │ Pega cards ready → assigna ao perfil correto
         │ Profile executa → QA valida → PASS ou FAIL
         │ FAIL → card de correção automático
         │ PASS → task concluída
         ─────────────────────────────────────────────────────────

 20:00 ─ Arquivista ──────────────────────────────────────────────
         │ Varre tasks concluídas do dia
         │ Atualiza CHANGELOG (Added/Fixed/Changed/Removed)
         │ Verifica HISTORICO, ROADMAP
         │ Push automático → Vercel deploy
         ─────────────────────────────────────────────────────────
```

### 3.2 Fluxo de uma task

```
┌──────────┐    ┌──────────────┐    ┌──────────┐    ┌──────┐    ┌───────────┐
│  Bruno   │───>│    Kanban    │───>│Dispatcher│───>│Profile│───>│    QA     │
│ (card)   │    │  (ready)     │    │          │    │(worker)│    │(validação)│
└──────────┘    └──────────────┘    └──────────┘    └──────────┘    └─────┬─────┘
                                                                         │
                                               ┌─────────────────────────┤
                                               │                         │
                                          ┌────▼────┐             ┌─────▼──────┐
                                          │  PASS   │             │    FAIL    │
                                          │(completa)│            │(cria card  │
                                          └────┬────┘             │ correção)  │
                                               │                  └─────┬──────┘
                                          ┌────▼────┐                   │
                                          │Arquivista│                  ▼
                                          │documenta│            ┌──────────────┐
                                          └─────────┘            │ Dispatcher   │
                                                                 │ re-tenta     │
                                                                 └──────────────┘
```

### 3.3 Gatilhos

| Gatilho | O que acontece | Autonomia |
|---|---|---|
| Cron 6h | PO analisa e cria cards | Autônomo (se não houver nada, 0 cards) |
| Cron 7h | Research coleta dados | Autônomo |
| Task criada no kanban | Dispatcher pega no próximo tick | Autônomo |
| QA FAIL | Card de correção automático | Autônomo (até 3 rounds) |
| QA PASS 3º FAIL | Task vai pra Bruno decidir | **Gate humano** |
| Publicação de conteúdo | Vercel deploy automático | Autônomo |
| Mudança irreversível | Bruno precisa aprovar | **Gate humano** |
| Card bloqueado >24h | Sentinela notifica Bruno | **Gate humano** |

---

## 4. Documentação

### 4.1 Documentos obrigatórios por projeto

| Documento | Função | Mantido por | Frequência |
|---|---|---|---|
| `README.md` | Visão geral, como contribuir | Arquivista | Sempre atual |
| `CHANGELOG.md` | Histórico de versões (Keep a Changelog) | Arquivista | Diário |
| `HISTORICO.md` | Narrativa de decisões e contexto | Arquivista | Por evento |
| `ROADMAP.md` | Próximos passos e metas | PO + Arquivista | Semanal |
| `DECISIONS.md` | ADRs (Architecture Decision Records) | Arquivista | Por decisão |
| `docs/TEAM-PLAYBOOK.md` | Este documento — metodologia de operação | Dani | Contínuo |

### 4.2 Template de ADR (DECISIONS.md)

```markdown
## [2026-MM-DD] — Título da decisão

**Contexto:** Por que essa decisão foi necessária?

**Alternativas consideradas:**
- Alternativa A: (prós e contras)
- Alternativa B: (prós e contras)

**Decisão:** O que foi escolhido e por quê.

**Consequências:** O que muda a partir de agora.

**Task relacionada:** t_xxxxxxxx
```

---

## 5. Convite de Novas Equipes

### 5.1 Template para novo squad

```bash
# 1. Definir propósito do squad
# Ex: "Squad de vídeos: criar conteúdo em vídeo sobre modelos locais"

# 2. Criar perfil para cada membro do squad
hermes profile create <nome> --clone-from seo --description "<propósito>"

# 3. Escrever SOUL.md para cada um

# 4. Conectar ao kanban (tasks com assignee = <nome>)

# 5. Se precisar de cron:
hermes cron create \
  --name "<squad>-<funcao>" \
  --schedule "0 6 * * *" \
  --script "<script>" \
  --prompt "<missão>"
```

### 5.2 Regras para convidar novos agentes

1. **Sempre headless primeiro** — sem Telegram, sem gateway. Só kanban.
2. **Profile.yaml com description** — sem isso o dispatcher não acha.
3. **SOUL.md obrigatório** — sem personalidade o agente age genérico.
4. **Teste de fumaça** — `hermes -p <nome> chat -q "teste"` antes de colocar em produção.
5. **QA obrigatório** — toda entrega de agente novo passa pelo QA antes de virar task.

---

## 6. Pontos de Validação Humana

### 6.1 O que Bruno precisa aprovar

- **Publicação de conteúdo que impacta a marca**
- **Decisões irreversíveis** (apagar arquivos, deletar services, gastar dinheiro)
- **Cards bloqueados por 3+ rounds de QA** — o agente não consegue resolver sozinho
- **Novos agentes** — Bruno aprova o SOUL.md antes de ativar
- **Mudanças na arquitetura** — adicionar/remover agentes do time

### 6.2 O que NÃO precisa de aprovação

- Cards de melhoria do PO (Bruno vê de manhã e decide o que fazer)
- Rascunhos de artigos (só publicam após passar por QA + redator)
- Documentação do Arquivista (push automático)
- Coleta de dados (research, métricas)
- Correções técnicas dentro do mesmo escopo

---

## 7. Métricas de Saúde do Time

| Métrica | Como medir | Alerta |
|---|---|---|
| Tasks concluídas/dia | `hermes kanban stats` | <2 tasks/dia = time ocioso |
| Taxa de QA FAIL | Cards de correção / total tasks | >30% = processo quebrado |
| Tempo médio de task | Do ready ao done | >4h = gargalo |
| Cards bloqueados | `hermes kanban list --status blocked` | >0 há 24h = algo parou |
| Ciclos PO sem cards | Quantos dias PO não criou nada | >3 dias = projeto estagnado |

---

## 8. Próximos Passos (Evolução do Time)

- [ ] **Squad de Vídeos** — criar conteúdo em vídeo sobre modelos locais
- [ ] **Squad de Comunidade** — engajamento, fórum, contribuições
- [ ] **Newsletter automática** — resumo semanal dos artigos
- [ ] **Dashboard de saúde do time** — métricas em tempo real
- [ ] **Multi-idioma** — artigos em EN para alcance global
- [ ] **Feedback loop de GA4** — PO lê tráfego real e ajusta estratégia

---

> *"A medida de inteligência é a capacidade de mudar."* — Albert Einstein
>
> Este playbook é vivo. Toda semana o Arquivista revisa e atualiza.