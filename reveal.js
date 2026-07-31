/*
 * @yachaydeep/brand — reveal.js
 * Drop-in framework-agnóstico para el "reveal on scroll" de motion.css.
 * Agrega `reveal-ready` al <html> (solo si el usuario NO pidió reducir
 * movimiento) y revela [data-reveal] / [data-reveal-stagger] al entrar en
 * viewport. Si el usuario pide reducir movimiento, o no hay JS, el contenido
 * queda visible (nunca se oculta).
 *
 * Vanilla:  <script src=".../reveal.js" defer></script>
 * React:    importar y llamar ydInitReveal() tras cada cambio de ruta.
 */
(function (global) {
  function ydInitReveal(root) {
    if (typeof window === "undefined") return;
    var mq = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)");
    if (mq && mq.matches) return;
    document.documentElement.classList.add("reveal-ready");
    var scope = root || document;
    var els = scope.querySelectorAll("[data-reveal]:not(.is-visible), [data-reveal-stagger]:not(.is-visible)");
    if (!els.length || !("IntersectionObserver" in window)) {
      Array.prototype.forEach.call(els, function (el) { el.classList.add("is-visible"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("is-visible"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    Array.prototype.forEach.call(els, function (el) { io.observe(el); });
  }
  global.ydInitReveal = ydInitReveal;
  if (typeof document !== "undefined") {
    if (document.readyState !== "loading") ydInitReveal();
    else document.addEventListener("DOMContentLoaded", function () { ydInitReveal(); });
  }
  if (typeof module !== "undefined" && module.exports) module.exports = { ydInitReveal: ydInitReveal };
})(typeof window !== "undefined" ? window : this);
