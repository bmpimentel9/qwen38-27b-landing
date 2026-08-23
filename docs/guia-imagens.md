# Guia de Estilo Visual Futurista — Imagens do Portal Modelos Locais ≤30B

> **Autoridade:** `docs/design/DESIGN-SYSTEM.md` (tokens) · `docs/DECISIONS.md` (ADR-002 Geist, ADR-003 font stack) · skill `pipe-criativos` (regras de espaço)
> **Consumidor principal:** perfil `fotografo` (gera briefs por artigo + home)
> **Task:** t_58e117a0 · diretordearte · 23/08/2026
> **Escopo:** todas as imagens do projeto — thumbnails de artigos (16:9), hero da home, cards de categoria, OG/social (1200×630)

---

## 1. Conceito único do estilo (o que torna as imagens "deste site")

**"Laboratório escuro de IA" (Dark AI Lab).** Uma imagem que só poderia pertencer a
um portal sério sobre modelos locais de 30B: hardware real em ambiente escuro de
estúdio, circuitos e grafos de rede neural como protagonistas visuais, luz precisa
e contida, acabamento técnico-premium. Nada de neon ciberpunk genérico, nada de
cidade do futuro clichê, nada de robôs sorrindo.

Três palavras-chave que TODA imagem do projeto deve honrar:
1. **Precisão** — cada elemento tem função; zero decoração aleatória.
2. **Hardware real** — o sujeito é a máquina que roda o modelo local (GPU, die,
   board, rack, chips), não um conceito abstrato solto no vácuo.
3. **Escuridão controlada** — fundo escuro profundo com UM ponto de luz âncora.

Isso conversa com o design system: a página já é dark-first, densa, quase
monocromática (Geist). As imagens estendem essa linguagem — a thumbnail no card
deve parecer nascida da mesma superfície `#151B27`, não uma foto importada.

---

## 2. Mood (o tom emocional)

| Eixo | Direção | Evitar |
|---|---|---|
| Sensação | Calmo, competente, "engenharia de verdade" | Caótico, infantil, over-the-top |
| Tempo | Futuro próximo (ano 2028, não 2300) | Ficção científica distante |
| Energia | Fria e focada, com UM toque de "vivo" (o glow) | Agitação, explosões, movimento excessivo |
| Audiência | Entusiasta técnico que roda LLM local | Leigo que só quer "algo bonito" |

O leitor do portal quer confiar no dado. A imagem passa a mensagem: *"isto é real,
isto funciona, isto está ao alcance da sua máquina."* O futurismo é **credível**,
não **maravilhoso**.

---

## 3. Paleta de cores

Derivada 1:1 dos tokens do design system (não inventar cor nova — a imagem deve
"casar" com a página).

### 3.1 Base (superfícies)

| Cor | Hex | Papel na imagem |
|---|---|---|
| Fundo profundo | `#0B0E14` | Fundo principal (mesmo `--bg` da página) |
| Superfície | `#151B27` | Placas, gabinetes, superfícies reflexivas |
| Superfície alta | `#1C2433` | Detalhes em relevo, heat sinks, layers |
| Hairline/borda | `#2A3446` | Linhas finas, divisões, arestas iluminadas |
| Cinza médio | `#8C96AB` | Metais, cabos, suportes (mesmo `--muted`) |

### 3.2 Acentos (função, nunca decoração)

Cada categoria do portal tem SUA cor de acento (mesmo mapeamento dos badges):

| Categoria | Acento | Hex | Uso na imagem |
|---|---|---|---|
| Guias | Violeta | `#A78BFA` | Glow principal, grafos, elementos de "neurônio" |
| Benchmarks | Ciano | `#2DD4BF` | Barras/grafos de desempenho, linhas de dados |
| Hardware | Verde | `#4ADE80` | LEDs de status, circuitos, "vida" da máquina |
| Releases | Âmbar | `#F5B841` | Foco de destaque, partículas de lançamento |
| Comunidade | Azul | `#3B82F6` | Conexões, rede, nós distribuídos |

**Regra de saturação:** acento cobre **no máximo 10-15% da área** da imagem e
aparece sempre **sobre** superfície escura — nunca como fundo cheio. Se a imagem
tem 2 acentos, um é dominante (70/30). O resto da imagem é quase monocromática
(base + cinzas).

