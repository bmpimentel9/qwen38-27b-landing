# Changelog

Registro de mudanças do projeto **Qwen3.8-27B landing page / Portal de
Modelos Locais de 30B**.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
ordem reversa (mais recente primeiro). Datas em ISO `YYYY-MM-DD`.

---

## [2026-08-19] — Pilar "Melhores modelos locais de 30B" (t_f81bb139)

### Added
- **Página-hub `/guia/melhores-modelos-locais-30b`**: primeiro best-of do
  portal. Veredito por caso de uso (código → Qwen3.8-27B; agentes MCP →
  Muse Glimmer 30B; hardware 12–16 GB → GPT-OSS-20B; contexto 1M →
  DeepSeek V4 Flash), tabela mestra de 6 modelos com GGUF medido, contexto
  nativo e licença. DeepSeek V4 Flash como "o intruso da lista" (284B
  totais / 13B ativos) com rotulagem honesta de memória superior. JSON-LD:
  TechArticle + BreadcrumbList + ItemList (6) + FAQPage (6). Fecha o item
  "Página de comparação — tabela interativa de modelos ≤30B" do ROADMAP
  médio prazo (versão tabela estática; interativa é follow-up seo-tech).
- **Companions**: sitemap 26→27 URLs; llms.txt +5 stats + link da página;
  card no /guia (primeiro da grade, tag "Comparativo"); FAQ do portal +1
  Q&A (HTML + JSON-LD).
