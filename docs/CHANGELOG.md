# Changelog

Registro de mudanças do projeto **Qwen3.8-27B landing page / Portal de
Modelos Locais de 30B**.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
ordem reversa (mais recente primeiro). Datas em ISO `YYYY-MM-DD`.

---

## [2026-08-24] — Correção QA: tamanho NVFP4 e downloads do Qwen no artigo-veredicto vs Nemotron (t_06352eae)

### Changed
- **Artigo** `guia/qwen3.8-vs-nemotron-3-5-lightning-30b-a3b/index.html`: tamanho real do checkpoint NVFP4 corrigido de "~15 GB" (teórico 30B×4bit/8) para **21,56 GB** (total_size 21.559.589.596 bytes, 52 shards safetensors, HF API 24/08) no corpo e na footnote de fontes; refresh do "dl/mês" do Qwen3.8-27B de 1,73M para **2,65M** (downloads acumulados 2.645.226, HF API 24/08).

## [2026-08-24] — Artigo-veredicto "Qwen3.8-27B ou Nemotron-3.5-Lightning-30B-A3B?" (t_eea4801f)

### Added
- **Artigo-veredicto** `guia/qwen3.8-vs-nemotron-3-5-lightning-30b-a3b/index.html`: o MoE agêntico da NVIDIA (30B/3B ativos, até 1M de contexto, OpenMDW-1.1) contra o 27B denso — tabela do par com os números oficiais do próprio NVIDIA mostrando derrota vs Qwen3.6-35B-A3B (SWE-bench Verified 51,56 vs 70,12; Terminal-Bench 2.1 24,58 vs 44,38; GPQA 75,44 vs 83,40), tabela GGUF (ggml-org oficial + Unsloth UD-quants + Ollama 25 GB), veredito por perfil, aviso de honestidade (claim "até 4×" rotulado, comunidade "incredibly variable"), 5 FAQs e JSON-LD TechArticle + FAQPage.
- **llms.txt**: 3 inserções aditivas — bullet novo no dossiê de vereditos (Agentes/execução ≤30B), entrada nova na lista de páginas e FAQ nova (Qual o melhor modelo local para agentes em 2026?).
- **FAQ** (`guia/faq/index.html`): 38ª pergunta "Qwen3.8-27B ou Nemotron-3.5-Lightning-30B-A3B para agentes?" na seção Comparações (h3 + Question JSON-LD com paridade).
- **Sitemap.xml**: 37 → 38 URLs (nova página com priority 0.8, lastmod 2026-08-24).
- **Guia** (`guia/index.html`): card novo no topo do card-grid (Comparativo, Novo 24/08).

## [2026-08-24] — Hub EN de execução "How to Run Qwen3.8-27B Locally" (t_60a99ce1)

### Added
- **Hub EN de execução `guia/en/how-to-run-qwen3-8-27b/index.html`** (novo): espelho-enriquecido do guia-mãe PT `como-rodar` — quick answer com 3 comandos para featured snippet, 5 métodos (Ollama, llama.cpp, vLLM, SGLang FP8 — novo como método 4, HuggingFace + MLX), tabela VRAM/quant com a contra-narrativa "16 GB é viável" (IQ4_XS 15.71 GB), sampling thinking vs instruct, troubleshooting com 6 fixes e FAQ com 10 Q&As EN. Head completo no padrão EN da hub `best-local-30b-models`, JSON-LD `@graph` com TechArticle + BreadcrumbList + FAQPage (10), `inLanguage: en`, hreflang bidirecional, datas 2026-08-24.
- **hreflang bidirecional** no par `como-rodar` (pt-BR) ↔ hub EN (`guia/en/how-to-run-qwen3-8-27b`); `como-rodar` PT ganhou também o link "View in English →" no header do artigo.
- **llms.txt**: subseção `### How to run Qwen3.8-27B locally (2026)` na seção `## English (GEO mirrors)` (diff aditivo).
- **sitemap.xml**: URL do hub EN (37 → 38), lastmod 2026-08-24, priority 0.9.
- **guia/index.html**: card novo "How to Run Qwen3.8-27B (EN)" (tag Inglês, MOFU · Novo 24/08).

---

## [2026-08-23] — Monetização: newsletter + affiliate de hardware + slots de ads (t_8dd9a051)

