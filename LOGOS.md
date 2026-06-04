# Guía de logotipos — Yachay Deep

Cómo editar: reemplaza el archivo en `assets/` **manteniendo el nombre exacto**
y haz push a `main`. El sync automático lo propaga al hub y a la app (workflow
"Sync de marca"). Regla general: **SVG con fondo transparente** siempre que el
arte lo permita; PNG solo donde se indica.

## Mapa de uso (qué archivo aparece dónde)

| Archivo | Espacio donde se ve | Tamaño renderizado | Lienzo/exportación recomendada |
|---|---|---|---|
| `logo-navbar.svg/png` | Navbar del hub (todas las páginas) | 48–56 px de alto | Lockup horizontal recortado, sin aire vertical |
| `logo-full.svg/png` | Sidebar y login de la app (SaaS), portal KAPAK, variante por defecto | 40–80 px alto (sidebar ~230 px ancho; login hasta ~350 px) | Lockup horizontal completo. SVG preferido; PNG ≥800 px ancho |
| `logo-hero.svg/png` | Héroe del hub (fondo claro) | 150–250 px de alto | Lockup grande. SVG preferido; PNG ≥1600 px ancho |
| `logo-hero-dark.svg/png` | Secciones sobre fondo oscuro (hub) y footer del landing de la app | 28–250 px de alto | Igual que hero pero wordmark claro |
| `banner.svg/png` | `og:image` (compartir en redes) y cabeceras anchas | 1200×630 fijo en redes | PNG **1200×630 exacto** para og:image (los crawlers no leen SVG) |
| `logo-icon.svg/png` | Isotipo: footer del hub (32 px), sidebar colapsado de la app (~40 px) | 32–48 px | Cuadrado 1:1. SVG + PNG 512×512 |
| `logo-icon-simple.svg/png` | Isotipo simplificado para tamaños mínimos | <32 px | 1:1, sin detalles finos |
| `favicon.svg/png` | Pestaña del navegador | 16–32 px | 1:1, legible a 16 px |
| `logo-stacked.svg/png` | Login de la app, splash screens | 120–250 px de alto | Lockup vertical (isotipo arriba, wordmark abajo), wordmark navy → fondos claros |

## Espacios que hoy NO se sincronizan (per-app, cambian rara vez)

- **Favicons derivados / PWA**: `favicon.ico`, `favicon-16/32.png`,
  `apple-touch-icon.png` (180×180), `icon-192/512.png` — viven en el `public/`
  de cada app. Si cambias el isotipo, regenera estos manualmente
  (realfavicongenerator.net lo hace de una).
- **Loaders/spinners**: hoy las apps usan texto ("Cargando…"). Si quieres un
  loader con el isotipo animado, se agrega como componente aparte.

## Checklist al cambiar un logo

1. Editar en `assets/` con el mismo nombre de archivo.
2. SVG: verificar fondo transparente y sin fuentes embebidas sin convertir a trazos.
3. PNG: exportar @2x del tamaño de uso máximo listado arriba.
4. `git push` a main → el Action propaga y Vercel despliega.
5. Revisar hub (navbar/hero/footer) y app (sidebar/login) en producción.
6. Si cambió el isotipo: regenerar favicons PWA de cada app (manual).