- **Fontes novas verificadas 19/08**: Muse Glimmer context length
  131.072+ e vocab 202.048 (model card); DeepSeek V4 Flash 284B/13B, 1M
  contexto, UD-IQ3_XXS 103 GB / 110 GB RAM mín (Unsloth); GPT-OSS-20B
  GGUF 11,27 GiB (llama.cpp #15396); Gemma 3 27B Q4_K_M 15,41 GB.

### Decisions
- DeepSeek V4 Flash entra por paridade de ativos/token (13B), não de
  totais — rotulado "intruso" em tabela, callout e FAQ para não gerar
  claim falso de que é ≤30B em memória.
- GPT-OSS-20B: GGUF 11,27 GiB como número principal (medido), "16 GB"
  do anúncio citado como "inclui contexto" — evita repetir o pattern do
  claim "roda em 13GB" sem fonte clara.

## [2026-08-19] — Artigo: Qwen3.8-27B está lento? 6 causas e fixes

### Added
- **Artigo "Qwen3.8-27B está lento? As 6 causas reais e o fix de cada uma"**
  (`guia/qwen3-8-27b-lento-causas-fixes/`, task kanban `t_1ced3026`, PO
  card das threads r/LocalLLaMA 1voa3ch + 1vriwym): primeiro conteúdo do
  portal dedicado à dor "por que está lento" (gap: 'lento' só aparecia em
  menções espalhadas). Tese verificada por dados: o decode do 3.8 é igual
  ao do 3.6 (73,6 vs 73,4 tok/s com thinking off, mesmo bench de 45
  configs — KGP Talkie 16/08; ~41,5 t/s na 3090 com "3.8 ≈ 3.6";
  17,3 vs 12,4 no Strix Halo, medição própria). As 6 causas: xhigh-trap
  (2,18s → 0,18s até a 1ª palavra), MTP desligado (nunca configurado — especulação é opt-in no
  llama.cpp; 3090: ~31,6 → 74 t/s, +134,5%), contexto
  estourando VRAM (32K = +2,5 GB; KV q4_0 136,7 vs 125,5 t/s), quant
  errada, backend/térmico (Vulkan > ROCm no R9700; prefill vLLM 3-4k
  t/s; throttling <500 MHz) e a regressão real documentada (M5 Max
  128 GB: 20-25 vs 30-40 t/s a 64K). Tabelas: causa→sintoma→fix→ganho
  medido e antes/depois (8 setups com fonte). Fontes lidas via índice
  de busca em 19/08 (Reddit bloqueia fetch direto): threads 1voa3ch,
  1vriwym, 1vqjeub, 1vpuhov, 1voojjz, Level1Techs pág. 3, KGP Talkie,
  blog AMD Day 0, dev.to jamilxt, Alibaba Cloud Medium, Cloud Codes
  (YouTube), Simon Willison, InsiderLLM, PR #22673. JSON-LD: TechArticle
  + HowTo (5 passos de diagnóstico) + FAQPage (7) + Breadcrumb.
- **Companions**: sitemap 25→26 URLs; llms.txt (+7 stats citáveis, +1
  página, +1 Q&A "Por que o Qwen3.8-27B parece mais lento que o
  Qwen3.6-27B?"); card no /guia/index.html (tag-hw Troubleshooting,
  BOFU, Novo 19/08); FAQ do portal +1 item (HTML e JSON-LD juntos — 30
  no FAQPage).

---

## [2026-08-19] — Artigo: LTX-2.5 local no ComfyUI (vídeo-gen open weights)

### Added
- **Artigo "LTX-2.5 com pesos abertos: gerar vídeo (com áudio) local no
  ComfyUI"**
  (`guia/ltx-2-5-video-local-comfyui/`, task kanban `t_460e2e51`, tema
  prioritário do daily 19/08): primeira cobertura de vídeo-gen open-weights
  que roda local no portal (gap: 0 menções a LTX nas 23 páginas). Dados
  verificados ao vivo em 19/08: 17 arquivos públicos no repo (desde 17/08),
  transformer 22B bf16 42,02 / comfy-int8 21,50 / nvfp4 18,72 GB; encoder
  gemma4-12b int8 15,37 GB; VAE de áudio 0,36 GB (áudio sincronizado nativo).
  Setup oficial ComfyUI int8 = 49,98 GB somados em arquivos (inclui prompt
  enhancer gemma4_e2b 10,28 GB do repo Comfy-Org/gemma-4 — achado próprio,
  ausente do discovery) — rótulo obrigatório "soma de arquivos, não pico de
  inferência". Rota comunitária GGUF medida: transformer Q4_K_M 15,09 GB +
  encoder Q5_K_M 9,51 GB (realrebelai/LTX-2.5_GGUFs 14,8k dl, Abiray 37,2k
  dl). Licença lida na íntegra (LTX-2.x Community License, 11/08/2026):
  comercial grátis < US$ 10M ARR agregado, sem branding obrigatório,
  derivados herdam a licença. Workflows oficiais confirmados no
  docs.comfy.org (T2V/I2V/FLF2V nativos, nós LTXV* no core). Cross-links:
  minimax-music3, qwen3-8-27b-visao-videos-local, hardware-local,
  como-rodar, modelos. JSON-LD: TechArticle + SoftwareApplication/AIModel +
  HowTo (5 passos) + FAQPage (8) + Breadcrumb.
- **Companions**: sitemap 23→24 URLs; llms.txt (+1 página, +6 stats citáveis,
  +1 Q&A "O LTX-2.5 roda em quantos GB?"); card no /guia/index.html
  (tag-guide, BOFU, Novo 19/08); FAQ do portal +1 item (HTML e JSON-LD
  juntos — 28 no FAQPage).

---

## [2026-08-19] — Artigo: Qwen3.8-27B com 256K de contexto em 24 GB

### Added
- **Artigo "Qwen3.8-27B com 256K de contexto em 24 GB: o guia do cache
  que cabe"** (`guia/qwen3-8-27b-contexto-256k-24gb/`, task kanban
  `t_2620c693`, Tema 2 do daily 19/08 — discovery `t_9be84165`): primeiro
  guia dedicado a contexto longo/256K do portal (gap: 11 menções espalhadas
  em 15 páginas, 0 páginas-destino). Ancorado no benchmark de produção de
  Michał Piszczek (piszczek.pl, 17-18/08) — lido integralmente e
  re-verificado ao vivo em 19/08.
  - Verificações obrigatórias do card cumpridas: (1) ctx nativo 262.144
    confirmado ao vivo no config.json oficial (max_position_embeddings=262144,
    64 camadas = 48 linear_attention + 16 full_attention, num_key_value_heads=4,
    head_dim=256); (2) todos os números citam "RTX PRO 4000 Blackwell,
    medição de terceiros (piszczek.pl)" — o portal não rodou o benchmark;
    (3) tabela de tiers declara 24 GB = MEDIDO vs 16 GB = ESTIMATIVA (link
    para o guia 16GB VRAM existente).
  - Correção factual vs. dados-âncora do card: no controle WikiText-2 do
    artigo, Q4_0 marcou PPL 6,3798 (perdeu para IQ4_XS, 6,1175) — Q4_0
    venceu em VELOCIDADE (44,95 vs 34,40 tok/s), não em PPL; o PPL 6,1127
    é do Q4_1 (melhor PPL, footprint não cabia com 256K+visão). O artigo
    declara esses números com precisão.
  - Conteúdo: a conta do KV cache (16 camadas × 4 KV heads × 256 head_dim ×
    2 × 262.144 tokens × ~0,5625 B/elemento Q4_0 ≈ 4,25 GiB); receita
    completa llama-server (ctx 262144, cache q4_0, flash-attn, MTP
    draft-mtp com spec-draft f16, ctx-checkpoints 4, fit off, mmproj na
    GPU auxiliar); seção "o que NÃO fazer" com 5 armadilhas medidas (Q4_0
    rápido-mais-sujado; NVFP4-MEDIUM pronto PPL 6,4949; drafter MTP
    +69,2 MiB → 50,44→37,02 tok/s; DSpark externo 46,6% mais lento;
    "alocado ≠ ocupado"); método de benchmark honesto (261.500 tokens
    reais, VRAM pós-fill, decode no cache quente); tabela por tier de
    VRAM; "você precisa de 256K?"; cross-refs para tokens-por-segundo
    (números short-context diferenciados), quantização GGUF, reasoning,
    16GB VRAM, visão e /hardware.
  - JSON-LD: TechArticle + HowTo (5 steps) + FAQPage (6 perguntas) +
    BreadcrumbList; GA4 G-016TVX8LEE com scroll_depth; canonical/OG/Twitter;
    title ≤60 chars e meta description ≤155.
  - Companions: sitemap (23→24 URLs), llms.txt (3 stats citáveis + página
    na lista + Q&A nova "Quantos tokens de contexto o Qwen3.8-27B suporta
    local?" substituindo a Q&A antiga de tamanho de contexto), card no
    `/guia` (tag-hw Contexto longo, BOFU · Novo 19/08), Q&A nova na FAQ do
    portal (HTML + JSON-LD, 27→28 perguntas).

---

## [2026-08-18] — Artigo: Qwen3.8-27B no Artificial Analysis (52 no AAII)

### Added
- **Artigo "Qwen3.8-27B no Artificial Analysis: 52 pontos — o que o dado diz
  (e o que não diz)"**
  (`guia/qwen3-8-27b-benchmark-artificial-analysis/`, task kanban `t_adedfbd2`,
  tema prioritário do daily 18/08): primeira cobertura do Artificial Analysis
  Intelligence Index no portal (gap: 0 menções a AAII antes deste artigo).
  Placar ao vivo lido do payload da página do modelo (18/08 19h45): Qwen 52,0 ·
  GPT-5.6 Luna (max) 52,3 · DeepSeek V4 Pro 0813 53,2 · GPT-5.6 Sol/Grok 4,6
  60,9 · Kimi K3 59,7 · GLM-5.3 59,5 · Nemotron 3 Ultra 38,3. Dados inéditos
  capturados: #1 entre 135 open weights ≤40B (mediana da classe: 9),
  verbosidade 160M tokens vs mediana 43M (evidência do overthinking medida
  pela própria AA), custo por tarefa do índice (Luna US$ 0,047 · DeepSeek
  US$ 0,252 · Qwen self-host US$ 0,00), metodologia v4.1.1 (9 avaliações
  listadas). Seção "o que o dado NÃO diz": score é COM reasoning, não vale
  para quantização local, índice agregado ≠ caso de uso, empate com Luna é
  sobre o agregado. Contexto 2.4T-A95B como parágrafo (não tema). FAQPage
  JSON-LD (6 perguntas) + TechArticle + SoftwareApplication/AIModel (ADR-008)
  + Breadcrumb; GA4 com scroll_depth. Re-verificações do dia: post Simon
  17/08 relido; HN story AAII agora com 371 pontos/174 comentários (eram
  349); página AAII re-capturada (score 52 inalterado).
  - Sitemap (22 URLs), llms.txt (stat citável + página + 2 Q&As: score AAII e
    "benchmarks verificados independentemente" reescrita com a ressalva AAII),
    card no `/guia` (tag-bench, MOFU · Novo 18/08).

---

## [2026-08-18] — Artigo: Tokens por segundo no hardware real (throughput compilado)
## [2026-08-18] — Artigo: Qwen3.8-27B enxerga — visão, vídeo e OCR locais (mmproj)

### Added
- **Artigo "Qwen3.8-27B enxerga: guia de imagem, vídeo e OCR no llama.cpp
  e Ollama"** (`guia/qwen3-8-27b-visao-videos-local/`, task kanban
  `t_933f2b89` — Tema 2 do discovery 18/08): primeiro guia multimodal do
  portal, atacando o gap de 0 páginas de visão/vídeo para uma VLM nativa
  com 3,56M de downloads de GGUF (unsloth, HF API 18/08).
  - Os 3 requisitos obrigatórios do card verificados ao vivo (18/08):
    (1) doc multimodal do llama.cpp (libmtmd) — `-hf` detecta mmproj
    automaticamente, `--mmproj file.gguf` no caminho manual, flags
    `--no-mmproj` e `--no-mmproj-offload`; (2) template oficial de prompt
    do model card — `image_url`/`video_url` OpenAI-style; (3) Ollama —
    `qwen3.8:latest`/`:27b` (18 GB, 256K) listam entrada "Text, Image",
    sem tag especial de visão (doc capabilities/vision: array `images`
    base64); vídeo NÃO listado no Ollama — tratado como diferenciação
    honesta entre stacks no artigo.
  - Conteúdo: mmproj medido 0,93 GB (BF16) / 0,63 GB (Q8_0) no repo
    oficial ggml-org + 0,93 GB (F16/BF16) na unsloth (HF API); passo a
    passo llama-server (auto e manual) + curl /v1/chat/completions;
    OCR (OmniDocBench 91,1, CharXiv 90,2 com CI, MathVision 94,6 com CI);
    bounding boxes bbox_2d escala 0-1000 do teste do Simon Willison
    (16/08, "such a good match", bbox-lab); vídeo hour-scale com o ajuste
    oficial do video_preprocessor_config.json (longest_edge 469762048 ≈
    224k video tokens); tabela VL completa de 13 benchmarks do model card
    (5 colunas); tabela de custo de VRAM; presets por hardware (24GB/16GB/
    unificada/Ollama); seção de erros comuns.
  - JSON-LD: TechArticle + HowTo (5 steps) + FAQPage (5 perguntas) +
    BreadcrumbList; GA4 G-016TVX8LEE com scroll_depth; canonical/OG/Twitter.
  - Companions: sitemap (21→22 URLs), llms.txt (+5 stats citáveis, página
    na lista, Q&A nova "O Qwen3.8-27B enxerga imagens?", linha na seção
    Multimodal), card no `/guia` (tag-guide, BOFU · Novo 18/08), Q&A nova
    na FAQ do portal (HTML + JSON-LD, 26→27 perguntas).

