# Yachay Deep — Arquitectura de marca y lockups

Cómo se relacionan **Yachay Deep** (la empresa) y sus productos, y cómo se
construyen los lockups. Este documento es la **fuente editable**; el PDF maquetado
para compartir/imprimir está en
[`docs/Yachay_Deep_Manual_de_Marca_y_Lockups.pdf`](./docs/Yachay_Deep_Manual_de_Marca_y_Lockups.pdf)
y se regenera con [`scripts/build-manual.py`](./scripts/build-manual.py).

Extiende —no reemplaza— a [`STYLE-GUIDE.md`](./STYLE-GUIDE.md) (color, tipografía,
patrones de UI y voz) y a [`LOGOS.md`](./LOGOS.md) (qué archivo de logo va en cada lugar).

---

## 1. Punto de partida

Yachay Deep dejó de ser un solo producto educativo y pasó a ser una **casa de productos digitales e inteligencia aplicada**. Es el mismo camino de
**Facebook → Meta** — la marca crece más allá de su origen y se crea un nivel-empresa
que da espacio a lo nuevo sin perder lo construido.

El reto de marca es **conectar sin uniformar**: que el cliente reconozca el respaldo
de Yachay Deep en Core, Kullki o FitBro, pero que cada producto pueda hablarle a su
propio público.

**Modelo de referencia:** el sistema de lockups endosados de la Universidad
Politécnica Salesiana (logo madre fijo + nombre de carrera + modificador de sede/modalidad).

| UPS (referencia) | Yachay Deep (equivalente) |
|---|---|
| Logo madre UPS (fijo) | Logo madre Yachay Deep (iceberg + wordmark) |
| Nombre de la carrera | Nombre del producto / unidad |
| Modificador: «Sede Quito» / «En línea» | Modificador: sector, estado o «por Yachay Deep Labs» |

---

## 2. Arquitectura: tres niveles

Decisión adoptada: arquitectura **híbrida con endoso** (marca madre fuerte, endoso
disciplinado en el núcleo y un poco más de aire en los productos de consumo).

| Nivel | Qué es | Marca |
|---|---|---|
| **1 — Marca madre** | **Yachay Deep.** La empresa. Casi nunca aparece sola: aparece endosando a un producto. | Logo madre |
| **2 — Núcleo (endoso fuerte)** | **Core · Academy · Studio · Research.** Viven de la confianza institucional. | Lockup rígido (Modo A) |
| **3 — Productos de Labs (endoso ligero)** | **Áncora · Kullki · Horario Inteligente · Polaris** (activos) y las apps en incubación (**Mikuy · Analytics · FitBro · Teseo**). Públicos distintos. | Identidad propia + sello (Modo B) |

> **Regla de oro:** a mayor cercanía con la venta institucional, más rígido el lockup.
> A mayor cercanía con el consumidor final, más aire para la marca propia — pero el
> endoso nunca desaparece.

---

## 3. Anatomía del lockup

Todo lockup del núcleo se construye con las mismas cuatro piezas, en este orden:

```
[ logo madre ]  |  Nombre del producto
                |  --- MODIFICADOR
```

| # | Pieza | Regla |
|---|---|---|
| 1 | **Logo madre** | Iceberg + wordmark «Yachay Deep». Nunca se altera, recolorea ni reproporciona. |
| 2 | **Divisor** | Línea vertical navy, de la misma altura que el wordmark. Separa marca madre y producto. |
| 3 | **Nombre del producto** | Tipografía display (Bricolage Grotesque), navy. 1–2 líneas. |
| 4 | **Modificador** | Mono, mayúsculas, con regla corta a la izquierda. Sector, modalidad o estado. Opcional. |

**Área de protección** = altura del iceberg (X). Mantener ≥ 1X de espacio libre
alrededor de todo el lockup. **Tamaño mínimo:** el wordmark «Yachay Deep» nunca por
debajo de `22 px` en pantalla / `16 mm` impreso; por debajo, usar solo el icono.

---

## 4. Modo A — Lockup rígido (endoso fuerte)

Para el núcleo: **Core, Academy, Studio, Research**. Mismo logo, mismo divisor, misma
tipografía. Solo cambian el nombre y el modificador.

Ejemplos de modificador:

- `Yachay Deep | Core` — PARA EDUCACIÓN SUPERIOR
- `Yachay Deep | Academy` — FORMACIÓN · EN LÍNEA
- `Yachay Deep | Studio` — CONSULTORÍA · TRANSFORMACIÓN DIGITAL
- `Yachay Deep | Research` — INVESTIGACIÓN APLICADA

**Hacer:** alinear al centro · respetar el divisor · nombre siempre en navy sobre
fondo claro · modificador opcional pero consistente.

**No hacer:** cambiar la tipografía del nombre · poner el nombre en dorado · omitir el
logo madre · inventar un divisor distinto.

---

## 5. Modo B — Identidad propia endosada (endoso ligero)

Para los productos de Labs: **Áncora, Kullki, Horario Inteligente, Polaris** y las apps en incubación. Marca propia con
personalidad, conectada por un sello discreto **«por Yachay Deep Labs»**. No le venden
al mismo público que Core, así que necesitan aire.

