# Estratégia SEO & Keyword Map — Guia Qwen3.8-27B

## Visão Geral

O Guia Qwen3.8-27B é um content hub (pillar + spokes) focado no modelo de linguagem Qwen3.8-27B (27B denso, Apache 2.0, 262K contexto, multimodal nativo). A estratégia segue o modelo hub-and-spoke: a página /guia/ é a pillar page, e cada artigo é um spoke que linka de volta ao pillar e entre si. A landing page principal (/) permanece intacta e linka para o guia.

## Arquitetura de Conteúdo (Topic Cluster)

```
                    [Landing: /]
                         |
                    [Pillar: /guia/]
                   /    |    |    |    \
                  /     |    |    |     \
     [Benchmarks] [Hardware] [Como Rodar] [Comunidade] [FAQ]
    /guia/bench   /guia/hw  /guia/rodar  /guia/comunidade /guia/faq
```

Cada spoke tem internal links para o pillar e para os outros spokes relevantes. O pillar linka para todos os spokes. A landing page principal linka para o pillar. Isso cria uma estrutura de linkagem interna forte que o Google usa para entender a autoridade topical.

## URLs e Estrutura

| Página | URL | Canonical |
|--------|-----|-----------|
| Landing principal | / | https://qwen38-27b-landing.vercel.app/ |
| Pillar (guia) | /guia/ | https://qwen38-27b-landing.vercel.app/guia/ |
| Benchmarks | /guia/benchmarks-comparativos | https://qwen38-27b-landing.vercel.app/guia/benchmarks-comparativos |
| Hardware | /guia/hardware-local | https://qwen38-27b-landing.vercel.app/guia/hardware-local |
| Como Rodar | /guia/como-rodar | https://qwen38-27b-landing.vercel.app/guia/como-rodar |
| Comunidade | /guia/comunidade-casos-uso | https://qwen38-27b-landing.vercel.app/guia/comunidade-casos-uso |
| FAQ | /guia/faq | https://qwen38-27b-landing.vercel.app/guia/faq |

## Keyword Map por Página

### Pillar: /guia/
| Keyword | Tipo | Intenção | Volume Est. | KD |
|---------|------|---------|-------------|-----|
| qwen3.8 27b | head | informacional | médio | 12 |
| guia qwen3.8 | long-tail | informacional | baixo | 5 |
| qwen3.8-27b modelo local | medium | informacional | baixo-médio | 10 |
| llm local 27b | long-tail | informacional | baixo | 8 |
| modelo ia local apache 2.0 | long-tail | informacional | baixo | 6 |

**Title tag:** Guia Qwen3.8-27B — Modelo Local de 27B Parâmetros, Apache 2.0 (59 chars)
**Meta description:** Guia completo do Qwen3.8-27B: modelo denso de 27B com 262K de contexto, Apache 2.0. Benchmarks, hardware, instalação (Ollama, llama.cpp, vLLM), casos de uso e FAQ. (155 chars)

### Spoke 01: Benchmarks Comparativos
| Keyword | Tipo | Intenção | Volume Est. | KD |
|---------|------|---------|-------------|-----|
| qwen3.8 27b benchmark | long-tail | informacional | médio | 10 |
| qwen3.8-27b vs gpt-oss-20b | long-tail | informacional | baixo | 6 |
| benchmark llm local | medium | informacional | médio | 18 |
| qwen3.8 desempenho | long-tail | informacional | baixo | 8 |
| modelos 30b comparativo | long-tail | informacional | baixo | 10 |
| gpqa qwen3.8 | long-tail | informacional | baixo | 5 |
| qwen3.8 vs qwen3.6 | long-tail | informacional | médio | 12 |

**Title tag:** Qwen3.8-27B vs Outros Modelos ~30B: Benchmarks Comparativos (57 chars)
**Meta description:** Comparativo completo de benchmarks do Qwen3.8-27B vs modelos de escala similar. LiveCodeBench, SWE-bench, OSWorld, GPQA, 26 resultados do model card oficial. (152 chars)

### Spoke 02: Guia de Hardware
| Keyword | Tipo | Intenção | Volume Est. | KD |
|---------|------|---------|-------------|-----|
| hardware para llm local | medium | transacional | médio | 15 |
| vram qwen3.8 27b | long-tail | informacional | médio | 8 |
| gpu para ia | medium | transacional | alto | 25 |
| requisitos qwen3.8 | long-tail | informacional | baixo | 6 |
| rodar qwen3.8 local | long-tail | transacional | médio | 10 |
| rtx 4090 llm | long-tail | informacional | médio | 12 |
| quanto vram para 27b | long-tail | informacional | médio | 8 |
| rodar ia no mac | long-tail | informacional | médio | 15 |

**Title tag:** Guia de Hardware para Rodar o Qwen3.8-27B Localmente (51 chars)
**Meta description:** Requisitos de VRAM, GPU, RAM e CPU para rodar o Qwen3.8-27B localmente. Tabela por nível de quantização, setups recomendados e dicas de configuração. (150 chars)

