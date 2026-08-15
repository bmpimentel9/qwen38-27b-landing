# Histórico de decisões

Narrativa das decisões importantes do projeto **Qwen3.8-27B landing page /
Portal de Modelos Locais de 30B**, com contexto, alternativas consideradas e
rationale. Cada entrada conta *por que* a decisão foi tomada, não apenas
*o que* foi decidido.

---

## 2026-08-15 — Instalar GA4 real (G-016TVX8LEE)

**Contexto.** Horas depois de o placeholder falso ser removido (ver entrada
"Remover GA4" abaixo), o Bruno decidiu medir o tráfego de verdade: o projeto
ganhou metas explícitas de visitas (ver ROADMAP) e não se gerencia o que não
se mede. O agente atlas criou a propriedade real **QWEN38-27B-LANDING**
(ID 549987691) na conta Google do projeto, e o commit `7afed08` (17:04)
instalou o Measurement ID `G-016TVX8LEE` — está live na produção.

**Alternativas consideradas.**
1. *Manter sem analytics.* Postura do ADR-004 — honesta, mas incompatível
   com metas de tráfego.
2. *Plausible/Umami (privacy-first).* Serviço/conta adicional; o projeto já
   opera o ecossistema Google (Search Console, Looker Studio).
3. *GA4 com IP anonimizado.* Gratuito, integração nativa com o resto da
   stack, `anonymize_ip` mitiga a privacidade.

**Decisão.** GA4 com ID real, tag assíncrona com `anonymize_ip: true`,
enhanced measurement do stream + eventos custom (`scroll_depth`,
`qwenTrackSearch()`).

**Rationale.** A decisão explícita que o ADR-004 exigia foi tomada pelo dono
do projeto. Com `anonymize_ip` e uma única requisição externa assíncrona, o
custo é mínimo e o valor (denominador para as metas do ROADMAP) é imediato.

**Consequências.** Tráfego mensurável desde 2026-08-15. O `preconnect` órfão
de `googletagmanager.com` deixou de ser pendência: a tag async o substituiu
(não existe mais `preconnect` no `index.html`). Registrado como ADR-007.

---

## 2026-08-15 — Fundação do projeto seo-local-models-30b

**Contexto.** Bruno pediu um projeto Hermes para o time SEO atuar sobre o
repositório `qwen38-27b-landing` (já deployado na Vercel), transformando a
landing em um portal sobre modelos locais de ~30B.

**O que foi feito.** Board kanban `seo-local-models-30b` criado; time de
perfis SEO (seo, seo-content, seo-tech, discovery, qa) entregou guia
completo (5 subpáginas), sitemap, robots.txt, FAQ, JSON-LD, performance e
a tag GA4 real. Pipeline de conteúdo diário definido: 7h pesquisa
(HuggingFace + arXiv) → card kanban → discovery valida → seo-content
escreve → revisão → deploy. Também nasceu o perfil **arquivista** para
documentação contínua e organização do repositório.

**Consequências.** O repo passa de landing única para portal em evolução —
novas seções (Modelos, Hardware, Benchmarks, Guia Rápido) e fluxo contínuo
de artigos.

---

## 2026-08-15 — Navegação responsiva (menu hambúrguer)

**Contexto.** Bruno reportou que o menu não aparecia no celular: o CSS do
portal escondia o nav em telas <900px (`display: none`) sem alternativa.

**Decisão.** Botão ☰ com dropdown flutuante; links corrigidos para cleanUrls
(`/modelos` em vez de `modelos.html`, que sofria redirect 308 por causa do
`cleanUrls: true` da Vercel). Commit `0bbb4a8`.

**Rationale.** Mobile-first: sem menu não há navegação no portal. O redirect
308 duplicava a latência de navegação em cada clique.

---

## 2026-08-15 — Remover Google Fonts e adotar font stack de sistema

**Contexto.** A página declarava `Inter` na `font-family` mas nunca carregava
a fonte de fato — caía silenciosamente para a stack do sistema. O redesign
Geist passou a carregar Inter e JetBrains Mono via Google Fonts, o que
introduziu um bloqueio de renderização: o LCP subiu para 4,8s. Para uma página
estática sem dependências de runtime, isso era contraditório.

**Alternativas consideradas.**
1. *Self-host das fontes* (WOFF2 no próprio domínio). Elimina o
   render-blocking e a dependência de terceiro, mas adiciona ~100 KB de
   assets e complexidade de build — a página é propositalmente sem build.
2. *`font-display: swap`*. Reduz o impacto do render-blocking, mas o CLS
   resultante (troca de fonte no meio do carregamento) degrada a experiência
   e a pontuação de Core Web Vitals.
3. *Font stack de sistema* (`system-ui` + `ui-monospace`). Zero requisições
   externas, zero bloqueio, aparência nativa em cada plataforma.

**Decisão.** Adotar a font stack de sistema.

**Rationale.** A página é documentação técnica de produto, não uma peça de
marketing — a densidade informacional importa mais que a tipografia de
marca. `system-ui` é o que o Geist usa por baixo dos panos quando Inter não
carrega, então o resultado visual é próximo. O ganho de performance (LCP
4,8s → < 1s esperado) compensa a perda de controle tipográfico.

**Consequências.** Aparência varia ligeiramente entre plataformas, mas sempre
dentro do espírito Geist. Removida a dependência de `fonts.googleapis.com`.

---

## 2026-08-15 — Remover o GA4 placeholder

