# @yachaydeep/brand

Fuente única de verdad de la marca **Yachay Deep**: tokens de color y tipografía,
activos gráficos y guía de estilo. Un cambio de marca se hace aquí y se propaga
a todos los consumidores.

## Instalación

```bash
npm install github:cvasconezp/yachaydeep-brand
```

## Uso

**Tailwind 4** (CSS-first) — en tu hoja principal:

```css
@import "tailwindcss";
@import "@yachaydeep/brand/theme.css";
```

**Tailwind 3** — en `tailwind.config.js`:

```js
import brandPreset from "@yachaydeep/brand/preset";

export default {
  presets: [brandPreset],
  /* ... */
};
```

**Tokens neutros** (cualquier herramienta):

```js
import tokens from "@yachaydeep/brand/tokens" with { type: "json" };
```

**Activos** (logos, banner, favicon): carpeta [`assets/`](./assets). Los proyectos
web los copian a su `public/` (mismo nombre de archivo = cero cambios de código
al actualizar el logo).

**Tipografía** — cargar en el `<head>` del consumidor:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=Instrument+Sans:wght@400;500;600;700&family=Spline+Sans+Mono:wght@400;500&display=swap" rel="stylesheet">
```

## Consumidores

| Proyecto | Cómo consume |
|---|---|
| `yachaydeep-web` (hub corporativo) | `theme.css` (Tailwind 4) + copia de `assets/` en `public/brand` |
| `yachay-deep` (SaaS Core) | `preset` (Tailwind 3); adoptará `theme.css` al migrar a TW4 |
| FitBro u otros | Opcional: mismos mecanismos si adoptan la identidad Yachay Deep |

Guía completa de uso de color, tipografía, patrones y voz: [STYLE-GUIDE.md](./STYLE-GUIDE.md).  
Arquitectura de marca y sistema de lockups (Hub + productos): [BRAND-ARCHITECTURE.md](./BRAND-ARCHITECTURE.md) · PDF en [`docs/`](./docs/Yachay_Deep_Manual_de_Marca_y_Lockups.pdf).

## Publicar un cambio

1. Editar tokens/activos aquí y subir la versión en `package.json`.
2. En cada consumidor: `npm update @yachaydeep/brand` (o reinstalar) y redeploy.
