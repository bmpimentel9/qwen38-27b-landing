/* ============================================================
   newsletter.js — Captura de email da newsletter (card t_8dd9a051)
   ============================================================
   Comportamento (PRD §8.1):
   - Intercepta submit de todo form .newsletter-form.
   - Envia para um endpoint CONFIGURÁVEL (sem redirecionar o leitor).
   - Sucesso/erro inline via <div class="newsletter-status"> (aria-live).
   - Sem popup, sem dark pattern. Progressive enhancement:
     sem JS, o form faz POST nativo para NEWSLETTER_CONFIG.action.

   COMO CONFIGURAR (sem chave hoje = form fica "em breve", honesto):
   -----------------------------------------------------------------
   1. Buttondown (recomendado — PRD): crie a newsletter, gere uma API
      key, e aponte:
        window.NEWSLETTER_CONFIG = {
          endpoint: "https://api.buttondown.com/v1/subscribers",
          token: "SUA_API_KEY_BUTTONDOWN"
        };
   2. Formspree: crie um form e aponte:
        window.NEWSLETTER_CONFIG = {
          endpoint: "https://formspree.io/f/SEU_FORM_ID"
        };
   3. Alternativa sem API: use o embed nativo do Buttondown no atributo
      action do form e deixe endpoint vazio — o JS apenas dá o feedback
      inline e deixa o POST nativo acontecer (redirect leve, aceitável
      apenas como fallback sem API).
   -----------------------------------------------------------------
   Config pode ser definida em um <script> ANTES deste arquivo, ou no
   atributo data-endpoint do próprio form (override por formulário).
   ============================================================ */

(function () {
  "use strict";

  var CONFIG = {
    endpoint: "",          // URL da API (Buttondown/Formspree). "" = form em modo "em breve".
    token: "",             // Token/API key (Buttondown usa Authorization: Token <key>).
    action: ""             // URL do embed nativo (fallback sem JS). "" = usa action do form.
  };
  if (window.NEWSLETTER_CONFIG) {
    for (var k in CONFIG) if (window.NEWSLETTER_CONFIG[k]) CONFIG[k] = window.NEWSLETTER_CONFIG[k];
  }

  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  function statusEl(form) {
    var el = form.querySelector(".newsletter-status");
    if (el) return el;
    el = document.createElement("div");
    el.className = "newsletter-status";
    el.setAttribute("aria-live", "polite");
    form.appendChild(el);
    return el;
  }

  function setStatus(form, state, msg) {
    var el = statusEl(form);
    el.textContent = msg;
    el.setAttribute("data-state", state);
  }

  function track(event, label) {
    if (typeof gtag === "function") {
      try { gtag("event", event, { event_category: "newsletter", event_label: label || "" }); }
      catch (e) { /* analytics nunca quebra o form */ }
    }
  }

  function endpointFor(form) {
    var perForm = form.getAttribute("data-endpoint");
    return (perForm && perForm.trim()) ? perForm.trim() : CONFIG.endpoint;
  }

  function submit(form) {
    var input = form.querySelector('input[type="email"]');
    var btn = form.querySelector("button[type=submit]");
    if (!input) return;

    var email = (input.value || "").trim();
    input.setAttribute("aria-invalid", "false");
    if (!EMAIL_RE.test(email)) {
      input.setAttribute("aria-invalid", "true");
      input.focus();
      setStatus(form, "error", "Digite um email válido.");
      track("newsletter_error", "invalid_email");
      return;
    }

    var endpoint = endpointFor(form);

    // Sem endpoint configurado: feedback honesto, sem fake success.
    if (!endpoint) {
      setStatus(form, "info", "Ainda não abrimos as inscrições — volte em breve.");
      track("newsletter_attempt", "no_endpoint");
      return;
    }

    if (btn) { btn.disabled = true; }
    input.setAttribute("aria-busy", "true");
    setStatus(form, "", "Enviando…");

    var headers = { "Content-Type": "application/json" };
    if (CONFIG.token) headers["Authorization"] = "Token " + CONFIG.token;

    fetch(endpoint, {
      method: "POST",
      headers: headers,
      body: JSON.stringify({ email: email })
    }).then(function (res) {
      if (res.ok || res.status === 200 || res.status === 201) {
        setStatus(form, "success", "Inscrição confirmada! Confira seu email para ativar.");
        input.value = "";
        track("newsletter_subscribe", endpoint);
      } else {
        setStatus(form, "error", "Não deu certo agora. Tente de novo em instantes.");
        track("newsletter_error", "http_" + res.status);
      }
    }).catch(function () {
      setStatus(form, "error", "Falha de conexão. Confira sua internet e tente de novo.");
      track("newsletter_error", "network");
    }).finally(function () {
      if (btn) { btn.disabled = false; }
      input.setAttribute("aria-busy", "false");
    });
  }

  function init() {
    var forms = document.querySelectorAll("form.newsletter-form");
    for (var i = 0; i < forms.length; i++) {
      (function (form) {
        // Fallback sem JS: aponta o action nativo p/ o embed configurado.
        if (CONFIG.action && (!form.getAttribute("action") || form.getAttribute("action") === "#")) {
          form.setAttribute("action", CONFIG.action);
        }
        form.addEventListener("submit", function (ev) {
          ev.preventDefault();
          submit(form);
        });
      })(forms[i]);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
