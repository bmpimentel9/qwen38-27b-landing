# Briefs de Imagem — Portal Modelos Locais ≤30B

> **Autoridade visual:** `docs/guia-imagens.md` (conceito "Dark AI Lab", paleta, protocolo de luz, §9 template)
> **Autor:** perfil `fotografo` · task `t_1b8ad9ff` · 23/08/2026
> **Consumidor:** perfil `programadora` (task `t_28240207`) — gera as imagens com modelo local
> **Escopo:** 30 artigos do `/guia/` + 1 home (`index.html`) = **31 imagens**

---

## Como usar este documento

Cada imagem nasce do mesmo esqueleto — o estilo é UM para o site inteiro:

| Campo | Regra (herdada do guia) |
|---|---|
| **Conceito** | "Dark AI Lab": hardware real em estúdio escuro, um único protagonista |
| **Fundo** | `#0B0E14` (mesmo `--bg` do design system) — a imagem "casa" com a página |
| **Luz** | Key light 45° cima-esquerda + glow do acento da categoria + rim light frio |
| **Enquadramento** | Sujeito no **terço direito**, **terço esquerdo limpo** (espaço negativo p/ título), câmera levemente alta |
| **Lente** | 35–50mm f/2.8–4 (macro 100mm f/8 só p/ die/GPU em detalhe) |
| **Acento** | ≤10–15% da área, sobre superfície escura, cor da categoria |
| **Mood** | Calmo, competente, "engenharia de verdade", futuro próximo (2028) |
| **Texto** | NUNCA no modelo — plate limpo, typeset PIL depois |
| **Formato** | 1200×675 (16:9) artigos · 1920×1080 (crop 21:9) home · WebP ≤120KB/≤200KB |

**Mapeamento categoria → acento (1:1 com o `class` dos badges no `guia/index.html`):**

| Badge do site | Categoria | Acento | Hex | Qtd. artigos |
|---|---|---|---|---|
| `tag-guide` | Guias | Violeta | `#A78BFA` | 15 |
| `tag-bench` | Benchmarks | Ciano | `#2DD4BF` | 8 |
| `tag-hw` | Hardware | Verde | `#4ADE80` | 6 |
| `tag-community` | Comunidade | Azul | `#3B82F6` | 1 |
| — | Home (hero) | Gradiente violeta→ciano | `#9085E9 → #22D3EE` | 1 |

**Prompt exato (modelo local):** sempre em inglês, prosa natural, 40–90 palavras,
ordem sujeito → ação → estilo → contexto → iluminação → técnica, terminando com
`no text, no letters, no typography, no watermark`.

---

# A. HOME — `index.html`

## A1. Hero da home (1920×1080, visual amplo)

- **Categoria:** Home · **Acento:** gradiente de marca violeta→ciano (`#9085E9 → #22D3EE`)
- **Luz:** key light 45° cima-esquerda; o feixe violeta→ciano é o herói; rim light frio nas bordas do hardware
- **Enquadramento:** cluster de hardware no **terço inferior-direito**; metade superior-esquerda vazia (respiro pro headline "Fronteira em 27 bilhões de parâmetros")
- **Lente:** 24mm f/2.8, câmera levemente alta, profundidade em camadas (bokeh de luz ao fundo)
- **Mood:** preciso, aspiracional, "laboratório de engenharia 2028", energia fria e focada
- **Elementos futuristas:** workstation aberta com GPU preta instalada, partículas de dados violeta, linhas de rede neural finas, feixe de luz energético atravessando a bancada
- **Arquivo alvo:** `hero-home.webp` (ou `home-hero.webp`), 1920×1080, ≤200 KB

**Prompt exato:**
```
A wide hero scene of a dark futuristic engineering desk in a near-future lab,
dominated by an open workstation with a sleek matte black GPU installed and
stacked RAM, illuminated by a single beam of violet-to-cyan light (#9085E9 to
#22D3EE) tracing across the surface like flowing energy. Floating above the
desk, subtle glowing data particles and thin neural-network lines in violet.
Environment: deep #0B0E14 with a large clean dark negative space across the
upper-left half. Shot on a 24mm f/2.8 lens, slightly high angle. Lighting: key
light from upper-left, the violet-cyan gradient beam as the only accent, cool
rim light on hardware edges. Composition: hardware cluster in the lower-right
third, generous empty negative space upper-left, soft layered bokeh. Mood:
precise, aspirational, calm premium tech, near-future lab. no text, no letters,
no typography, no watermark.
```

---

# B. GUIAS — acento violeta `#A78BFA` (15 artigos · badge `tag-guide`)

## B1. `guia/como-rodar` — "Como Rodar o Qwen3.8-27B: Ollama, llama.cpp, vLLM, HuggingFace"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45° cima-esquerda; glow violeta nos traces da placa; rim light frio
- **Enquadramento:** workstation aberta no terço direito; espaço negativo à esquerda (título)
- **Lente:** 35mm f/4, câmera levemente alta, profundidade em camadas
- **Mood:** competente, "o caminho pra rodar", futuro próximo
- **Elementos futuristas:** placa-mãe com traces iluminados em violeta partindo como 4 caminhos (um por método), CPU e GPU com heat sink de cobre, cabos organizados
- **Arquivo alvo:** `como-rodar.webp` · **Alt:** "Placa-mãe escura com circuitos violeta e GPU instalada — guia para rodar o Qwen3.8-27B localmente"

**Prompt exato:**
```
An open workstation motherboard on a dark lab bench, matte black PCB with a
copper heat sink over the CPU and a GPU card installed, thin glowing #A78BFA
violet circuit traces branching across the board like four distinct paths.
Environment: deep #0B0E14 background with soft violet bokeh lights far behind.
Shot on a 35mm f/4 lens from a slightly high angle. Lighting: one strong key
light from upper-left at 45 degrees, violet glow (#A78BFA) from the traces as
the only accent, thin cool rim light on the edges. Composition: board on the
right third, left third kept as clean empty negative space, shallow depth of
field, layered foreground bokeh. Mood: calm, competent, premium technical
product photography, near-future engineering lab. no text, no letters, no
typography, no watermark.
```