**Gradiente de marca (para OG/hero):** o degradê oficial é violeta→ciano
`#9085E9 → #22D3EE` (já usado no `og-image.svg`) — reservado para bordas finas,
linhas de energia ou um único feixe de luz. Nunca cobrir a imagem inteira.

---

## 4. Iluminação

A iluminação é o que mais define o estilo. Protocolo fixo:

1. **Luz principal:** um único key light direcional (frasco de estúdio, softbox ou
   feixe de "projetor"), vindo de cima-lateral (45°). Cria sombras definidas mas
   suaves — *rembrandt técnico*, não holofote duro.
2. **Glow de acento:** uma segunda fonte de luz **colorida e fraca**, emitida pelo
   próprio hardware (LED, tela, trace energizado) — é o "coração vivo" da máquina.
   Sempre o acento da categoria.
3. **Rim light (luz de contorno):** filete de luz fria na borda do objeto para
   separá-lo do fundo escuro (sutil, 1-2px de brilho na aresta).
4. **Sem luz plana, sem luz global difusa.** Contraste é a regra: escuro domina,
   luz pontual foca.

**Fórmula mental:** *"produto de hardware fotografado em estúdio escuro, com a
fonte de luz principal acima à esquerda e um brilho colorido do próprio
dispositivo como único acento."*

---

## 5. Enquadramento e lente

| Contexto | Enquadramento | Lente simulada |
|---|---|---|
| Thumbnail de artigo (16:9) | Sujeito à direita (terço direito), **espaço negativo à esquerda** para título | 35mm–50mm, f/2.8–4, profundidade média |
| Hero da home (larga 21:9/16:9) | Hardware em destaque no terço central-inferior, respiro generoso acima | 24–35mm, ambiente + detalhe |
| Card de categoria / OG 1200×630 | Composição equilibrada, sujeito central com margem ≥ 8% | 50mm, f/2.8 |
| Detalhe técnico (macro, GPU) | Close no die/heat sink/traces, textura visível | 100mm macro, f/8 (nitidez total) |

**Regras de enquadramento:**
- **Regra dos terços em ação:** sujeito principal sempre numa interseção ou
  ocupando um terço; nunca morto no centro (exceto OG institucional).
- **Espaço negativo para texto:** nas thumbnails, o terço esquerdo (ou superior,
  se o card for retrato) fica **livre de detalhes** — é onde o título/lead vai
  viver (ver §8). Peça isso explicitamente no prompt.
- **Profundidade em camadas:** foreground desfocado (bokeh de luz), sujeito nítido,
  fundo escuro com profundidade — nunca parede chapada.
- **Ângulo:** ligeiramente acima do objeto (5-15° de câmera alta) para
  "perspectiva de engenheiro observando a bancada". Nunca nadir/contra-plongée.

---

## 6. Composição

- **Grid implícito:** os elementos da imagem seguem eixos verticais/horizontais
  limpos — o hardware tem ângulos retos; respeite-os. Nada torto, nada "artístico".
- **Um protagonista:** uma única peça de hardware (ou um único conceito de dado)
  é o sujeito. Todo o resto apoia.
- **Linhas de energia:** use os traces/cabos/arestas como linhas de guia que
  levam o olho ao protagonista (composição diagonal suave).
- **Simetria permitida, assimetria preferida:** assimetria com peso no terço
  direito para thumbnails (deixa o título respirar à esquerda).
- **Bokeh de luz:** 2-3 pontos de luz desfocados ao fundo, na cor do acento —
  profundidade sem poluição.

---

## 7. Tipografia (se houver texto)

**Regra-mãe do pipe-criativos: o modelo de imagem NÃO escreve texto.**

- **Plate sem texto:** o prompt SEMPRE pede `no text, no letters, no typography,
  no watermark`. O modelo gera só a imagem.
- **Typeset determinístico (PIL):** qualquer título/lead/CTA é escrito em código
  depois, com as fontes do sistema do projeto:
  - Headline: `Anton` (condensed bold) — ou, se não couber, `system-ui` black 800.
  - Apoio/números: `ui-monospace` (números de benchmark SEMPRE mono — ADR-003).
  - Cor do texto: branco `#E8EDF6` sobre scrim escuro; acento da categoria para o
    número/CTA.
- **Zona limpa:** o terço de espaço negativo mapeado no prompt (§5) é onde o
  typeset entra. **Nenhuma letra sobre hardware denso.**
