#!/usr/bin/env python3
"""QA da monetização (t_8dd9a051) com Playwright — 5 passagens, cobertura total."""
import glob, json, sys
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8123"
HARDWARE = {"hardware-local", "quantizacao-gguf-30b-quanto-cabe-na-sua-gpu",
            "tokens-por-segundo-30b-hardware-real", "lemonade-sdk-v11-6-llm-local-gpu-npu-amd",
            "qwen38-27b-16gb-vram-llama-cpp", "qwen3-8-27b-contexto-256k-24gb"}
ARTICLES = sorted(
    p.split("/")[1] for p in glob.glob("guia/*/index.html")
    if not p.startswith("guia/en/")
)

results = []
def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))

with sync_playwright() as p:
    browser = p.chromium.launch(args=["--no-sandbox"])

    def new_page(vw):
        errors = []
        page = browser.new_page(viewport={"width": vw, "height": 900})
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))
        return page, errors

    # ---------- PASSAGEM 1 + 2: home (roda + faz o que foi pedido) ----------
    for vw, label in [(1440, "desktop"), (390, "mobile")]:
        page, errors = new_page(vw)
        page.goto(BASE + "/", wait_until="networkidle")
        check(f"home/{label}: seção newsletter presente", page.locator("section.newsletter").count() == 1)
        check(f"home/{label}: form newsletter no footer", page.locator("footer .newsletter-form").count() == 1)
        check(f"home/{label}: link privacidade >= 2", page.locator('a[href="/privacidade"]').count() >= 2)
        disc = page.locator("footer").inner_text()
        check(f"home/{label}: disclosure affiliate no footer", "comissão que mantém o blog gratuito" in disc)
        ad_vis = page.locator(".ad-slot").first.evaluate("el => getComputedStyle(el).display")
        check(f"home/{label}: ad-slot display:none", ad_vis == "none", ad_vis)
        css_ok = page.evaluate("() => [...document.styleSheets].map(x=>x.href||'').join(' ').includes('blog-monetizacao.css')")
        check(f"home/{label}: blog-monetizacao.css carregado", css_ok)
        if vw == 390:
            over = page.evaluate("() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
            check(f"home/{label}: zero overflow horizontal", over <= 0, f"{over}px")
        check(f"home/{label}: zero erros JS", len(errors) == 0, "; ".join(errors[:2]))
        page.close()

    # ---------- Newsletter JS: caminhos de erro (passagem 3) ----------
    page, errors = new_page(1440)
    page.goto(BASE + "/", wait_until="networkidle")
    page.locator("section.newsletter input[type=email]").fill("email-errado")
    page.locator("section.newsletter button").click()
    page.wait_for_timeout(300)
    st = page.locator("section.newsletter .newsletter-status").inner_text()
    check("nl: email inválido -> erro inline", "válido" in st, st)

    page.locator("section.newsletter input[type=email]").fill("bruno@exemplo.com")
    page.locator("section.newsletter button").click()
    page.wait_for_timeout(300)
    st = page.locator("section.newsletter .newsletter-status").inner_text()
    check("nl: sem endpoint -> info 'em breve'", "ainda não abrimos" in st.lower(), st)

    # endpoint mockado: sucesso / 500 / rede fora
    page2 = browser.new_page(viewport={"width": 1440, "height": 900})
    page2.add_init_script("window.NEWSLETTER_CONFIG = { endpoint: 'https://mock.api/subscribers' };")
    page2.goto(BASE + "/", wait_until="networkidle")
    page2.route("https://mock.api/subscribers", lambda r: r.fulfill(status=200, content_type="application/json", body="{}"))
    page2.locator("section.newsletter input[type=email]").fill("bruno@exemplo.com")
    page2.locator("section.newsletter button").click()
    page2.wait_for_timeout(600)
    st = page2.locator("section.newsletter .newsletter-status").inner_text()
    check("nl: endpoint OK -> sucesso inline (sem redirect)", "confirmada" in st.lower(), st)
    check("nl: URL não mudou (sem redirect)", "localhost:8123/" in page2.url, page2.url)

    page2.route("https://mock.api/subscribers", lambda r: r.fulfill(status=500, body="boom"))
    page2.locator("section.newsletter input[type=email]").fill("bruno@exemplo.com")
    page2.locator("section.newsletter button").click()
    page2.wait_for_timeout(600)
    st = page2.locator("section.newsletter .newsletter-status").inner_text()
    check("nl: HTTP 500 -> erro inline", "não deu certo" in st.lower(), st)

    page2.route("https://mock.api/subscribers", lambda r: r.abort("failed"))
    page2.locator("section.newsletter input[type=email]").fill("bruno@exemplo.com")
    page2.locator("section.newsletter button").click()
    page2.wait_for_timeout(600)
    st = page2.locator("section.newsletter .newsletter-status").inner_text()
    check("nl: rede fora -> erro inline", "falha de conexão" in st.lower(), st)
    page2.close(); page.close()

    # ---------- TODOS os artigos (passagens 1,2,3,5) ----------
    bad_articles = []
    for slug in ARTICLES:
        page, errors = new_page(1440)
        r = page.request.get(BASE + f"/guia/{slug}")
        if r.status != 200:
            bad_articles.append(f"{slug}: HTTP {r.status}")
            page.close(); continue
        page.goto(BASE + f"/guia/{slug}", wait_until="networkidle")
        nl = page.locator("section.newsletter[aria-labelledby=nl-art]").count()
        ad_vis = page.locator(".ad-slot").first.evaluate("el => getComputedStyle(el).display") if page.locator(".ad-slot").count() else "none"
        aff = page.locator(".affiliate").count()
        js_loaded = page.evaluate("() => typeof window !== 'undefined' && !!document.querySelector('script[src*=\"newsletter.js\"]')")
        if nl != 1: bad_articles.append(f"{slug}: newsletter inline={nl}")
        if ad_vis != "none": bad_articles.append(f"{slug}: ad-slot visível={ad_vis}")
        expected_aff = 1 if slug in HARDWARE else 0
        if aff != expected_aff: bad_articles.append(f"{slug}: affiliate={aff} esperado={expected_aff}")
        if not js_loaded: bad_articles.append(f"{slug}: newsletter.js não carregado")
        if errors: bad_articles.append(f"{slug}: JS errors: {'; '.join(errors[:2])}")
        page.close()
    check(f"todos {len(ARTICLES)} artigos: newsletter+ad-slot+affiliate corretos, zero erros JS",
          not bad_articles, "; ".join(bad_articles[:5]))

    # ---------- Mobile 390px: amostra (hardware + não-hardware longo) ----------
    for slug in ["tokens-por-segundo-30b-hardware-real", "como-rodar", "qwen3.8-vs-qwen3.6-27b"]:
        page, errors = new_page(390)
        page.goto(BASE + f"/guia/{slug}", wait_until="networkidle")
        over = page.evaluate("() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
        btn_h = page.locator(".newsletter-form button").first.evaluate("el => el.getBoundingClientRect().height")
        check(f"artigo/{slug}/mobile: zero overflow", over <= 0, f"{over}px")
        check(f"artigo/{slug}/mobile: botão newsletter >= 44px", btn_h >= 44, f"{btn_h:.0f}px")
        check(f"artigo/{slug}/mobile: zero erros JS", len(errors) == 0, "; ".join(errors[:2]))
        page.close()

    # ---------- Privacidade ----------
    page, _ = new_page(1440)
    page.goto(BASE + "/privacidade.html", wait_until="networkidle")
    robots = page.locator('meta[name="robots"]').get_attribute("content") or ""
    check("privacidade: meta robots index", "index" in robots, robots)
    txt = page.inner_text("main")
    check("privacidade: LGPD + direitos", "LGPD" in txt and "direitos" in txt.lower())
    check("privacidade: disclosure affiliate", "afiliado" in txt)
    check("privacidade: consentimento newsletter", "consentimento" in txt.lower())
    over = page.evaluate("() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
    check("privacidade: zero overflow", over <= 0, f"{over}px")
    page.close()

    # ---------- Passagem 5: outras páginas não quebradas ----------
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    for path in ["/modelos.html", "/benchmarks.html", "/hardware.html", "/guia-rapido.html", "/404.html", "/guia"]:
        r = page.request.get(BASE + path)
        check(f"nao-queuebrado: {path} -> 200", r.status == 200, str(r.status))
    page.close()
    browser.close()

fails = [r for r in results if not r[1]]
print(f"\n===== {len(results)-len(fails)}/{len(results)} passaram =====")
sys.exit(1 if fails else 0)