## B2. `guia/como-rodar-sglang-qwen3-8-27b` — "SGLang + FP8 oficial: servidor de alto throughput"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta das partículas de token fluindo pro servidor; rim light frio
- **Enquadramento:** blade de servidor no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, câmera levemente alta
- **Mood:** "infraestrutura que entrega tok/s", preciso
- **Elementos futuristas:** blade de rack escuro com heatsink, fluxo de partículas de token entrando como luz violeta (alta vazão), LEDs de status
- **Arquivo alvo:** `como-rodar-sglang.webp`

**Prompt exato:**
```
A single dark server blade standing upright on a lab bench, brushed aluminum
with a matte black heat sink, a stream of tiny glowing #A78BFA violet token
particles flowing into its edge like data being served, small status LEDs
along the front. Environment: deep #0B0E14 background with soft violet bokeh.
Shot on a 50mm f/2.8 lens, slightly high angle. Lighting: strong key light from
upper-left at 45 degrees, violet glow (#A78BFA) of the token stream as the only
accent, thin cool rim light on the edges. Composition: blade on the right third,
left third clean empty negative space, shallow depth of field. Mood: precise,
calm, premium technical product photography, near-future engineering lab. no
text, no letters, no typography, no watermark.
```

## B3. `guia/como-rodar-vllm-qwen3-8-27b` — "vLLM em produção: prefix caching e bugs reais"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta dos blocos de cache empilhados; rim light
- **Enquadramento:** torre de servidor no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "produção", contido, confiável
- **Elementos futuristas:** torre de servidor com camadas de cache (blocos translúcidos empilhados com traces violeta = prefix caching), cabos organizados
- **Arquivo alvo:** `como-rodar-vllm.webp`

**Prompt exato:**
```
A compact server tower on a dark bench with a transparent side window revealing
stacked translucent cache layers and a GPU, thin #A78BFA violet circuit traces
lighting each layer like a prefix-cache stack, one neat cable to the side.
Environment: deep #0B0E14 background with soft violet bokeh. Shot on a 50mm
f/2.8 lens, slightly high angle. Lighting: one strong key light from upper-left
at 45 degrees, violet glow (#A78BFA) from the cache layers as the only accent,
thin cool rim light separating the case. Composition: tower on the right third,
left third kept clean empty negative space, shallow depth of field. Mood: calm,
competent, premium hardware photography, near-future engineering lab. no text,
no letters, no typography, no watermark.
```

## B4. `guia/quantizacao-multilingue-portugues` — "Quantização rouba mais de quem fala português?"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta apenas na camada "português" destacada; rim light
- **Enquadramento:** pilha de wafers de silício no terço direito; negativo à esquerda
- **Lente:** 100mm macro f/8 (nitidez nas camadas)
- **Mood:** análise séria, "o dado por trás do idioma", futuro próximo
- **Elementos futuristas:** camadas de silício empilhadas (uma camada com traces violeta mais intensa = o português sob pressão da quantização), textura de die visível
- **Arquivo alvo:** `quantizacao-multilingue-portugues.webp`

**Prompt exato:**
```
A stack of silicon wafer layers on a dark lab bench, close-up macro shot showing
the texture of chip dies and thin #A78BFA violet circuit traces on one central
layer glowing brighter than the others, suggesting a language under pressure,
other layers dim and matte. Environment: deep #0B0E14 background with a faint
violet bokeh. Shot on a 100mm macro f/8 lens, slightly high angle. Lighting:
one strong key light from upper-left at 45 degrees, the violet glow (#A78BFA)
on the single layer as the only accent, thin cool rim light on the stack edges.
Composition: wafer stack on the right third, left third clean empty negative
space, crisp depth of field. Mood: precise, analytical, premium technical
photography, near-future engineering lab. no text, no letters, no typography,
no watermark.
```

## B5. `guia/melhores-modelos-locais-30b` — "Melhores modelos locais de 30B (ago/2026)"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta nos 11 módulos; rim light
- **Enquadramento:** fileira de módulos GPU no terço direito; negativo à esquerda
- **Lente:** 35mm f/4, levemente alta
- **Mood:** "a estante do acervo", organizado, confiável
- **Elementos futuristas:** prateleira escura com 11 módulos GPU compactos, um levemente mais iluminado (o destaque), traces violeta
- **Arquivo alvo:** `melhores-modelos-locais-30b.webp`

**Prompt exato:**
```
A dark shelf holding eleven compact GPU modules in a row on a lab bench, each
matte black with a small glowing #A78BFA violet accent, the one in the center
slightly brighter as the standout, organized and evenly spaced. Environment:
deep #0B0E14 background with soft violet bokeh far behind. Shot on a 35mm f/4
lens from a slightly high angle. Lighting: one strong key light from upper-left
at 45 degrees, the violet glow (#A78BFA) on each module as the only accent, thin
cool rim light on the edges. Composition: row of modules on the right third,
left third kept clean empty negative space, shallow depth of field. Mood: calm,
organized, premium technical product photography, near-future engineering lab.
no text, no letters, no typography, no watermark.
```

## B6. `guia/qwen3.8-vs-qwen3-coder-30b-a3b` — "Qwen3.8-27B ou Qwen3-Coder 30B-A3B?"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta nos dois módulos lado a lado; rim light
- **Enquadramento:** dois módulos GPU emparelhados no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "confronto honesto", decisão por perfil de uso
- **Elementos futuristas:** dois GPUs de arquiteturas diferentes (um denso, um MoE) com traces violeta de intensidades diferentes, sombra de medição
- **Arquivo alvo:** `qwen3.8-vs-qwen3-coder-30b-a3b.webp`

**Prompt exato:**
```
Two GPU cards standing side by side on a dark lab bench, one a solid dense matte
black card, the other with a more open layered design, both with thin glowing
#A78BFA violet circuit traces of slightly different brightness, a subtle light
shadow between them suggesting a measured comparison. Environment: deep #0B0E14
background with soft violet bokeh. Shot on a 50mm f/2.8 lens, slightly high
angle. Lighting: one strong key light from upper-left at 45 degrees, violet glow
(#A78BFA) from the traces as the only accent, thin cool rim light. Composition:
the two cards on the right third, left third clean empty negative space, shallow
depth of field. Mood: precise, calm, premium technical photography, near-future
engineering lab. no text, no letters, no typography, no watermark.
```

