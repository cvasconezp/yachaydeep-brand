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
| **3 — Consumo (endoso ligero)** | **Kullki · FitBro · Polla Mundialista.** Públicos distintos (comunidad, deporte, entretenimiento). | Identidad propia + sello (Modo B) |

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

Para productos de consumo: **Kullki, FitBro, Polla Mundialista**. Marca propia con
personalidad, conectada por un sello discreto **«por Yachay Deep Labs»**. No le venden
al mismo público que Core, así que necesitan aire.

| Producto | Tono | Endoso |
|---|---|---|
| **Kullki** | Comunitario, kichwa, cálido | por Yachay Deep Labs |
| **FitBro** | Deporte y bienestar, enérgico | por Yachay Deep Labs |
| **Polla Mundialista** | Entretenimiento (producto licenciado a terceros) | por Yachay Deep Labs |

**Cuándo usar Modo B:** cuando el producto le habla a un público distinto del
institucional y una estética «universidad» le restaría cercanía. La marca respira;
el endoso permanece. Cada producto puede desarrollar su propio wordmark; lo invariable
es el sello de endoso.

---

## 6. El sello de endoso «por Yachay Deep Labs»

El hilo que conecta toda la casa. Discreto pero presente en cada producto de Nivel 3.

| Aspecto | Regla |
|---|---|
| Texto | `por Yachay Deep Labs` (productos de Labs) · `por Yachay Deep` (resto) |
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
| Modo B con aire para Kullki/FitBro/Polla | Forzar el lockup rígido en productos de consumo |

> **En una frase:** el sistema de la Salesiana es el camino correcto para el núcleo de
> la marca; dale a Kullki, FitBro y la Polla un par de centímetros más de aire que a una
> «carrera», porque no le venden al mismo público.

---

## Regenerar el PDF

```bash
pip install weasyprint        # requiere Pango/Cairo en el sistema
python scripts/build-manual.py
# -> docs/Yachay_Deep_Manual_de_Marca_y_Lockups.pdf
```

El generador lee el logo y la paleta desde este repo, así que el manual se mantiene
sincronizado con la marca: si cambia un token o el logo, se regenera y queda al día.
