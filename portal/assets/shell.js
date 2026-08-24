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

    var mb = document.getElementById("menu-btn"), dr = document.getElementById("drawer");
    if (mb && dr) {
      mb.addEventListener("click", function () {
        var on = dr.classList.toggle("on");
        mb.setAttribute("aria-expanded", on ? "true" : "false");
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && dr.classList.contains("on")) {
          dr.classList.remove("on"); mb.setAttribute("aria-expanded", "false"); mb.focus();
        }
      });
    }
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