## B7. `guia/en/why-is-qwen3-8-27b-slow` — "Why is Qwen3.8-27B slow? (EN)"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta no velocímetro; rim light
- **Enquadramento:** GPU com mostrador no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "a física que não se resolve", direto, confiável
- **Elementos futuristas:** GPU densa com um mostrador/tacômetro holográfico, grão de silício visível (o custo físico do denso), traces violeta
- **Arquivo alvo:** `why-is-qwen3-8-27b-slow.webp`

**Prompt exato:**
```
A dense matte black GPU card on a dark bench with a holographic tachometer dial
floating above it, needle low, the silicon die texture visible on the card,
thin #A78BFA violet circuit traces across the PCB. Environment: deep #0B0E14
background with soft violet bokeh. Shot on a 50mm f/2.8 lens, slightly high
angle. Lighting: one strong key light from upper-left at 45 degrees, violet glow
(#A78BFA) of the traces as the only accent, thin cool rim light. Composition:
card on the right third, left third clean empty negative space, shallow depth of
field. Mood: calm, precise, premium technical product photography, near-future
engineering lab. no text, no letters, no typography, no watermark.
```

## B8. `guia/qwen3-8-27b-reasoning-configuracao-ideal` — "Desativar overthinking e configurar reasoning"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta no grafo de raciocínio podado; rim light
- **Enquadramento:** grafo neural acima da GPU no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "pensar menos, entregar mais", focado
- **Elementos futuristas:** grafo de rede neural em holograma sendo podado (ramos cortados, núcleo compacto), GPU com traces violeta abaixo
- **Arquivo alvo:** `qwen3-8-27b-reasoning-configuracao-ideal.webp`

**Prompt exato:**
```
A matte black GPU card on a dark bench with a small holographic neural-network
graph floating above it, the graph pruned and compact with thin #A78BFA violet
branches and a few cut stubs, suggesting trimmed reasoning, glowing circuit
traces across the card. Environment: deep #0B0E14 background with soft violet
bokeh. Shot on a 50mm f/2.8 lens, slightly high angle. Lighting: one strong key
light from upper-left at 45 degrees, the violet glow (#A78BFA) of the graph as
the only accent, thin cool rim light. Composition: card on the right third, left
third clean empty negative space, shallow depth of field. Mood: calm, focused,
premium technical product photography, near-future engineering lab. no text, no
letters, no typography, no watermark.
```

## B9. `guia/qwen3-8-27b-visao-videos-local` — "Qwen3.8-27B enxerga: visão, vídeo e OCR locais"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta no módulo de visão; rim light
- **Enquadramento:** GPU com módulo de câmera acoplado no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "o modelo que vê", curioso, competente
- **Elementos futuristas:** GPU com um pequeno módulo de visão (chip + lente) conectado por traces violeta, bounding boxes holográficos flutuando
- **Arquivo alvo:** `qwen3-8-27b-visao-videos-local.webp`

**Prompt exato:**
```
A matte black GPU card on a dark bench with a small attached vision module — a
tiny camera lens on a chip — connected by thin glowing #A78BFA violet circuit
traces, faint holographic bounding boxes floating above the lens. Environment:
deep #0B0E14 background with soft violet bokeh. Shot on a 50mm f/2.8 lens,
slightly high angle. Lighting: one strong key light from upper-left at 45
degrees, the violet glow (#A78BFA) from the traces as the only accent, thin cool
rim light. Composition: card on the right third, left third clean empty negative
space, shallow depth of field. Mood: calm, competent, premium technical product
photography, near-future engineering lab. no text, no letters, no typography,
no watermark.
```

## B10. `guia/minimax-music3-musica-local` — "MiniMax Music3 local: música com IA em 8GB"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta na forma de onda; rim light
- **Enquadramento:** GPU com forma de onda holográfica no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "a máquina que compõe", surpreendente, contido
- **Elementos futuristas:** GPU com uma forma de onda sonora em holograma violeta e um pequeno alto-falante escuro, partículas de nota flutuando
- **Arquivo alvo:** `minimax-music3-musica-local.webp`

**Prompt exato:**
```
A matte black GPU card on a dark bench beside a small matte speaker, a delicate
holographic sound waveform in #A78BFA violet floating above, tiny glowing
particles drifting like musical notes, thin circuit traces across the card.
Environment: deep #0B0E14 background with soft violet bokeh. Shot on a 50mm
f/2.8 lens, slightly high angle. Lighting: one strong key light from upper-left
at 45 degrees, the violet waveform glow (#A78BFA) as the only accent, thin cool
rim light. Composition: card on the right third, left third clean empty negative
space, shallow depth of field. Mood: calm, precise, premium technical product
photography, near-future engineering lab. no text, no letters, no typography,
no watermark.
```

## B11. `guia/ltx-2-5-video-local-comfyui` — "LTX-2.5 local: vídeo com áudio no ComfyUI"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta na linha do tempo; rim light
- **Enquadramento:** GPU com linha do tempo de vídeo holográfica no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "gerar movimento local", criativo, preciso
- **Elementos futuristas:** GPU com uma linha do tempo de vídeo holográfica (frames como quadradinhos de luz violeta) e um marcador de play, traces na placa
- **Arquivo alvo:** `ltx-2-5-video-local-comfyui.webp`

**Prompt exato:**
```
A matte black GPU card on a dark bench with a holographic video timeline
floating above — a row of tiny square light frames in #A78BFA violet with a
glowing play marker — thin circuit traces across the PCB. Environment: deep
#0B0E14 background with soft violet bokeh. Shot on a 50mm f/2.8 lens, slightly
high angle. Lighting: one strong key light from upper-left at 45 degrees, the
violet glow (#A78BFA) of the frames as the only accent, thin cool rim light.
Composition: card on the right third, left third clean empty negative space,
shallow depth of field. Mood: calm, focused, premium technical product
photography, near-future engineering lab. no text, no letters, no typography,
no watermark.
```

## B12. `guia/faq` — "FAQ — Perguntas Frequentes"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta no núcleo de conhecimento; rim light
- **Enquadramento:** núcleo radiante no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "respostas rápidas", claro, confiável
- **Elementos futuristas:** um núcleo central de dados com linhas radiais de conhecimento (sem texto — apenas nós de luz violeta)
- **Arquivo alvo:** `faq.webp`

