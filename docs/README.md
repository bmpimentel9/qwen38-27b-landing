# Documentação do projeto

Esta pasta centraliza a documentação viva do projeto **Qwen3.8-27B landing
page**. O `README.md` da raiz descreve o projeto para quem chega; aqui fica o
registro contínuo — o que mudou, por que mudou, o que foi decidido e o que vem
depois.

## Estrutura

| Arquivo         | Função                                                  | Quando é atualizado                          |
| --------------- | ------------------------------------------------------- | -------------------------------------------- |
| `CHANGELOG.md`  | Registro semântico de mudanças por versão/data          | A cada commit ou task concluída              |
| `HISTORICO.md`  | Narrativa de decisões com contexto e alternativas       | Sempre que uma decisão importante é tomada   |
| `DECISIONS.md`  | ADRs leves (Architecture Decision Records)              | Sempre que uma decisão arquitetural é tomada |
| `ROADMAP.md`    | Próximos passos com base no board do kanban             | Semanalmente ou quando o board muda           |

## Convenções

- **Idioma**: português (PT-BR) em todos os documentos.
- **Datas**: formato ISO `YYYY-MM-DD`.
- **CHANGELOG**: ordem reversa (mais recente primeiro), seguindo o formato
  [Keep a Changelog](https://keepachangelog.com/). Seções: `Added`, `Changed`,
  `Fixed`, `Removed`.
- **HISTORICO**: cada entrada tem data, contexto, alternativas consideradas,
  decisão e rationale. É narrativo — conta a história, não só o fato.
- **DECISIONS**: cada ADR tem título, contexto, decisão e consequências.
  Numerados sequencialmente (`ADR-001`, `ADR-002`, …).
- **ROADMAP**: itens ordenados por prioridade, com origem (task kanban, ideia,
  feedback) e estado.
- **Autor**: tarefas automatizadas do Arquivista são assinadas como
  `Arquivista (Hermes)`; commits manuais do Bruno mantêm a autoria original.

## Fontes

- Commits do Git (histórico do repositório).
- Board do kanban (`seo-local-models-30b`).
- Discussões e decisões registradas em tarefas e revisões.

## Manutenção

A documentação é mantida pelo **Arquivista**, o agente de documentação do
Hermes. Um job do agendador do Hermes (diário, 20h, perfil `arquivista`)
executa `~/.hermes/scripts/daily_doc.py`, que compila as tasks concluídas
no CHANGELOG e faz commit + push quando há mudanças; decisões e roadmap são
atualizadas conforme eventos acontecem.

Para sugerir mudanças, abra uma issue ou edite diretamente — todo documento é
texto plano versionado junto com o código.
