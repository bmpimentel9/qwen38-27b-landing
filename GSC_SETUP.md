# Google Search Console — Guia de Configuração

Documento técnico criado pelo SEO (perfil `seo`) para o Bruno executar os passos
manuais de verificação de propriedade e submissão de sitemap no Google Search Console.

**Domínio:** `https://qwen38-27b-landing.vercel.app`
**GA4 Measurement ID:** `G-016TVX8LEE` (propriedade 549987691)
**Sitemap:** `https://qwen38-27b-landing.vercel.app/sitemap.xml`

---

## O que já foi feito (automático, pelo agente SEO)

1. Meta tag `google-site-verification` adicionada no `<head>` de TODAS as 12 páginas HTML
   do portal. O token está como placeholder `SEU_TOKEN_DE_VERIFICACAO_AQUI` — precisa
   ser substituído pelo token real gerado pelo GSC (passo 2 abaixo).
2. Sitemap.xml atualizado de 6 para 11 URLs — agora inclui todas as páginas indexáveis:
   - Home (/)
   - /guia (hub de conteúdo)
   - /hardware, /modelos, /benchmarks, /guia-rapido (páginas do portal)
   - /guia/benchmarks-comparativos, /guia/hardware-local, /guia/como-rodar (artigos)
   - /guia/comunidade-casos-uso, /guia/faq (artigos)
3. Robots.txt já estava configurado corretamente (permite Googlebot e todos os LLM crawlers,
   aponta para sitemap.xml).

---

## Passos manuais — o que o Bruno precisa fazer

### Passo 1: Acessar o Google Search Console

1. Abrir https://search.google.com/search-console
2. Fazer login com a conta Google do Bruno (mesma do GA4)

### Passo 2: Adicionar propriedade (escolher UMA das opções)

#### OPÇÃO A (recomendada): Verificação via Google Analytics 4

Como o GA4 (G-016TVX8LEE) já está instalado e ativo no site, o GSC pode verificar
a propriedade automaticamente via vinculação com o GA4.

1. No GSC, clicar em "Adicionar propriedade"
2. Escolher "Prefixo de URL" e digitar: `https://qwen38-27b-landing.vercel.app`
3. Na tela de verificação, escolher "Google Analytics" como método
4. Se a conta Google do Bruno for a mesma do GA4, a verificação é instantânea

#### OPÇÃO B: Verificação via HTML tag (EXECUTADA em 17/08)

✅ **Token real injetado em 17/17 páginas** via `scripts/inject_gsc_token.py` (token `tfpagcf…`).
Gate anti-regressão `scripts/check_head.py` bloqueia merge se faltar.

**Único passo manual pendente (30s):** no GSC → Configurações → Verificação do Google →
Tag HTML → clicar **Verificar**. Confirma o 2º método na hora; sem o clique,
o Google re-verifica sozinho no re-crawl periódico (não é blocker).

### Passo 3: Submeter o sitemap

1. No GSC, ir em "Sitemaps" (menu lateral esquerdo)
2. Digitar: `sitemap.xml` (o GSC já sabe o domínio)
3. Clicar em "Enviar"
4. Aguardar status "Êxito" (pode levar alguns minutos)

### Passo 4: Solicitar indexação (URL Inspection)

Para cada uma das 6 URLs prioritárias abaixo:

1. No GSC, ir em "Inspeção de URL" (barra de pesquisa no topo)
2. Colar a URL completa (ex: `https://qwen38-27b-landing.vercel.app/`)
3. Clicar em "Solicitar indexação"
4. Repetir para as 6 URLs:

**URLs prioritárias para indexação:**

| # | URL | Prioridade | Motivo |
|---|-----|------------|--------|
| 1 | `https://qwen38-27b-landing.vercel.app/` | Alta | Home — keyword alvo: "modelos locais 30B" |
| 2 | `https://qwen38-27b-landing.vercel.app/guia/benchmarks-comparativos` | Alta | Keyword: "qwen3.8 27b benchmark" |
| 3 | `https://qwen38-27b-landing.vercel.app/guia/hardware-local` | Alta | Keyword: "hardware para llm local" |
| 4 | `https://qwen38-27b-landing.vercel.app/guia/como-rodar` | Alta | Keyword: "como rodar qwen3.8 27b local" |
| 5 | `https://qwen38-27b-landing.vercel.app/guia/comunidade-casos-uso` | Média | Keyword: "qwen3.8 casos de uso" |
| 6 | `https://qwen38-27b-landing.vercel.app/guia/faq` | Média | Long-tail FAQ queries |