**Prompt exato:**
```
A small dark knowledge core on a lab bench — a cube of matte black with thin
#A78BFA violet light lines radiating outward to small glowing nodes, like quick
answers spreading, resting on a dark surface. Environment: deep #0B0E14
background with soft violet bokeh. Shot on a 50mm f/2.8 lens, slightly high
angle. Lighting: one strong key light from upper-left at 45 degrees, the violet
glow (#A78BFA) of the radiating lines as the only accent, thin cool rim light.
Composition: core on the right third, left third clean empty negative space,
shallow depth of field. Mood: calm, clear, premium technical product photography,
near-future engineering lab. no text, no letters, no typography, no watermark.
```

## B13. `guia/ollama` — "Ollama: do ollama run ao MTP em produção"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta no caminho do comando; rim light
- **Enquadramento:** desktop tower no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "a porta de entrada", simples, competente
- **Elementos futuristas:** torre desktop com janela lateral transparente revelando camadas de Modelfile (blocos empilhados com traces violeta) e um único feixe de luz entrando (o "ollama run"), GPU e RAM visíveis
- **Arquivo alvo:** `ollama.webp`

**Prompt exato:**
```
A desktop tower on a dark bench with a transparent side window revealing GPU,
RAM sticks and stacked translucent Modelfile layers with thin #A78BFA violet
circuit edges, a single beam of violet light entering the front like one
command. Environment: deep #0B0E14 background with soft violet bokeh. Shot on a
50mm f/2.8 lens, slightly high angle. Lighting: one strong key light from
upper-left at 45 degrees, the violet glow (#A78BFA) of the layers as the only
accent, thin cool rim light. Composition: tower on the right third, left third
clean empty negative space, shallow depth of field. Mood: calm, simple,
competent, premium hardware photography, near-future engineering desk. no text,
no letters, no typography, no watermark.
```

## B14. `guia/en/best-local-30b-models` — "Best Local 30B Models (EN)"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta no grid de módulos; rim light
- **Enquadramento:** grid de 11 módulos no terço direito; negativo à esquerda
- **Lente:** 35mm f/4, levemente alta
- **Mood:** "o acervo em inglês", organizado, confiável
- **Elementos futuristas:** uma grade/caixas modulares escuras com 11 GPUs compactas (layout em cofre/rack), cada uma com acento violeta, uma mais brilhante
- **Arquivo alvo:** `best-local-30b-models.webp`

**Prompt exato:**
```
A dark vault-like rack grid on a lab bench holding eleven compact GPU modules
in neat compartments, each matte black with a small glowing #A78BFA violet
accent, the central one slightly brighter as the standout, clean right angles.
Environment: deep #0B0E14 background with soft violet bokeh far behind. Shot on
a 35mm f/4 lens from a slightly high angle. Lighting: one strong key light from
upper-left at 45 degrees, the violet glow (#A78BFA) on the modules as the only
accent, thin cool rim light. Composition: rack grid on the right third, left
third kept clean empty negative space, shallow depth of field. Mood: calm,
organized, premium technical product photography, near-future engineering lab.
no text, no letters, no typography, no watermark.
```

## B15. `guia/qwen3.8-vs-ornith-1-5-35b-a3b` — "Qwen3.8-27B ou Ornith-1.5-35B-A3B?"

- **Categoria:** Guias · **Acento:** violeta `#A78BFA`
- **Luz:** key 45°; glow violeta nos dois dies no trilho de medição; rim light
- **Enquadramento:** trilho com dois dies no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "o trending contra o denso", honesto, medido
- **Elementos futuristas:** um trilho de medição escuro com dois módulos de silício — um denso (malha completa) e um MoE (apenas nós ativos acesos) — conectados por uma linha de luz violeta, como eixo de comparação
- **Arquivo alvo:** `qwen3.8-vs-ornith-1-5-35b-a3b.webp`

**Prompt exato:**
```
A dark measurement rail on a lab bench holding two silicon die modules, one a
solid dense matte black lattice, the other a sparser MoE design with only a few
#A78BFA violet active nodes lit, a thin line of violet light connecting them as
a comparison axis. Environment: deep #0B0E14 background with soft violet bokeh.
Shot on a 50mm f/2.8 lens, slightly high angle. Lighting: one strong key light
from upper-left at 45 degrees, the violet glow (#A78BFA) of the lit nodes as the
only accent, thin cool rim light. Composition: rail on the right third, left
third clean empty negative space, shallow depth of field. Mood: calm, honest,
premium technical product photography, near-future engineering lab. no text, no
letters, no typography, no watermark.
```

---

# C. BENCHMARKS — acento ciano `#2DD4BF` (8 artigos · badge `tag-bench`)

## C1. `guia/benchmarks-comparativos` — "Benchmarks Comparativos (26 resultados)"

- **Categoria:** Benchmarks · **Acento:** ciano `#2DD4BF`
- **Luz:** key 45°; glow ciano no grafo 3D; rim light
- **Enquadramento:** GPU com grafo de barras holográfico no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "o placar dos dados", exato, confiável
- **Elementos futuristas:** GPU com holograma de gráfico 3D de barras em acrílico escuro (barras ciano), tokens de texto fluindo ao fundo
- **Arquivo alvo:** `benchmarks-comparativos.webp`

**Prompt exato:**
```
A matte black GPU accelerator card standing upright on a dark lab bench with a
small dark glass hologram floating in front showing a rising 3D bar chart made
of light, thin glowing #2DD4BF cyan circuit traces branching across the PCB.
Environment: deep #0B0E14 background with soft cyan bokeh lights far behind.
Shot on a 50mm f/2.8 lens, slightly high angle. Lighting: strong key light from
upper-left at 45 degrees, cyan glow (#2DD4BF) of the chart and traces as the
only accent, thin cool rim light on the edges. Composition: subject on the right
third, left third kept as clean empty negative space, shallow depth of field.
Mood: precise, calm, premium technical product photography, near-future
engineering lab. no text, no letters, no typography, no watermark.
```

## C2. `guia/qwen3-8-27b-uncensored-abliterated` — "Qwen3.8-27B-Uncensored: 980 mil downloads em 6 dias"

