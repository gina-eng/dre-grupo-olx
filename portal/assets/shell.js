// Chrome compartilhado: tema persistente entre páginas e drawer no mobile.
(function () {
  var TKEY = "dre-olx-tema";
  try {
    var saved = localStorage.getItem(TKEY);
    if (saved === "dark" || saved === "light") document.documentElement.setAttribute("data-theme", saved);
  } catch (e) {}

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    var btn = document.getElementById("theme");
    if (btn) btn.addEventListener("click", function () {
      var r = document.documentElement;
      var dark = r.getAttribute("data-theme") === "dark" ||
        (!r.hasAttribute("data-theme") && window.matchMedia("(prefers-color-scheme: dark)").matches);
      var next = dark ? "light" : "dark";
      r.setAttribute("data-theme", next);
      try { localStorage.setItem(TKEY, next); } catch (e) {}
    });

    var mb = document.getElementById("menu-btn"),
        dr = document.getElementById("drawer"),
        bd = document.getElementById("drawer-bd"),
        fc = document.getElementById("drawer-close");
    if (mb && dr && bd) {
      var abrir = function () {
        bd.hidden = false;
        requestAnimationFrame(function () { bd.classList.add("on"); });
        dr.classList.add("on");
        dr.setAttribute("aria-hidden", "false");
        mb.setAttribute("aria-expanded", "true");
        document.body.style.overflow = "hidden";
        var alvo = dr.querySelector("a, button");
        if (alvo) alvo.focus();
      };
      var fechar = function () {
        bd.classList.remove("on");
        setTimeout(function () { bd.hidden = true; }, 220);
        dr.classList.remove("on");
        dr.setAttribute("aria-hidden", "true");
        mb.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
        mb.focus();
      };
      mb.addEventListener("click", abrir);
      bd.addEventListener("click", fechar);
      if (fc) fc.addEventListener("click", fechar);
      dr.addEventListener("click", function (e) {
        if (e.target.closest("a")) fechar();
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && dr.classList.contains("on")) fechar();
      });
    }
  });

  // Índice "Nesta página": montado a partir dos <h2> do conteúdo, com realce
  // da seção visível. Fica fora do HTML gerado para não haver duas listas a manter.
  ready(function () {
    var toc = document.getElementById("toc");
    var dtoc = document.getElementById("dtoc");
    var host = document.querySelector(".doc-main") || document.querySelector("main");
    if (!host || (!toc && !dtoc)) return;

    var hs = Array.prototype.slice.call(host.querySelectorAll("h2"));
    if (!hs.length) return;

    var links = [];
    hs.forEach(function (h, i) {
      if (!h.id) {
        h.id = "sec-" + (h.textContent || "")
          .toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "")
          .replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 40) || "sec-" + i;
      }
      h.style.scrollMarginTop = "5rem";
      var texto = (h.textContent || "").trim();
      [toc, dtoc].forEach(function (destino) {
        if (!destino) return;
        var a = document.createElement("a");
        a.className = "nav-item nav-sub";
        a.href = "#" + h.id;
        a.textContent = texto;
        destino.appendChild(a);
        if (destino === toc) links.push(a);
      });
    });
    ["toc-label", "dtoc-label"].forEach(function (id) {
      var r = document.getElementById(id);
      if (r) r.hidden = false;
    });

    if (!("IntersectionObserver" in window)) return;
    var visiveis = new Set();
    function realca() {
      var alvo = null;
      hs.forEach(function (h) { if (visiveis.has(h) && !alvo) alvo = h; });
      links.forEach(function (a, i) {
        if (alvo && hs[i] === alvo) a.setAttribute("aria-current", "true");
        else a.removeAttribute("aria-current");
      });
    }
    var io = new IntersectionObserver(function (ents) {
      ents.forEach(function (e) {
        if (e.isIntersecting) visiveis.add(e.target); else visiveis.delete(e.target);
      });
      realca();
    }, { rootMargin: "-72px 0px -60% 0px" });
    hs.forEach(function (h) { io.observe(h); });
  });

  // Progresso do formulário, lido pelo painel.
  window.dreProgresso = function () {
    try {
      var s = JSON.parse(localStorage.getItem("dre-olx-kickoff-v1") || "{}");
      var n = 0;
      // As chaves "D-*" são o checklist de dados A-J, não as 88 perguntas.
      Object.keys(s).forEach(function (k) {
        if (k.indexOf("D-") !== 0 && String(s[k]).trim()) n++;
      });
      return n;
    } catch (e) { return 0; }
  };
})();
