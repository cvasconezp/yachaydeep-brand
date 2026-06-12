import base64, os
# Generador del Manual de marca y lockups de Yachay Deep Hub.
# Requisitos: pip install weasyprint  (Pango/Cairo en el sistema)
# Uso: python scripts/build-manual.py  -> genera docs/Yachay_Deep_Hub_Manual_de_Marca_y_Lockups.pdf
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
DOCS = os.path.join(ROOT, "docs")
os.makedirs(DOCS, exist_ok=True)

def b64(p):
    return "data:image/png;base64,"+base64.b64encode(open(p,"rb").read()).decode()

LOGO_FULL=b64(os.path.join(ASSETS,"logo-full.png"))
LOGO_DARK=b64(os.path.join(ASSETS,"logo-hero-dark.png"))
LOGO_ICON=b64(os.path.join(ASSETS,"logo-icon.png"))

# Paleta real (tokens)
NAVY="#1B3A6B"; DARK="#0F2444"; LIGHT="#2B5AA0"; GOLD="#E8A838"; GOLDL="#F5C563"
ICE="#A8DCE8"; ICEL="#D8EFF4"

def lockup_rigid(name, modifier):
    return f'''
    <div class="lk">
      <img class="lk-logo" src="{LOGO_FULL}">
      <div class="lk-div"></div>
      <div class="lk-name">
        <div class="lk-prod">{name}</div>
        <div class="lk-mod"><span class="lk-rule"></span>{modifier}</div>
      </div>
    </div>'''

def lockup_soft(name, tagline):
    return f'''
    <div class="lk soft">
      <div class="lk-mark">{name[0]}</div>
      <div class="lk-name">
        <div class="lk-prod soft-prod">{name}</div>
        <div class="lk-endorse">por Yachay Deep Labs</div>
      </div>
    </div>
    <p class="cap">{tagline}</p>'''

HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=Instrument+Sans:wght@400;500;600;700&family=Spline+Sans+Mono:wght@400;500&display=swap');
@page {{ size: A4; margin: 0; }}
@page content {{
  margin: 20mm 18mm 18mm 18mm;
  @bottom-center {{ content: "Yachay Deep Hub · Manual de marca y lockups · v1.0 · 2026"; font-family: 'Spline Sans Mono', monospace; font-size: 7pt; color: #9aa6b2; }}
  @bottom-right {{ content: counter(page); font-family: 'Spline Sans Mono', monospace; font-size: 7pt; color: #9aa6b2; }}
}}
* {{ box-sizing: border-box; }}
body {{ margin:0; font-family:'Instrument Sans', system-ui, sans-serif; color:#23303f; font-size:10.2pt; line-height:1.5; }}
h1,h2,h3 {{ font-family:'Bricolage Grotesque','Instrument Sans',sans-serif; color:{NAVY}; margin:0; }}
.page {{ page: content; padding:0; }}
.brk {{ break-before: page; }}
.eyebrow {{ font-family:'Spline Sans Mono',monospace; font-size:7.5pt; letter-spacing:.22em; text-transform:uppercase; color:{GOLD}; font-weight:600; }}
.h2 {{ font-size:19pt; font-weight:800; margin:2px 0 4px; }}
.lead {{ color:#566372; font-size:10.5pt; margin:0 0 14px; max-width:165mm; }}
.rule {{ height:3px; width:46px; background:{GOLD}; border-radius:2px; margin:10px 0 16px; }}
p {{ margin:0 0 9px; }}
strong {{ color:{NAVY}; }}
.small {{ font-size:9pt; color:#6b7886; }}
.mono {{ font-family:'Spline Sans Mono',monospace; }}

/* COVER */
.cover {{ height:297mm; background:linear-gradient(150deg,{NAVY},{DARK} 60%,{NAVY}); color:#fff; padding:26mm 22mm; position:relative; }}
.cover .logo {{ height:74px; }}
.cover .ttl {{ font-family:'Bricolage Grotesque'; font-weight:800; color:#fff; font-size:38pt; line-height:1.05; margin-top:64mm; }}
.cover .sub {{ color:{ICE}; font-size:15pt; margin-top:8px; max-width:150mm; }}
.cover .tagline {{ margin-top:18px; font-family:'Spline Sans Mono',monospace; font-size:9pt; letter-spacing:.12em; color:{GOLDL}; text-transform:uppercase; }}
.cover .meta {{ position:absolute; bottom:24mm; left:22mm; right:22mm; border-top:2px solid rgba(232,168,56,.5); padding-top:12px; color:{ICE}; font-size:9pt; display:flex; justify-content:space-between; }}
.cover .goldbar {{ position:absolute; top:0; left:0; right:0; height:6px; background:linear-gradient(to right,{NAVY},{GOLD},{GOLDL}); }}

/* LOCKUP COMPONENTS */
.lk {{ display:flex; align-items:center; gap:16px; padding:14px 0; }}
.lk-logo {{ height:58px; }}
.lk-div {{ width:2px; height:54px; background:{NAVY}; opacity:.85; }}
.lk-name {{ display:flex; flex-direction:column; }}
.lk-prod {{ font-family:'Bricolage Grotesque'; font-weight:700; color:{NAVY}; font-size:20pt; line-height:1.05; }}
.lk-mod {{ font-family:'Spline Sans Mono',monospace; font-size:7.5pt; letter-spacing:.18em; text-transform:uppercase; color:{LIGHT}; margin-top:6px; display:flex; align-items:center; gap:8px; }}
.lk-rule {{ display:inline-block; width:26px; height:1.5px; background:{LIGHT}; }}
.lk.soft {{ gap:14px; }}
.lk-mark {{ width:52px; height:52px; border-radius:14px; background:linear-gradient(135deg,{NAVY},{DARK}); color:{GOLDL}; font-family:'Bricolage Grotesque'; font-weight:800; font-size:24pt; display:flex; align-items:center; justify-content:center; }}
.soft-prod {{ font-size:19pt; }}
.lk-endorse {{ font-family:'Spline Sans Mono',monospace; font-size:7pt; letter-spacing:.16em; text-transform:uppercase; color:#8a97a5; margin-top:4px; }}
.cap {{ font-size:8.6pt; color:#6b7886; margin:2px 0 0; }}

.box {{ border:1px solid #e3e8ee; border-radius:12px; padding:16px 18px; margin:10px 0; }}
.box.tint {{ background:#f6f9fc; }}
.box.gold {{ background:#fdf6e6; border-color:#f0dca8; }}
.lbl {{ font-family:'Spline Sans Mono',monospace; font-size:7.5pt; letter-spacing:.14em; text-transform:uppercase; color:{GOLD}; font-weight:600; margin-bottom:8px; }}
.cols {{ display:flex; gap:14px; }}
.col {{ flex:1; }}
.ok {{ color:#1E7E34; font-weight:700; }} .no {{ color:#B02A2A; font-weight:700; }}

/* arquitectura */
.tier {{ display:flex; align-items:center; gap:14px; border:1px solid #e3e8ee; border-radius:12px; padding:12px 16px; margin:8px 0; }}
.tier .tg {{ width:8px; align-self:stretch; border-radius:6px; }}
.tier h3 {{ font-size:12.5pt; }}
.tier p {{ margin:2px 0 0; }}

/* paleta */
.sw {{ display:flex; gap:10px; flex-wrap:wrap; }}
.chip {{ width:78px; }}
.chip .col-box {{ height:46px; border-radius:8px; border:1px solid rgba(0,0,0,.06); }}
.chip .nm {{ font-family:'Spline Sans Mono',monospace; font-size:7pt; margin-top:4px; color:#566372; }}
.chip .hx {{ font-family:'Spline Sans Mono',monospace; font-size:7pt; color:#9aa6b2; }}

table {{ width:100%; border-collapse:collapse; font-size:9pt; margin:6px 0; }}
th {{ background:{NAVY}; color:#fff; text-align:left; padding:7px 9px; font-weight:600; font-size:8.5pt; }}
td {{ border:1px solid #e3e8ee; padding:7px 9px; vertical-align:top; }}
.clearspace {{ position:relative; display:inline-block; padding:26px; background:repeating-linear-gradient(45deg,#f1f5f9,#f1f5f9 6px,#fff 6px,#fff 12px); border:1px dashed {GOLD}; border-radius:10px; }}
.clearspace img {{ height:52px; display:block; }}
.note {{ font-size:8.6pt; color:#6b7886; }}
</style></head><body>

<!-- COVER -->
<div class="cover">
  <div class="goldbar"></div>
  <img class="logo" src="{LOGO_DARK}">
  <div class="ttl">Sistema de marca<br>y lockups</div>
  <div class="sub">Arquitectura de marca endosada para Yachay Deep Hub y sus productos</div>
  <div class="tagline">Convertimos datos en conocimiento — en el aula, en la empresa y en la comunidad</div>
  <div class="meta"><span>Manual de marca · v1.0</span><span>Junio 2026 · Yachay Deep Hub</span></div>
</div>

<!-- 1. FILOSOFÍA -->
<div class="page">
  <div class="eyebrow">01 · Punto de partida</div>
  <div class="h2">Una casa, muchos productos</div>
  <div class="rule"></div>
  <p>Yachay Deep dejó de ser un solo producto educativo para convertirse en <strong>Yachay Deep Hub</strong>: una casa de productos digitales e inteligencia aplicada. Es el mismo camino de <strong>Facebook → Meta</strong> — la marca crece más allá de su origen y se crea un nivel-empresa que da espacio a todo lo nuevo, sin perder lo construido.</p>
  <p>El reto de marca es el de cualquier casa con varios productos: <strong>conectar sin uniformar</strong>. Que un cliente reconozca el respaldo de Yachay Deep en Core, Kullki o FitBro, pero que cada producto pueda hablarle a su propio público.</p>
  <div class="box gold">
    <div class="lbl">El modelo de referencia</div>
    <p style="margin:0">La Universidad Politécnica Salesiana resuelve esto con un <strong>sistema de lockups endosados</strong>: un logo madre fijo + el nombre de cada carrera + un modificador (sede o modalidad). Yachay Deep adopta esa misma lógica, adaptada a productos en vez de carreras.</p>
  </div>
  <table>
    <tr><th>UPS (referencia)</th><th>Yachay Deep Hub (equivalente)</th></tr>
    <tr><td>Logo madre UPS (fijo)</td><td>Logo madre Yachay Deep (iceberg + wordmark)</td></tr>
    <tr><td>Nombre de la carrera</td><td>Nombre del producto / unidad</td></tr>
    <tr><td>Modificador: «Sede Quito» / «En línea»</td><td>Modificador: sector, estado o «por Yachay Deep Labs»</td></tr>
  </table>
</div>

<!-- 2. ARQUITECTURA -->
<div class="page brk">
  <div class="eyebrow">02 · Arquitectura de marca</div>
  <div class="h2">Tres niveles</div>
  <div class="rule"></div>
  <p class="lead">La decisión adoptada es una arquitectura <strong>híbrida con endoso</strong>: marca madre fuerte, con endoso disciplinado en el núcleo y un poco más de aire en los productos de consumo.</p>

  <div class="tier"><div class="tg" style="background:{NAVY}"></div><div><h3>Nivel 1 — Marca madre</h3><p><strong>Yachay Deep Hub.</strong> La empresa. Su logo y nombre encabezan todo. Casi nunca aparece sola al público: aparece <em>endosando</em> a un producto.</p></div></div>
  <div class="tier"><div class="tg" style="background:{LIGHT}"></div><div><h3>Nivel 2 — Núcleo (endoso fuerte)</h3><p><strong>Core · Academy · Studio · Research.</strong> Viven de la confianza institucional. Usan <strong>lockup rígido</strong> con el logo madre, igual que una carrera de la UPS.</p></div></div>
  <div class="tier"><div class="tg" style="background:{GOLD}"></div><div><h3>Nivel 3 — Productos de consumo (endoso ligero)</h3><p><strong>Kullki · FitBro · Polla Mundialista.</strong> Le hablan a públicos distintos (comunidad, deporte, entretenimiento). Tienen <strong>identidad propia</strong> + el sello «por Yachay Deep Labs».</p></div></div>

  <div class="box tint"><p style="margin:0" class="small"><strong>Regla de oro:</strong> a mayor cercanía con la venta institucional (universidades, instituciones), más rígido el lockup. A mayor cercanía con el consumidor final, más aire para la marca propia — pero el endoso nunca desaparece.</p></div>
</div>

<!-- 3. ANATOMÍA -->
<div class="page brk">
  <div class="eyebrow">03 · Anatomía del lockup</div>
  <div class="h2">Las cuatro partes</div>
  <div class="rule"></div>
  <p class="lead">Todo lockup del núcleo se construye con las mismas cuatro piezas, en este orden y alineación.</p>
  <div class="box">
    {lockup_rigid("Core", "para educación superior")}
  </div>
  <table>
    <tr><th>#</th><th>Pieza</th><th>Regla</th></tr>
    <tr><td>1</td><td><strong>Logo madre</strong></td><td>Iceberg + wordmark «Yachay Deep». Nunca se altera, recolorea ni reproporciona.</td></tr>
    <tr><td>2</td><td><strong>Divisor</strong></td><td>Línea vertical navy, de la misma altura que el wordmark. Separa marca madre y producto.</td></tr>
    <tr><td>3</td><td><strong>Nombre del producto</strong></td><td>Tipografía display (Bricolage Grotesque), navy. 1–2 líneas.</td></tr>
    <tr><td>4</td><td><strong>Modificador</strong></td><td>Mono, mayúsculas, con regla corta a la izquierda. Sector, modalidad o estado. Opcional.</td></tr>
  </table>
  <div class="box tint">
    <div class="lbl">Área de protección y tamaño mínimo</div>
    <div class="cols" style="align-items:center">
      <div class="col" style="flex:0 0 auto"><span class="clearspace"><img src="{LOGO_FULL}"></span></div>
      <div class="col">
        <p style="margin:0 0 6px"><strong>Área de protección = altura del iceberg (X).</strong> Mantén al menos 1X de espacio libre alrededor de todo el lockup. Nada invade esa zona.</p>
        <p style="margin:0" class="small"><strong>Tamaño mínimo:</strong> el wordmark «Yachay Deep» nunca por debajo de <span class="mono">22&nbsp;px</span> de alto en pantalla / <span class="mono">16&nbsp;mm</span> impreso. Por debajo, usar solo el icono.</p>
      </div>
    </div>
  </div>
</div>

<!-- 4. MODO A -->
<div class="page brk">
  <div class="eyebrow">04 · Modo A</div>
  <div class="h2">Lockup rígido — endoso fuerte</div>
  <div class="rule"></div>
  <p class="lead">Para el núcleo: <strong>Core, Academy, Studio, Research</strong>. Mismo logo, mismo divisor, misma tipografía. Solo cambian el nombre y el modificador — como las carreras de la UPS.</p>
  <div class="box">
    {lockup_rigid("Core", "para educación superior")}
    {lockup_rigid("Academy", "formación · en línea")}
    {lockup_rigid("Studio", "consultoría · transformación digital")}
    {lockup_rigid("Research", "investigación aplicada")}
  </div>
  <div class="cols">
    <div class="col box"><div class="lbl" style="color:#1E7E34">Hacer</div>
      <p class="small" style="margin:0">Alinear verticalmente al centro · respetar el divisor · nombre siempre en navy sobre fondo claro · modificador opcional pero consistente.</p></div>
    <div class="col box"><div class="lbl" style="color:#B02A2A">No hacer</div>
      <p class="small" style="margin:0">Cambiar la tipografía del nombre · poner el nombre en dorado · omitir el logo madre · inventar un divisor distinto.</p></div>
  </div>
</div>

<!-- 5. MODO B -->
<div class="page brk">
  <div class="eyebrow">05 · Modo B</div>
  <div class="h2">Identidad propia endosada — endoso ligero</div>
  <div class="rule"></div>
  <p class="lead">Para productos de consumo: <strong>Kullki, FitBro, Polla Mundialista</strong>. Marca propia con personalidad, conectada por un sello discreto «por Yachay Deep Labs». No le venden al mismo público que Core, así que necesitan aire.</p>
  <div class="cols">
    <div class="col box">{lockup_soft("Kullki","Caja de ahorro comunitaria · tono kichwa, cálido")}</div>
    <div class="col box">{lockup_soft("FitBro","Deporte y bienestar · tono enérgico")}</div>
  </div>
  <div class="cols">
    <div class="col box">{lockup_soft("Polla Mundialista","Entretenimiento · producto licenciado a terceros")}</div>
    <div class="col box tint"><div class="lbl">Cuándo usar Modo B</div><p class="small" style="margin:0">Cuando el producto le habla a un público distinto del institucional y una estética «universidad» le restaría cercanía. La marca respira; el endoso permanece.</p></div>
  </div>
  <p class="note">Nota: los recuadros con inicial son ejemplos de marcador de posición. Cada producto puede desarrollar su propio wordmark; lo invariable es el endoso «por Yachay Deep Labs».</p>
</div>

<!-- 6. EL SELLO -->
<div class="page brk">
  <div class="eyebrow">06 · El sello de endoso</div>
  <div class="h2">«por Yachay Deep Labs»</div>
  <div class="rule"></div>
  <p class="lead">El hilo que conecta toda la casa. Discreto pero presente en cada producto del Nivel 3.</p>
  <table>
    <tr><th>Aspecto</th><th>Regla</th></tr>
    <tr><td>Texto</td><td><span class="mono">por Yachay Deep Labs</span> (productos de Labs) · <span class="mono">por Yachay Deep</span> (resto)</td></tr>
    <tr><td>Tipografía</td><td>Mono (Spline Sans Mono), mayúsculas, tracking amplio</td></tr>
    <tr><td>Tamaño</td><td>Pequeño: ~55–65% del cuerpo. Acompaña, no compite</td></tr>
    <tr><td>Color</td><td>Gris medio sobre claro · hielo ({ICE}) sobre navy</td></tr>
    <tr><td>Posición</td><td>Bajo el nombre del producto, o al pie de la pieza</td></tr>
  </table>
  <div class="box tint"><div class="lbl">Ya implementado en el sitio</div><p class="small" style="margin:0">En <span class="mono">yachaydeep.com/labs</span> cada tarjeta de producto lleva el sello «POR YACHAY DEEP LABS» (Core no lo lleva: es la marca insignia, va con lockup rígido).</p></div>
</div>

<!-- 7. PALETA Y TIPOGRAFÍA -->
<div class="page brk">
  <div class="eyebrow">07 · Fundamentos</div>
  <div class="h2">Paleta y tipografía</div>
  <div class="rule"></div>
  <p class="small">Fuente única de verdad: <span class="mono">@yachaydeep/brand</span>. Estos tokens no se editan en cada pieza; se cambian en el paquete y se propagan.</p>
  <div class="sw" style="margin:12px 0 4px">
    <div class="chip"><div class="col-box" style="background:{NAVY}"></div><div class="nm">brand</div><div class="hx">{NAVY}</div></div>
    <div class="chip"><div class="col-box" style="background:{DARK}"></div><div class="nm">brand-dark</div><div class="hx">{DARK}</div></div>
    <div class="chip"><div class="col-box" style="background:{LIGHT}"></div><div class="nm">brand-light</div><div class="hx">{LIGHT}</div></div>
    <div class="chip"><div class="col-box" style="background:{GOLD}"></div><div class="nm">brand-gold</div><div class="hx">{GOLD}</div></div>
    <div class="chip"><div class="col-box" style="background:{GOLDL}"></div><div class="nm">gold-light</div><div class="hx">{GOLDL}</div></div>
    <div class="chip"><div class="col-box" style="background:{ICE}"></div><div class="nm">brand-ice</div><div class="hx">{ICE}</div></div>
    <div class="chip"><div class="col-box" style="background:{ICEL}"></div><div class="nm">ice-light</div><div class="hx">{ICEL}</div></div>
  </div>
  <p class="small"><strong>Dorado = solo acción y acento</strong> (CTAs, eyebrows, métricas, barra de tarjeta). Nunca como fondo extenso. En lockups, el nombre del producto va en navy, nunca en dorado.</p>
  <div class="box">
    <div class="lbl">Tipografía</div>
    <p style="font-family:'Bricolage Grotesque';font-size:17pt;color:{NAVY};margin:0 0 2px">Bricolage Grotesque — Display</p>
    <p class="small" style="margin:0 0 10px">Titulares, héroes y <strong>nombres de producto</strong> en lockups. Pesos 600–800.</p>
    <p style="font-size:12pt;margin:0 0 2px">Instrument Sans — Cuerpo</p>
    <p class="small" style="margin:0 0 10px">Texto e interfaz. Pesos 400–700.</p>
    <p class="mono" style="font-size:11pt;margin:0 0 2px">Spline Sans Mono — Datos</p>
    <p class="small" style="margin:0">Modificadores, sello de endoso, datos, handles. Pesos 400–500.</p>
  </div>
</div>

<!-- 8. USO -->
<div class="page brk">
  <div class="eyebrow">08 · Usos</div>
  <div class="h2">Correcto e incorrecto</div>
  <div class="rule"></div>
  <table>
    <tr><th style="width:50%">Sí <span style="color:#bfe3c8">✓</span></th><th>No <span style="color:#f3c2c2">✕</span></th></tr>
    <tr><td>Logo madre intacto en todo lockup del núcleo</td><td>Recolorear, estirar o rotar el logo</td></tr>
    <tr><td>Nombre de producto en navy, tipografía display</td><td>Nombre de producto en dorado</td></tr>
    <tr><td>Dorado solo para acción/acento</td><td>Fondos extensos dorados</td></tr>
    <tr><td>Endoso «por Yachay Deep Labs» discreto y consistente</td><td>Endoso del mismo tamaño que el nombre</td></tr>
    <tr><td>Respetar 1X de área de protección</td><td>Texto u otros logos invadiendo el lockup</td></tr>
    <tr><td>Modo B con aire para Kullki/FitBro/Polla</td><td>Forzar el lockup rígido en productos de consumo</td></tr>
  </table>
  <div class="box gold">
    <div class="lbl">En una frase</div>
    <p style="margin:0">El sistema de la Salesiana es el camino correcto para el núcleo de la marca; dale a Kullki, FitBro y la Polla un par de centímetros más de aire que a una «carrera», porque no le venden al mismo público.</p>
  </div>
  <p class="note" style="margin-top:14px">Este manual extiende —no reemplaza— el <span class="mono">STYLE-GUIDE.md</span> del paquete <span class="mono">@yachaydeep/brand</span>, que cubre patrones de UI, componentes y voz.</p>
</div>

</body></html>'''

open(os.path.join(DOCS,"manual.html"),"w",encoding="utf-8").write(HTML)
from weasyprint import HTML as WP
WP(filename=os.path.join(DOCS,"manual.html")).write_pdf(os.path.join(DOCS,"Yachay_Deep_Hub_Manual_de_Marca_y_Lockups.pdf"))
print("PDF OK", os.path.getsize(os.path.join(DOCS,"Yachay_Deep_Hub_Manual_de_Marca_y_Lockups.pdf")), "bytes")