- **Categoria:** Benchmarks · **Acento:** ciano `#2DD4BF`
- **Luz:** key 45°; glow ciano no portão aberto; rim light
- **Enquadramento:** GPU com portão holográfico aberto no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "o dado do fenômeno", analítico, contido
- **Elementos futuristas:** GPU com um portão de luz ciano se abrindo (as recusas removidas), contador de downloads holográfico (sem texto — apenas barras subindo)
- **Arquivo alvo:** `qwen3-8-27b-uncensored-abliterated.webp`

**Prompt exato:**
```
A matte black GPU card on a dark bench with a holographic gate of #2DD4BF cyan
light opening in front of it, small rising light bars beside it suggesting
climbing downloads, thin cyan circuit traces across the PCB. Environment: deep
#0B0E14 background with soft cyan bokeh. Shot on a 50mm f/2.8 lens, slightly
high angle. Lighting: one strong key light from upper-left at 45 degrees, the
cyan glow (#2DD4BF) of the gate as the only accent, thin cool rim light.
Composition: card on the right third, left third clean empty negative space,
shallow depth of field. Mood: calm, analytical, premium technical product
photography, near-future engineering lab. no text, no letters, no typography,
no watermark.
```

## C3. `guia/1-ano-gpt-oss-modelos-locais-2026` — "1 ano de gpt-oss: 12M downloads/mês"

- **Categoria:** Benchmarks · **Acento:** ciano `#2DD4BF`
- **Luz:** key 45°; glow ciano no anel anual; rim light
- **Enquadramento:** GPU com anel de órbita no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "um ano de números", retrospectivo, confiável
- **Elementos futuristas:** GPU com um anel orbital de luz ciano em torno (o ciclo de 1 ano), partículas de download orbitando como dados
- **Arquivo alvo:** `1-ano-gpt-oss-modelos-locais-2026.webp`

**Prompt exato:**
```
A matte black GPU card on a dark bench with a thin #2DD4BF cyan orbital ring of
light circling it like an annual cycle, small glowing particles orbiting along
the ring like downloads, faint cyan circuit traces on the card. Environment:
deep #0B0E14 background with soft cyan bokeh. Shot on a 50mm f/2.8 lens,
slightly high angle. Lighting: one strong key light from upper-left at 45
degrees, the cyan ring glow (#2DD4BF) as the only accent, thin cool rim light.
Composition: card on the right third, left third clean empty negative space,
shallow depth of field. Mood: calm, retrospective, premium technical product
photography, near-future engineering lab. no text, no letters, no typography,
no watermark.
```

## C4. `guia/qwen3.8-vs-qwen3.6-27b` — "Qwen3.8-27B vs Qwen3.6-27B: vale o upgrade?"

- **Categoria:** Benchmarks · **Acento:** ciano `#2DD4BF`
- **Luz:** key 45°; glow ciano nas duas GPUs (uma mais brilhante); rim light
- **Enquadramento:** duas GPUs de gerações diferentes no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "vale o upgrade?", honesto, direto
- **Elementos futuristas:** duas GPU cards lado a lado — a nova com traces ciano mais intensos e um brilho a mais, a antiga mais apagada; gráfico de barras holográfico entre elas
- **Arquivo alvo:** `qwen3.8-vs-qwen3.6-27b.webp`

**Prompt exato:**
```
Two GPU cards side by side on a dark bench, the newer one with brighter #2DD4BF
cyan circuit traces and a soft glow, the older one dimmer, a small holographic
bar chart floating between them in cyan light. Environment: deep #0B0E14
background with soft cyan bokeh. Shot on a 50mm f/2.8 lens, slightly high angle.
Lighting: one strong key light from upper-left at 45 degrees, the cyan glow
(#2DD4BF) as the only accent, thin cool rim light. Composition: the pair on the
right third, left third clean empty negative space, shallow depth of field.
Mood: calm, honest, premium technical product photography, near-future
engineering lab. no text, no letters, no typography, no watermark.
```

## C5. `guia/muse-glimmer-30b-agente-local` — "Meta Muse Glimmer 30B: agente local 24/7"

- **Categoria:** Benchmarks · **Acento:** ciano `#2DD4BF`
- **Luz:** key 45°; glow ciano no núcleo sempre-ativo; rim light
- **Enquadramento:** módulo agêntico no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "sempre ligado", vigilante, competente
- **Elementos futuristas:** módulo de agente compacto com núcleo de luz ciano pulsando (24/7), linhas de rede neural ao redor, LED de atividade
- **Arquivo alvo:** `muse-glimmer-30b-agente-local.webp`

**Prompt exato:**
```
A compact always-on agent module on a dark bench, matte black with a pulsing
#2DD4BF cyan light core at its center, thin neural-network lines radiating
around it, a small activity LED, resting on a dark surface. Environment: deep
#0B0E14 background with soft cyan bokeh. Shot on a 50mm f/2.8 lens, slightly
high angle. Lighting: one strong key light from upper-left at 45 degrees, the
cyan core glow (#2DD4BF) as the only accent, thin cool rim light. Composition:
module on the right third, left third clean empty negative space, shallow depth
of field. Mood: calm, vigilant, premium technical product photography,
near-future engineering lab. no text, no letters, no typography, no watermark.
```

## C6. `guia/agent-memory-leaderboard-resultados` — "Agent Memory Leaderboard: primeiros resultados"

- **Categoria:** Benchmarks · **Acento:** ciano `#2DD4BF`
- **Luz:** key 45°; glow ciano nas barras do pódio; rim light
- **Enquadramento:** módulo de memória com pódio holográfico no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "quem lembra mais", analítico, justo
- **Elementos futuristas:** módulo de memória (chips) com um pódio holográfico de barras ciano à frente, linhas de conexão de dados
- **Arquivo alvo:** `agent-memory-leaderboard-resultados.webp`

**Prompt exato:**
```
A dark memory module on a lab bench — a board with visible memory chips — with a
small holographic podium of #2DD4BF cyan light bars rising in front of it,
thin data connection lines between the chips, matte finish. Environment: deep
#0B0E14 background with soft cyan bokeh. Shot on a 50mm f/2.8 lens, slightly
high angle. Lighting: one strong key light from upper-left at 45 degrees, the
cyan bar glow (#2DD4BF) as the only accent, thin cool rim light. Composition:
module on the right third, left third clean empty negative space, shallow depth
of field. Mood: calm, analytical, premium technical product photography,
near-future engineering lab. no text, no letters, no typography, no watermark.
```

