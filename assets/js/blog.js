/* ============================================================
   assets/js/blog.js — JS global mínimo (zero dependência, ADR-001)
   Design system: assets/css/blog.css
   Responsável por: tema, hambúrguer, busca (índice estático),
   TOC scrollspy, newsletter (delega à task de monetização).
   Tudo é progressive enhancement: sem JS, o site continua navegável.
   ============================================================ */
(function () {
  "use strict";

  var root = document.documentElement;

  /* ---------- 1. Tema (localStorage + prefers-color-scheme) ---------- */
  var themeBtn = document.querySelector("[data-theme-toggle]");
  try {
    var savedTheme = localStorage.getItem("theme");
    var prefersLight =
      window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches;
    root.setAttribute("data-theme", savedTheme || (prefersLight ? "light" : "dark"));
  } catch (e) {
    /* localStorage indisponível: segue o padrão dark do CSS */
  }
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }

  /* ---------- 2. Hambúrguer mobile (<900px) ---------- */
  var navToggle = document.querySelector("[data-nav-toggle]");
  var navLinks = document.querySelector(".nav-links");
  if (navToggle && navLinks) {
    navToggle.addEventListener("click", function () {
      var open = navLinks.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    // fecha o menu ao clicar num link
    navLinks.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        navLinks.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---------- 3. Busca (índice estático + fallback sem JS) ---------- */
  var searchBtn = document.querySelector("[data-search-open]");
  var searchOverlay = document.getElementById("search");
  var searchInput = document.querySelector("[data-search-input]");
  var searchResults = document.querySelector("[data-search-results]");
  var indexCache = null;

  function loadIndex() {
    if (indexCache) return Promise.resolve(indexCache);
    return fetch("/assets/js/blog-index.json", { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) {
        indexCache = data;
        return data;
      });
  }

  function renderResults(term) {
    if (!searchResults) return;
    var t = (term || "").trim().toLowerCase();
    if (!t) {
      searchResults.innerHTML =
        '<a href="/guia/"><span class="sm">Todos os artigos →</span></a>';
      return;
    }
    loadIndex()
      .then(function (items) {
        var hits = items.filter(function (a) {
          return (
            (a.title || "").toLowerCase().indexOf(t) !== -1 ||
            (a.category || "").toLowerCase().indexOf(t) !== -1 ||
            (a.tags || []).some(function (tag) {
              return tag.toLowerCase().indexOf(t) !== -1;
            })
          );
        });
        if (window.qwenTrackSearch) {
          try { window.qwenTrackSearch(t); } catch (e) {}
        }
        if (!hits.length) {
          searchResults.innerHTML =
            '<p style="padding:12px 16px;font-size:.85rem;color:var(--muted)">Nada encontrado para "' +
            term + '". <a href="/guia/">Ver todos os artigos →</a></p>';
          return;
        }
        searchResults.innerHTML = hits
          .slice(0, 8)
          .map(function (a) {
            return (
              '<a href="' + a.url + '">' +
              '<span class="badge-cat ' + catClass(a.category) + '">' + a.category + "</span> " +
              escapeHtml(a.title) + "</a>"
            );
          })
          .join("");
      })
      .catch(function () {
        // fallback: índice indisponível → link para o arquivo
        searchResults.innerHTML =
          '<a href="/guia/"><span class="sm">Índice indisponível agora — ver todos os artigos →</span></a>';
      });
  }

  function catClass(cat) {
    var map = { Guias: "guides", Benchmarks: "bench", Hardware: "hw", Releases: "releases", Comunidade: "community" };
    return map[cat] || "guides";
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function openSearch() {
    if (!searchOverlay) return;
    searchOverlay.hidden = false;
    searchOverlay.classList.add("open");
    if (searchInput) setTimeout(function () { searchInput.focus(); }, 30);
  }
  function closeSearch() {
    if (!searchOverlay) return;
    searchOverlay.classList.remove("open");
    searchOverlay.hidden = true;
  }

  if (searchBtn && searchOverlay) {
    searchBtn.addEventListener("click", openSearch);
    searchOverlay.addEventListener("click", function (e) {
      if (e.target === searchOverlay) closeSearch();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeSearch();
    });
  }
  if (searchInput && searchResults) {
    searchInput.addEventListener("input", function () { renderResults(searchInput.value); });
  }

  /* ---------- 4. TOC: estado desktop/mobile (PRD §5.3) ----------
     O <details class="toc-details"> nasce fechado no HTML: em mobile vira
     toggle colapsável nativo (zero-JS). Em desktop (>=1025px) o JS força
     open para o TOC ficar sempre visível/sticky — um <details> fechado
     esconde o conteúdo via slot interno do UA, então CSS não resolve sozinho. */
  var tocDetails = document.querySelector(".toc-details");
  var tocDesktop = window.matchMedia
    ? window.matchMedia("(min-width: 1025px)")
    : null;
  function syncTocState() {
    if (tocDetails && tocDesktop) tocDetails.open = tocDesktop.matches;
  }
  syncTocState();
  if (tocDesktop && tocDesktop.addEventListener) {
    tocDesktop.addEventListener("change", syncTocState);
  } else if (tocDesktop && tocDesktop.addListener) {
    tocDesktop.addListener(syncTocState); // Safari <14
  }

  /* ---------- 4b. TOC scrollspy (artigos — progressive) ---------- */
  var toc = document.querySelector(".toc");
  var tocLinks = toc ? Array.prototype.slice.call(toc.querySelectorAll("a")) : [];
  var headings = tocLinks
    .map(function (a) {
      var id = a.getAttribute("href");
      return id && id[0] === "#" ? document.getElementById(id.slice(1)) : null;
    })
    .filter(Boolean);

  if (toc && tocLinks.length && headings.length && "IntersectionObserver" in window) {
    var spy = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          tocLinks.forEach(function (a) {
            a.classList.toggle(
              "active",
              a.getAttribute("href") === "#" + en.target.id
            );
          });
        });
      },
      { rootMargin: "-20% 0px -70% 0px", threshold: 0 }
    );
    headings.forEach(function (h) { spy.observe(h); });
  }

  /* ---------- 5. Rodapé: ano corrente ---------- */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());

  /* ---------- 6. Fallback de imagem do pack (t_c197a42b) ----------
     Se a arte webp/avif não carregar, marca o wrapper (.post-thumb-wrap
     ou .fc-media-wrap) com data-fallback="on" para o CSS exibir o
     monograma de categoria em seu lugar. Progressive enhancement. */
  function bindImgFallback() {
    var imgs = document.querySelectorAll(
      ".post-thumb-wrap .post-thumb img, .fc-media-wrap .fc-media img"
    );
    Array.prototype.forEach.call(imgs, function (img) {
      var wrap = img.closest(".post-thumb-wrap, .fc-media-wrap");
      if (!wrap) return;
      img.addEventListener("error", function () {
        wrap.setAttribute("data-fallback", "on");
      });
      // se já veio quebrada (cache), garante o fallback
      if (img.complete && img.naturalWidth === 0) {
        wrap.setAttribute("data-fallback", "on");
      }
    });
  }
  bindImgFallback();
  // cards injetados depois (busca/mobile) re-binding
  if (document.body) {
    var mo = new MutationObserver(function () { bindImgFallback(); });
    mo.observe(document.body, { childList: true, subtree: true });
  }
})();