### Added
- **Newsletter (Buttondown-ready, endpoint configurável)** nos 3 placements do PRD §8.1:
  - Home: seção `Receba o resumo semanal` (entre "Por categoria" e o footer).
  - Fim de artigo: form inline em **todos os 28 artigos** de `/guia/*`.
  - Footer global: mini-form na 5ª coluna + disclosure de afiliado + link `Política de privacidade`.
  - `assets/js/newsletter.js`: wrapper JS `fetch` a endpoint configurável (`window.NEWSLETTER_CONFIG`), feedback inline (`aria-live`), **sem redirecionar** o leitor, sem popup, sem dark pattern. Fallback honesto sem endpoint: "Ainda não abrimos as inscrições". Sem-JS: POST nativo ao `action` configurável. Evento GA4 `newsletter_subscribe`/`newsletter_error`.
  - `templates/newsletter.html`: fragmento canônico com as 3 variações (fonte única, padrão BIND-08).
- **Affiliate de hardware (PRD §8.2)** em 6 artigos de hardware/compra (`hardware-local`, `quantizacao-gguf-30b-quanto-cabe-na-sua-gpu`, `tokens-por-segundo-30b-hardware-real`, `lemonade-sdk-v11-6-llm-local-gpu-npu-amd`, `qwen38-27b-16gb-vram-llama-cpp`, `qwen3-8-27b-contexto-256k-24gb`): bloco "Hardware recomendado para rodar este modelo" com tabela (produto · onde comprar), disclosure obrigatório sempre visível (estilo Tecnoblog) e links `rel="sponsored noopener"`. Comentário no markup indica onde adicionar `?tag=SEUTAG` (Amazon Associates/ML) para ativar a comissão. `templates/affiliate.html` = fragmento canônico.
- **Slots de ads (PRD §8.3, desligados)**: `.ad-slot` com `display:none` + comentário `<!-- ad slot: ativar quando tráfego >20k/mês -->` na home e em todos os artigos. Ativar na Fase 3 = só CSS + 1 script.
- **`privacidade.html`** (página nova, LGPD): o que coletamos (email da newsletter + GA4 com `anonymize_ip`), finalidade, disclosure de afiliado, consentimento/descadastro da newsletter, direitos LGPD e contato. Canonical `/privacidade` (clean URL, padrão do site), meta robots index, GSC token, entrada no sitemap.
- **`assets/css/blog-monetizacao.css`**: componentes `.newsletter` (3 variações), `.affiliate`, `.ad-slot`, `.newsletter-status` — compõem com os tokens do design system (`var(--surface)` etc.) e funcionam nas páginas atuais (fallback em camadas).
- **Scripts de manutenção**: `scripts/integrar_monetizacao.py` (aplica/atualiza os blocos nas páginas) e `scripts/qa_monetizacao.py` (Playwright, 42 asserts).

### Changed
- **index.html**: `<link>` monetizacao.css + `<script defer>` newsletter.js; seção newsletter na home; 5ª coluna no footer; disclosure + link de privacidade no rodapé.
- **28 artigos de `/guia/*`**: newsletter inline + ad-slot no fim do corpo (antes do footer); link CSS + script JS no head. Os 6 de hardware/compra ganham também o bloco affiliate (disclosure + `rel=sponsored`).
- **sitemap.xml**: entrada aditiva `/privacidade`.

### Notes
- **Endpoint da newsletter não configurado** (sem chave Buttondown/Formspree): form ativo, feedback honesto "em breve", sem fake success. Ativar = definir `window.NEWSLETTER_CONFIG` (instruções no topo do `newsletter.js`).
- **check_head.py**: pré-existente em main, a entrada `sitemap:/guia/qwen3-8-27b-lm-studio` aponta para página inexistente (não tocada neste card; regen de sitemap é escopo do card de template/home). Todas as outras checagens C1-C5 passam (privacidade mapeada corretamente).

---

## [2026-08-23] — Hub page EN "Best Local 30B Models (Aug/2026)" — espelho GEO (t_e6d5bf5c)

### Added
- **Hub page EN** (`guia/en/best-local-30b-models`): espelho em inglês da hub PT `melhores-modelos-locais-30b` — 11 modelos, tabela GGUF medida interativa (sortable + filtros por caso de uso + contador "N of 11"), 7 vereditos, seção rivais LCB v6, FAQ 7, JSON-LD 5 blocos `inLanguage: en`, datas canônicas 2026-08-23, `proficiencyLevel: Beginner`. Números byte-idênticos ao PT; prosa EN com ponto decimal; link recíproco "Original in Portuguese" → hub PT.
- **hreflang bidirecional** em 4 páginas (hub EN/PT + artigo slow EN/PT), sem `x-default`.
- **llms.txt**: seção `## English (GEO mirrors)` com subseção `### Best local 30B models (Aug/2026)` (resumo + stats citáveis + link), conteúdo do bloco slow intocado.
- **Sitemap**: URL `guia/en/best-local-30b-models` (lastmod 2026-08-23, changefreq weekly, priority 0.9) — 35 → 36 URLs.
- **Card no `guia/index`**: "Best Local 30B Models (EN)" (tag Inglês, MOFU · Novo 23/08).