## C7. `guia/tokens-por-segundo-30b-hardware-real` — "Tokens por segundo no hardware real"

- **Categoria:** Benchmarks · **Acento:** ciano `#2DD4BF`
- **Luz:** key 45°; glow ciano no fluxo de tokens; rim light
- **Enquadramento:** GPU com fluxo de tokens e velocímetro no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "o número que todo mundo pergunta", direto
- **Elementos futuristas:** GPU com um fluxo de partículas de token ciano atravessando (velocidade), tacômetro holográfico com ponteiro alto
- **Arquivo alvo:** `tokens-por-segundo-30b-hardware-real.webp`

**Prompt exato:**
```
A matte black GPU card on a dark bench with a stream of #2DD4BF cyan token
particles flowing across it in motion, a holographic tachometer floating above
with the needle high, thin cyan circuit traces on the card. Environment: deep
#0B0E14 background with soft cyan bokeh. Shot on a 50mm f/2.8 lens, slightly
high angle. Lighting: one strong key light from upper-left at 45 degrees, the
cyan glow (#2DD4BF) of the stream as the only accent, thin cool rim light.
Composition: card on the right third, left third clean empty negative space,
shallow depth of field. Mood: calm, direct, premium technical product
photography, near-future engineering lab. no text, no letters, no typography,
no watermark.
```

## C8. `guia/qwen3-8-27b-benchmark-artificial-analysis` — "Qwen3.8-27B no Artificial Analysis: 52 pontos"

- **Categoria:** Benchmarks · **Acento:** ciano `#2DD4BF`
- **Luz:** key 45°; glow ciano no placar; rim light
- **Enquadramento:** GPU com placar holográfico no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "o índice independente", confiante, medido
- **Elementos futuristas:** GPU com um painel de placar holográfico (marcador alto em barras ciano, sem número escrito), medidor de escala
- **Arquivo alvo:** `qwen3-8-27b-benchmark-artificial-analysis.webp`

**Prompt exato:**
```
A matte black GPU card on a dark bench with a holographic scoreboard panel
floating above, a high marker bar in #2DD4BF cyan light on a dark gauge scale,
thin cyan circuit traces across the PCB. Environment: deep #0B0E14 background
with soft cyan bokeh. Shot on a 50mm f/2.8 lens, slightly high angle. Lighting:
one strong key light from upper-left at 45 degrees, the cyan glow (#2DD4BF) of
the scoreboard as the only accent, thin cool rim light. Composition: card on the
right third, left third clean empty negative space, shallow depth of field.
Mood: calm, measured, premium technical product photography, near-future
engineering lab. no text, no letters, no typography, no watermark.
```

---

# D. HARDWARE — acento verde `#4ADE80` (6 artigos · badge `tag-hw`)

## D1. `guia/hardware-local` — "Guia de Hardware para rodar o Qwen3.8-27B"

- **Categoria:** Hardware · **Acento:** verde `#4ADE80`
- **Luz:** key 45°; glow verde nos LEDs de status; rim light
- **Enquadramento:** rack/torre de servidor no terço direito; negativo à esquerda
- **Lente:** 35mm f/4, levemente alta
- **Mood:** "a máquina certa", sólido, confiável
- **Elementos futuristas:** rack de servidores compacto com gabinete estilo Strix Halo, VRAM empilhada, LEDs verdes de status na borda, cabos organizados
- **Arquivo alvo:** `hardware-local.webp`

**Prompt exato:**
```
A compact server rack on a dark bench with brushed aluminum panels and a
transparent side window revealing stacked DDR5 RAM sticks and a small GPU die,
glowing #4ADE80 green status LEDs along the front edge, one neat cable to a
monitor off-frame. Environment: dark studio, deep #0B0E14 background with a
soft green rim glow on the cabinet edges. Shot on a 35mm f/4 lens from a
slightly high angle. Lighting: one strong key light from upper-left, green LED
glow (#4ADE80) as the only accent, thin cool rim light separating the case.
Composition: rack on the right third, left third kept clean as empty negative
space, layered depth with a faint bokeh. Mood: calm, competent, premium hardware
photography, near-future engineering desk. no text, no letters, no typography,
no watermark.
```

## D2. `guia/qwen3-8-27b-contexto-256k-24gb` — "Qwen3.8-27B com 256K de contexto em 24 GB"

- **Categoria:** Hardware · **Acento:** verde `#4ADE80`
- **Luz:** key 45°; glow verde na torre de cache; rim light
- **Enquadramento:** torre de camadas de cache no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "cabe e roda", exato, impressionante
- **Elementos futuristas:** torre de camadas de KV cache (blocos translúcidos empilhados) com glow verde, medidor de contexto holográfico alto
- **Arquivo alvo:** `qwen3-8-27b-contexto-256k-24gb.webp`

**Prompt exato:**
```
A tall stack of translucent cache layers on a dark bench, each block glowing
with thin #4ADE80 green circuit edges, a holographic context meter floating
beside it with the marker near the top, matte dark base. Environment: deep
#0B0E14 background with soft green bokeh. Shot on a 50mm f/2.8 lens, slightly
high angle. Lighting: one strong key light from upper-left at 45 degrees, the
green glow (#4ADE80) of the stack as the only accent, thin cool rim light.
Composition: stack on the right third, left third clean empty negative space,
shallow depth of field. Mood: calm, precise, premium technical product
photography, near-future engineering lab. no text, no letters, no typography,
no watermark.
```

## D3. `guia/quantizacao-gguf-30b-quanto-cabe-na-sua-gpu` — "Quantização GGUF: quanto cabe na sua GPU?"

- **Categoria:** Hardware · **Acento:** verde `#4ADE80`
- **Luz:** key 45°; glow verde nos blocos de quant; rim light
- **Enquadramento:** blocos empilhados de quantização no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "a tabela real", didático, exato
- **Elementos futuristas:** blocos de quantização empilhados como cubos de peso (do menor IQ2 ao maior Q8) com edges verdes, um medidor de VRAM holográfico
- **Arquivo alvo:** `quantizacao-gguf-30b-quanto-cabe-na-sua-gpu.webp`

