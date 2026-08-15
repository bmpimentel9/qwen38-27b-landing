# Qwen3.8-27B — landing page

Página informativa (não oficial) sobre o lançamento dos pesos abertos do
**Qwen3.8-27B** em 14/08/2026: especificações, os 26 benchmarks do model card,
requisitos de hardware, throughput medido em máquina real e a recepção da
comunidade.

🔗 https://qwen38-27b-landing.vercel.app

## Arquitetura

- `index.html` — página estática única, sem build e sem dependências de runtime
  (a única requisição externa é a fonte Inter/JetBrains Mono no Google Fonts).
- `vercel.json` — deploy estático na Vercel.

## Deploy

O projeto na Vercel está conectado a este repositório, com `main` como branch de
produção: todo push na `main` publica sozinho, e cada PR ganha um deploy de
pré-visualização. Antes disso o deploy era feito por upload de arquivo, o que
deixava o site e o repositório divergirem em silêncio.

## Design

O layout é modelado no **Geist**, o design system open-source da Vercel:
superfícies neutras quase monocromáticas, hairlines de 1px, tipografia Inter com
JetBrains Mono para números e código, raio de 8/12px e densidade de documentação
técnica. Tema claro e escuro com alternância manual (a preferência fica no
`localStorage`; o padrão segue o sistema).

As cores de série dos gráficos foram escolhidas por função — violeta para o
Qwen3.8, laranja para modelos de fronteira, cinza recessivo para a geração
anterior — e **validadas para daltonismo e contraste** nos dois temas (ΔE CVD
adjacente ≥ 8 e contraste ≥ 3:1 contra a superfície do card).

Acessibilidade: marcos semânticos, link de pular para o conteúdo, foco visível,
tabela como equivalente textual de todos os gráficos, respeito a
`prefers-reduced-motion` e rótulos diretos em todas as barras (nenhum valor
existe só no tooltip).

## Dados

Benchmarks e especificações vêm do [model card oficial](https://huggingface.co/Qwen/Qwen3.8-27B)
e são reportados pela própria Qwen — a página diz isso explicitamente. As
referências de modelos de fronteira vêm de model cards e anúncios de terceiros,
sem harness compartilhado.

As medições de throughput ("Medido nesta máquina") são próprias: decode em platô
térmico, 400 tokens por rodada, 9 rodadas, em um ASUS ROG Flow Z13 (Strix Halo,
Radeon 8060S, 128 GB unificados) com Ollama sobre Vulkan.

Fontes completas no rodapé da página.