### Spoke 03: Como Rodar
| Keyword | Tipo | Intenção | Volume Est. | KD |
|---------|------|---------|-------------|-----|
| como rodar qwen3.8 27b local | long-tail | transacional | médio | 8 |
| ollama qwen3.8 | long-tail | transacional | alto | 12 |
| llama.cpp qwen3.8 | long-tail | transacional | médio | 10 |
| vllm qwen3.8 | long-tail | transacional | baixo | 6 |
| huggingface qwen3.8 | long-tail | informacional | médio | 8 |
| instalar qwen3.8 localmente | long-tail | transacional | alto | 15 |
| ollama install qwen3.8 | long-tail | transacional | médio | 8 |

**Title tag:** Como Rodar o Qwen3.8-27B Localmente: Ollama, llama.cpp, vLLM, HuggingFace (70 chars)
**Meta description:** Guia passo a passo para rodar o Qwen3.8-27B localmente via Ollama, llama.cpp, vLLM e HuggingFace. Comandos, configurações, dicas de performance e troubleshooting. (152 chars)

### Spoke 04: Comunidade e Casos de Uso
| Keyword | Tipo | Intenção | Volume Est. | KD |
|---------|------|---------|-------------|-----|
| qwen3.8 27b casos de uso | long-tail | informacional | baixo | 6 |
| qwen3.8 comunidade | long-tail | informacional | baixo | 5 |
| llm local aplicação | long-tail | informacional | médio | 12 |
| ia local programação | long-tail | informacional | médio | 12 |
| modelo local reddit | long-tail | informacional | baixo | 8 |
| qwen3.8 hacker news | long-tail | informacional | baixo | 5 |

**Title tag:** Comunidade e Casos de Uso Reais do Qwen3.8-27B (48 chars)
**Meta description:** Reações da comunidade (Hacker News, r/LocalLLaMA, X) e casos de uso reais do Qwen3.8-27B: programação agêntica, uso de computador, análise de documentos. (150 chars)

### Spoke 05: FAQ
| Keyword | Tipo | Intenção | Volume Est. | KD |
|---------|------|---------|-------------|-----|
| faq qwen3.8 27b | long-tail | informacional | baixo | 4 |
| dúvidas qwen3.8 | long-tail | informacional | baixo | 5 |
| perguntas frequentes llm local | long-tail | informacional | baixo | 5 |
| qwen3.8 ollama dúvidas | long-tail | informacional | baixo | 3 |
| o que é atenção híbrida | long-tail | informacional | médio | 10 |
| quantização llm explicação | long-tail | informacional | médio | 10 |
| thinking mode qwen3.8 | long-tail | informacional | baixo | 5 |

**Title tag:** FAQ — Perguntas Frequentes sobre o Qwen3.8-27B (46 chars)
**Meta description:** Perguntas frequentes sobre o Qwen3.8-27B. Respostas diretas sobre hardware, performance, quantização, thinking mode, multimodalidade, licença e mais. (150 chars)

## Análise de Intenção de Busca

### TOFU (Top of Funnel) — Informacional
- "o que é qwen3.8 27b" → Pillar
- "o que é atenção híbrida" → FAQ
- "qwen3.8 27b benchmark" → Benchmarks
- "o que é thinking mode" → FAQ
- "qwen3.8 comunidade" → Comunidade

### MOFU (Middle of Funnel) — Pesquisa/Comparação
- "qwen3.8 vs qwen3.6" → Benchmarks
- "qwen3.8-27b vs gpt-oss-20b" → Benchmarks
- "denso vs moe llm" → FAQ
- "ollama vs llama.cpp" → Como Rodar + FAQ
- "rtx 4090 vs 5090 para ia" → Hardware

### BOFU (Bottom of Funnel) — Transacional/Ação
- "como rodar qwen3.8 27b local" → Como Rodar
- "instalar qwen3.8 localmente" → Como Rodar
- "comprar gpu para ia" → Hardware (checklist de compra)
- "baixar qwen3.8 gguf" → Como Rodar
- "ollama run qwen3.8" → Como Rodar

## Featured Snippet Targets

Cada página foi estruturada para capturar featured snippets:

1. **Pillar (/guia/):** "o que é qwen3.8 27b" — definido no H2 "O que é o Qwen3.8-27B?"
2. **Benchmarks:** "qwen3.8 27b benchmark" — tabela comparativa como resposta direta
3. **Hardware:** "vram qwen3.8 27b" — tabela de VRAM por quantização como resposta direta
4. **Como Rodar:** "como rodar qwen3.8 27b" — passo a passo numerado
5. **FAQ:** "o que é atenção híbrida" — parágrafo de definição clara
6. **FAQ:** "qual gpu para qwen3.8 27b" — lista direta de GPUs recomendadas

## Estratégia de Internal Linking