**Prompt exato:**
```
A neat stack of dark translucent cubes on a lab bench, each slightly larger than
the last, with thin #4ADE80 green light edges suggesting quantization levels,
a small holographic VRAM meter beside them, matte dark surface. Environment:
deep #0B0E14 background with soft green bokeh. Shot on a 50mm f/2.8 lens,
slightly high angle. Lighting: one strong key light from upper-left at 45
degrees, the green glow (#4ADE80) of the edges as the only accent, thin cool rim
light. Composition: stack on the right third, left third clean empty negative
space, shallow depth of field. Mood: calm, didactic, premium technical product
photography, near-future engineering lab. no text, no letters, no typography,
no watermark.
```

## D4. `guia/lemonade-sdk-v11-6-llm-local-gpu-npu-amd` — "Lemonade v11.6: LLM local com GPU+NPU (AMD)"

- **Categoria:** Hardware · **Acento:** verde `#4ADE80`
- **Luz:** key 45°; glow verde na ponte GPU↔NPU; rim light
- **Enquadramento:** placa com dois chips conectados no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "hardware AMD bem usado", inovador, competente
- **Elementos futuristas:** placa escura com dois dies (GPU e NPU) conectados por um traço verde luminoso (a ponte de orquestração), LEDs de status
- **Arquivo alvo:** `lemonade-sdk-v11-6-llm-local-gpu-npu-amd.webp`

**Prompt exato:**
```
A dark circuit board on a lab bench with two silicon dies side by side, a thin
#4ADE80 green light bridge connecting them like an orchestration path, small
status LEDs, matte black PCB. Environment: deep #0B0E14 background with soft
green bokeh. Shot on a 50mm f/2.8 lens, slightly high angle. Lighting: one
strong key light from upper-left at 45 degrees, the green glow (#4ADE80) of the
bridge as the only accent, thin cool rim light. Composition: board on the right
third, left third clean empty negative space, shallow depth of field. Mood:
calm, competent, premium technical product photography, near-future engineering
lab. no text, no letters, no typography, no watermark.
```

## D5. `guia/qwen3-8-27b-lento-causas-fixes` — "Qwen3.8-27B está lento? 6 causas e os fixes"

- **Categoria:** Hardware (badge `tag-hw` Troubleshooting) · **Acento:** verde `#4ADE80`
- **Luz:** key 45°; glow verde no medidor; rim light
- **Enquadramento:** GPU com velocímetro holográfico no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "diagnóstico que resolve", contido
- **Elementos futuristas:** GPU com um medidor de velocidade holográfico acima (ponteiro baixo), seis pontos de LED verde (as 6 causas), traces iluminados
- **Arquivo alvo:** `qwen3-8-27b-lento-causas-fixes.webp`

**Prompt exato:**
```
A matte black GPU card on a dark bench with a small holographic speedometer
gauge floating above it, the needle sitting low, and six tiny #4ADE80 green LED
indicators along the edge, glowing circuit traces across the PCB. Environment:
deep #0B0E14 background with soft green bokeh. Shot on a 50mm f/2.8 lens,
slightly high angle. Lighting: one strong key light from upper-left at 45 degrees,
the green glow (#4ADE80) of the LEDs as the only accent, thin cool rim light.
Composition: card on the right third, left third clean empty negative space,
shallow depth of field. Mood: calm, diagnostic, premium technical product
photography, near-future engineering lab. no text, no letters, no typography,
no watermark.
```

## D6. `guia/qwen38-27b-16gb-vram-llama-cpp` — "Qwen3.8-27B em 16GB de VRAM (llama.cpp)"

- **Categoria:** Hardware (badge `tag-hw` Tutorial) · **Acento:** verde `#4ADE80`
- **Luz:** key 45°; glow verde nos módulos de VRAM; rim light
- **Enquadramento:** GPU com módulos de memória no terço direito; negativo à esquerda
- **Lente:** 50mm f/2.8, levemente alta
- **Mood:** "cabe na sua placa", exato, esperançoso
- **Elementos futuristas:** GPU com módulos de VRAM visíveis (chips de memória empilhados), um deles com glow verde, medidor de ocupação holográfico
- **Arquivo alvo:** `qwen38-27b-16gb-vram-llama-cpp.webp`

**Prompt exato:**
```
A matte black GPU card on a dark bench with its VRAM memory modules visible on
the backplate, one module glowing with thin #4ADE80 green traces, a small
holographic capacity meter floating above showing memory almost full but neatly
fitted. Environment: deep #0B0E14 background with soft green bokeh. Shot on a
50mm f/2.8 lens, slightly high angle. Lighting: one strong key light from
upper-left at 45 degrees, the green glow (#4ADE80) as the only accent, thin
cool rim light. Composition: card on the right third, left third clean empty
negative space, shallow depth of field. Mood: calm, precise, premium technical
product photography, near-future engineering lab. no text, no letters, no
typography, no watermark.
```

---

# E. COMUNIDADE — acento azul `#3B82F6` (1 artigo · badge `tag-community`)

## E1. `guia/comunidade-casos-uso` — "Comunidade e Casos de Uso Reais"

- **Categoria:** Comunidade · **Acento:** azul `#3B82F6`
- **Luz:** key 45°; glow azul na malha de conexões; rim light
- **Enquadramento:** rede de nós no terço direito; negativo à esquerda
- **Lente:** 35mm f/4, levemente alta
- **Mood:** "pessoas rodando local", conectado, humano-técnico
- **Elementos futuristas:** rede de nós interconectados (pequenos módulos como máquinas domésticas) com malha de luz azul entre eles, distribuídos numa bancada
- **Arquivo alvo:** `comunidade-casos-uso.webp`

**Prompt exato:**
```
A small cluster of compact home computer modules on a dark bench, connected by a
fine mesh of #3B82F6 blue light lines forming a network, each module matte black
with a faint blue node glow, distributed across the surface. Environment: deep
#0B0E14 background with soft blue bokeh. Shot on a 35mm f/4 lens from a slightly
high angle. Lighting: one strong key light from upper-left at 45 degrees, the
blue mesh glow (#3B82F6) as the only accent, thin cool rim light. Composition:
cluster on the right third, left third clean empty negative space, shallow depth
of field. Mood: calm, connected, premium technical product photography,
near-future engineering lab. no text, no letters, no typography, no watermark.
```

