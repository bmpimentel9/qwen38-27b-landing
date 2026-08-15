# 📖 HISTÓRICO — Projeto SEO Local Models 30B

> Narrativa das principais decisões, marcos e contexto do projeto.
> Um diário de bordo do que aconteceu e por quê.

---

## 2026-08-15 — Fundação do projeto

Bruno pediu a criação de um projeto para o time SEO atuar: um portal sobre
**modelos locais de 30B de parâmetros**, tendo como base o repositório
GitHub `qwen38-27b-landing` (já deployado na Vercel).

**O que foi feito:**
- Projeto `seo-local-models-30b` criado no Hermes com board kanban
- Repositório clonado localmente em `~/qwen38-27b-landing`
- Três tasks principais criadas para o time SEO (seo, seo-content, seo-tech)
- O time SEO entregou 15 tasks no total: sitemap, robots.txt, guia completo
  (5 subpáginas), FAQ, JSON-LD estruturado, GA4 tagging, performance

**Pipeline de evolução diária:**
Cron às 7h pesquisa HuggingFace + arXiv → cria card kanban → discovery
valida → seo-content escreve artigo → redator revisa → seo-tech faz deploy

---

## 2026-08-15 — GA4 instalado

O agente **atlas** criou uma propriedade GA4 real no Google Analytics
usando o navegador Chrome já logado na conta do Bruno.

- Measurement ID: **G-016TVX8LEE**
- Eventos configurados: page_view, scroll_depth, search
- Propriedade: QWEN38-27B-LANDING (ID 549987691)
- Looker Studio travou (UI scrolling loop) — tracking já coleta dados

---

## 2026-08-15 — Navegação responsiva

Bruno reportou que o menu não aparecia no celular. O time SEO havia
configurado o CSS para esconder o nav em telas <900px (`display: none`)
sem hamburguer alternativo.

**Solução:** Adicionado botão ☰ com dropdown flutuante. Links corrigidos
para cleanUrls (`/modelos` em vez de `modelos.html`).

---

## 2026-08-15 — Arquivista

Bruno pediu um agente dedicado a documentação e organização, para manter
todos os projetos 100% organizados. Criado o perfil **arquivista**,
headless, que mantém CHANGELOG, DECISIONS, HISTORICO, ROADMAP e organização
do repositório.