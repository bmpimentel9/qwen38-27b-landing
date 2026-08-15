# Histórico de decisões

Narrativa das decisões importantes do projeto **Qwen3.8-27B landing page**,
com contexto, alternativas consideradas e rationale. Cada entrada conta *por
que* a decisão foi tomada, não apenas *o que* foi decidido.

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

## 2026-08-15 — Remover GA4 (Google Analytics 4)

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

**Decisão.** Remover o snippet GA4. Reativar apenas quando houver um ID válido
e uma decisão explícita de coletar analytics.

**Rationale.** Um tracker que não rastreia nada é só peso. Melhor não ter
analytics do que ter analytics falso. A página é estática e leve por
princípio; adicionar tracking é uma decisão consciente, não um padrão.

**Consequências.** Não há medição de tráfego até que GA4 (ou alternativa como
Plausible/Umami) seja configurado deliberadamente. O `preconnect` para
`googletagmanager.com` foi mantido no `0fc7b79` mas tornou-se órfão — ver
próxima limpeza.

---

## 2026-08-14 — Redesenha a landing sobre o Geist

**Contexto.** A página anterior funcionava, mas era uma peça de marketing:
gradiente roxo sobre preto, barras animadas com glow, emojis nos títulos das
seções e um subconjunto de 11 benchmarks. Para um lançamento de modelo de
fronteira, o registro visual que páginas de lançamento usam é documentação
técnica de produto — denso, neutro, honesto.

**Alternativas consideradas.**
1. *Manter o design roxo/glow e adicionar mais dados*. Conflito estético:
   a estética de marketing competing com a densidade de dados.
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
2. *Colocar as medições no rodapé, em letra miúda*. Meio-termio covarde.
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

---

## 2026-08-15 — Conectar o repositório à Vercel (deploy automático)

**Contexto.** Antes, o deploy era feito por upload de arquivo na Vercel. O
site e o repositório podiam (e de fato divergiram) sem que nada acusasse —
entre o redesign e a publicação, o conteúdo publicado estava desatualizado
em relação ao código versionado.

**Alternativas consideradas.**
1. *Manter upload manual*. Simples, mas silenciosamente desyncável — já
   tinha acontecido.
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