### Changed
- **Hub PT `guia/melhores-modelos-locais-30b`**: +2 links hreflang (pt-BR self + en) e link "View in English" no nav — única mudança no arquivo (hotspot).
- **Artigos slow PT/EN**: par hreflang bidirecional (en ↔ pt), selfs corretos, sem `x-default`.

## [2026-08-23] — Página uncensored: OBLITERATUS V3 "Deep Liberation" (t_0e16ae1c)

### Added
- **Seção "OBLITERATUS V3 — Deep Liberation: a quarta peça do ecossistema"** em `guia/qwen3-8-27b-uncensored-abliterated`: repo OBLITERATUS/Qwen3.8-27B-OBLITERATED (Pliny the Prompter / suite elder-plinius, criado 19/08, V3 atualizado 23/08 03:58 UTC) — tabela V1→V2→V3 (MMLU 84,5→81,4→84,3→82,3; recusa dura e deflexão suave; cyber/código 20/20; thinking-mode compatível na V3), método de *complementary abliteration blending* (SVD+LEACE), settings ótimos documentados (temp 0 · repetition_penalty 1,15 · max ≥2048 · sem system prompt · thinking OFF), 5 GGUFs (IQ4_XS 15,42 a Q8_0 29,05 GB + mmproj 0,93) e callout de honestidade com limitações do próprio README.
- **JSON-LD**: SoftwareApplication `#obliteratus` (Qwen3.8-27B-OBLITERATED, V3 Deep Liberation, 244.834 downloads/577 likes, Apache 2.0) + `about` estendido no TechArticle; dateModified 2026-08-23.

### Changed
- **Meta/description/OG/Twitter** da página uncensored: menção ao OBLITERATUS V3 e keywords `obliteratus`, `deep liberation` (grep "obliterat" no repo passou de 0 ocorrências).
- **Sitemap.xml**: lastmod de `guia/qwen3-8-27b-uncensored-abliterated` atualizado para 2026-08-23 (a página já tinha entrada própria — nenhuma URL nova).

## [2026-08-23] — Artigo-veredicto "Qwen3.8-27B ou Ornith-1.5-35B-A3B?" (t_65080d35)