---

# F. Checklist do fotógrafo (pré-entrega de cada imagem)

- [ ] Sujeito é hardware real ou conceito de dado (nunca robô/cidade clichê)?
- [ ] Fundo `#0B0E14`-família, escuro e limpo?
- [ ] Acento é o da categoria (tabela acima), ≤10–15% da área?
- [ ] Espaço negativo mapeado está livre de detalhes (zona do título)?
- [ ] Key light 45° + glow do dispositivo + rim light sutil?
- [ ] Texto NENHUM na imagem (plate limpo p/ typeset PIL)?
- [ ] Dimensão/format/peso conforme §11 do guia (16:9 1200×675 artigos · 1920×1080 home)?
- [ ] Alt text descritivo com keyword?
- [ ] Imagem "casa" com a superfície do design system?

---

# G. Índice completo (31 imagens)

| # | Slug | Categoria | Acento | Arquivo |
|---|---|---|---|---|
| A1 | `/` (home) | Home | `#9085E9→#22D3EE` | `hero-home.webp` |
| B1 | `/guia/como-rodar` | Guias | `#A78BFA` | `como-rodar.webp` |
| B2 | `/guia/como-rodar-sglang-qwen3-8-27b` | Guias | `#A78BFA` | `como-rodar-sglang.webp` |
| B3 | `/guia/como-rodar-vllm-qwen3-8-27b` | Guias | `#A78BFA` | `como-rodar-vllm.webp` |
| B4 | `/guia/quantizacao-multilingue-portugues` | Guias | `#A78BFA` | `quantizacao-multilingue-portugues.webp` |
| B5 | `/guia/melhores-modelos-locais-30b` | Guias | `#A78BFA` | `melhores-modelos-locais-30b.webp` |
| B6 | `/guia/qwen3.8-vs-qwen3-coder-30b-a3b` | Guias | `#A78BFA` | `qwen3.8-vs-qwen3-coder-30b-a3b.webp` |
| B7 | `/guia/en/why-is-qwen3-8-27b-slow` | Guias | `#A78BFA` | `why-is-qwen3-8-27b-slow.webp` |
| B8 | `/guia/qwen3-8-27b-reasoning-configuracao-ideal` | Guias | `#A78BFA` | `qwen3-8-27b-reasoning-configuracao-ideal.webp` |
| B9 | `/guia/qwen3-8-27b-visao-videos-local` | Guias | `#A78BFA` | `qwen3-8-27b-visao-videos-local.webp` |
| B10 | `/guia/minimax-music3-musica-local` | Guias | `#A78BFA` | `minimax-music3-musica-local.webp` |
| B11 | `/guia/ltx-2-5-video-local-comfyui` | Guias | `#A78BFA` | `ltx-2-5-video-local-comfyui.webp` |
| B12 | `/guia/faq` | Guias | `#A78BFA` | `faq.webp` |
| B13 | `/guia/ollama` | Guias | `#A78BFA` | `ollama.webp` |
| B14 | `/guia/en/best-local-30b-models` | Guias | `#A78BFA` | `best-local-30b-models.webp` |
| B15 | `/guia/qwen3.8-vs-ornith-1-5-35b-a3b` | Guias | `#A78BFA` | `qwen3.8-vs-ornith-1-5-35b-a3b.webp` |
| C1 | `/guia/benchmarks-comparativos` | Benchmarks | `#2DD4BF` | `benchmarks-comparativos.webp` |
| C2 | `/guia/qwen3-8-27b-uncensored-abliterated` | Benchmarks | `#2DD4BF` | `qwen3-8-27b-uncensored-abliterated.webp` |
| C3 | `/guia/1-ano-gpt-oss-modelos-locais-2026` | Benchmarks | `#2DD4BF` | `1-ano-gpt-oss-modelos-locais-2026.webp` |
| C4 | `/guia/qwen3.8-vs-qwen3.6-27b` | Benchmarks | `#2DD4BF` | `qwen3.8-vs-qwen3.6-27b.webp` |
| C5 | `/guia/muse-glimmer-30b-agente-local` | Benchmarks | `#2DD4BF` | `muse-glimmer-30b-agente-local.webp` |
| C6 | `/guia/agent-memory-leaderboard-resultados` | Benchmarks | `#2DD4BF` | `agent-memory-leaderboard-resultados.webp` |
| C7 | `/guia/tokens-por-segundo-30b-hardware-real` | Benchmarks | `#2DD4BF` | `tokens-por-segundo-30b-hardware-real.webp` |
| C8 | `/guia/qwen3-8-27b-benchmark-artificial-analysis` | Benchmarks | `#2DD4BF` | `qwen3-8-27b-benchmark-artificial-analysis.webp` |
| D1 | `/guia/hardware-local` | Hardware | `#4ADE80` | `hardware-local.webp` |
| D2 | `/guia/qwen3-8-27b-contexto-256k-24gb` | Hardware | `#4ADE80` | `qwen3-8-27b-contexto-256k-24gb.webp` |
| D3 | `/guia/quantizacao-gguf-30b-quanto-cabe-na-sua-gpu` | Hardware | `#4ADE80` | `quantizacao-gguf-30b-quanto-cabe-na-sua-gpu.webp` |
| D4 | `/guia/lemonade-sdk-v11-6-llm-local-gpu-npu-amd` | Hardware | `#4ADE80` | `lemonade-sdk-v11-6-llm-local-gpu-npu-amd.webp` |
| D5 | `/guia/qwen3-8-27b-lento-causas-fixes` | Hardware | `#4ADE80` | `qwen3-8-27b-lento-causas-fixes.webp` |
| D6 | `/guia/qwen38-27b-16gb-vram-llama-cpp` | Hardware | `#4ADE80` | `qwen38-27b-16gb-vram-llama-cpp.webp` |
| E1 | `/guia/comunidade-casos-uso` | Comunidade | `#3B82F6` | `comunidade-casos-uso.webp` |

> **Nomes de arquivo:** `artigo-slug.webp` (lowercase, hífens) · alt text sempre
> descritivo e com a keyword do artigo. Este documento é o contrato entre o
> fotógrafo (briefs) e a programadora (geração): qualquer desvio aprovado no A/B
> deve voltar pro `docs/guia-imagens.md` (seção nova) antes de virar padrão.