### Passo 5: Vincular GA4 ao GSC (opcional, mas recomendado)

1. No GSC, ir em "Configurações" → "Propriedade associada do GA4"
2. Selecionar a propriedade GA4 (QWEN38-27B-LANDING, G-016TVX8LEE)
3. Isso habilita dados combinados de aquisição (Search) + comportamento (Analytics)

---

## Como monitorar depois (para o relatório semanal do atlas)

### O que verificar no GSC (semanalmente):

1. **Desempenho > Resultados da pesquisa:**
   - Consultas (queries) que trazem tráfego
   - Posições médias por query
   - Impressões e CTR
   - Páginas mais impressas

2. **Cobertura > Páginas:**
   - Páginas indexadas vs não indexadas
   - Erros de indexação
   - Exclusões (verificar se não há páginas importantes excluídas)

3. **Sitemaps:**
   - Status do sitemap (deve estar "Êxito")
   - URLs descobertas vs indexadas

4. **Inspeção de URL:**
   - Verificar se páginas específicas estão indexadas
   - Ver a última rastreada pelo Googlebot
   - Solicitar re-indexação após atualizações de conteúdo

### Keywords-alvo para monitorar (meta 30 dias: top 10):

| Keyword | Volume estimado | Dificuldade | Página-alvo |
|---------|-----------------|-------------|-------------|
| modelos locais 30B | Baixo-médio | Baixa | Home (/) |
| qwen3.8 27b benchmark | Médio | Média | /guia/benchmarks-comparativos |
| hardware para llm local | Médio | Baixa-média | /guia/hardware-local |
| como rodar qwen3.8 27b local | Baixo | Baixa | /guia/como-rodar |
| qwen3.8 casos de uso | Baixo | Baixa | /guia/comunidade-casos-uso |
| faq qwen3.8 27b | Baixo | Baixa | /guia/faq |

### Métricas de referência (baseline dia 0 = 2026-08-15):

- Impressões: 0 (site novo, sem dados GSC ainda)
- Cliques: 0
- Posição média: N/A
- Páginas indexadas: 0 (antes da submissão)

### Anotação para o relatório semanal do atlas:

```
## GSC — Status semanal

- Propriedade: https://qwen38-27b-landing.vercel.app
- Verificada em: [DATA]
- Sitemap submetido em: [DATA]
- Sitemap status: [Êxito/Pendente]
- URLs no sitemap: 11
- URLs indexadas: [N]
- URLs solicitadas para indexação: 6
- Impressões (7d): [N]
- Cliques (7d): [N]
- CTR médio: [N]%
- Posição média: [N]

### Top queries (7d):
1. [query] — [N] impressões, pos [N]
2. [query] — [N] impressões, pos [N]
3. [query] — [N] impressões, pos [N]

### Próximas ações:
- [ ] Re-solicitar indexação de páginas não indexadas após 7 dias
- [ ] Verificar erros de cobertura
- [ ] Monitorar queries com impressões mas baixa CTR (oportunidade de otimização de title/description)
```

---

## Observações técnicas

- O domínio `vercel.app` é um subdomínio gerenciado pela Vercel. Verificação via DNS TXT
  não é possível para subdomínios Vercel (não temos acesso ao DNS zone).
- A verificação via HTML tag é o método mais confiável para este caso.
- A verificação via GA4 é a mais rápida (instantânea) se a conta Google for a mesma.
- O GSC pode levar de 1 a 3 dias para processar o sitemap e começar a rastrear.
- A solicitação de indexação manual (URL Inspection) acelera o processo, mas não
  garante indexação — o Google decide com base na qualidade do conteúdo.
- O Googlebot respeita o robots.txt, que já permite todos os crawlers.
- O sitemap.xml e robots.txt têm cache de 24h na Vercel (configurado no vercel.json).