| Producto | Tono | Endoso |
|---|---|---|
| **Áncora** | Docente, práctico, sereno | por Yachay Deep Labs |
| **Kullki** | Comunitario, kichwa, cálido | por Yachay Deep Labs |
| **Horario Inteligente** | Estudiantil, directo (identificador: 📅) | por Yachay Deep Labs |
| **Polaris** | Guía del estudiante (identificador: constelación de la Osa Menor) | por Yachay Deep Labs |
| **Mikuy · Analytics · FitBro · Teseo** | En incubación | en Yachay Deep Labs |

> La Polla Mundialista queda fuera del roster de marca: no aparece en piezas de la casa.

**Cuándo usar Modo B:** cuando el producto le habla a un público distinto del
institucional y una estética «universidad» le restaría cercanía. La marca respira;
el endoso permanece. Cada producto puede desarrollar su propio wordmark; lo invariable
es el sello de endoso.

---

## 6. El sello de endoso «por Yachay Deep Labs»

El hilo que conecta toda la casa. Discreto pero presente en cada producto de Nivel 3.

| Aspecto | Regla |
|---|---|
| Texto | `por Yachay Deep Labs` (productos activos de Labs) · `en Yachay Deep Labs` (en incubación; nunca «un producto de» ni «Powered by») · `por Yachay Deep` (resto) |
| Tipografía | Mono (Spline Sans Mono), mayúsculas, tracking amplio |
| Tamaño | ~55–65 % del cuerpo. Acompaña, no compite |
| Color | Gris medio sobre claro · hielo (`#A8DCE8`) sobre navy |
| Posición | Bajo el nombre del producto, o al pie de la pieza |

> Ya implementado en `yachaydeep.com/labs`: cada tarjeta de producto lleva el sello
> «POR YACHAY DEEP LABS». Core no lo lleva: es la marca insignia, va con lockup rígido.

---

## 7. Fundamentos (resumen)

Paleta y tipografía completas en [`STYLE-GUIDE.md`](./STYLE-GUIDE.md) y
[`tokens.json`](./tokens.json). Reglas que afectan a los lockups:

- **Dorado = solo acción y acento.** En lockups, el nombre del producto va en **navy**,
  nunca en dorado.
- **Nombres de producto** en `Bricolage Grotesque` (display).
- **Modificadores y sello de endoso** en `Spline Sans Mono`.

---

## 8. Usos — correcto / incorrecto

| Sí | No |
|---|---|
| Logo madre intacto en todo lockup del núcleo | Recolorear, estirar o rotar el logo |
| Nombre de producto en navy, tipografía display | Nombre de producto en dorado |
| Dorado solo para acción/acento | Fondos extensos dorados |
| Endoso discreto y consistente | Endoso del mismo tamaño que el nombre |
| Respetar 1X de área de protección | Texto u otros logos invadiendo el lockup |
| Modo B con aire para Áncora, Kullki y las apps de Labs | Forzar el lockup rígido en productos de Labs |

> **En una frase:** el sistema de la Salesiana es el camino correcto para el núcleo de
> la marca; dale a los productos de Labs un par de centímetros más de aire que a una
> «carrera», porque no le venden al mismo público.

---

## 9. Color de submarca, incubación y piezas animadas

Reglas acordadas al producir los logos animados, reels y el hero de la casa (oct-2026):

| Regla | Detalle |
|---|---|
| **El iceberg nunca se recolorea** | Cuando Yachay Deep aparece junto a una submarca, solo sus **letras** pueden adoptar el acento de la submarca; el ícono (sol, punta, cuerpo, red, monograma YD) conserva siempre sus colores. Sobre blanco, el navy se mantiene y solo cambia el dorado. |
| **Negativos de submarca** | Sobre fondos oscuros se usan las versiones `-negativo` de `assets/` (Áncora: A blanca + visto naranja; Kullki: verdes aclarados + moneda dorada + palabra blanca). No se ponen en recuadro blanco. |
| **Incubación con menos protagonismo** | Las apps en incubación no tienen logo propio: se muestran con el **ícono de Yachay Deep \| su emoji** (🍽️ Mikuy, 📊 Analytics, 🏋️ FitBro, 🚀 Teseo), más pequeñas que las activas y con el rótulo «Incubación». |
| **Unidades sin color propio** | Research, Labs, Studio y Academy usan solo el navy de la casa. En piezas de la casa, **Research Institute** es la base: va destacado, debajo de las demás unidades. |
| **Cierre de transiciones** | Toda transición Yachay Deep → producto de Labs termina con el isotipo, el nombre y el sello «por Yachay Deep Labs» (como Kullki y Áncora). |

Las piezas animadas (Remotion) viven en el repo `yachaydeep-motion`; los renders,
en el Dropbox de marca (`Imagen de marca/Videos animados`). No se versionan aquí.

---

## Regenerar el PDF

```bash
pip install weasyprint        # requiere Pango/Cairo en el sistema
python scripts/build-manual.py
# -> docs/Yachay_Deep_Manual_de_Marca_y_Lockups.pdf
```

El generador lee el logo y la paleta desde este repo, así que el manual se mantiene
sincronizado con la marca: si cambia un token o el logo, se regenera y queda al día.