### Added
- **Artigo-veredicto** `guia/qwen3.8-vs-ornith-1-5-35b-a3b/index.html`: o novo MoE local (35B/3B ativos, MIT, trending no HF) contra o 27B denso — tabela do par, tabela GGUF oficial + AD-quants AtomicChat, veredito por perfil, aviso de honestidade BenchLM (49,3/100, rank #136, coverage insuficiente), 4 FAQs e JSON-LD TechArticle + FAQPage.
- **llms.txt**: 3 inserções aditivas — bullet novo no dossiê de vereditos (Código/agentes ≤30B), entrada nova na lista de páginas e FAQ nova (Qual o melhor modelo local para código e agentes em 2026?).
- **FAQ** (`guia/faq/index.html`): 37ª pergunta "Qwen3.8-27B ou Ornith-1.5-35B-A3B para código e agentes?" na seção Comparações (h3 + Question JSON-LD com paridade).
- **Sitemap.xml**: 35 → 36 URLs (nova página com priority 0.8, lastmod 2026-08-23).
- **Guia** (`guia/index.html`): card novo no topo do card-grid (Comparativo, Novo 23/08).

## [2026-08-22] — Comunidade: novos relatos de cibersegurança com MCPs e cloth simulator single-shot (t_f4533dbe)

### Added
- **Seção "Novos Relatos — Agosto/2026"** em `guia/comunidade-casos-uso`: relato de analista sênior de cibersegurança (Potential_Block4598) sobre Qwen3.8-27B com Ghidra + Vbox MCP + debugger MCP — "devoured the malware that Opus couldn't". Thread `1vonuu0` com 5 citações literais verificáveis.
- **Sub-seção "Geração de Código Single-Shot"**: cloth simulator HTML single-file com física perfeita (UDPSendToFailed), jogo Snake 3D (slavik-dev, único modelo além do Opus a conseguir), Tetris com sons retrô (Pear_Virtual), protocolo de rede nível Claude/Codex (michael_quigley). Thread `1voa3ch` com 4 citações literais verificáveis.

### Changed
- **Sitemap.xml**: lastmod de `guia/comunidade-casos-uso` atualizado para 2026-08-22.

## [2026-08-22] — Guia Ollama do Qwen3.8-27B: Modelfile customizado, MTP, reasoning, visão e flash-attn (t_fe2ac331)

### Added
- **Guia Ollama dedicado** (`guia/ollama/index.html`): 12 tags catalogadas (18–56 GB), Modelfile customizado com num_ctx/draft_num_predict/num_gpu, reasoning effort xhigh→off via API/Modelfile/CLI, MTP embutido nas tags -mtp- (draft_num_predict 4 nativo), visão Text+Image sem mmproj extra, flash attention automático, overhead Ollama vs llama.cpp (~0% decode, ~2–5% API), FAQ com 7 perguntas + dica do xhigh default.
- **JSON-LD**: TechArticle + HowTo (6 steps) + FAQPage (7 perguntas) + BreadcrumbList.
- **Sitemap**: URL `guia/ollama` (priority 0.9, lastmod 2026-08-22).
- **llms.txt**: entrada do Ollama com descrição + 2 stats citáveis (566.2K downloads, 12 tags).

### Changed
- **Sitemap.xml**: 30 → 31 URLs (ollama adicionado).

## [2026-08-21] — Hub page: linha 11 = Qwen3-Coder-30B-A3B na tabela mestra (t_e0bd2b3c)

### Added
- **Hub page 10→11 linhas**: Qwen3-Coder-30B-A3B inserido após Apriel na tabela mestra interativa — MoE 30,5B, 3,3B ativos (128 experts, 8 ativos), IQ4_XS 16,38 GB, Q4_K_M 18,56 GB (Unsloth), contexto 262.144 (1M YaRN), Apache 2.0, sem visão, lançamento 31/07/2025. Tags de filtro: código + velocidade.
- **Callout recíproco hub→artigo** na seção vs: link para `/guia/qwen3.8-vs-qwen3-coder-30b-a3b` com SWE-bench Verified 51,6 e throughput 3,3× o denso.

### Changed
- **JSON-LD**: TechArticle (description com 11 modelos + Qwen3-Coder), ItemList (numberOfItems 10→11, ListItem posição 10 Coder, posição 11 DeepSeek), Dataset (description 11 modelos, variableMeasured expandido com Coder em gguf/contexto/licenca/visao/lancamento).
- **Meta/título**: title, description, OG, Twitter — "os 10" → "os 11", "10 modelos" → "11 modelos", menção ao Coder adicionada.
- **Texto visível**: lead, hero h2, hero p, quick-answer rivais, tabela-mestra h2, counter, footer — "dez" → "onze", "10" → "11", Coder incluído no texto da página.
- **Filter/counter**: botão "Todos (11)", counter "11 de 11 modelos", JS hardcoded `' de 11 modelos'`.

## [2026-08-21] — Hub page: extensão 6→10 modelos com 4 rivais 30B + seção vs (t_ac520ed5)

### Added
- **Hub page 6→10 linhas**: GLM-4.7-Flash, Nemotron-Cascade-2-30B-A3B, Gemma 4 31B e Apriel-1.6-15b-Thinker na tabela mestra interativa (filtros e sort), com dados de model cards oficiais verificados via HF API em 20/08.
- **Seção nova "Qwen3.8-27B vs os rivais 30B"** (antes da Metodologia): tabela LCB v6 com 6 linhas (Qwen 90,3 · Cascade 2 87,2 · Gemma 4 80,0 · Nano 68,3 · GLM 64,0 · GPT-OSS 61,0), mais três observações honestas sobre código, throughput/agentic e 12 GB, com contraponto empírico glukhov.org/pt.
- **FAQ da MOFU**: "Qwen3.8-27B ou GLM-4.7-Flash?" — JSON-LD FAQPage estendido para 7 perguntas.
- **Meta keywords**: glm 4.7 flash, gemma 4 31b, nemotron cascade 2, apriel, melhor modelo 30b moe vs denso.
- **Hero e TOC**: "os seis" → "os dez" em 6 superfícies.

### Changed
- **JSON-LD**: TechArticle (headline/description com 10 modelos, dateModified→2026-08-21), ItemList (numberOfItems 6→10 + 4 ListItems), Dataset (description/license/variableMeasured expandidos), FAQPage (1 nova pergunta + Gemma gap update).
- **Veredito-visão**: menção ao Gemma 4 31B (GPQA 84,3, MMMU Pro 76,9).
- **Veredito-hardware-fraco**: GPT-OSS mantém vencedor; Apriel 1.6 adicionado como residente 12 GB (7,91 GB).
- **Fontes e footer**: rivais, GGUFs Unsloth/bartowski, glukhov.org/pt adicionados.
- **Companions**: guia/index.html card atualizado, llms.txt, sitemap lastmod.
- **Warnings W1-W3 (hygiene)**: segundo h1 → h2, Dataset.license → MIT URL, title 68→58c, meta description 176→∼155c.

### Fixed
- **Counter JS**: `' de 6 modelos'` → `' de 10 modelos'` (hardcoded no JS do filtro).

## [2026-08-21] — Artigo "Quantização rouba mais de quem fala português?" + companions (t_e5d3270d)

### Added
- **Artigo novo `/guia/quantizacao-multilingue-portugues`**: o paper LCD (arXiv 2608.11786,
  12/08/2026, preprint single-author) mede que GPTQ INT3 degrada idiomas não-inglês 2–4×
  mais que o inglês — e não testou português. Artigo com a tabela de ratios por idioma, a
  estimativa honesta para PT (banda romance 1,5–1,7×, sempre rotulada como inferência), a
  cura LoRA rank-2 de 0,12%/20 min e o cruzamento com a tabela PPL medida do portal
  (WikiText-2 = inglês, o idioma-piso do dano). JSON-LD TechArticle + FAQPage(3).
- **llms.txt: 8 inserções aditivas** (6 bullets de citações + 1 entrada de página + 1 FAQ).
- **/guia/faq: 36ª pergunta** "Quantização piora o modelo em português?" — inserida após
  "O Qwen3.8-27B fala português?" (existente byte-idêntica), DOM + JSON-LD estendidos.
- **sitemap.xml: 32 URLs** (nova entrada `/guia/quantizacao-multilingue-portugues`).
- **guia/index.html: card novo no topo** do card-grid (padrão PR #34/#38).
- **Links internos nas irmãs de quantização** (1 por página, no corpo do texto):
  `quantizacao-gguf-30b-quanto-cabe-na-sua-gpu` (card 12–16 GB) e
  `qwen38-27b-16gb-vram-llama-cpp` (callout da tabela de quants).

## [2026-08-21] — H2 de objeção "é o mesmo modelo?" (t_20f0ae18)

### Added
- **H2 `#mesmo-modelo` no artigo `/guia/qwen3.8-vs-qwen3.6-27b`**: resposta à tese
  viral do r/LocalLLaMA (thread 1voblcs, 1.100 upvotes, 191 comentários) de que
  "Qwen3.8-27B é idêntico ao Qwen3.6-27B". Resposta na primeira frase: não — é a
  mesma arquitetura com pesos diferentes (26 vitórias em 26 benchmarks, mediana
  +9,8). Seção com a origem da tese, o que a thread acerta (config.json
  idêntico, mesma classe `Qwen3_5ForConditionalGeneration`), as 3 provas
  mensuráveis (scores por benchmark, tamanho de arquivo 17,11 vs 16,82 GB,
  throughput) e onde a objeção acerta (conhecimento: +1,4 a +1,8). Pergunta
  sem dono na SERP PT-BR (busca 21/08); formato pergunta-resposta disputa
  featured snippet.
- **Verificação própria arquivo-por-arquivo (21/08, HF API)**: config.json dos
  dois modelos é idêntico em arquitetura (só `transformers_version` difere);
  vocabulário BPE idêntico (248.044 tokens); mas o 3.8 traz chat template
  reescrito (injeta reasoning effort, xhigh default) e 7 added_tokens de áudio
  novos. Receita usada no H2 como prova adicional — e correção de fato: textos
  anteriores diziam "mesmo tokenizer e chat template", o template não é o
  mesmo (corrigido em 8 superfícies: H2, FAQ do artigo ×2, JSON-LD do artigo,
  FAQ page ×2, llms.txt ×2).
- **Nova pergunta na `/guia/faq`** (seção Comparações, primeira posição):
  "O Qwen3.8-27B é igual ao Qwen3.6-27B?" com link para o H2.
- **FAQ item no FAQ do próprio artigo vs** (primeira posição).

### Changed
- **JSON-LD FAQPage**: 7→8 perguntas no artigo vs, 33→34 na `/guia/faq` —
  paridade 1:1 com os h3, pergunta nova na primeira posição das duas páginas.
- **dateModified** do TechArticle vs: 2026-08-16 → 2026-08-21; lastmod das
  duas URLs no sitemap.xml.
- **llms.txt**: +1 stat citável ("é o mesmo modelo?"), +1 Q&A completo na
  seção Perguntas frequentes, descrição do link do artigo vs atualizada.
- **Card no `/guia`**: descrição atualizada, badge "Atualizado 21/08".

---
## [2026-08-21] — Artigo-veredicto "Qwen3.8-27B ou Qwen3-Coder 30B-A3B?" (t_8ec53707)

### Added
- **Artigo `/guia/qwen3.8-vs-qwen3-coder-30b-a3b`**: o vs-article MOFU da query-alvo
  "melhor modelo 30B para codar local" — o coder local mais instalado (11,9M
  downloads GGUF/mês, verificado ao vivo na HF API em 21/08) contra o 27B denso
  novo. Ossatura clonada do vs-article 3.8-vs-3.6: tabela do par com GGUF
  medido (IQ4_XS 16,38 / Q4_K_M 18,56 / UD-Q3_K_XL 13,81 GB na tree unsloth),
  âncora de throughput de classe 3,3× rotulada (56,6 vs 17,3 tok/s, medição
  própria Strix Halo com o Qwen3.6-35B como âncora da classe), a nuance do
  "deprecated → Coder-Next" (Artificial Analysis), veredito por perfil em 4
  cards (🟢🟢🟡🟡) e FAQ de 4 perguntas com textos citáveis. JSON-LD:
  TechArticle + FAQPage. Nota de rodapé obrigatória: SWE-bench Pro ≠ Verified,
  sem head-to-head oficial do par.
- **Companions**: llms.txt +3 inserções (bullet do dossiê de vereditos +
  entrada de página + FAQ nova); /guia/faq 33→34 perguntas (h3 + Question
  JSON-LD em paridade, seção Comparações); sitemap 30→31 URLs; card no topo do
  card-grid do /guia/ (tag Comparativo, MOFU).

---

## [2026-08-20] — Guia "Qwen3.8-27B no vLLM em produção" (t_dfd9c398)

### Added
- **Guia `/guia/como-rodar-vllm-qwen3-8-27b`**: o guia do segundo motor
  oficial de serving (o SGLang já tinha o seu desde 18/08; o vLLM era
  citado em 10 páginas sem guia dedicado). Comando de produção flag por
  flag (0.27.1), prefix caching no híbrido Mamba (default True no global,
  #50991 do caminho Mamba entrou após o corte da 0.27.1 — flag explícita
  recomendada; armadilha multimodal #52583), MTP com aceitação medida por
  precisão (FP8 0,771 / NVFP4-Inferact 0,897 / NVFP4-unsloth 0,788),
  contexto 262K→1M (hf-overrides aninhado em text_config), hardware
  verificado (GB300 TP4, 2× 5090 TP2, 1× 5090 eager 32K, 4× A5000,
  Ascend 950PR) e tabela dos 6 bugs abertos com workaround (#52682,
  #52583, #52564, #52475, MXFP4, #52734). JSON-LD: TechArticle + HowTo
  (5 steps) + FAQPage (6) + BreadcrumbList.
- **Companions**: sitemap 28→29 URLs; llms.txt +4 stats citáveis + link
  da página; card no /guia (tag Tutorial, BOFU).

### Fixed
- **Erro factual de versão em 9 superfícies**: "requer vLLM ≥ 0.27.2"
  não existe — PyPI vai de 0.27.1 (11/08) direto a 0.28.0rc1; exigência
  real da recipe oficial é 0.17.0+. Corrigido em guia/index.html (×2),
  faq (×2), como-rodar, hardware-local (×2), reasoning-config e
  como-rodar-sglang. (Nota: a thread r/LocalLLaMA 1vspexl citada no
  briefing estava inacessível — Reddit, espelhos redlib e PullPush
  bloqueados; o guia foi construído sobre fontes primárias verificáveis:
  recipe oficial recipes.vllm.ai, código da 0.27.1 e issues do GitHub.)

---

## [2026-08-20] — Artigo: 1 ano de gpt-oss (retrospectiva de adoção)

### Added
- **Artigo "1 ano de gpt-oss: 12 milhões de downloads/mês — e o que
  mudou no hardware local desde então"** (`guia/1-ano-gpt-oss-modelos-locais-2026/`,
  task kanban `t_01a0f16e`, Tema 2 do daily 20/08 — discovery `t_0b9e4ef4`):
  primeira retrospectiva do portal (gap: 2 menções passivas a gpt-oss no
  llms.txt, 0 artigos dedicados; 0 artigos no nicho comparando gerações
  anuais). Ancorada no aniversário exato (criado 2025-08-04 na HF API) e no
  post de William Callahan (19/08) que reacendeu o tema.
  - Dados-âncora re-verificados ao vivo na HF API em 20/08/2026 antes da
    escrita: gpt-oss-20b 7.590.370 dl/mês + 4.934 likes; gpt-oss-120b
    4.680.489 dl/mês + 5.114 likes (soma 12.270.859/mês); Qwen3.8-27B
    1.373.584 dl/mês + 11.733 likes (criado 2026-08-05). Post do
    williamcallahan re-lido integralmente (citação exata + fleet metrics
    Strix Halo ~29 / 5090 ~106 / M1 Ultra ~15 tok/s).
  - Regra anti-invenção do card cumprida: "2× mais inteligente" é sempre
    atribuído como PERCEPÇÃO de williamcallahan (blockquote com link),
    contraposto no mesmo fôlego pelo AAII 52 (medido, Artificial Analysis);
    seção dedicada "Downloads e likes não provam nada sobre qualidade"
    (downloads ≠ qualidade; likes ≠ qualidade; n=1 ≠ benchmark; geração-2025
    × geração-2026 sem benchmark cruzado publicado — lacuna declarada, não
    preenchida por estimativa).
  - Verificação adicional: configs oficiais dos 3 modelos (gpt-oss MoE
    32/128 especialistas, 4 ativos, MXFP4, 128K — vs Qwen3.8-27B denso
    híbrido 48+16, 256K) puxados ao vivo na escrita.
  - Conteúdo: tabela de adoção (downloads/likes com datas); citação
    traduzida; percepção vs medição; tabela comparativa de engenharia
    2025→2026 (4 mudanças estruturais); veredito por hardware (12–16 GB →
    gpt-oss-20b segue o pick; 24 GB+ → Qwen3.8-27B; RAM unificada → 120b
    ou 27B por multimodalidade/contexto/velocidade); callout de
    transparência das fontes; cross-refs para AAII, comparativo geracional,
    melhores ≤30B, 256K, tokens/s, guia-rapido, quantização, FAQ.
  - JSON-LD: TechArticle + 2× SoftwareApplication (gpt-oss-20b/120b,
    applicationCategory AIModel — ADR-008) + FAQPage (7 perguntas) +
    BreadcrumbList; GA4 G-016TVX8LEE com scroll_depth; canonical/OG/Twitter.
  - Companions: sitemap (27→28 URLs), llms.txt (+2 stats citáveis + página
    na lista + Q&A nova "Vale a pena rodar gpt-oss em 2026?"), card no
    `/guia` (primeiro da grade, tag-bench Retrospectiva, MOFU · Novo 20/08),
    Q&A nova na FAQ do portal (HTML + JSON-LD, "Comparações").

### Fixed
- **sitemap.xml malformado (preexistente)**: o bloco da URL do
  contexto-256k tinha dois `<loc>` sem o `</url><url>` de separação —
  parsers XML estritos descartavam a URL (27 `<loc>` no arquivo, 26
  parseados). Corrigido: 28 URLs agora parseiam limpas; a página do
  contexto-256k volta a constar no sitemap válido.
- **Card duplicado no `/guia` (preexistente)**: bloco do reasoning
  ("Configuração de reasoning: desativar o overthinking") aparecia 2× na
  grade de cards (idênticos). Removida a segunda ocorrência.

---

## [2026-08-20] — Artigo "Qwen3.8-27B-Uncensored: 980 mil downloads em 6 dias" (t_a5fe3174)

### Added
- **Artigo `/guia/qwen3-8-27b-uncensored-abliterated`** (Tema 1 do daily
  20/08, discovery t_0b9e4ef4): história de ecossistema + guia técnico do
  abliterated. Gap fechado: 0 menções a uncensored/abliterated/heretic em
  todo o portal, enquanto 3 repos derivados somam 1.058.505 downloads e 2
  foram atualizados no dia 20/08. Âncoras (verificadas ao vivo 20/08, README
  do JonathanColetti lido integralmente): 979.768 downloads em 6 dias;
  recusas 98/100 → 12/100 (100 prompts nocivos held-out, modo non-thinking)
  com KL de primeiro token 0,1191; MMLU 83,4→83,3 e demais deltas dentro do
  erro-padrão (0-shot, lm-eval-harness, bf16, mesma sessão); fronteira de
  Pareto publicada (200 trials Heretic, 23 pontos não-dominados); MTP
  re-enxertado do checkpoint base e verificado arquivo por arquivo (65/65
  blocos); tabela PPL wikitext-2 por quant com o aviso de não-ordenabilidade
  (IQ2_M único separável, ~2,8σ). Heretic: 27.920 stars (GitHub API).
  JSON-LD: TechArticle + 2× SoftwareApplication (AIModel, ADR-008) + HowTo +
  FAQPage (6) + BreadcrumbList. Tom: técnico, sem tutorial de uso nocivo,
  limitações do README reportadas na íntegra (incluindo "reduzida, não
  eliminada"); FP8 gated citado apenas por metadados públicos.
- **FAQ do portal**: nova Q&A "O que é um modelo abliterated?" (HTML +
  JSON-LD, 31→32 perguntas) com cross-ref para o artigo novo.
- **Companions**: sitemap.xml (28 URLs; +fix de `</url>` faltante na entrada
  do LTX-2.5 herdado de main), llms.txt (3 blocos de stats citáveis + página
  + Q&A), card "Análise" no topo do /guia.
- **Cross-refs**: quantizacao-gguf-30b, qwen3-8-27b-reasoning-configuracao-ideal
  (MTP), qwen3-8-27b-visao-videos-local, como-rodar-sglang (FP8 oficial),
  qwen38-27b-16gb-vram.

## [2026-08-20] — Atualização diária

### Added
- Auto-cura: corrigir 28 customização(ões) perdida(s) pós-update (programadora)
- 🌅 Daily Content 20/08 — modelos locais ≤30B (discovery)

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
  GGUF 11,27 GiB (llama.cpp #15396); Gemma 3 27B Q4_K_M 16,55 GB (bartowski, decimal — corrigido na revisão R1: 15,41 era GiB rotulado como GB).

### Decisions
- DeepSeek V4 Flash entra por paridade de ativos/token (13B), não de
  totais — rotulado "intruso" em tabela, callout e FAQ para não gerar
  claim falso de que é ≤30B em memória.
- GPT-OSS-20B: GGUF 11,27 GiB como número principal (medido), "16 GB"
  do anúncio citado como "inclui contexto" — evita repetir o pattern do
  claim "roda em 13GB" sem fonte clara.

## [2026-08-19] — Correção QA (t_b6a7139d): âncora 73,6 vs 73,4
reatribuída ao pareamento correto

### Fixed
- **[CRÍTICO] Par 73,6 vs 73,4 tok/s reatribuído**: o bench de 45
  configs da KGP Talkie testou somente o Qwen3.8-27B — 73,6 é thinking
  ON e 73,4 é thinking OFF do mesmo modelo; o bench não tem número do
  3.6. O artigo e companions apresentavam o par como "decode 3.8 vs
  3.6 com thinking off" em 16 superfícies: meta description,
  og/twitter description, JSON-LD TechArticle, FAQ #1 (HTML +
  JSON-LD), lead do hero, resposta rápida, stat-card, veredito, causa
  6, "erros comuns", card do /guia, FAQ do portal (HTML + JSON-LD) e
  llms.txt (3 blocos). Reframe para o pareamento real (thinking on vs
  off: o raciocínio não muda o decode, muda o tempo até a 1ª palavra,
  2,18 s → 0,18 s) e tese "decode 3.8 = decode 3.6" reancorada no que
  existe: InsiderLLM ~41,5 t/s ("3.8 ≈ 3.6") na 3090, Strix Halo 17,3
  vs 12,4 (medição própria) e dev.to (pesos de tamanho idêntico). O
  parágrafo "O benchmark que desarma a briga" já descrevia o
  pareamento on/off corretamente e não foi alterado. Detecção: QA
  t_80c62de4 (veredito FAIL sobre o source primário).
- **[MÉDIO] Multiplicador de MTP na 5090**: "1,81× (73,4 → 151,2
  t/s)" corrigido para "2,06× com draft n=2 e thinking off (73,4 →
  151,2 t/s)" no corpo (Causa 2) e na tabela resumo. No source, o
  1,81× é o pico do draft n=3 (73,6 → 133,6); o próprio KGP chama o
  n=2+off de "2.06x". Bases 73,6 → 73,4 corrigidas também na medição
  de referência e na tabela antes/depois.
- **[BAIXO] FAQ do artigo**: 6 perguntas h3 harmonizadas verbatim com
  o JSON-LD (ex.: "MTP tem custo?" → "Ativar MTP tem algum custo?")
  para máxima elegibilidade de featured snippet.
- **[BAIXO] Resíduo do fix irmão (t_9babb5d1, 5f95fe8)**: o
  twitter:description dizia ainda "MTP renomeado" (claim falso já
  corrigido nas demais superfícies) — alinhado para "MTP
  desligado".

## [2026-08-19] — Artigo: Qwen3.8-27B está lento? 6 causas e fixes

### Added
- **Artigo "Qwen3.8-27B está lento? As 6 causas reais e o fix de cada uma"**
  (`guia/qwen3-8-27b-lento-causas-fixes/`, task kanban `t_1ced3026`, PO
  card das threads r/LocalLLaMA 1voa3ch + 1vriwym): primeiro conteúdo do
  portal dedicado à dor "por que está lento" (gap: 'lento' só aparecia em
  menções espalhadas). Tese verificada por dados: o decode do 3.8 é igual
  ao do 3.6 (~41,5 t/s na 3090 com "3.8 ≈ 3.6"; 17,3 vs 12,4 no Strix
  Halo, medição própria); no bench de 45 configs o thinking não muda o
  decode do 3.8 — 73,6 on vs 73,4 off, só o tempo até a 1ª palavra
  (2,18 s → 0,18 s). As 6 causas: xhigh-trap
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