**Contexto.** O projeto tinha um snippet GA4 com o ID `G-QWEN3827B`. Esse ID
era um placeholder — não correspondia a uma propriedade real, então não
coletava dados. Carregava o script do `googletagmanager.com` à toa, adicionando
uma requisição externa e um footprint de privacidade desnecessário.

**Alternativas consideradas.**
1. *Manter o snippet com ID placeholder*. Zero valor, custo real (requisição
   externa, cookie banner eventualmente necessário).
2. *Criar uma propriedade GA4 real e plugar o ID*. Exige conta do Google,
   configuração de propriedade, e a página passaria a coletar dados de
   visitantes — decisão que o dono do projeto deve tomar explicitamente, não
   um agente de automatização.
3. *Remover o snippet*. Zero requisições externas, zero footprint, zero
   dados — honesto enquanto não há decisão de medir tráfego.

**Decisão.** Remover o snippet GA4 placeholder (commit `d554f7c`). Reativar
apenas com ID válido e decisão explícita.

**Rationale.** Um tracker que não rastreia nada é só peso. Melhor não ter
analytics do que ter analytics falso. A página é estática e leve por
princípio; adicionar tracking é uma decisão consciente, não um padrão.

**Consequências.** A decisão explícita veio no mesmo dia: a entrada
"Instalar GA4 real (G-016TVX8LEE)" acima (e o ADR-007) documentam a
reinstalação deliberada, agora com ID válido. O `preconnect` para
`googletagmanager.com` que ficara órfão deixou de existir com a tag async.

---

## 2026-08-15 — Conectar o repositório à Vercel (deploy automático)

**Contexto.** Antes, o deploy era feito por upload de arquivo na Vercel. O
site e o repositório podiam (e de fato divergiram) sem que nada acusasse —
entre o redesign e a publicação, o conteúdo publicado estava desatualizado
em relação ao código versionado.

**Alternativas consideradas.**
1. *Manter upload manual*. Simples, mas silenciosamente divergence-prone —
   já tinha acontecido.
2. *GitHub Actions com deploy via CLI da Vercel*. Funciona, mas adiciona
   configuração e secrets.
3. *Conectar o repositório diretamente na Vercel*. `main` = produção,
   cada PR ganha preview deploy. Zero configuração extra no repo.

**Decisão.** Conectar o repositório à Vercel, `main` como branch de produção.

**Rationale.** O deploy automático elimina a classe inteira de bugs "o site
não reflete o repo". Cada PR ganha preview, o que permite validar mudanças
antes do merge. O commit que documenta a integração também serve de teste:
se o deploy automático estiver ativo, o merge publica sozinho.

**Consequências.** O `vercel.json` ganhou caching headers, security headers
e redirects. O `README.md` da raiz foi atualizado para documentar a
integração.

---

## 2026-08-14 — Redesenhar a landing sobre o Geist

**Contexto.** A página anterior funcionava, mas era uma peça de marketing:
gradiente roxo sobre preto, barras animadas com glow, emojis nos títulos das
seções e um subconjunto de 11 benchmarks. Para um lançamento de modelo de
fronteira, o registro visual que páginas de lançamento usam é documentação
técnica de produto — denso, neutro, honesto.

**Alternativas consideradas.**
1. *Manter o design roxo/glow e adicionar mais dados*. Conflito estético:
   a estética de marketing competindo com a densidade de dados.
2. *Adotar o design system Linear*. Semelhante ao Geist, mas menos documentado
   e sem referência pública canônica.
3. *Adotar o Geist* (design system open-source da Vercel). Superfícies neutras
   quase monocromáticas, hairlines de 1px, raio 8/12px, densidade de
   documentação. Referência pública, bem documentada, alinhada com o tom
   desejado.

**Decisão.** Adotar o Geist como referência de design.

**Rationale.** O Geist é o registro visual que páginas de produto da Vercel
usam — exatamente o tom de "documentação técnica de produto" que a página
precisava. Neutro o suficiente para não competir com os dados, estruturado
o suficiente para acomodar 26 benchmarks, dois temas e gráficos sem virar
circo.

**Consequências.** A página ganhou tema claro e escuro completos, navegação
fixa, e uma paleta de gráficos validada por script (cor por função, não por
decoração). Perdeu os gradientes e glows — ganho deliberado.

---

## 2026-08-14 — Incluir "Medido nesta máquina" como contraponto honesto

**Contexto.** Páginas de lançamento de modelo tendem ao entusiasmo
incondicional. O projeto tinha medições reais de throughput (decode em platô
térmico, 400 tokens/rodada, 9 rodadas) que mostravam o custo de um modelo
denso de 27B: 10,6 tok/s contra 56,6 tok/s do MoE de 35B — 5,3× mais lento.

**Alternativas consideradas.**
1. *Omitir as medições*. Página mais "vendável", mas desonesta — o leitor
   interessado em rodar localmente precisa saber o custo de velocidade.
2. *Colocar as medições no rodapé, em letra miúda*. Meio-termo covarde.
3. *Dar às medições uma seção própria, com contexto metodológico.*

**Decisão.** Seção própria, "Medido nesta máquina", com hardware, método e
contexto explícitos.

**Rationale.** Nenhuma outra página de lançamento tem isso. É o contraponto
honesto ao entusiasmo do resto da página — e é exatamente o que um
desenvolvedor decidindo entre denso e MoE precisa ver. A diferença entre
prefill e decode é explicada, não escondida.

**Consequências.** A página ganhou uma seção que nenhum competidor tem, e
uma posição de honestidade metodológica que se reflete no aviso explícito de
que scores são reportados pelo fabricante.
