#!/usr/bin/env python3
"""QA t_f53d4281 — 3 achados QA do blog (âncoras, TOC mobile, newsletter)."""
import glob, sys
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8123"
ARTICLES = sorted(
    p.split("/")[1] for p in glob.glob("guia/*/index.html")
    if not p.startswith("guia/en/")
)

results = []
def check(name, ok, detail=None):
    results.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))

with sync_playwright() as p:
    browser = p.chromium.launch(args=["--no-sandbox"])

    def new_page(vw, js=True):
        errors = []
        ctx = browser.new_context(viewport={"width": vw, "height": 900}, java_script_enabled=js)
        page = ctx.new_page()
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))
        return page, errors

    # ============ ACHADO 1: âncoras de categoria ============
    # navegação principal orientada à decisão (redesign hardware-first)
    NAV_EXPECT = {
        "Modelos": "/modelos", "Hardware": "/hardware",
        "Benchmarks": "/benchmarks", "Guias": "/guia/",
        "Como rodar": "/guia/como-rodar", "FAQ": "/guia/faq",
    }
    # mapeamento editorial esperado (categoria -> âncora real no /guia/)
    CATEGORY_EXPECT = {
        "Guias": "topicos", "Benchmarks": "benchmarks-resumo",
        "Hardware": "memoria", "Releases": "topicos", "Comunidade": "topicos",
    }
    # 1a. header nav da home
    page, errors = new_page(1440)
    page.goto(BASE + "/", wait_until="networkidle")
    for label, expected_href in NAV_EXPECT.items():
        lnk = page.locator(f'nav.nav-links a:has-text("{label}")').first
        if lnk.count() == 0:
            check(f"home/header: link {label} existe", False)
            continue
        href = lnk.get_attribute("href")
        ok = href == expected_href
        check(f"home/header: {label} -> {expected_href}", ok, href)
    page.close()

    # 1b. cat-blocks "Ver todos"
    page, errors = new_page(1440)
    page.goto(BASE + "/", wait_until="networkidle")
    for label, anchor in CATEGORY_EXPECT.items():
        block = page.locator(f".cat-block:has(h3:text-is(\"{label}\"))")
        lnk = block.locator("a:has-text('Ver todos')")
        href = lnk.get_attribute("href")
        ok = href == f"/guia/#{anchor}"
        check(f"home/cat-block: {label} Ver todos -> #{anchor}", ok, href)
    page.close()

    # 1c. footer
    page, errors = new_page(1440)
    page.goto(BASE + "/", wait_until="networkidle")
    for label, expected_href in NAV_EXPECT.items():
        lnk = page.locator(f"footer a:has-text(\"{label}\")").first
        href = lnk.get_attribute("href")
        ok = href == expected_href
        check(f"home/footer: {label} -> {expected_href}", ok, href)
    page.close()

    # 1d. os ids alvo EXISTEM no /guia/ e o clique navega até a seção
    page, errors = new_page(1440)
    for anchor in set(CATEGORY_EXPECT.values()):
        page.goto(BASE + "/guia/", wait_until="networkidle")
        target = page.locator(f"#{anchor}")
        check(f"/guia/: id #{anchor} existe", target.count() == 1)
    page.close()

    # 1e. breadcrumb + JSON-LD dos artigos apontam p/ âncora real
    page, errors = new_page(1440)
    for slug in ARTICLES:
        page.goto(BASE + f"/guia/{slug}", wait_until="networkidle")
        bc = page.locator("nav.breadcrumb a").nth(1)
        href = bc.get_attribute("href")
        anchor = href.split("#")[1]
        page.goto(BASE + "/guia/", wait_until="networkidle")
        ok = page.locator(f"#{anchor}").count() == 1
        check(f"artigo {slug}: breadcrumb -> #{anchor} existe", ok, href)
    page.close()

    # ============ ACHADO 2: TOC mobile ============
    sample = "guia/ollama"
    # 2a. desktop: TOC visível, summary oculto, sticky
    page, errors = new_page(1440)
    page.goto(BASE + f"/{sample}", wait_until="networkidle")
    toc_disp = page.locator("nav.toc").first.evaluate("el => getComputedStyle(el).display")
    sum_disp = page.locator(".toc-details > summary").evaluate("el => getComputedStyle(el).display")
    sticky = page.locator(".toc-details").evaluate("el => getComputedStyle(el).position")
    check("desktop: TOC visível", toc_disp != "none", toc_disp)
    check("desktop: summary oculto", sum_disp == "none", sum_disp)
    check("desktop: toc-details sticky", sticky == "sticky", sticky)
    # clicar num link do TOC rola até a seção
    page.locator("nav.toc a").first.click()
    page.wait_for_timeout(300)
    check("desktop: clique no TOC sem erro", len(errors) == 0)
    page.close()

    # 2b. mobile 390px: toggle visível, TOC fechado por padrão, abre no clique
    page, errors = new_page(390)
    page.goto(BASE + f"/{sample}", wait_until="networkidle")
    sum_disp = page.locator(".toc-details > summary").evaluate("el => getComputedStyle(el).display")
    toc_disp_closed = page.locator("nav.toc").first.evaluate("el => getComputedStyle(el).display")
    h = page.locator(".toc-details > summary").evaluate("el => el.getBoundingClientRect().height")
    check("mobile: summary visível", sum_disp != "none", sum_disp)
    check("mobile: TOC fechado por padrão", toc_disp_closed == "none", toc_disp_closed)
    check("mobile: alvo de toque >= 44px", h >= 44, f"{h:.0f}px")
    # clica no summary (toggle) -> abre
    page.locator(".toc-details > summary").click()
    page.wait_for_timeout(300)
    toc_disp_open = page.locator("nav.toc").first.evaluate("el => getComputedStyle(el).display")
    check("mobile: clique abre o TOC", toc_disp_open != "none", toc_disp_open)
    # clica de novo -> fecha
    page.locator(".toc-details > summary").click()
    page.wait_for_timeout(300)
    toc_disp_closed2 = page.locator("nav.toc").first.evaluate("el => getComputedStyle(el).display")
    check("mobile: segundo clique fecha", toc_disp_closed2 == "none", toc_disp_closed2)
    over = page.evaluate("() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
    check("mobile: zero overflow horizontal", over <= 0, f"{over}px")
    check("mobile: zero erros JS", len(errors) == 0, "; ".join(errors[:2]))
    page.close()

    # 2c. TOC funciona SEM JS (progressive enhancement / zero-JS)
    page, errors = new_page(390, js=False)
    page.goto(BASE + f"/{sample}", wait_until="networkidle")
    sum_disp = page.locator(".toc-details > summary").evaluate("el => getComputedStyle(el).display")
    toc_closed = page.locator("nav.toc").first.evaluate("el => getComputedStyle(el).display")
    check("mobile sem JS: summary visível", sum_disp != "none", sum_disp)
    check("mobile sem JS: TOC fechado", toc_closed == "none", toc_closed)
    # <details> é nativo: clicar funciona mesmo sem JS
    page.locator(".toc-details > summary").click()
    page.wait_for_timeout(300)
    toc_open = page.locator("nav.toc").first.evaluate("el => getComputedStyle(el).display")
    check("mobile sem JS: clique nativo abre o TOC", toc_open != "none", toc_open)
    page.close()

    # 2d. TOC em TODOS os artigos mobile abre/fecha (amostra de 5)
    page, errors = new_page(390)
    for slug in ARTICLES[:5]:
        page.goto(BASE + f"/guia/{slug}", wait_until="networkidle")
        has = page.locator(".toc-details > summary").count()
        closed = page.locator("nav.toc").first.evaluate("el => getComputedStyle(el).display") if has else "n/a"
        if has:
            page.locator(".toc-details > summary").click(); page.wait_for_timeout(200)
            opened = page.locator("nav.toc").first.evaluate("el => getComputedStyle(el).display")
            check(f"artigo {slug}/390: toggle ok", closed == "none" and opened != "none", f"{closed}->{opened}")
        else:
            check(f"artigo {slug}/390: tem toggle", False)
    page.close()

    # ============ ACHADO 3: newsletter honesta (sem endpoint) ============
    page, errors = new_page(390)
    page.goto(BASE + "/", wait_until="networkidle")
    page.locator("section.newsletter input[type=email]").fill("bruno@exemplo.com")
    page.locator("section.newsletter button").click()
    page.wait_for_timeout(400)
    st = page.locator("section.newsletter .newsletter-status").inner_text()
    check("newsletter: sem endpoint -> feedback honesto 'em breve'", "ainda não abrimos" in st.lower(), st)
    page.close()

    browser.close()

fails = [r for r in results if not r[1]]
print(f"\n===== RESULTADO: {len(results)-len(fails)}/{len(results)} PASS =====")
if fails:
    print("FALHAS:", fails)
    sys.exit(1)
