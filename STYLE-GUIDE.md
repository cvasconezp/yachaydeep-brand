# Yachay Deep — Design System (ligero)

> **Arquitectura de marca y lockups** (cómo se relacionan Yachay Deep Hub y sus productos, y cómo se construyen los lockups): ver [BRAND-ARCHITECTURE.md](./BRAND-ARCHITECTURE.md).

Fuente única de verdad de la marca. Tres archivos:

| Archivo | Para qué | Quién lo consume |
|---|---|---|
| `theme.css` | Tokens en formato Tailwind 4 (`@theme`) | `yachaydeep-web` (sitio corporativo) |
| `preset.cjs` | Mismos tokens en formato Tailwind 3 | `yachay-deep/frontend` (app) — copia sincronizada en `frontend/brand.preset.cjs` |
| `tokens.json` | Tokens en formato neutro (W3C draft) | Documentación, herramientas, Figma |

**Regla de oro:** un cambio de marca se hace AQUÍ y se propaga. Nunca se edita
un color/fuente directamente en un consumidor. Tras editar, copiar `preset.cjs`
a `yachay-deep/frontend/brand.preset.cjs` (hasta que la app migre a Tailwind 4).

## Paleta

| Token | Hex | Uso |
|---|---|---|
| `brand` | `#1B3A6B` | Navy institucional. Fondos de autoridad, títulos sobre claro |
| `brand-dark` | `#0F2444` | Extremo de gradientes, footer |
| `brand-light` | `#2B5AA0` | Hovers/enlaces sobre navy |
| `brand-gold` | `#E8A838` | **Solo acción y acento**: CTAs, eyebrows, métricas, barra de tarjeta. Nunca fondo extenso |
| `brand-gold-light` | `#F5C563` | Hover del dorado |
| `brand-ice` | `#A8DCE8` | Detalle frío sobre navy (coordenadas, metadatos) |
| `brand-ice-light` | `#D8EFF4` | Fondos suaves claros |

Apoyo neutro: escala `gray` de Tailwind. Verde `emerald` reservado a WhatsApp/estados activos.

## Tipografía

| Rol | Fuente | Pesos | Uso |
|---|---|---|---|
| Display (`font-display`) | Bricolage Grotesque | 600–800 | H1/H2 de héroes y secciones |
| Cuerpo (`font-sans`) | Instrument Sans | 400–700 | Todo lo demás (default del body) |
| Mono (`font-mono`) | Spline Sans Mono | 400–500 | Datos, handles, coordenadas |

Carga (en `index.html`): Google Fonts con `preconnect`. La app (dashboard) aún
usa la sans del sistema; adoptará estas fuentes al migrar a Tailwind 4.

## Patrones canónicos

- **Eyebrow**: `text-xs uppercase tracking-[0.25em] text-brand-gold font-semibold` sobre el título.
- **Sección oscura**: `bg-gradient-to-br from-brand via-brand-dark to-brand` + decoraciones `bg-brand-gold/10 blur-3xl rounded-full` absolutas.
- **Tarjeta destacada**: blanca `rounded-3xl shadow-xl border-gray-100` con barra superior `h-1.5 bg-gradient-to-r from-brand via-brand-gold to-brand-gold-light`.
- **Tarjeta interactiva**: `rounded-2xl shadow-lg hover:shadow-2xl hover:-translate-y-1 transition-all duration-300` + flecha `→` que se desplaza en hover.
- **Chip credencial**: `text-[11px] bg-white/5 border border-white/10 px-2.5 py-1 rounded-full` (sobre navy).
- **Botón primario**: `bg-brand-gold hover:bg-brand-gold-light text-brand-dark font-semibold rounded-lg/xl`.
- **Botón pill secundario**: borde `border-gray-200` con hover dorado (`hover:border-brand-gold hover:text-brand-gold`).
- **Métrica**: número `text-3xl font-bold text-brand-gold` + etiqueta `text-sm text-blue-200` (sobre navy).

Demo viva: ruta `/design` del sitio corporativo.

## Voz

Español directo, primera persona del plural, datos con propósito humano
("cada dato representa una persona"). Evitar jerga sin explicar; los números
siempre con contexto.
