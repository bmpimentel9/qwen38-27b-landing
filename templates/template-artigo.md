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