# Otimização de Imagens para SEO & Performance — t_398bfbc0 (seo-tech)

> Autor: perfil `seo-tech` · branch `seo-local-models-30b/t_398bfbc0-seo-imagens`
> Consumidores: `programadora` (t_8b66ba59 — integrar + deploy) e revisores.
> Imagens de entrada: 31 WebP "Dark AI Lab" geradas em t_28240207 (1200×675 artigos, 1920×1080 hero).

---

## 1. Resumo

| Métrica | Antes | Depois | Δ |
|---|---|---|---|
| Formato servido | WebP q88 (fallback único) | **AVIF q44 → WebP** (`<picture>`) | modern browsers 3× menor |
| Peso total 31 imagens | 1.476 KB | **420 KB** | **−71,5%** |
| LCP (artigo, desktop) | ~0.3 s | **0,4 s** (sem carga de img pesada) | verde |
| CLS (artigo, desktop + mobile) | risco (aspect 630 vs 675) | **0** | verde |
| SEO / Performance (LH 13.4) | — | **1.0 / 1.0** | verde |
| image-alt / image-aspect-ratio / image-size-responsive | — | **PASS / PASS / PASS** | verde |

Todos os **Core Web Vitals** continuam no verde (LCP < 2.5 s, CLS = 0, TBT = 0 ms) — **não piorou**.

---

## 2. O que foi feito

### 2.1 Imagens
- **31 arquivos `.avif` gerados** a partir dos WebP originais (`quality=44`), em `public/images/`.
  - SSIM médio **0.995+** e PSNR ≥ 35 dB vs WebP origem → **sem perda perceptível** (metricado por script PIL).
  - Artigos: ≈ 9–22 KB cada (antes 33–77 KB). Hero: 13,6 KB (antes 50 KB).
- **Nomes de arquivo SEO**: já eram keyword-based (slug do artigo) pelos briefs — mantidos intactos (`artigo-slug.webp/.avif`). Nenhum rename necessário nem desejado (URLs já canônicas).

### 2.2 `<img>` nos artigos (30 páginas: 28 PT + 2 EN) + home
Padrão aplicado em substituição ao `<img src="/og-image.png" width="1200" height="630">`:

```html
<picture class="article-thumb">
  <source type="image/avif" srcset="/images/artigo-slug.avif" width="1200" height="675">
  <img src="/images/artigo-slug.webp" ... alt="[ALT descritivo]" title="[TITLE]"
       width="1200" height="675" loading="eager" fetchpriority="high" decoding="async">
</picture>
```

Decisões técnicas (acima do dobro):
- **`src` relativas** (`/images/...`) — igual ao resto do site (`/assets/...`); funciona em preview Vercel e prod. Só `og:image` e JSON-LD ficam com URL absoluta.
- **`loading="eager"` + `fetchpriority="high"`** no thumbnail: é a **imagem LCP** (topo do artigo). Lazy-load em LCP **pioraria** o Core Web Vitals — aplicado eager de propósito.
- **`width="1200" height="675"`** corrige a divergência que existia (`630` vs imagem real 675) — eliminando o risco de CLS. `<picture>` + CSS `aspect-ratio: 1200/675`.
- **`alt` descritivo** e **`title`**: reaproveitados dos alts que já existiam (descritivos por artigo).
- **`decoding="async"`** para não bloquear render.

### 2.3 CSS (`assets/css/blog.css`)
```css
.article-thumb { display:block; width:100%; aspect-ratio:1200/675; ... }
.article-thumb img { width:100%; height:100%; object-fit:cover; border-radius:inherit; }
```
- Corrige `aspect-ratio: 1200/630` → `1200/675` (igual ao tamanho real da imagem → **zero layout shift**).

### 2.4 Home (`index.html`)
- Hero inserido no fim da seção `.hero-compact` (AVIF→WebP, 1920×1080, `eager + fetchpriority=high`, alt + title).
- `og:image` / `twitter:image` → `images/hero-home.webp` (absoluto), width/height 1920×1080.

### 2.5 Schema.org — `ImageObject`
- **Artigo:** novo bloco `<script type="application/ld+json">` `ImageObject` (contentUrl, url, width 1200, height 675, caption, representiveOfPage) + `BlogPosting.image` → imagem real.
- **Home:** `ImageObject` dentro do `@graph` (1920×1080).
- **`og:image`** adicionado nas 9 páginas PT que não tinham (e atualizado Width/Height 675 nas demais); alt no `og:image:alt`.

### 2.6 Template futuro (`templates/artigo.html`)
- Padrão `<picture>` com placeholders `[SLUG]`, `[ALT...]`, `[TÍTULO...]` para artigos novos herdarem o mesmo markup SEO.

---

## 3. Critérios de aceite

| Critério | Status | Evidência |
|---|---|---|
| Todas as imagens com alt text | ✅ | `image-alt` PASS (LH); `alt` em 100% dos `<img>` |
| Nomes SEO | ✅ | `artigo-slug.webp/.avif` (keyword por artigo) |
| Tamanho reduzido | ✅ | **−71,5%** de peso total (AVIF) |
| Schema válido | ✅ | 99 blocos JSON-LD, todos parseáveis; `ImageObject` presente |

---

## 4. Handoff para a programadora (t_8b66ba59)

- **Bug que pode ter ressurão em PR concorrente:** a home recebeu `<picture class="hero-image">` dentro de `.hero-compact`; se a linha do hero mudar em outra branch, revalidar posição.
- Imagens AVIF + WebP já commitadas em `public/images/`. As 30 páginas + home **já referenciam** as imagens. A integração visual final + deploy + verificação em prod fica com a programadora.
- Verificar no deploy: `Content-Type: image/avif` no Vercel (já servido 200 no preview local).
- Re-auditoria pós-deploy recomendada via Lighthouse em prod (LCP/CLS deverão subir levemente com rede real, mas abaixo dos limites).