### Links implementados:
- Landing (/) → Pillar (/guia/)
- Pillar → todos os spokes (card grid)
- Pillar → Landing (card "Landing Page Oficial")
- Benchmarks → Hardware, Como Rodar, Landing
- Hardware → Como Rodar, Benchmarks, FAQ
- Como Rodar → Hardware, FAQ, Comunidade
- Comunidade → Como Rodar, FAQ, Benchmarks
- FAQ → Como Rodar, Comunidade, Benchmarks, Hardware
- Todos → Pillar (nav)

### Anchor texts otimizados:
- "tabela completa de VRAM por quantização" (Hardware)
- "guia passo a passo: como rodar o Qwen3.8-27B" (Como Rodar)
- "guia de instalação" (Como Rodar)
- "requisitos de hardware" (Hardware)
- "FAQ completo" (FAQ)
- "casos de uso da comunidade" (Comunidade)
- "comparativos de benchmarks" (Benchmarks)
- "landing page oficial" (Landing)

## PAA (People Also Ask) Targets

Perguntas para capturar do Google PAA:

1. "Quanto de VRAM para rodar Qwen3.8-27B?" → Hardware (tabela) + FAQ
2. "Qwen3.8-27B roda em RTX 3090?" → Hardware (tier mínimo) + FAQ
3. "Qual a diferença entre Qwen3.8 e Qwen3.6?" → Benchmarks + FAQ
4. "Como instalar Qwen3.8 no Ollama?" → Como Rodar (passo a passo)
5. "Qwen3.8-27B fala português?" → FAQ
6. "O que é thinking mode no Qwen3.8?" → Como Rodar + FAQ
7. "Qwen3.8-27B vs ChatGPT: qual é melhor?" → FAQ
8. "Consigo rodar Qwen3.8 sem placa de vídeo?" → Hardware (CPU) + FAQ
9. "O que é atenção híbrida?" → FAQ
10. "Qwen3.8-27B é denso ou MoE?" → Pillar + FAQ

## Oportunidades de Expansão (Cluster Expansion)

Para futuro crescimento do cluster:

1. **Qwen3.8-27B no Mac: Guia MLX Detalhado** — tutorial específico para Apple Silicon
2. **Fine-tuning do Qwen3.8-27B com Unsloth** — tutorial prático
3. **RAG Local com Qwen3.8-27B + ChromaDB** — guia de implementação
4. **Qwen3.8-27B como API com vLLM em produção** — guia de deploy
5. **Multimodalidade na prática: analisando imagens com Qwen3.8-27B** — guia visual
6. **Otimização de Performance: Flash Attention, KV Cache, Tensor Parallel** — deep dive técnico
7. **Qwen3.8-27B vs DeepSeek (local vs API)** — head-to-head
8. **Computer Use com Qwen3.8-27B: automatizando tarefas de desktop** — guia agêntico

## Notas Técnicas SEO

- Todas as páginas têm `<html lang="pt-BR">`
- Title tags entre 46-70 chars (ideal ≤60)
- Meta descriptions entre 150-155 chars
- Headings hierárquicos: H1 único → H2 seções → H3 subseções
- Tabelas para dados comparativos (Google favorece tables para featured snippets)
- Canonical URLs absolutos em todas as páginas (https://qwen38-27b-landing.vercel.app/...)
- OG tags (og:type, og:title, og:description, og:url) em todas as 6 páginas
- Navegação consistente em todas as páginas (nav com 7 links: Home, Guia, Benchmarks, Hardware, Como Rodar, Comunidade, FAQ)
- CSS inline em cada página (sem dependência externa — funciona offline)
- Links internos com anchor text otimizada
- Callouts e tips para destacar informações-chave
- Estrutura de diretórios: /guia/ (pillar) + /guia/artigo/ (spokes) — URLs limpas

## Dados do Modelo (baselados na landing live e fontes oficiais)

- **Modelo:** Qwen3.8-27B (denso, não MoE)
- **Parâmetros:** 27B (todos ativos por token)
- **Camadas:** 64
- **Contexto nativo:** 262.144 tokens
- **Contexto extensível:** 1.000.000 (RoPE scaling)
- **Atenção:** Híbrida (16 × 3×DeltaNet → 1×Gated Attn)
- **Multimodalidade:** Nativa (texto, imagem, vídeo, documentos)
- **Licença:** Apache 2.0
- **Lançamento:** 14 de agosto de 2026
- **Hugging Face:** Qwen/Qwen3.8-27B (9.69k likes)
- **Ollama:** qwen3.8:27b (18GB, 256K contexto, 67.1K downloads)
- **VRAM 4 bits:** ~14–17 GB
- **VRAM FP8:** ~27 GB
- **VRAM BF16:** ~54 GB
- **vLLM:** ≥ 0.27.2
- **Benchmarks:** 26 publicados (LiveCodeBench 90,3, OSWorld 84,3, GPQA 89,2, MathVision 94,6)
- **Throughput (Strix Halo, Q5_K_M):** 10,6 tok/s decode