---

### Added
- **Artigo "Tokens por segundo no hardware real"**
  (`guia/tokens-por-segundo-30b-hardware-real/`, task kanban `t_507fe40f` — órfão
  do discovery de 16/08 materializado): tabela principal hardware × stack ×
  quantização × tok/s com 15 configurações e fonte por linha — RTX 5090
  SGLang NVFP4+DSpark 206,1 tok/s (tweet oficial Qwen + post SGLang), 3090
  llama.cpp 41,5 (InsiderLLM), Strix Halo 17,3 (medição própria), 3060 12GB
  ~9,7 com MTP (HF discussion #61), DGX Spark 38, MacBook M5 7,16→10,47.
  Metodologia explícita (nossa e de cada fonte), seção "por que 10→206"
  (banda de memória ÷ bytes por token), MTP on/off com contexto por número,
  expectativa por hardware brasileiro (3060 12GB, 4060 Ti 16GB, 3090 usada,
  RX 7600, Strix Halo), tabela oficial Muse Glimmer/DFlash. FAQPage JSON-LD
  (5 perguntas) + TechArticle + Breadcrumb; GA4 com scroll_depth.
  - Dados-âncora re-verificados no dia da publicação (18/08): downloads GGUF
    3.561.466 (eram 1.945.635 em 16/08 — base quase dobrou em 2 dias);
    PR #22673 (MTP llama.cpp) confirmado MERGED via gh; correção do dado do
    discovery: números Muse são M4/M5 **Max** (não "M5 Pro"), valores do
    model card oficial 23,7→37,8 / 26,6→50,2 / 74,9→233,4.
  - Sitemap (19 URLs, dedupe verificado), llms.txt (4 stats citáveis novos +
    página + FAQ "Quantos tokens por segundo roda o Qwen3.8-27B?") e card no
    `/guia` (tag-bench, MOFU · Novo 18/08) atualizados.

---

## [2026-08-18] — Artigo: Configuração de reasoning do Qwen3.8-27B (overthinking + MTP)

### Added
- **Novo artigo BOFU** (`guia/qwen3-8-27b-reasoning-configuracao-ideal/`, task `t_99ee1e28` —
  seo-content): guia prático para desativar/dosar o reasoning e acelerar com MTP,
  cobrindo o gap de 0 menções a overthinking/MTP/Simon no portal (sitemap verificado
  18/08) enquanto o tema domina a review mais citada do lançamento.
  - Dados-âncora re-verificados ao vivo em 18/08: review Simon Willison 16/08
    (xhigh-trap: 21 min / 22.276 reasoning tokens para 3.223 de output; reasoning off:
    137s / 3.715 tokens; MTP +72% no DGX Spark), README oficial do llama.cpp (flags
    `--reasoning [on|off|auto]`, `--reasoning-effort minimal…max`, `--reasoning-budget
    -1/0/N`, `--reasoning-preserve`, `--spec-type draft-mtp`), PR #22673 do llama.cpp
    **MERGED em 16/05/2026** (builds atuais já incluem MTP; decode 22,97 → 42,45 t/s
    ~1,85×, prefill ~0,51×), HF discussion unsloth #7 (`--reasoning-budget 0` como fix
    para overthinking que estoura contexto), docs Ollama capabilities/thinking
    (`"think": false` ou low/medium/high/max).
  - MTP com contexto por número: +72% DGX Spark (Simon), ~1,85× no mesmo GGUF (PR
    #22673), +16% RTX 3090 draft 1 (ik_llama.cpp), 2,2-2,4× Qwen3.6-27B Q8_0
    (tproger) — números não contraditórios, contextos diferentes, citados como tal.
  - Tabela overthinking × hardware com medições próprias (Strix Halo Q4_K_M 17,3 t/s;
    Q5_K_M 10,6 t/s) mostrando o custo do xhigh-trap em tok/s de hardware BR.
  - 3 presets de comando (24GB com MTP / 16GB com n-gram + KV q8_0 / Strix Halo
    thinking off), seção de erros comuns, FAQ de 6 perguntas.
  - JSON-LD: TechArticle + HowTo (5 passos) + FAQPage + Breadcrumb; GA4 gtag +
    scroll_depth incluídos.
  - Downloads GGUF atualizados na publicação: 3.561.466 (18/08, HF API) — base
    instalada que busca "como desligar o thinking".
  - Cross-links: guia 16GB VRAM, quantização GGUF, como-rodar, FAQ, comparativo 3.8 vs 3.6.
- `sitemap.xml`: URL nova (priority 0.9, lastmod 2026-08-18).
- `llms.txt`: entrada na lista de páginas + 2 stats citáveis (xhigh-trap 21min/22.276
  tokens vs 137s off; MTP +72% DGX Spark e ~1,85× decode PR #22673).
- `guia/index.html`: card do artigo (tag-guide Tutorial, BOFU · Novo 18/08).
- `guia/faq/index.html`: nova Q&A "Como desativar o thinking (overthinking) do
  Qwen3.8-27B?" (HTML + JSON-LD FAQPage, 26 perguntas, JSON validado).

## [2026-08-18] — Artigo: SGLang + FP8 oficial (órfão 16/08 materializado)

### Added
- **Novo artigo BOFU** (`guia/como-rodar-sglang-qwen3-8-27b/`, task `t_77b213f6`
  — seo-content, tema órfão do discovery de 16/08 materializado): tutorial do
  servidor SGLang com o checkpoint FP8 oficial do Qwen3.8-27B. Primeira
  cobertura de SGLang do portal (gap verificado por grep: 0 menções antes).
  Instalação uv/venv + Docker (`lmsysorg/sglang:qwen38-27b`), comando
  `launch_server` com parsers qwen3 e explicação flag a flag, contexto 262K
  nativo + 1M via YaRN (comando oficial do README FP8), thinking/instruct com
  sampling do model card, MTP via EAGLE 3/1/4, benchmark `bench_serving`,
  tabela FP8 × GGUF cross-linkada, decisão SGLang × llama.cpp/Ollama e
  troubleshooting (mamba-full-memory-ratio, chunked-prefill, OOM em 32GB).
- Dados verificados no dia da publicação (18/08, HF API): checkpoint FP8 com
  741.011 downloads (era 352.971 em 16/08) e 30,89 GB somando os safetensors
  da tree API; PyPI sglang 0.5.17 é a mais recente.
- Card do artigo no `/guia` (tag-guide) e na home; sitemap + llms.txt
  (citação citável + lista de páginas) atualizados.

---

## [2026-08-18] — Artigo: MiniMax Music3 local (primeira cobertura de música local)

### Added
- **Novo artigo BOFU** (`guia/minimax-music3-musica-local/`, task `t_432eb96f` —
  seo-content, tema órfão do discovery t_7130b492 materializado): tutorial de
  setup do modelo de música da MiniMax com pesos abertos, atendendo a janela
  "minimax music3 local" / "gerar música IA local" sem cobertura pt-BR.
  - Dados re-verificados ao vivo em 18/08 antes de citar (exigência do card):
    model card `MiniMaxAI/MiniMax-Music3` (criado 07/08, atualizado 14/08),
    tree da HF API (flowmatching_vae.pth 9,83 GB + dav.pth 0,49 GB), LICENSE
    Community (comercial OK com atribuição; autorização só > US$ 20 mi/ano).
  - **Correção de dado-âncora do discovery**: o "2,4B params" do discovery é
    só o módulo Flow Matching — o pipeline soma ~11,1B (Global LLM 8B init
    Qwen3-8B + Local LLM 0,6B + Flow Matching 2,4B + Flow-VAE 123M). O artigo
    abre com uma seção dedicada ao mito do "2,4B".
  - Tiers de VRAM oficiais (docs diffusers, branch minimax-music3-integration):
    ~23 GB full bf16 / ~22 GB auto CPU offload / **8 GB com group offloading
    leaf_level + use_stream** — este último é o degrau que viabiliza
    3060 Ti/4060 e vira o gancho do título.
  - Três rotas documentadas: diffusers (script + 8GB, com código completo),
    SGLang-Omni (servidor oficial /v1/audio/speech, 2 GPUs dividem estágios),
    ComfyUI (nativo, template oficial, pesos Comfy-Org 285k downloads).
  - Tabela hardware BR (8/16/24 GB + 2×8), 3 exemplos de prompt pt-BR (MPB
    acústica, lo-fi instrumental, arena rock), limitações honestas de
    pt-BR cantado, seção de licença comercial.
  - JSON-LD: TechArticle + SoftwareApplication (applicationCategory "AIModel"
    conforme ADR-008) + HowTo (5 passos) + FAQPage (6) + Breadcrumb; GA4
    gtag + scroll_depth incluídos.
  - Âncoras internas para `guia/qwen38-27b-16gb-vram-llama-cpp`,
    `guia/hardware-local`, `guia/como-rodar`, `guia/quantizacao-gguf-30b-quanto-cabe-na-sua-gpu`.
- `sitemap.xml`: URL nova (priority 0.9, lastmod 2026-08-18).
- `llms.txt`: 3 stats citáveis do Music3 + entrada na lista de páginas.
- `guia/index.html`: card do artigo (tag-guide Tutorial, BOFU · Novo 18/08).


## [2026-08-18] — Artigo: Configuração de reasoning do Qwen3.8-27B (overthinking + MTP)

### Added
- **Novo artigo BOFU** (`guia/qwen3-8-27b-reasoning-configuracao-ideal/`, task `t_99ee1e28` —
  seo-content): guia prático para desativar/dosar o reasoning e acelerar com MTP,
  cobrindo o gap de 0 menções a overthinking/MTP/Simon no portal (sitemap verificado
  18/08) enquanto o tema domina a review mais citada do lançamento.
  - Dados-âncora re-verificados ao vivo em 18/08: review Simon Willison 16/08
    (xhigh-trap: 21 min / 22.276 reasoning tokens para 3.223 de output; reasoning off:
    137s / 3.715 tokens; MTP +72% no DGX Spark), README oficial do llama.cpp (flags
    `--reasoning [on|off|auto]`, `--reasoning-effort minimal…max`, `--reasoning-budget
    -1/0/N`, `--reasoning-preserve`, `--spec-type draft-mtp`), PR #22673 do llama.cpp
    **MERGED em 16/05/2026** (builds atuais já incluem MTP; decode 22,97 → 42,45 t/s
    ~1,85×, prefill ~0,51×), HF discussion unsloth #7 (`--reasoning-budget 0` como fix
    para overthinking que estoura contexto), docs Ollama capabilities/thinking
    (`"think": false` ou low/medium/high/max).
  - MTP com contexto por número: +72% DGX Spark (Simon), ~1,85× no mesmo GGUF (PR
    #22673), +16% RTX 3090 draft 1 (ik_llama.cpp), 2,2-2,4× Qwen3.6-27B Q8_0
    (tproger) — números não contraditórios, contextos diferentes, citados como tal.
  - Tabela overthinking × hardware com medições próprias (Strix Halo Q4_K_M 17,3 t/s;
    Q5_K_M 10,6 t/s) mostrando o custo do xhigh-trap em tok/s de hardware BR.
  - 3 presets de comando (24GB com MTP / 16GB com n-gram + KV q8_0 / Strix Halo
    thinking off), seção de erros comuns, FAQ de 6 perguntas.
  - JSON-LD: TechArticle + HowTo (5 passos) + FAQPage + Breadcrumb; GA4 gtag +
    scroll_depth incluídos.
  - Downloads GGUF atualizados na publicação: 3.561.466 (18/08, HF API) — base
    instalada que busca "como desligar o thinking".
  - Cross-links: guia 16GB VRAM, quantização GGUF, como-rodar, FAQ, comparativo 3.8 vs 3.6.
- `sitemap.xml`: URL nova (priority 0.9, lastmod 2026-08-18) — inserção idempotente,
  preservando a entrada minimax-music3 (editada concorrentemente por task irmã).
- `llms.txt`: entrada na lista de páginas + 2 stats citáveis (xhigh-trap 21min/22.276
  tokens vs 137s off; MTP +72% DGX Spark e ~1,85× decode PR #22673).
- `guia/index.html`: card do artigo (tag-guide Tutorial, BOFU · Novo 18/08).
- `guia/faq/index.html`: nova Q&A "Como desativar o thinking (overthinking) do
  Qwen3.8-27B?" (HTML + JSON-LD FAQPage, 26 perguntas, JSON validado).

## [2026-08-18] — Artigo: Qwen3.8-27B em 16GB de VRAM com llama.cpp

### Added
- **Novo artigo BOFU** (`guia/qwen38-27b-16gb-vram-llama-cpp/`, task `t_8cd3cf24` —
  seo-content): guia técnico para rodar o 27B denso em GPU de 16GB com
  llama.cpp, atendendo demanda comprovada no r/LocalLLaMA (threads "Squeezing
  Qwen3.8-27B onto a Single 16GB GPU" e "After pushing 1M+ tokens") com zero
  de cobertura pt-BR na SERP.
  - Dados medidos ao vivo via Hugging Face API (18/08): IQ4_XS 15,71 GB ·
    UD-Q3_K_XL 13,44 GB · Q4_K_M 17,11 GB · UD-IQ2_M 10,32 GB · mmproj 0,93 GB.
  - Retenção de qualidade citando benchmark da comunidade r/LocalLLM (18/08):
    IQ4_XS 98,5%, UD-Q3_K_XL 97,8% (ppl KL 7,0615 vs 7,1113).
  - Flags verificadas no README oficial do llama.cpp: `--spec-type
    ngram-simple` (speculative decoding sem drafter), `--cache-type-k/v q8_0`
    + `--flash-attn on`, `--no-mmproj`, `--n-gpu-layers` com offload parcial
    (preset Q4_K_M).
  - 3 presets de comando (IQ4_XS qualidade / UD-Q3_K_XL contexto 64K+ /
    Q4_K_M offload parcial), tabela de throughput da comunidade (~20 t/s na
    RTX 4070 Ti Super), seção de erros comuns, FAQ de 6 perguntas.
  - JSON-LD: TechArticle + HowTo (5 passos) + FAQPage + Breadcrumb; GA4
    gtag + scroll_depth incluídos.
  - Âncoras internas para `guia/quantizacao-gguf-30b-quanto-cabe-na-sua-gpu`,
    `guia/como-rodar`, `guia/hardware-local`.
- `sitemap.xml`: URL nova (priority 0.9, lastmod 2026-08-18).
- `llms.txt`: entrada na lista de páginas com números citáveis.
- `guia/index.html`: card do artigo (tag-hw Tutorial, BOFU · Novo 18/08).

### Fixed
- `sitemap.xml`: preservado lastmod 2026-08-17 do Lemonade (editado
  externamente após a última leitura em disco).

## [2026-08-16] — Artigos do dia + GA4 coverage no portal todo

### Added
- **Artigo Agent Memory Leaderboard** (`guia/agent-memory-leaderboard-resultados/`):
  análise dos resultados inaugurais com rankings completos verificados ao vivo na API.
- **Artigo Lemonade SDK v11.6** (`guia/lemonade-sdk-v11-6-llm-local-gpu-npu-amd/`):
  release notes, comparativo e caveat de suporte AMD.
- **Artigo comparativo geracional 27B denso** (`guia/qwen3.8-vs-qwen3.6-27b`,
  task kanban `t_b4f73b4b` — redator):
  26 benchmarks do model card com pares apples-to-apples, throughput real medido
  no Strix Halo (3.8/3.6 em Q4_K_M, 400 tok × 9 rodadas, platô térmico),
  tabela GGUF com GB reais via HF API, e veredito por perfil de uso.
  FAQPage JSON-LD com 7 perguntas; link no índice `/guia`, na home, no sitemap
  e no `llms.txt`.
- Medição de throughput do Qwen3.6-27B denso (Q4_K_M) no Strix Halo — 12,4 tok/s
  decode, comparado ao 3.8-27B no mesmo quant (17,3 tok/s).
- **Tag GA4 G-016TVX8LEE inserida nas 11 páginas sem cobertura**:
  modelos, hardware, benchmarks, guia-rapido, guia, como-rodar, faq,
  benchmarks-comparativos, comunidade-casos-uso, hardware-local,
  qwen3.8-vs-qwen3.6-27b. Agora 14/14 páginas do portal têm analytics.
- `qwenTrackSearch()` removida do index.html (função morta, sem caller).
- Ambos os novos artigos com JSON-LD + GA4, sitemap e llms.txt atualizados.
- `guia/index.html` e `index.html` (home): +2 cards cada (tags tag-bench e
  tag-hw), com marcador "Novo 16/08".

### Fixed
- **Correções QA round 1** (task `t_85dc4eab` — redator): tabela GGUF
  completada com as células que estavam "—" (3.8 Q3_K_M = 13,82 GB;
  3.6 Q8_0 = 28,60 GB, coluna Diferença recalculada); FAQPage JSON-LD
  realinhado 1:1 com as 7 perguntas visíveis; ficha técnica corrigida —
  MTP do 3.6 marcado como documentado (o claim "não documentado" era falso);
  removidos claims sem fonte ("201 idiomas", "~85% de taxa de aceitação
  AtomicChat"); aritmética corrigida (35B MoE: 3,3× vs 3.8 / 4,6× vs 3.6,
  antes "+5,4×"; 0,29 GB ≈ 290 MB, antes "170 MB"); "22 de 27" → 23 de 27;
  medianas ajustadas (+6,8 conhecimento geral, +1,6 média em percepção
  passiva); typo 17,1 → 17,3 tok/s.

---

## [2026-08-15] — Atualização diária

### Added
- `docs/team/PLAYBOOK.md` — metodologia de operação do time Hermes
  (`f14a0e0`, arquivista).
- Compilação do board `seo-local-models-30b`: 24 tasks concluídas em
  2026-08-15 — correções R1/R2 (performance, a11y, SEO), 2 artigos do dia,
  nav consistente com cleanUrls, GSC e as respectivas validações QA.
  Detalhes nas entradas "[2026-08-15]" acima; registro completo no board.

*(Entry gerada automaticamente pelo job das 20h e curada pelo Arquivista.)*

---

## [2026-08-15] — Fix: referências de benchmark sem fonte oficial substituídas pelas colunas reais do model card

### Fixed
- **Landing, guia de benchmarks, llms.txt e FAQ** (`t_6dd8d927` — seo-content):
  referências de "fronteira" que citavam modelos/valores inexistentes no model
  card (GPT-5.6 Sol, Opus 4.8, Opus 5, Qwen3.8-Max 86,1/74,8) substituídas pelas
  colunas oficiais do card: **Qwen3.7-Plus · Muse Glimmer-30B · Opus 4.6 Max**.
- `index.html`: barras dos gráficos (Opus 4.8→4.6 Max 78,2; GPT-5.6 Sol→Qwen3.7-Plus
  64,0/57,6/14,2; Opus 5→Opus 4.6 Max 53,4; + barra OSWorld Opus 4.6 Max 72,7);
  tabela de 26 benchmarks com colunas v3.6 preenchidas (36,2/70,3/87,8/24,0/69,1/
  85,1/89,4/78,4/84,1/28,9/62,5/45,0/42,6) e referências reais nas 26 linhas;
  legendas e caption atualizados ("Referências do model card").
- `guia/benchmarks-comparativos/`: 3 tabelas + parágrafos narrativos recalculados
  (GPQA "próximo de" → distâncias reais 1,1/2,1 pts; OSWorld/CoWorkBench claims).
- `llms.txt` (l.49 e resumo) e `guia/faq/` (pergunta vs ChatGPT) realinhados.
- Regra do projeto reafirmada: toda referência de benchmark deve ter linha
  correspondente no model card — zero termos proibidos, 26/26 refs verificadas,
  deltas aritméticos conferidos (26 no index, 40 no guia).

---

## [2026-08-15] — Artigos do dia: Muse Glimmer 30B + tabela GGUF, e navegação consistente

### Added
- **2 artigos do dia** (`188ba96`, task `t_7ab9d2fd` — seo-content + discovery):
  - *Muse Glimmer 30B* (`/guia/muse-glimmer-30b-agente-local`) — 29,6B denso
    Apache 2.0 multimodal para agentes locais 24/7; benchmarks oficiais vs
    Gemma4-31B/Qwen3.6-27B + cruzamento honesto com o Qwen3.8-27B nos 4
    benchmarks comuns.
  - *Tabela real de quantização GGUF ≤30B*
    (`/guia/quantizacao-gguf-30b-quanto-cabe-na-sua-gpu`) — GB medidos via
    HF API (Qwen3.8-27B vs Muse Glimmer), IQ2 a Q8, mmproj, drafter, GPU
    por tier.
  - GA4 (`G-016TVX8LEE`) + `scroll_depth` nas 2 novas páginas; JSON-LD
    (TechArticle + SoftwareApplication/FAQPage + BreadcrumbList); 2 cards
    no índice do `/guia`; 2 URLs no sitemap; seções novas no `llms.txt`.
- **Links dos 5 artigos do `/guia` na home** (`40cef50`).
- **Página 404 com links internos** para modelos, hardware, benchmarks e
  guia (`5b462e7`).

### Fixed
- **Navegação consistente em todo o portal** — cleanUrls em todas as páginas
  do portal e menu hambúrguer mobile (<900px) nas 4 páginas do portal
  (`40cef50`, `da6a636`; PRs #5 e #6, task `t_72542ef7`).
- **Acessibilidade do menu hambúrguer** — `aria-expanded`, `aria-label` e
  `type="button"` no `nav-toggle` das 4 páginas do portal (`0f2fa61`).

---

## [2026-08-15] — Consolidação da documentação em `docs/`

### Changed
- Documentação consolidada em `docs/`: os `CHANGELOG.md`, `HISTORICO.md` e
  `ROADMAP.md` da raiz foram mesclados para cá (conteúdo único preservado) e
  substituídos na raiz por stubs de redirecionamento. ADR-004 marcado como
  superado pelo ADR-007 (GA4 real). CHANGELOG completado com os commits que
  faltavam de 2026-08-15. A versão `0.1.0` que vivia na raiz foi absorvida
  pelas entradas por data.
  *(Arquivista — task kanban `t_2e42bec9`)*

---

## [2026-08-15] — Correções R1/R2, GA4 real, portal e Search Console

### Added
- **GA4 real instalado** — Measurement ID `G-016TVX8LEE` (propriedade
  QWEN38-27B-LANDING, ID 549987691), substituindo o ID placeholder
  `G-QWEN3827B` que tinha sido removido no `d554f7c`. Tag async com
  `anonymize_ip:true`; enhanced measurement do stream (page_view, scroll,
  click_outbound, file_download, site_search, video_*) + eventos custom
  `scroll_depth` (25/50/75/100%) e helper `qwenTrackSearch()`.
  (`7afed08` — task "GA4: Analytics & Dashboard", agente atlas)
- **Verificação do Google Search Console** — meta tag
  `google-site-verification` em todas as páginas + `GSC_SETUP.md` com o
  passo a passo; sitemap expandido com as 6 URLs do guia como entradas
  individuais. (`d256ec3`, PR #4 — task kanban `t_65295f98`)
- **Portal de modelos locais** — seções Modelos, Hardware, Benchmarks e
  Guia Rápido; CSS compartilhado em `assets/css/portal.css`; template de
  artigo em `templates/template-artigo.md`. (`45dcb1a`)
- **Menu responsivo com hambúrguer** para telas <900px. (`0bbb4a8`)
- Agente **Arquivista** (Hermes) responsável pela documentação contínua, e
  rotina `~/.hermes/scripts/daily_doc.py` que compila tasks concluídas no
  CHANGELOG (agendada diariamente às 20h no perfil do Arquivista).

### Fixed
- **Scrollspy `SyntaxError` na home** — `document.querySelector('/guia')`
  usava seletor inválido (href com barra); navegação destacava seção errada
  e gerava erro no console. (`ffb0c3c`)
- **`aggregateRating` fabricado removido do JSON-LD** — reviewCount 397 e
  ratingValue 4,8 não correspondiam a fonte real (risco de penalização
  manual do Google por rich snippet enganoso). `llms.txt` completado com os
  26 benchmarks do model card. (`4f4dbb5` — QA `t_251e9f6c`)
- **Menu sumia em telas <900px** — o CSS escondia o nav sem alternativa;
  adicionado botão ☰ com dropdown flutuante, e links corrigidos para
  cleanUrls (`/modelos` em vez de `modelos.html`, que sofria redirect 308).
  (`0bbb4a8`)
- Meta description da home encurtada para 152 caracteres (limite 155 do
  Google). (`ffb0c3c`)

### Changed
- Título da home atualizado para "Portal de Modelos Locais de 30B";
  `vercel.json` com `cleanUrls: true` e headers de segurança/cache.
  (`45dcb1a`, `0bbb4a8`)

---

## [2026-08-15] — Estrutura de documentação inicial

### Changed
- **PLAYBOOK.md 0.1.0 → 0.2.0** (revisão semanal do Arquivista, com base em
  dados reais do sistema): seção 2.1 agora lista `Sentinela` e nomeia os perfis
  reais (`product-owner`, `qa`, …) com os crons que os acionam
  (`product-owner-morning` 06:00, `daily-research-30b` 07:00,
  `arquivista-daily-doc` 20:00, `sentinel-audit`, `auto-cura-hermes`);
  seção 4.1 corrige o caminho do playbook (`docs/team/PLAYBOOK.md`, não
  `docs/TEAM-PLAYBOOK.md`) e o mantenedor (Arquivista, semanal); seção 5.1
  corrige a sintaxe do `hermes cron create` (schedule e prompt são posicionais);
  seção 7 ganha snapshot real de 2026-08-15 (24 tasks/dia, retrabalho QA 37,5%,
  2 cards bloqueados <24h).
  *(Arquivista — task kanban `t_158f6aba`)*

### Added
- Pasta `docs/` com documentação estruturada do projeto: `README.md`,
  `CHANGELOG.md`, `HISTORICO.md`, `DECISIONS.md`, `ROADMAP.md`.
  `README.md` da raiz atualizado com seção "Documentação" apontando para
  `docs/`. *(Arquivista — task kanban `t_f56140db`, commit `17d8439`)*

---

## [2026-08-15] — Performance, acessibilidade e SEO finos

### Changed
- **Font stack de sistema** substitui Google Fonts (render-blocking). Antes o
  LCP ficava em 4,8s por causa do carregamento síncrono das fontes Inter e
  JetBrains Mono; agora zero requisições externas de fonte, stack
  `system-ui` + `ui-monospace`.
- Contraste de texto melhorado para WCAG AA: `--fg-3` dark `#6f6f6f` → `#8b8b8b`
  (3,94:1 → 5,81:1); `--fg-3` light `#8f8f8f` → `#767676` (3,23:1 → 4,54:1).
- Ordem de headings corrigida: `h4` no rodapé → `p.foot-title` (não quebra a
  sequência `h1`–`h3`).
- Meta description encurtada: 239 → 152 caracteres (≤ 155, limite do Google).

### Added
- `og-image.png` 1200×630 gerado do `og-image.svg` para Open Graph/Twitter Card.
- `robots.txt` com allowlist explícita para GPTBot, ClaudeBot, PerplexityBot e
  20+ crawlers de IA.
- `sitemap.xml` com URL principal, `lastmod` e `changefreq`.
- `llms.txt` com conteúdo estruturado para crawlers de LLM (GEO).
- `manifest.json` — PWA manifest com ícone SVG, theme color e categorias.
- `404.html` — página 404 customizada com design consistente.
- `vercel.json` — caching headers (assets imutáveis 1 ano), security headers,
  8 redirects.
- JSON-LD enriquecido: `TechArticle` + `BreadcrumbList` + `FAQPage` (4 Q&As).
- `noscript` — fallback acessível para usuários sem JS.

### Fixed
- Mojibake corrigido no relatório anexado.
- Três trechos residuais em inglês traduzidos para pt-BR: "Quantizações
  day-zero" → "no lançamento"; "GGUF de 4 bits (Unsloth, day-zero)" → "no dia do
  lançamento"; meta description "open-weight" → "de pesos abertos".
- Três citações da comunidade perdidas no redesign restauradas, agora
  traduzidas. Página volta a ter as 15 originais.
- `IFBench` exibia seta "↑" como placeholder — valor real 79,5 preenchido.
- Classe CSS `hero` (cabeçalho) colidia com `td.n.hero` (células de destaque),
  herdando `padding:76px` e desalinhando colunas. Renomeada para `n lead`.

### Removed
- **GA4 placeholder removido** (ID `G-QWEN3827B` era falso, não coletava
  dados). *Reinstalado horas depois com ID real — ver a entrada
  "[2026-08-15] — Correções R1/R2..." acima e o ADR-007.* (`d554f7c`)

---

## [2026-08-14] — Landing page inicial e redesign Geist

### Added
- Página informativa (não oficial) sobre o lançamento dos pesos abertos do
  **Qwen3.8-27B** (14/08/2026): especificações, 26 benchmarks do model card,
  requisitos de hardware, throughput medido em máquina real e recepção da
  comunidade.
- Seção "Medido nesta máquina": decode em platô térmico (400 tokens/rodada,
  9 rodadas) no ASUS ROG Flow Z13 (Strix Halo, Radeon 8060S, 128 GB unificados)
  com Ollama sobre Vulkan — 10,6 tok/s no Qwen3.8-27B denso (Q5_K_M) contra
  56,6 tok/s no Qwen3.6-35B MoE.
- Redesign sobre o design system **Geist** (Vercel): superfícies neutras,
  hairlines de 1px, raio 8/12px, tema claro e escuro com alternância manual
  persistida em `localStorage`.
- Barra de navegação fixa com destaque da seção atual via `IntersectionObserver`.
- Paleta de gráficos validada por script: cor por função (violeta = Qwen3.8,
  laranja = fronteira proprietária, cinza = geração anterior), ΔE CVD ≥ 8,
  contraste ≥ 3:1.
- Marcos semânticos, link de pular para o conteúdo, foco visível, `aria-pressed`
  nos filtros, `aria-current` na navegação, `prefers-reduced-motion` respeitado.
- Meta tags Open Graph e Twitter, canonical, `theme-color` por esquema,
  JSON-LD `schema.org/TechArticle`.
- Comandos prontos para Ollama, llama.cpp e vLLM, cada um com botão de copiar.
- Deploy automático na Vercel conectado ao repositório (`main` = produção).

### Changed
- De 11 para 26 benchmarks na tabela — todos os resultados do model card oficial.
- Arquitetura detalhada: 64 camadas no padrão 16 × (3 × Gated DeltaNet →
  1 × Gated Attention), contagem de heads e dimensões.
- Nova seção multimodal com nove métricas próprias da torre de visão.
- Página afirmava "thinking-only" — corrigido para documentar os dois modos
  (thinking: temp 1.0 / top_p 0.95; instruct: temp 0.7 / top_p 0.80 /
  presence_penalty 1.5).