- Contraste: scrim vertical + halo escuro atrás do texto (protocolo validado da
  skill `arte-fal-modelos`).

Exceção única: OG/social de marca (ex.: o `og-image.svg` existente) pode usar o
template tipográfico do site via SVG/código — nunca pedir texto ao modelo.

---

## 8. Vocabulário visual por categoria (elementos futuristas)

O "futurismo" vem destes elementos, usados em **composições** realistas (não em
ilustração solta):

| Categoria | Elementos-sujeito | Acento |
|---|---|---|
| Guias | GPU die em macro, heat sink, camadas de silício, placa-mãe com traces iluminados | Violeta |
| Benchmarks | Grafos 3D de barras/linhas em acrílico escuro, tokens de texto fluindo, medidores | Ciano |
| Hardware | Rack de servidores compacto, gabinete Strix Halo-like, VRAM empilhada, cabos organizados | Verde |
| Releases | Caixa de modelo "abrindo", peso abrindo com glow, partículas de energia | Âmbar |
| Comunidade | Nós de rede interconectados, cluster de máquinas em casa, malha de conexões | Azul |

Metáfora futurista recorrente e barata de executar: **o hardware é o herói** —
uma GPU/die/board fotografada como peça de joalheria em estúdio escuro. Funciona
para qualquer artigo, comunica "local + potência + real".

---

## 9. Template de prompt reutilizável (para modelos locais)

Regras de prompt dos modelos locais (FLUX e derivados — validado na skill `imagem`):
- **Em inglês**, prosa natural e fluida (o encoder é um LLM), 40–90 palavras.
- Ordem de prioridade: sujeito → ação → estilo → contexto/fundo → iluminação → técnica.
- Descreva o que QUER (sem "no blur", "sem texto" vira "no text, no letters, no typography").
- Ancore as cores de marca em hex DENTRO de objetos (ex.: "a GPU is #151B27 with #2DD4BF traces").
- Cite câmera/lente para realismo.

### Template (copiar e preencher os slots)

```
[SUJEITO] — [1 peça de hardware ou conceito de dado], [material/textura ex.: brushed
aluminum, matte black PCB], with [ELEMENTO FUTURISTA: glowing #HEX circuit traces /
a holographic data graph / stacked silicon layers].

Environment: [superfície escura da bancada / dark studio], background in deep
#0B0E14 with soft bokeh of [cor] lights. Single [lente ex.: 50mm f/2.8] shot,
slightly high angle.

Lighting: one strong key light from upper-left at 45°, a subtle [COR] glow
(#HEX) emitted from the device as the only accent, thin cool rim light on the edges.

Composition: subject on the [right/center] third, [left/top] third kept as clean
empty negative space, shallow depth of field, layered foreground bokeh.

Mood: precise, calm, premium technical product photography, near-future
engineering lab. no text, no letters, no typography, no watermark.
```

**Slots obrigatórios sempre preenchidos:** sujeito · material · elemento
futurista (com hex) · fundo · lente · luz (key + glow) · composição (com o espaço
negativo mapeado) · mood.

---

## 10. Três exemplos de prompts prontos

### Exemplo A — Artigo de Benchmarks (categoria Benchmarks, ciano)
```
A matte black GPU accelerator card standing upright on a dark lab bench, its
copper heat sink visible, with thin glowing #2DD4BF circuit traces branching
across the PCB like a neural network. In front of the card, a small dark glass
hologram floats showing a rising bar chart made of light. Environment: deep
#0B0E14 background with soft cyan bokeh lights far behind. Shot on a 50mm f/2.8
lens, slightly high angle. Lighting: strong key light from upper-left at 45
degrees, cyan glow (#2DD4BF) emitted from the traces as the only accent, thin
cool rim light on the edges. Composition: subject on the right third, left third
kept as clean empty negative space, shallow depth of field. Mood: precise, calm,
premium technical product photography, near-future engineering lab. no text, no
letters, no typography, no watermark.
```

