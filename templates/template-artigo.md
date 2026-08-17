---
layout: artigo
title: "[TÍTULO DO ARTIGO]"
date: YYYY-MM-DD
author: "Time Hermes"
tags: [modelos, 30B, local, hardware]
tipo: artigo
---

# [TÍTULO DO ARTIGO]

> *Resumo em uma linha — o que o leitor vai aprender.*

## 🔍 Contexto

2-3 parágrafos: por que esse tópico importa, o que mudou no ecossistema, qual o
gatilho para este artigo (novo modelo, benchmark, hardware, paper).

## ⚙️ Detalhes técnicos

- **Modelo / Hardware / Tópico:** nome e link oficial
- **Parâmetros:** XB
- **Contexto:** XX tokens
- **Quantização disponível:** GGUF / AWQ / GPTQ / BnB
- **Hardware mínimo:** RAM/VRAM recomendada
- **Licença:** Apache 2.0 / CC BY-NC / outra

## 📊 Benchmark (se aplicável)

| Modelo | Params | MMLU | GPQA | HumanEval | Velocidade (tok/s) |
|--------|--------|------|------|-----------|-------------------|
| Este   | XB     | XX%  | XX%  | XX%       | XX tok/s (Strix Halo) |
| Comparable 1 | YB | YY% | YY% | YY% | YY tok/s |

*Benchmarks em hardware local (AMD Strix Halo, 40GB VRAM, Ollama/Qwen).*

## 💻 Como rodar local

**Requisitos:**
- RAM: X GB | VRAM: Y GB
- Ollama / llama.cpp / HuggingFace Transformers

**Passo a passo:**

```bash
# Exemplo com Ollama
ollama pull [modelo]
ollama run [modelo] "Seu prompt aqui"
```

**Dica de hardware:** [placa recomendada + expectativa de performance]

## 🗣️ Reações da comunidade

- Trending no HuggingFace: ⭐ XX likes
- Reddit r/LocalLLaMA: [link para thread]
- GitHub: [link para issues/discussions]

## 📚 Leia mais

- [Link oficial do modelo / hardware]
- [Paper original]
- [Nosso guia de hardware local](/hardware)
- [Benchmarks completos](/benchmarks)

---

*Publicado pelo Time Hermes · [qwen38-27b-landing.vercel.app](https://qwen38-27b-landing.vercel.app)*

---

## Head obrigatório (copiar do artigo mais recente)

Todo artigo novo deve copiar o `<head>` completo do artigo mais recente (guia/*/index.html). O script `scripts/check_head.py` valida antes de cada merge.

Bloco de referência (token igual em todas as páginas):

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="google-site-verification" content="tfpagcfTcW5Dv8rv3Rwa1rxtkKJ9qO1LCMu1zsGZdYQ" />
<!-- + title, description, robots, canonical, OG/Twitter, gtag GA4 G-016TVX8LEE (ver index.html) -->
```

**Regra:** herdar o head do artigo mais recente. `check_head.py` é o gate — merge bloqueia se falhar.