### Exemplo B — Artigo de Hardware local (categoria Hardware, verde)
```
A compact mini PC tower with brushed aluminum panels and a transparent side
window revealing stacked DDR5 RAM sticks and a small GPU die, glowing green
#4ADE80 status LEDs along the front edge. A single neat cable runs to a monitor
off-frame. Environment: dark studio, deep #0B0E14 background with a soft green
rim glow on the cabinet edges. Shot on a 35mm f/4 lens from a slightly high
angle. Lighting: one strong key light from upper-left, green LED glow (#4ADE80)
as the only accent, thin cool rim light separating the case from the dark
background. Composition: tower on the right third, upper-left and left thirds
kept clean as empty negative space, layered depth with a faint bokeh. Mood:
calm, competent, premium hardware photography, near-future engineering desk. no
text, no letters, no typography, no watermark.
```

### Exemplo C — Hero da home (visual amplo, acento violeta→ciano)
```
A wide hero scene: a dark futuristic desk in a near-future engineering room,
dominated by an open workstation with a sleek black GPU installed, illuminated by
a single beam of violet-to-cyan light (#9085E9 to #22D3EE) tracing across the
surface like energy. Floating above the desk, subtle glowing data particles and
thin neural-network lines in violet. Environment: deep #0B0E14 with a large clean
dark negative space across the upper-left half. Shot on a 24mm f/2.8 lens, slight
high angle. Lighting: key light from upper-left, the violet-cyan gradient beam as
the hero accent, cool rim light on hardware edges. Composition: hardware cluster
in the lower-right third, generous empty negative space upper-left for the
headline, soft layered bokeh. Mood: precise, aspirational, calm premium tech,
near-future lab. no text, no letters, no typography, no watermark.
```

---

## 11. Especificações técnicas (formato e peso)

| Uso | Dimensão | Formato | Peso alvo |
|---|---|---|---|
| Thumbnail de artigo (feed) | 16:9, base 1200×675 | WebP (ou JPG q80) | ≤ 120 KB |
| Hero da home | 1920×1080 (crop 21:9 com reserva) | WebP | ≤ 200 KB |
| OG/Twitter (social) | 1200×630 | PNG/WebP | ≤ 150 KB |
| Card de categoria | 16:9, base 1200×675 | WebP | ≤ 120 KB |

- `loading="lazy"` no feed; hero e featured `eager` (design system §6).
- **Alt text sempre descritivo** e com keyword natural, ex.: "Placa de GPU com
  circuitos ciano em estúdio escuro — rodando Qwen3.8-27B localmente".
- Nomes de arquivo: `artigo-slug.webp` (lowercase, hífens) — SEO-friendly.

---

## 12. Regras invioláveis (QA de espaço — herdadas do pipe-criativos)

1. **Nenhum texto ultrapassa borda** — margem mínima = 4% do lado menor.
2. **Nenhuma letra em cima de rosto** — e aqui: **nenhuma letra em cima de
   hardware denso**; texto só no espaço negativo mapeado.
3. **Safe zones respeitadas** — thumbnail 16:9: texto na faixa central, nunca
   colado nas bordas; OG 1200×630: margem ≥ 48px.
4. **Contraste garantido** — headline nunca soma no fundo claro; scrim/halo
   resolve.
5. **Copy verbatim** — se houver typeset, texto idêntico ao aprovado.
6. **Um acento dominante** — nunca 3 cores de categoria na mesma imagem.

---

## 13. Checklist do fotógrafo (pré-entrega de cada imagem)

- [ ] Sujeito é hardware real ou conceito de dado (nunca robô/cidade clichê)?
- [ ] Fundo `#0B0E14`-família, escuro e limpo?
- [ ] Acento é o da categoria, ≤ 10-15% da área?
- [ ] Espaço negativo mapeado está livre de detalhes (zona do título)?
- [ ] Key light 45° + glow do dispositivo + rim light sutil?
- [ ] Texto NENHUM na imagem (plate limpo p/ typeset)?
- [ ] Dimensão/format/peso conforme §11?
- [ ] Alt text descritivo com keyword?
- [ ] Imagem "casa" com a superfície do design system (não parece foto importada)?

---

## 14. Referências visuais (mood de busca)

- Fotografia de produto de hardware em estúdio escuro (Apple product photography,
  NVIDIA press shots de GPUs).
- Macro photography de microchips e circuitos (fotografia de die shots).
- Estética "engineering desk / battle station" limpa, sem RGB festivo.
- Visualizações de redes neurais com cores de marca contidas.

> Este guia é vivo: qualquer desvio aprovado (uma imagem que performou bem no
> A/B, um novo modelo local mais capaz) volta pra cá como nova seção. Registro no
> `DIARIO-VISUAL.md` quando isso acontecer.
