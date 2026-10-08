#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del sitio de Estudio J, C & S.

    python3 tools/build.py

Lee el contenido de tools/contenido_*.py y escribe el sitio completo en sitio/
(HTML, sitemap.xml y robots.txt). La carpeta sitio/ es la que se sube al hosting.
"""

import json
import os
import re
import sys
from datetime import date
from html import escape as e

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contenido_servicios import AREAS, SERVICIOS, MOTIVOS, FAQ_INICIO  # noqa: E402
from contenido_articulos import ARTICULOS, CATEGORIAS  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sitio")
VERSION = date.today().strftime("%Y%m%d")

# ---------------------------------------------------------------------------
# Configuración general
# ---------------------------------------------------------------------------
SITE = "https://estudiojcs.com.ar"
ESTUDIO = {
    "nombre": "Estudio J, C & S",
    "razon": "Jaikin, Carabajal & Santoro",
    "email": "info@estudiojcs.com.ar",
    "telefonos": [("+54 9 11 5178-5782", "+5491151785782"), ("+54 9 11 2296-1982", "+5491122961982")],
    "horario": "Lunes a viernes de 9:00 a 17:00 hs.",
    "whatsapp": "5491151785782",
    "whatsapp_texto": "Hola, quisiera realizar una consulta jurídica.",
}
# ID de Google Tag Manager (por ejemplo "GTM-XXXXXXX"). Vacío = sin analítica.
GTM_ID = ""
# Foto del hero: dejá None para usar la composición tipográfica, o indicá la
# ruta a una imagen .webp (por ejemplo "/assets/img/hero.webp").
HERO_FOTO = None

WA = "https://wa.me/{}?text={}".format(
    ESTUDIO["whatsapp"], "Hola%2C%20quisiera%20realizar%20una%20consulta%20jur%C3%ADdica.")

# Equipo (página El Estudio). Para sumar integrantes, agregá elementos.
# Los textos entre corchetes son espacios a completar por el estudio.
EQUIPO = [
    {"nombre": "[Nombre] Jaikin", "cargo": "[Cargo]", "area": "[Especialización]",
     "bio": "[Breve descripción profesional.]", "foto": "/assets/img/equipo/jaikin.svg", "linkedin": ""},
    {"nombre": "[Nombre] Carabajal", "cargo": "[Cargo]", "area": "[Especialización]",
     "bio": "[Breve descripción profesional.]", "foto": "/assets/img/equipo/carabajal.svg", "linkedin": ""},
    {"nombre": "[Nombre] Santoro", "cargo": "[Cargo]", "area": "[Especialización]",
     "bio": "[Breve descripción profesional.]", "foto": "/assets/img/equipo/santoro.svg", "linkedin": ""},
]

PROCESO = [
    ("Escuchamos", "Nos contás qué pasó y qué necesitás lograr."),
    ("Analizamos", "Revisamos la documentación, los riesgos y las alternativas posibles."),
    ("Definimos la estrategia", "Te explicamos las opciones y los pasos a seguir, con claridad."),
    ("Acompañamos", "Seguimiento cercano y comunicación directa durante todo el proceso."),
]

DISCLAIMER = "La información de esta página es general y no reemplaza el análisis profesional de cada caso."

# ---------------------------------------------------------------------------
# URLs
# ---------------------------------------------------------------------------
def url_area(k):
    return "/{}/".format(AREAS[k]["slug"])


def url_servicio(slug):
    return "/{}/".format(slug)


def url_articulo(slug):
    return "/informacion-juridica/{}/".format(slug)


def url_categoria(slug):
    return "/informacion-juridica/categoria/{}/".format(slug)


ART_BY_SLUG = {a["slug"]: a for a in ARTICULOS}


def enlazar(html):
    """Resuelve {{s:slug|texto}} y {{a:slug|texto}} en enlaces internos."""
    def rep(m):
        kind, slug, text = m.group(1), m.group(2), m.group(3)
        if kind == "s":
            assert slug in SERVICIOS, slug
            href = url_servicio(slug)
        else:
            assert slug in ART_BY_SLUG, slug
            href = url_articulo(slug)
        return '<a href="{}">{}</a>'.format(href, text)
    return re.sub(r"\{\{([sa]):([a-z0-9-]+)\|([^}]+)\}\}", rep, html)


# ---------------------------------------------------------------------------
# Íconos
# ---------------------------------------------------------------------------
ARROW = '<svg class="i-arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
WA_ICON = '<svg class="i-wa" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.26-.47-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.42-.08-.12-.27-.2-.57-.34zM12.05 21.79h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.83 9.83 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.88 9.88zm8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.69 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.17-3.49-8.42z"/></svg>'
PHONE_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>'
MAIL_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M3.5 6l8.5 7 8.5-7" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>'
CLOCK_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
LI_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M7 10v7M7 7v.01M11 17v-4a2 2 0 0 1 4 0v4M11 10v7" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'


def logo(cls=""):
    return ('<span class="logo {cls}"><span class="logo__mono" aria-hidden="true">'
            '<b>J</b><i></i><b>C</b><i></i><b>S</b></span>'
            '<span class="logo__text"><span class="logo__studio">Estudio Jurídico</span>'
            '<span class="logo__name">Jaikin, Carabajal &amp; Santoro</span></span></span>').format(cls=cls)


def monograma():
    return ('<div class="monogram" aria-hidden="true"><div class="monogram__row">'
            '<span class="monogram__l">J</span><span class="monogram__rules"></span>'
            '<span class="monogram__l">C</span><span class="monogram__rules"></span>'
            '<span class="monogram__l">S</span></div>'
            '<span class="monogram__name">Jaikin, Carabajal &amp; Santoro</span></div>')


def tel_links(sep="<br>"):
    return sep.join('<a href="tel:{}" data-track="telefono">{}</a>'.format(t, e(l)) for l, t in ESTUDIO["telefonos"])


def low(n):
    """Pasa a minúsculas respetando siglas."""
    out = n.lower()
    for sig in ("SAS", "SRL", "ART"):
        out = re.sub(r"\b{}\b".format(sig.lower()), sig, out)
    return out


def btn(href, text, kind="primary", arrow=True, extra=""):
    return '<a class="btn btn--{}" href="{}"{}>{}{}</a>'.format(kind, href, extra, e(text), " " + ARROW if arrow else "")


def btn_wa(text="Hablar por WhatsApp", kind="wa"):
    return '<a class="btn btn--{}" href="{}" target="_blank" rel="noopener" data-track="whatsapp">{} {}</a>'.format(kind, WA, WA_ICON, e(text))


def consultar(motivo=None, text="Consultar ahora", kind="primary"):
    extra = ' data-motivo="{}"'.format(e(motivo)) if motivo else ""
    return btn("#contacto", text, kind, extra=extra)


# ---------------------------------------------------------------------------
# Datos estructurados
# ---------------------------------------------------------------------------
def schema_estudio():
    return {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "@id": SITE + "/#estudio",
        "name": ESTUDIO["nombre"],
        "alternateName": ["Estudio JCS", ESTUDIO["razon"]],
        "description": "Estudio jurídico en Buenos Aires. Derecho Civil y Comercial, Laboral, de Familia y Consorcios y Expensas. Atención personalizada para personas, empresas, emprendedores y consorcios.",
        "url": SITE + "/",
        "logo": SITE + "/assets/img/logo.png",
        "image": SITE + "/assets/img/og-image.jpg",
        "email": ESTUDIO["email"],
        "telephone": ESTUDIO["telefonos"][0][1],
        "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "Ciudad Autónoma de Buenos Aires",
                    "addressRegion": "Buenos Aires", "addressCountry": "AR"},
        "areaServed": [{"@type": "City", "name": "Ciudad Autónoma de Buenos Aires"},
                       {"@type": "State", "name": "Provincia de Buenos Aires"}],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "09:00", "closes": "17:00"}],
        "contactPoint": [{"@type": "ContactPoint", "telephone": t, "contactType": "customer service",
                          "areaServed": "AR", "availableLanguage": "es"} for _, t in ESTUDIO["telefonos"]],
        "knowsAbout": [s.get("nombre_largo", s["nombre"]) for s in SERVICIOS.values()],
    }


def schema_faq(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def schema_breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
                                for i, (n, u) in enumerate(items)]}


def schema_servicio(nombre, desc, path, tipo):
    return {"@context": "https://schema.org", "@type": "Service", "name": nombre, "serviceType": tipo,
            "description": desc, "url": SITE + path, "provider": {"@id": SITE + "/#estudio"},
            "areaServed": {"@type": "City", "name": "Buenos Aires"}}


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
def head(p):
    url = SITE + p["path"]
    robots = "noindex, follow" if p.get("noindex") else "index, follow, max-image-preview:large"
    schemas = "\n  ".join('<script type="application/ld+json">{}</script>'.format(
        json.dumps(s, ensure_ascii=False, separators=(",", ":"))) for s in p.get("schemas", []))
    gtm = ""
    if GTM_ID:
        gtm = ("<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});"
               "var f=d.getElementsByTagName(s)[0],j=d.createElement(s);j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i;"
               "f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{}');</script>").format(GTM_ID)
    og_type = "article" if p.get("article") else "website"
    extra_og = ""
    if p.get("article"):
        extra_og = '<meta property="article:published_time" content="{}">'.format(p["article"])
    return """<!doctype html>
<html lang="es-AR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#0d1726">
  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="es_AR">
  <meta property="og:site_name" content="Estudio J, C &amp; S">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{site}/assets/img/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  {extra_og}
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="preload" href="/assets/fonts/bodoni-moda.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/hanken-grotesk.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/css/styles.css?v={v}">
  <script>document.documentElement.classList.add('js');</script>
  <script src="/assets/js/main.js?v={v}" defer></script>
  {gtm}
  {schemas}
</head>""".format(title=e(p["title"]), desc=e(p["description"]), robots=robots, url=url, og_type=og_type,
                   site=SITE, extra_og=extra_og, v=VERSION, gtm=gtm, schemas=schemas)


def nav_html(current):
    items = []
    items.append('<li><a href="/"{}>Inicio</a></li>'.format(' aria-current="page"' if current == "inicio" else ""))
    for k in ["civil", "laboral", "familia", "consorcios"]:
        a = AREAS[k]
        subs = list(a["servicios"])
        if a.get("destacado"):
            subs.insert(subs.index("constitucion-de-sociedades") + 1, a["destacado"])
        sub = "".join('<li><a href="{}">{}</a></li>'.format(url_servicio(s), e(SERVICIOS[s].get("nombre_largo", SERVICIOS[s]["nombre"]))) for s in subs)
        cur = ' aria-current="page"' if current == k else ""
        items.append(
            '<li class="has-sub"><a href="{u}"{cur}>{n}</a>'
            '<div class="sub"><ul><li class="sub__all"><a href="{u}">Ver {n}</a></li>{sub}</ul></div></li>'.format(
                u=url_area(k), cur=cur, n=e(a["menu"]), sub=sub))
    items.append('<li><a href="/el-estudio/"{}>El Estudio</a></li>'.format(' aria-current="page"' if current == "estudio" else ""))
    items.append('<li><a href="/contacto/"{}>Contacto</a></li>'.format(' aria-current="page"' if current == "contacto" else ""))
    return "".join(items)


def mobile_nav():
    blocks = ['<li><a class="m-top" href="/">Inicio</a></li>']
    for k in ["civil", "laboral", "familia", "consorcios"]:
        a = AREAS[k]
        subs = list(a["servicios"]) + ([a["destacado"]] if a.get("destacado") else [])
        sub = "".join('<li><a href="{}">{}</a></li>'.format(url_servicio(s), e(SERVICIOS[s].get("nombre_largo", SERVICIOS[s]["nombre"]))) for s in subs)
        blocks.append('<li><a class="m-top" href="{}">{}</a><ul class="m-sub">{}</ul></li>'.format(url_area(k), e(a["menu"]), sub))
    blocks.append('<li><a class="m-top" href="/el-estudio/">El Estudio</a></li>')
    blocks.append('<li><a class="m-top" href="/informacion-juridica/">Información jurídica</a></li>')
    blocks.append('<li><a class="m-top" href="/contacto/">Contacto</a></li>')
    return "".join(blocks)


def header(p):
    gtm_ns = ""
    if GTM_ID:
        gtm_ns = '<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'.format(GTM_ID)
    return """<body>
{gtm_ns}
<a class="skip-link" href="#contenido">Saltar al contenido</a>
<div class="topbar">
  <div class="container topbar__inner">
    <span>{horario}</span>
    <ul>
      <li><a href="tel:{t1}" data-track="telefono">{p1}</a></li>
      <li><a href="tel:{t2}" data-track="telefono">{p2}</a></li>
      <li><a href="mailto:{email}" data-track="email">{email}</a></li>
      <li><a href="/informacion-juridica/">Información jurídica</a></li>
    </ul>
  </div>
</div>
<header class="header" data-header>
  <div class="container header__inner">
    <a class="header__brand" href="/" aria-label="Estudio J, C &amp; S — Inicio">{logo}</a>
    <nav class="nav" aria-label="Principal"><ul class="nav__list">{nav}</ul></nav>
    <div class="header__actions">
      <a class="btn btn--primary btn--sm" href="{cta}">Consultar ahora</a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu-movil" aria-label="Abrir menú" data-menu-btn><span><i></i><i></i><i></i></span></button>
    </div>
  </div>
</header>
<div class="mobile-nav" id="menu-movil" data-mobile-nav>
  <nav aria-label="Menú móvil"><ul class="m-list">{mnav}</ul></nav>
  <div class="mobile-nav__cta">
    <a class="btn btn--primary btn--block" href="{cta}">Consultar ahora {arrow}</a>
    {wa}
  </div>
  <div class="mobile-nav__contact">{tels}<a href="mailto:{email}">{email}</a><span>{horario}</span></div>
</div>
<main id="contenido">""".format(
        gtm_ns=gtm_ns, horario=e(ESTUDIO["horario"]), t1=ESTUDIO["telefonos"][0][1], p1=ESTUDIO["telefonos"][0][0],
        t2=ESTUDIO["telefonos"][1][1], p2=ESTUDIO["telefonos"][1][0], email=ESTUDIO["email"], logo=logo(),
        nav=nav_html(p.get("current")), mnav=mobile_nav(), arrow=ARROW, wa=btn_wa("WhatsApp", "wa btn--block"),
        tels=tel_links(""), cta="/contacto/" if p.get("noform") else "#contacto",
    )


def footer(p):
    areas = "".join('<li><a href="{}">{}</a></li>'.format(url_area(k), e(AREAS[k]["nombre"])) for k in AREAS)
    servicios = "".join('<li><a href="{}">{}</a></li>'.format(url_servicio(s), e(SERVICIOS[s].get("nombre_largo", SERVICIOS[s]["nombre"])))
                        for s in ["accidentes-de-transito", "seguros", "danos-y-perjuicios", "constitucion-de-sas",
                                  "despidos", "art-accidentes-de-trabajo", "sucesiones", "cobro-de-expensas"])
    return """</main>
<section class="footer-cta is-dark" aria-labelledby="fcta">
  <div class="container footer-cta__inner">
    <div>
      <p class="kicker">Contanos tu caso</p>
      <h2 id="fcta">¿Necesitás asesoramiento jurídico? <em>Hablemos.</em></h2>
    </div>
    <div class="btn-row">{c1}{c2}</div>
  </div>
</section>
<footer class="footer">
  <div class="container footer__grid">
    <div class="footer__brand">
      <a href="/" aria-label="Inicio">{logo}</a>
      <p>Derecho Civil y Comercial · Laboral · Familia · Consorcios y Expensas</p>
      <p>Buenos Aires, Argentina</p>
    </div>
    <div>
      <p class="footer__title">Contacto</p>
      <ul>
        <li>{tels}</li>
        <li><a href="mailto:{email}" data-track="email">{email}</a></li>
        <li>{horario}</li>
        <li><a href="{wa}" target="_blank" rel="noopener" data-track="whatsapp">WhatsApp</a></li>
      </ul>
    </div>
    <div>
      <p class="footer__title">Áreas</p>
      <ul>{areas}<li><a href="/el-estudio/">El Estudio</a></li></ul>
    </div>
    <div>
      <p class="footer__title">Servicios</p>
      <ul>{servicios}</ul>
    </div>
    <div>
      <p class="footer__title">Información jurídica</p>
      <ul>{cats}</ul>
    </div>
  </div>
  <div class="container footer__legal">
    <span>© <span data-year>{year}</span> Estudio J, C &amp; S — Jaikin, Carabajal &amp; Santoro. Todos los derechos reservados.</span>
    <span><a href="/politica-de-privacidad/">Política de Privacidad</a> · <a href="/contacto/">Contacto</a></span>
  </div>
</footer>
<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="Escribinos por WhatsApp" data-track="whatsapp">{wa_icon}<span>Consultanos</span></a>
</body>
</html>
""".format(
        c1=btn("/contacto/" if p.get("noform") else "#contacto", "Consultar ahora", "light"), c2=btn_wa("Hablar con un abogado"), logo=logo("logo--light"),
        tels=tel_links(), email=ESTUDIO["email"], horario=e(ESTUDIO["horario"]), wa=WA, areas=areas,
        servicios=servicios, cats="".join('<li><a href="{}">{}</a></li>'.format(url_categoria(k), e(c["nombre"])) for k, c in CATEGORIAS.items()),
        year=date.today().year, wa_icon=WA_ICON,
    )


# ---------------------------------------------------------------------------
# Componentes
# ---------------------------------------------------------------------------
def breadcrumb(items):
    out = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            out.append('<li aria-current="page">{}</li>'.format(e(n)))
        else:
            out.append('<li><a href="{}">{}</a></li>'.format(u, e(n)))
    return '<nav aria-label="Ruta de navegación"><ol class="breadcrumb">{}</ol></nav>'.format("".join(out))


def page_hero(crumbs, kicker, h1, lead, actions, aside=""):
    return """<section class="page-hero">
  <div class="container">
    {bc}
    <div class="page-hero__grid">
      <div>
        <p class="kicker">{kicker}</p>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
        <div class="btn-row">{actions}</div>
      </div>
      {aside}
    </div>
  </div>
</section>""".format(bc=breadcrumb(crumbs), kicker=e(kicker), h1=h1, lead=e(lead), actions=actions, aside=aside)


def hero_aside():
    return """<aside class="quick-card" aria-label="Contacto rápido">
        <p class="quick-card__title">Hablá con un abogado</p>
        <ul>
          <li>{phone}<span>{tels}</span></li>
          <li>{clock}<span>{horario}</span></li>
        </ul>
        {wa}
      </aside>""".format(phone=PHONE_ICON, tels=tel_links(), clock=CLOCK_ICON, horario=e(ESTUDIO["horario"]),
                         wa=btn_wa("Escribinos por WhatsApp", "wa btn--block"))


def faq_block(faqs, title="Preguntas frecuentes", h2_id="faq"):
    items = "".join(
        '<details class="faq__item reveal"><summary><h3>{}</h3></summary><div class="faq__a"><p>{}</p></div></details>'.format(e(q), e(a))
        for q, a in faqs)
    return """<section class="section" aria-labelledby="{id}">
  <div class="container faq-layout">
    <div class="section-head">
      <p class="kicker reveal">Preguntas frecuentes</p>
      <h2 id="{id}" class="reveal">{title}</h2>
      <p class="note reveal">{disc}</p>
      <div class="reveal" style="margin-top:28px">{btn}</div>
    </div>
    <div class="faq">{items}</div>
  </div>
</section>""".format(id=h2_id, title=title, disc=DISCLAIMER, items=items, btn=btn("#contacto", "Hacer una consulta", "outline"))


def cta_band(titulo, texto, acciones, dark=False):
    return """<div class="cta-band{d} reveal">
  <div><p class="cta-band__title">{t}</p><p>{x}</p></div>
  <div class="btn-row">{a}</div>
</div>""".format(d=" cta-band--dark" if dark else "", t=titulo, x=e(texto), a=acciones)


def proceso_block(pasos=None, titulo="Cómo trabajamos", kicker="Nuestro método", dark=True):
    pasos = pasos or PROCESO
    li = "".join('<li class="step reveal"><span class="step__n">{:02d}</span><h3>{}</h3><p>{}</p></li>'.format(i + 1, e(t), e(d))
                 for i, (t, d) in enumerate(pasos))
    return """<section class="section{d}" aria-labelledby="proc">
  <div class="container">
    <div class="section-head"><p class="kicker reveal">{k}</p><h2 id="proc" class="reveal">{t}</h2></div>
    <ol class="steps">{li}</ol>
  </div>
</section>""".format(d=" is-dark" if dark else "", k=e(kicker), t=titulo, li=li)


def form_block(motivo=None, titulo="Contanos tu caso", lead="Completá el formulario y un abogado del estudio va a revisar tu consulta. También podés escribirnos por WhatsApp.", h_tag="h2"):
    opts = ['<option value="">Seleccioná una opción</option>'] + [
        '<option value="{0}"{1}>{0}</option>'.format(e(m), " selected" if m == motivo else "") for m in MOTIVOS]
    return """<section class="section contact is-dark" id="contacto" aria-labelledby="contacto-title">
  <div class="container contact__grid">
    <div class="contact__info">
      <p class="kicker reveal">Contacto</p>
      <{h} id="contacto-title" class="contact__title reveal">{titulo}</{h}>
      <p class="lead reveal">{lead}</p>
      <ul class="contact__list reveal">
        <li>{phone}<div><span class="label">Teléfonos</span>{tels}</div></li>
        <li>{mail}<div><span class="label">Email</span><a href="mailto:{email}" data-track="email">{email}</a></div></li>
        <li>{clock}<div><span class="label">Horario</span><span>{horario}</span></div></li>
      </ul>
      <div class="reveal">{wa}</div>
    </div>
    <div class="form-card reveal">
      <form action="/enviar.php" method="post" data-contact-form novalidate>
        <input type="hidden" name="pagina" value="">
        <input type="hidden" name="utm" value="">
        <input type="hidden" name="_t" value="">
        <div class="hp" aria-hidden="true"><label for="f-web">No completar</label><input id="f-web" name="sitio_web" type="text" tabindex="-1" autocomplete="off"></div>
        <div class="form-grid">
          <div class="field"><label for="f-nombre">Nombre</label><input id="f-nombre" name="nombre" type="text" autocomplete="name" required><span class="field__error">Completá tu nombre.</span></div>
          <div class="field"><label for="f-telefono">Teléfono</label><input id="f-telefono" name="telefono" type="tel" inputmode="tel" autocomplete="tel" placeholder="Ej.: 11 1234-5678" required><span class="field__error">Ingresá un teléfono de contacto.</span></div>
          <div class="field full"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required><span class="field__error">Ingresá un email válido.</span></div>
          <div class="field full"><label for="f-motivo">Motivo de consulta</label><select id="f-motivo" name="motivo" required>{opts}</select><span class="field__error">Elegí el motivo de tu consulta.</span></div>
          <div class="field full"><label for="f-mensaje">Mensaje</label><textarea id="f-mensaje" name="mensaje" rows="4" placeholder="Contanos brevemente qué pasó o qué necesitás." required></textarea><span class="field__error">Contanos brevemente tu consulta.</span></div>
          <label class="consent full"><input type="checkbox" name="acepta" value="si" required><span>Acepto la <a href="/politica-de-privacidad/">Política de Privacidad</a>.</span></label>
        </div>
        <button class="btn btn--accent btn--block" type="submit">Enviar consulta {arrow}</button>
        <p class="form-status" role="status" aria-live="polite" data-status></p>
        <div class="form-fallback" data-fallback>
          <a class="btn btn--wa" data-fallback-wa href="{wa_url}" target="_blank" rel="noopener">{wa_icon} Enviar por WhatsApp</a>
          <a class="btn btn--outline" data-fallback-mail href="mailto:{email}">Enviar por email</a>
        </div>
        <p class="form-note">Tus datos se usan solo para responder tu consulta.</p>
      </form>
    </div>
  </div>
</section>""".format(h=h_tag, titulo=titulo, lead=e(lead), phone=PHONE_ICON, tels=tel_links(), mail=MAIL_ICON,
                     email=ESTUDIO["email"], clock=CLOCK_ICON, horario=e(ESTUDIO["horario"]),
                     wa=btn_wa("Escribinos por WhatsApp"), opts="".join(opts), arrow=ARROW, wa_url=WA, wa_icon=WA_ICON)


def service_card(slug, num=None):
    s = SERVICIOS[slug]
    n = '<span class="card__n">{:02d}</span>'.format(num) if num else ""
    return """<article class="card reveal">
  {n}<h3><a href="{u}">{name}</a></h3>
  <p>{res}</p>
  <span class="card__more" aria-hidden="true">Ver más {arrow}</span>
</article>""".format(n=n, u=url_servicio(slug), name=e(s.get("nombre_largo", s["nombre"])), res=e(s["resumen"]), arrow=ARROW)


def article_card(a, show_cat=True):
    cat = '<a class="post__cat" href="{}">{}</a>'.format(url_categoria(a["categoria"]), e(CATEGORIAS[a["categoria"]]["nombre"])) if show_cat else ""
    return """<article class="post reveal">
  {cat}
  <h3><a href="{u}">{t}</a></h3>
  <p>{r}</p>
  <span class="post__meta">{min} min de lectura</span>
</article>""".format(cat=cat, u=url_articulo(a["slug"]), t=e(a["titulo"]), r=e(a["resumen"]), min=lectura(a))


def lectura(a):
    words = len(re.sub(r"<[^>]+>", " ", a["cuerpo"]).split())
    return max(2, -(-words // 200))


def team_card(m):
    def f(text, cls, tag="span"):
        ph = " placeholder" if text.startswith("[") else ""
        return '<{t} class="{c}{p}">{x}</{t}>'.format(t=tag, c=cls, p=ph, x=e(text))
    li = ""
    if m.get("linkedin"):
        li = '<a class="member__li" href="{}" target="_blank" rel="noopener">{} LinkedIn</a>'.format(e(m["linkedin"]), LI_ICON)
    alt = "Fotografía de " + m["nombre"].replace("[Nombre] ", "")
    return """<article class="member reveal">
  <div class="member__photo"><img src="{foto}" alt="{alt}" width="800" height="1000" loading="lazy" decoding="async"></div>
  <div class="member__body"><h3>{nombre}</h3>{cargo}{area}{bio}{li}</div>
</article>""".format(foto=m["foto"], alt=e(alt), nombre=e(m["nombre"]), cargo=f(m["cargo"], "member__role"),
                     area=f(m["area"], "member__area"), bio=f(m["bio"], "member__bio", "p"), li=li)


# ---------------------------------------------------------------------------
# Páginas
# ---------------------------------------------------------------------------
PAGES = []


def write(p, body):
    html = head(p) + "\n" + header(p) + "\n" + body + "\n" + footer(p)
    path = p["path"]
    rel = path.strip("/")
    full = os.path.join(OUT, rel, "index.html") if path.endswith("/") else os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(html)
    PAGES.append(p)


def build_home():
    p = {"path": "/", "current": "inicio",
         "title": "Estudio jurídico en Buenos Aires | Abogados J, C & S",
         "description": "Estudio jurídico en Buenos Aires: civil y comercial, laboral, sucesiones y expensas. Atención personalizada para personas, empresas y consorcios.",
         "schemas": [schema_estudio(),
                     {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#web", "name": ESTUDIO["nombre"],
                      "url": SITE + "/", "inLanguage": "es-AR", "publisher": {"@id": SITE + "/#estudio"}},
                     schema_faq(FAQ_INICIO)]}

    router = [("Tuve un accidente de tránsito", "accidentes-de-transito"), ("El seguro no me paga", "seguros"),
              ("Me despidieron", "despidos"), ("Tuve un accidente de trabajo", "art-accidentes-de-trabajo"),
              ("Necesito hacer una sucesión", "sucesiones"), ("Tengo deudores de expensas", "cobro-de-expensas"),
              ("Quiero constituir una SAS", "constitucion-de-sas"), ("Me rechazaron un cheque", "cheques-sin-fondos")]
    router_html = "".join('<li><a href="{}">{}</a></li>'.format(url_servicio(s), e(t)) for t, s in router)

    valores = [("Atención personalizada", "Cada caso merece ser analizado de manera particular."),
               ("Dedicación", "Nos involucramos activamente en cada asunto y mantenemos una comunicación cercana con nuestros clientes."),
               ("Innovación", "Incorporamos nuevas herramientas y tecnologías para mejorar nuestro trabajo y brindar respuestas más eficientes."),
               ("Estrategia", "Analizamos cada situación buscando la alternativa jurídica más conveniente para el cliente.")]
    valores_html = "".join('<li class="value reveal"><span class="value__n">{:02d}</span><h3>{}</h3><p>{}</p></li>'.format(i + 1, e(t), e(d))
                           for i, (t, d) in enumerate(valores))

    civil_cards = "".join(service_card(s, i + 1) for i, s in enumerate(AREAS["civil"]["servicios"]))
    consorcio_items = "".join('<li><strong>{}</strong><span>{}</span></li>'.format(e(t), e(d)) for t, d in AREAS["consorcios"]["items"])
    posts = "".join(article_card(a) for a in [ART_BY_SLUG[s] for s in [
        "que-hacer-despues-de-un-accidente-de-transito", "como-constituir-una-sas-en-argentina",
        "que-hacer-si-un-propietario-no-paga-las-expensas"]])

    visual = ('<img class="hero__photo" src="{}" alt="" width="1200" height="1400" fetchpriority="high">'.format(HERO_FOTO)
              if HERO_FOTO else monograma())

    body = """
<section class="hero" aria-labelledby="hero-title">
  <div class="container hero__grid">
    <div class="hero__copy">
      <p class="kicker">Estudio jurídico · Buenos Aires</p>
      <h1 id="hero-title">Soluciones jurídicas pensadas <em>para vos y tu negocio.</em></h1>
      <p class="hero__lead">Asesoramiento legal personalizado, estratégico y cercano para resolver conflictos y proteger tus intereses.</p>
      <div class="btn-row">
        {c1}
        <a class="btn btn--outline" href="#servicios">Conocé nuestros servicios</a>
      </div>
      <ul class="hero__facts">
        <li>Civil y Comercial</li><li>Laboral</li><li>Familia</li><li>Consorcios y Expensas</li>
      </ul>
    </div>
    <div class="hero__visual{photo}">{visual}</div>
  </div>
  <div class="router">
    <div class="container">
      <p class="router__label">¿Qué necesitás resolver?</p>
      <ul class="router__list">{router}</ul>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="valor-title">
  <div class="container">
    <div class="split-head">
      <div>
        <p class="kicker reveal">Por qué elegirnos</p>
        <h2 id="valor-title" class="reveal">Una mirada jurídica enfocada <em>en tu caso.</em></h2>
      </div>
      <p class="lead reveal">Nos abocamos a comprender cada situación de manera particular, brindando una respuesta personalizada y estratégica. Combinamos experiencia jurídica, dedicación, innovación y cercanía para acompañar a nuestros clientes en la toma de decisiones y en la resolución de sus conflictos.</p>
    </div>
    <ul class="values">{valores}</ul>
  </div>
</section>

<section class="section is-white" id="servicios" aria-labelledby="civil-title">
  <div class="container">
    <div class="split-head">
      <div>
        <p class="kicker reveal">Servicios · Área 01</p>
        <h2 id="civil-title" class="reveal">Derecho Civil <em>y Comercial</em></h2>
      </div>
      <p class="lead reveal">Reclamos por accidentes, seguros y daños, y acompañamiento a empresas y emprendedores en la constitución de sociedades y el cobro de sus créditos.</p>
    </div>
    <div class="cards">{civil_cards}</div>
    <div class="section-actions reveal">
      {b_civil}
      {c_civil}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="lab-title">
  <div class="container areas-duo">
    <div class="area-panel reveal">
      <p class="kicker">Servicios · Área 02</p>
      <h2 id="lab-title"><a href="{u_lab}">Derecho Laboral</a></h2>
      <p class="area-panel__sub">Asesoramiento y representación en conflictos laborales.</p>
      <ul class="area-panel__list">
        <li><a href="{u_desp}"><strong>Despidos</strong><span>{r_desp}</span></a></li>
        <li><a href="{u_art}"><strong>ART</strong><span>{r_art}</span></a></li>
      </ul>
      {c_lab}
    </div>
    <div class="area-panel reveal">
      <p class="kicker">Servicios · Área 03</p>
      <h2><a href="{u_fam}">Derecho de Familia</a></h2>
      <p class="area-panel__sub">Acompañamiento cercano en situaciones familiares que requieren una respuesta jurídica clara.</p>
      <ul class="area-panel__list">
        <li><a href="{u_suc}"><strong>Sucesiones</strong><span>{r_suc}</span></a></li>
      </ul>
      {c_fam}
    </div>
  </div>
</section>

<section class="section is-dark sas-band" aria-labelledby="sas-title">
  <div class="container sas-band__grid">
    <div>
      <p class="kicker reveal">Constitución de sociedades</p>
      <h2 id="sas-title" class="reveal">Constituí tu SAS con <em>asesoramiento jurídico.</em></h2>
      <p class="lead reveal">Te acompañamos durante el proceso de constitución y puesta en funcionamiento de tu sociedad, con explicaciones claras en cada etapa.</p>
      <div class="btn-row reveal">{c_sas}<a class="btn btn--outline" href="{u_sas}">Cómo funciona</a></div>
    </div>
    <ol class="mini-steps reveal">
      <li><span>1</span>Asesoramiento inicial</li>
      <li><span>2</span>Redacción del estatuto</li>
      <li><span>3</span>Inscripción</li>
      <li><span>4</span>CUIT y puesta en marcha</li>
    </ol>
  </div>
</section>

<section class="section is-white" id="consorcios" aria-labelledby="cons-title">
  <div class="container">
    <div class="split-head">
      <div>
        <p class="kicker reveal">Servicios · Área 04</p>
        <h2 id="cons-title" class="reveal"><a href="{u_cons}">Consorcios <em>y Expensas</em></a></h2>
      </div>
      <p class="lead reveal">Asesoramiento jurídico para consorcios, administraciones y propietarios.</p>
    </div>
    <ul class="item-grid">{cons_items}</ul>
    <div class="debtors reveal">
      <div>
        <p class="kicker">Para administradores de consorcios</p>
        <h2>¿Tenés deudores en tu consorcio?</h2>
        <p>Ayudamos a consorcios y administraciones a gestionar el recupero de expensas adeudadas y avanzar con las acciones legales necesarias para obtener su cobro.</p>
        <div class="btn-row">{c_exp}<a class="btn btn--outline" href="{u_cobro}">Cobro de expensas</a></div>
      </div>
      <ol class="debtors__steps">
        <li><span>01</span>Revisión de la deuda</li>
        <li><span>02</span>Intimación al deudor</li>
        <li><span>03</span>Ejecución de expensas</li>
        <li><span>04</span>Cobro</li>
      </ol>
    </div>
  </div>
</section>

<section class="section studio-teaser" aria-labelledby="est-title">
  <div class="container studio-teaser__grid">
    <div>
      <p class="kicker reveal">El Estudio</p>
      <h2 id="est-title" class="reveal">Detrás de cada consulta hay <em>una situación particular.</em></h2>
      <p class="reveal">En Estudio J, C &amp; S nos abocamos a comprender cada caso de manera personalizada, acompañando a nuestros clientes durante todo el proceso y buscando alternativas jurídicas concretas para cada situación.</p>
      <div class="reveal" style="margin-top:28px">{b_est}</div>
    </div>
    <ul class="pillars reveal">
      <li>Personalización</li><li>Experiencia</li><li>Innovación</li><li>Estrategia</li>
    </ul>
  </div>
</section>

{proceso}

<section class="section is-white" aria-labelledby="blog-title">
  <div class="container">
    <div class="split-head">
      <div>
        <p class="kicker reveal">Información jurídica</p>
        <h2 id="blog-title" class="reveal">Respuestas claras a <em>preguntas frecuentes.</em></h2>
      </div>
      <p class="lead reveal">Guías prácticas para entender tu situación antes de dar el próximo paso.</p>
    </div>
    <div class="posts">{posts}</div>
    <div class="section-actions reveal">{b_blog}</div>
  </div>
</section>

{faq}

{form}
""".format(
        c1=consultar(), photo=" hero__visual--photo" if HERO_FOTO else "", visual=visual, router=router_html,
        valores=valores_html, civil_cards=civil_cards,
        b_civil=btn(url_area("civil"), "Ver Derecho Civil y Comercial", "primary"),
        c_civil=btn_wa("Hablar con un abogado", "outline"),
        u_lab=url_area("laboral"), u_desp=url_servicio("despidos"), r_desp=e(SERVICIOS["despidos"]["resumen"]),
        u_art=url_servicio("art-accidentes-de-trabajo"), r_art=e(SERVICIOS["art-accidentes-de-trabajo"]["resumen"]),
        c_lab=consultar("Despido", "Consultar por Derecho Laboral"),
        u_fam=url_area("familia"), u_suc=url_servicio("sucesiones"), r_suc=e(SERVICIOS["sucesiones"]["resumen"]),
        c_fam=consultar("Sucesión", "Consultar por sucesiones"),
        c_sas=consultar("Constitución de sociedades / SAS", "Quiero constituir una SAS", "accent"),
        u_sas=url_servicio("constitucion-de-sas"), u_cons=url_area("consorcios"), cons_items=consorcio_items,
        c_exp=consultar("Expensas / consorcio", "Consultar por deudas de expensas", "accent"),
        u_cobro=url_servicio("cobro-de-expensas"), b_est=btn("/el-estudio/", "Conocé el estudio", "outline"),
        proceso=proceso_block(), posts=posts, b_blog=btn("/informacion-juridica/", "Ver toda la información jurídica", "outline"),
        faq=faq_block(FAQ_INICIO, "Lo que suelen preguntarnos"),
        form=form_block(),
    )
    write(p, body)


def build_area(k):
    a = AREAS[k]
    path = url_area(k)
    crumbs = [("Inicio", "/"), (a["nombre"], path)]
    p = {"path": path, "current": k, "title": a["title"], "description": a["description"],
         "schemas": [schema_estudio(), schema_servicio(a["nombre"], a["description"], path, a["nombre"]),
                     schema_breadcrumb(crumbs), schema_faq(a["faqs"])]}

    cards = "".join(service_card(s, i + 1) for i, s in enumerate(a["servicios"]))
    extra = ""
    if k == "civil":
        soc = SERVICIOS["constitucion-de-sociedades"]
        items = "".join('<li><strong>{}</strong><span>{}</span></li>'.format(e(t), e(d)) for t, d in soc["situaciones"])
        extra = """<section class="section is-white" aria-labelledby="soc-title">
  <div class="container">
    <div class="split-head">
      <div><p class="kicker reveal">Empresas y emprendedores</p><h2 id="soc-title" class="reveal">Constitución <em>de sociedades</em></h2></div>
      <p class="lead reveal">{res} Te ayudamos a elegir el tipo societario y a poner en marcha tu sociedad.</p>
    </div>
    <ul class="item-grid">{items}</ul>
    {band}
  </div>
</section>""".format(res=e(soc["resumen"]), items=items, band=cta_band(
            "Constituí tu SAS con asesoramiento jurídico.", "Te acompañamos durante el proceso de constitución y puesta en funcionamiento de tu sociedad.",
            consultar("Constitución de sociedades / SAS", "Quiero constituir una SAS", "accent") + btn(url_servicio("constitucion-de-sas"), "Ver Constitución de SAS", "outline"), dark=True))
    if k == "consorcios":
        items = "".join('<li><strong>{}</strong><span>{}</span></li>'.format(e(t), e(d)) for t, d in a["items"])
        extra = """<section class="section is-white" aria-labelledby="items-title">
  <div class="container">
    <div class="section-head"><p class="kicker reveal">Qué hacemos</p><h2 id="items-title" class="reveal">Asesoramiento integral <em>en propiedad horizontal</em></h2></div>
    <ul class="item-grid">{items}</ul>
    <div class="debtors reveal">
      <div>
        <p class="kicker">Para administradores de consorcios</p>
        <h2>¿Tenés deudores en tu consorcio?</h2>
        <p>Ayudamos a consorcios y administraciones a gestionar el recupero de expensas adeudadas y avanzar con las acciones legales necesarias para obtener su cobro.</p>
        <div class="btn-row">{c}<a class="btn btn--outline" href="{u}">Cobro de expensas</a></div>
      </div>
      <ol class="debtors__steps"><li><span>01</span>Revisión de la deuda</li><li><span>02</span>Intimación al deudor</li><li><span>03</span>Ejecución de expensas</li><li><span>04</span>Cobro</li></ol>
    </div>
  </div>
</section>""".format(items=items, c=consultar("Expensas / consorcio", "Consultar por deudas de expensas", "accent"), u=url_servicio("cobro-de-expensas"))

    otros = ""
    if a.get("otros"):
        otros = cta_band(e(a["otros"]), "Analizamos tu situación y te explicamos qué alternativas tenés.",
                         consultar(a["motivo"], "Contanos tu caso") + btn_wa("WhatsApp", "outline"))

    cats = {"civil": ["derecho-civil", "derecho-comercial", "sociedades"], "laboral": ["derecho-laboral"],
            "familia": ["derecho-de-familia"], "consorcios": ["consorcios-y-expensas"]}[k]
    arts = [x for x in ARTICULOS if x["categoria"] in cats][:3]
    posts = ""
    if arts:
        posts = """<section class="section is-white" aria-labelledby="art-title">
  <div class="container">
    <div class="section-head"><p class="kicker reveal">Información jurídica</p><h2 id="art-title" class="reveal">Guías relacionadas</h2></div>
    <div class="posts">{}</div>
  </div>
</section>""".format("".join(article_card(x) for x in arts))

    intro = "".join("<p>{}</p>".format(e(x)) for x in a["intro"])
    body = page_hero(crumbs, a["kicker"], e(a["h1"]), a["lead"],
                     consultar(a["motivo"], a["cta"], "accent") + btn_wa("WhatsApp", "outline"), hero_aside()) + """
<section class="section" aria-labelledby="serv-title">
  <div class="container">
    <div class="split-head">
      <div><p class="kicker reveal">Servicios</p><h2 id="serv-title" class="reveal">¿En qué podemos <em>ayudarte?</em></h2></div>
      <div class="lead reveal prose-lead">{intro}</div>
    </div>
    <div class="cards">{cards}</div>
    {otros}
  </div>
</section>
{extra}
{proceso}
{faq}
{posts}
{form}
""".format(intro=intro, cards=cards, otros=otros, extra=extra, proceso=proceso_block(),
           faq=faq_block(a["faqs"], "Dudas frecuentes sobre {}".format(e(a["nombre"]))), posts=posts,
           form=form_block(a["motivo"], "Consultá por <em>{}</em>".format(e(a["nombre"]))))
    write(p, body)


def build_servicio(slug):
    s = SERVICIOS[slug]
    a = AREAS[s["area"]]
    path = url_servicio(slug)
    nombre = s.get("nombre_largo", s["nombre"])
    crumbs = [("Inicio", "/"), (a["nombre"], url_area(s["area"]))]
    if s.get("padre"):
        crumbs.append((SERVICIOS[s["padre"]]["nombre"], url_servicio(s["padre"])))
    crumbs.append((nombre, path))
    p = {"path": path, "current": s["area"], "title": s["title"], "description": s["description"],
         "schemas": [schema_estudio(), schema_servicio(nombre, s["description"], path, a["nombre"]),
                     schema_breadcrumb(crumbs), schema_faq(s["faqs"])]}

    intro = "".join("<p>{}</p>".format(e(x)) for x in s["intro"])
    sit = "".join('<li class="reveal"><h3>{}</h3><p>{}</p></li>'.format(e(t), e(d)) for t, d in s["situaciones"]) if s.get("situaciones") else ""
    docs = "".join("<li>{}</li>".format(e(d)) for d in s["documentos"])

    beneficios = ""
    if s.get("beneficios"):
        beneficios = """<section class="section is-white" aria-labelledby="ben-title">
  <div class="container">
    <div class="section-head"><p class="kicker reveal">Por qué una SAS</p><h2 id="ben-title" class="reveal">Una forma ágil de darle <em>estructura a tu proyecto</em></h2></div>
    <ul class="detail-grid">{}</ul>
  </div>
</section>""".format("".join('<li class="reveal"><h3>{}</h3><p>{}</p></li>'.format(e(t), e(d)) for t, d in s["beneficios"]))

    situaciones = ""
    if sit:
        situaciones = """<section class="section is-white" aria-labelledby="sit-title">
  <div class="container">
    <div class="section-head"><p class="kicker reveal">Qué hacemos</p><h2 id="sit-title" class="reveal">¿En qué casos <em>podemos ayudarte?</em></h2></div>
    <ul class="detail-grid">{sit}</ul>
    {band}
  </div>
</section>""".format(sit=sit, band=cta_band("¿Tu caso se parece a alguno de estos?", "Contanos qué pasó y te explicamos qué alternativas tenés.",
                                            consultar(s["motivo"], "Contanos tu caso") + btn_wa("Hablar con un abogado", "outline")))

    rel_s = "".join('<li><a href="{}">{}</a></li>'.format(url_servicio(r), e(SERVICIOS[r].get("nombre_largo", SERVICIOS[r]["nombre"]))) for r in s.get("relacionados", []))
    rel_s += '<li><a href="{}">{}</a></li>'.format(url_area(s["area"]), e(a["nombre"]))
    arts = [x for x in ARTICULOS if x["servicio"] == slug]
    rel_a = "".join('<li><a href="{}">{}</a></li>'.format(url_articulo(x["slug"]), e(x["titulo"])) for x in arts)
    related = """<section class="section is-white" aria-labelledby="rel-title">
  <div class="container related">
    <div><p class="kicker reveal">Seguí leyendo</p><h2 id="rel-title" class="reveal">Información relacionada</h2></div>
    <div class="related__cols">
      <div class="reveal"><p class="related__label">Servicios relacionados</p><ul class="link-list">{rs}</ul></div>
      {ra}
    </div>
  </div>
</section>""".format(rs=rel_s, ra='<div class="reveal"><p class="related__label">Guías</p><ul class="link-list">{}</ul></div>'.format(rel_a) if rel_a else "")

    body = page_hero(crumbs, a["nombre"], e(s["h1"]), s["lead"],
                     consultar(s["motivo"], s["cta"], "accent") + btn_wa("WhatsApp", "outline"), hero_aside()) + """
<section class="section" aria-labelledby="intro-title">
  <div class="container intro">
    <div>
      <p class="kicker reveal">{nombre}</p>
      <h2 id="intro-title" class="reveal">Cómo te <em>ayudamos</em></h2>
    </div>
    <div class="prose reveal">{intro}</div>
  </div>
</section>
{beneficios}
{situaciones}
{proceso}
<section class="section" aria-labelledby="docs-title">
  <div class="container docs">
    <div>
      <p class="kicker reveal">Para la primera consulta</p>
      <h2 id="docs-title" class="reveal">Qué conviene <em>tener a mano</em></h2>
      <p class="reveal">No hace falta que tengas todo para empezar: con lo que tengas analizamos tu caso y te indicamos qué falta.</p>
      <div class="btn-row reveal" style="margin-top:28px">{c}</div>
    </div>
    <ul class="checklist reveal">{docs}</ul>
  </div>
</section>
{faq}
{related}
{form}
""".format(nombre=e(nombre), intro=intro, beneficios=beneficios, situaciones=situaciones,
           proceso=proceso_block(s.get("pasos"), "Cómo es <em>el proceso</em>" if s.get("pasos") else "Cómo trabajamos"),
           c=consultar(s["motivo"], s["cta"], "primary"), docs=docs,
           faq=faq_block(s["faqs"], "Preguntas sobre {}".format(e(low(nombre)))),
           related=related, form=form_block(s["motivo"]))
    write(p, body)


def build_estudio():
    path = "/el-estudio/"
    crumbs = [("Inicio", "/"), ("El Estudio", path)]
    p = {"path": path, "current": "estudio",
         "title": "El Estudio: abogados en Buenos Aires | J, C & S",
         "description": "Jaikin, Carabajal & Santoro: un estudio jurídico en Buenos Aires enfocado en la atención personalizada, la dedicación, la innovación y la estrategia.",
         "schemas": [schema_estudio(), schema_breadcrumb(crumbs),
                     {"@context": "https://schema.org", "@type": "AboutPage", "url": SITE + path, "about": {"@id": SITE + "/#estudio"}}]}
    pilares = [("Personalización", "Cada caso es distinto. Nos tomamos el tiempo de entender tu situación antes de proponer una respuesta."),
               ("Experiencia", "Aplicamos nuestra experiencia profesional para anticipar escenarios y tomar mejores decisiones."),
               ("Innovación", "Incorporamos herramientas y tecnologías que nos permiten trabajar mejor y responder con más agilidad."),
               ("Estrategia", "Buscamos la alternativa jurídica más conveniente para cada cliente, con un plan claro para avanzar.")]
    pil = "".join('<li class="pillar reveal"><span class="pillar__n">{:02d}</span><h3>{}</h3><p>{}</p></li>'.format(i + 1, e(t), e(d)) for i, (t, d) in enumerate(pilares))
    areas = "".join('<li><a href="{}"><strong>{}</strong><span>{}</span></a></li>'.format(url_area(k), e(a["nombre"]), e(a["lead"])) for k, a in AREAS.items())
    body = page_hero(crumbs, "El Estudio · Jaikin, Carabajal & Santoro",
                     "Un estudio jurídico que se toma el tiempo de <em>entender tu caso.</em>",
                     "Atención personalizada, dedicación, innovación y estrategia para personas, empresas e instituciones.",
                     consultar(text="Consultar ahora", kind="accent") + btn_wa("WhatsApp", "outline")) + """
<section class="section" aria-labelledby="quienes">
  <div class="container intro">
    <div><p class="kicker reveal">Quiénes somos</p><h2 id="quienes" class="reveal">Detrás de cada consulta hay <em>una situación particular</em></h2></div>
    <div class="prose prose--lg reveal">
      <p>En Estudio J, C &amp; S entendemos que detrás de cada consulta jurídica existe una situación particular que requiere tiempo, análisis y una respuesta adecuada.</p>
      <p>Por eso nos abocamos a comprender cada caso de manera personalizada, acompañando a nuestros clientes durante todo el proceso y buscando alternativas jurídicas concretas para cada situación.</p>
      <p>Combinamos experiencia profesional, dedicación e innovación para brindar un servicio jurídico cercano, estratégico y adaptado a las necesidades de cada cliente.</p>
      <p>Nuestro objetivo es que cada persona, empresa o institución que nos consulta encuentre no solamente asesoramiento jurídico, sino también una estrategia clara para avanzar.</p>
    </div>
  </div>
</section>
<section class="section is-dark" aria-labelledby="pilares">
  <div class="container">
    <div class="section-head"><p class="kicker reveal">Lo que nos define</p><h2 id="pilares" class="reveal">Cuatro ideas que guían <em>nuestro trabajo</em></h2></div>
    <ul class="pillars-grid">{pil}</ul>
  </div>
</section>
{proceso}
<section class="section is-white" id="equipo" aria-labelledby="equipo-title">
  <div class="container">
    <div class="split-head">
      <div><p class="kicker reveal">Equipo</p><h2 id="equipo-title" class="reveal">Jaikin, Carabajal <em>&amp; Santoro</em></h2></div>
      <p class="lead reveal">Las personas que acompañan cada consulta.</p>
    </div>
    <div class="team">{team}</div>
  </div>
</section>
<section class="section" aria-labelledby="areas-title">
  <div class="container">
    <div class="section-head"><p class="kicker reveal">Áreas de práctica</p><h2 id="areas-title" class="reveal">En qué podemos <em>ayudarte</em></h2></div>
    <ul class="area-links">{areas}</ul>
  </div>
</section>
{form}
""".format(pil=pil, proceso=proceso_block(dark=False), team="".join(team_card(m) for m in EQUIPO), areas=areas, form=form_block())
    write(p, body)


def build_contacto():
    path = "/contacto/"
    crumbs = [("Inicio", "/"), ("Contacto", path)]
    faqs = [("¿Cómo es la primera consulta?", FAQ_INICIO[1][1]),
            ("¿Puedo consultar por WhatsApp?", FAQ_INICIO[2][1]),
            ("¿Qué información debo enviar?", "Contanos brevemente qué pasó y, si es posible, qué documentación tenés. No envíes contraseñas, claves bancarias ni números completos de tarjetas.")]
    p = {"path": path, "current": "contacto",
         "title": "Contacto: consultá a un abogado | Estudio J, C & S",
         "description": "Contactá a Estudio J, C & S: teléfonos +54 9 11 5178-5782 y +54 9 11 2296-1982, WhatsApp e info@estudiojcs.com.ar. Lunes a viernes de 9:00 a 17:00 hs.",
         "schemas": [schema_estudio(), schema_breadcrumb(crumbs), schema_faq(faqs),
                     {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + path, "about": {"@id": SITE + "/#estudio"}}]}
    body = """<section class="page-hero page-hero--compact">
  <div class="container">{bc}
    <p class="kicker">Contacto</p>
    <h1>Hablemos de <em>tu caso.</em></h1>
    <p class="lead">Elegí el canal que te resulte más cómodo. Un abogado del estudio va a revisar tu consulta.</p>
    <ul class="channels">
      <li><a href="{wa}" target="_blank" rel="noopener" data-track="whatsapp">{wai}<span><strong>WhatsApp</strong>{p1}</span></a></li>
      <li><a href="tel:{t1}" data-track="telefono">{ph}<span><strong>Teléfono</strong>{p1}</span></a></li>
      <li><a href="tel:{t2}" data-track="telefono">{ph}<span><strong>Teléfono</strong>{p2}</span></a></li>
      <li><a href="mailto:{email}" data-track="email">{mail}<span><strong>Email</strong>{email}</span></a></li>
    </ul>
  </div>
</section>
{form}
{faq}
""".format(bc=breadcrumb(crumbs), wa=WA, wai=WA_ICON, p1=ESTUDIO["telefonos"][0][0], t1=ESTUDIO["telefonos"][0][1],
           p2=ESTUDIO["telefonos"][1][0], t2=ESTUDIO["telefonos"][1][1], ph=PHONE_ICON, email=ESTUDIO["email"], mail=MAIL_ICON,
           form=form_block(titulo="Envianos tu consulta", h_tag="h2"), faq=faq_block(faqs, "Antes de escribirnos"))
    write(p, body)


def blog_nav(active=None):
    items = ['<li><a href="/informacion-juridica/"{}>Todos</a></li>'.format(' aria-current="page"' if active is None else "")]
    for k, c in CATEGORIAS.items():
        items.append('<li><a href="{}"{}>{}</a></li>'.format(url_categoria(k), ' aria-current="page"' if active == k else "", e(c["nombre"])))
    return '<nav aria-label="Categorías"><ul class="cat-nav">{}</ul></nav>'.format("".join(items))


def build_blog():
    path = "/informacion-juridica/"
    crumbs = [("Inicio", "/"), ("Información jurídica", path)]
    p = {"path": path, "title": "Información jurídica: guías legales claras | Estudio J, C & S",
         "description": "Guías jurídicas claras sobre accidentes de tránsito, seguros, despidos, ART, sucesiones, expensas, cheques rechazados y constitución de SAS en Argentina.",
         "schemas": [schema_estudio(), schema_breadcrumb(crumbs),
                     {"@context": "https://schema.org", "@type": "Blog", "name": "Información jurídica", "url": SITE + path,
                      "publisher": {"@id": SITE + "/#estudio"},
                      "blogPost": [{"@type": "BlogPosting", "headline": a["titulo"], "url": SITE + url_articulo(a["slug"])} for a in ARTICULOS]}]}
    body = """<section class="page-hero page-hero--compact">
  <div class="container">{bc}
    <p class="kicker">Información jurídica</p>
    <h1>Información jurídica <em>clara y útil</em></h1>
    <p class="lead">Guías prácticas para entender tu situación y saber cuál es el próximo paso. Si tenés dudas sobre tu caso, consultanos.</p>
  </div>
</section>
<section class="section">
  <div class="container">{nav}<div class="posts posts--grid">{posts}</div></div>
</section>
{form}
""".format(bc=breadcrumb(crumbs), nav=blog_nav(), posts="".join(article_card(a) for a in ARTICULOS), form=form_block())
    write(p, body)

    for k, c in CATEGORIAS.items():
        cpath = url_categoria(k)
        ccr = crumbs + [(c["nombre"], cpath)]
        arts = [a for a in ARTICULOS if a["categoria"] == k]
        cp = {"path": cpath, "title": "{}: información jurídica | J, C & S".format(c["nombre"]),
              "description": "{} Guías del Estudio J, C & S.".format(c["descripcion"]),
              "schemas": [schema_estudio(), schema_breadcrumb(ccr)]}
        body = """<section class="page-hero page-hero--compact">
  <div class="container">{bc}
    <p class="kicker">Información jurídica</p>
    <h1>{n}</h1>
    <p class="lead">{d}</p>
  </div>
</section>
<section class="section">
  <div class="container">{nav}<div class="posts posts--grid">{posts}</div></div>
</section>
{form}
""".format(bc=breadcrumb(ccr), n=e(c["nombre"]), d=e(c["descripcion"]), nav=blog_nav(k),
           posts="".join(article_card(a, False) for a in arts) or '<p class="note">Próximamente publicaremos artículos en esta categoría.</p>',
           form=form_block())
        write(cp, body)


def build_articulo(a):
    path = url_articulo(a["slug"])
    cat = CATEGORIAS[a["categoria"]]
    s = SERVICIOS[a["servicio"]]
    crumbs = [("Inicio", "/"), ("Información jurídica", "/informacion-juridica/"), (cat["nombre"], url_categoria(a["categoria"])), (a["titulo"], path)]
    p = {"path": path, "title": "{} | Estudio J, C & S".format(a["title"]) if len(a["title"]) < 52 else a["title"],
         "description": a["description"], "article": a["fecha"],
         "schemas": [schema_estudio(), schema_breadcrumb(crumbs),
                     {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["titulo"],
                      "description": a["description"], "datePublished": a["fecha"], "dateModified": a["fecha"],
                      "inLanguage": "es-AR", "mainEntityOfPage": SITE + path, "image": SITE + "/assets/img/og-image.jpg",
                      "author": {"@id": SITE + "/#estudio"}, "publisher": {"@id": SITE + "/#estudio"},
                      "articleSection": cat["nombre"]}]}
    otros = [x for x in ARTICULOS if x["slug"] != a["slug"] and (x["categoria"] == a["categoria"] or x["servicio"] == a["servicio"])]
    otros += [x for x in ARTICULOS if x not in otros and x["slug"] != a["slug"]]
    fecha = "{}/{}/{}".format(a["fecha"][8:10], a["fecha"][5:7], a["fecha"][:4])
    body = """<article class="article">
  <header class="page-hero page-hero--compact article__head">
    <div class="container">{bc}
      <p class="kicker"><a href="{ucat}">{cat}</a></p>
      <h1>{t}</h1>
      <p class="lead">{r}</p>
      <p class="article__meta"><time datetime="{f}">{fecha}</time> · {min} min de lectura · Estudio J, C &amp; S</p>
    </div>
  </header>
  <div class="section article__wrap">
    <div class="container article__grid">
      <div class="prose article__body">
        {cuerpo}
        <p class="note">{disc}</p>
      </div>
      <aside class="article__aside">
        <div class="aside-card">
          <p class="aside-card__kicker">¿Te pasó algo así?</p>
          <p class="aside-card__title">Hablá con un abogado sobre tu caso.</p>
          <p>Conocé cómo trabajamos <a href="{us}">{sn}</a>.</p>
          {c}
          {w}
        </div>
      </aside>
    </div>
  </div>
</article>
<section class="section is-white" aria-labelledby="mas">
  <div class="container">
    <div class="section-head"><p class="kicker">Información jurídica</p><h2 id="mas">También te puede interesar</h2></div>
    <div class="posts">{otros}</div>
  </div>
</section>
{form}
""".format(bc=breadcrumb(crumbs), ucat=url_categoria(a["categoria"]), cat=e(cat["nombre"]), t=e(a["titulo"]),
           r=e(a["resumen"]), f=a["fecha"], fecha=fecha, min=lectura(a), cuerpo=enlazar(a["cuerpo"]), disc=DISCLAIMER,
           us=url_servicio(a["servicio"]), sn=e(low(s.get("nombre_largo", s["nombre"]))),
           c=consultar(s["motivo"], "Contanos tu caso", "accent").replace('class="btn', 'class="btn btn--block', 1),
           w=btn_wa("WhatsApp", "outline btn--block"), otros="".join(article_card(x) for x in otros[:3]),
           form=form_block(s["motivo"]))
    write(p, body)


def build_simple():
    # Política de privacidad
    path = "/politica-de-privacidad/"
    crumbs = [("Inicio", "/"), ("Política de Privacidad", path)]
    p = {"path": path, "noform": True, "title": "Política de Privacidad | Estudio J, C & S",
         "description": "Política de privacidad y tratamiento de datos personales del sitio web de Estudio J, C & S.",
         "schemas": [schema_estudio(), schema_breadcrumb(crumbs)]}
    body = """<section class="page-hero page-hero--compact"><div class="container">{bc}<p class="kicker">Legal</p><h1>Política de Privacidad</h1></div></section>
<section class="section is-white"><div class="container container--narrow prose">
  <h2>Responsable</h2>
  <p>Estudio J, C &amp; S (Jaikin, Carabajal &amp; Santoro), con domicilio en <span class="placeholder">[completar domicilio]</span>, Ciudad Autónoma de Buenos Aires. Contacto: <a href="mailto:{email}">{email}</a>.</p>
  <h2>Datos que recopilamos</h2>
  <p>Solo los datos que nos enviás voluntariamente al completar el formulario o al contactarnos: nombre, email, teléfono, motivo de consulta y mensaje. También registramos la página desde la que nos escribiste y, si llegaste desde una campaña, su origen.</p>
  <h2>Finalidad</h2>
  <p>Usamos esos datos únicamente para responder tu consulta y, si corresponde, prestarte nuestros servicios. No los cedemos ni los comercializamos.</p>
  <h2>Confidencialidad</h2>
  <p>La información que nos compartís se trata con reserva y conforme al secreto profesional. No envíes por este medio contraseñas, claves bancarias, códigos de verificación ni números completos de tarjetas.</p>
  <h2>Tus derechos</h2>
  <p>Podés solicitar el acceso, la rectificación, la actualización o la supresión de tus datos escribiendo a <a href="mailto:{email}">{email}</a>, conforme a la Ley 25.326 de Protección de los Datos Personales.</p>
  <p>La Agencia de Acceso a la Información Pública, en su carácter de Órgano de Control de la Ley N.º 25.326, tiene la atribución de atender las denuncias y reclamos que interpongan quienes resulten afectados en sus derechos por incumplimiento de las normas vigentes en materia de protección de datos personales.</p>
  <h2>Cookies y medición</h2>
  <p>Este sitio no utiliza cookies propias. Si en el futuro se incorporan herramientas de medición o publicidad, esta política se actualizará para informarlo.</p>
  <p class="note">Última actualización: {hoy}.</p>
</div></section>""".format(bc=breadcrumb(crumbs), email=ESTUDIO["email"], hoy=date.today().strftime("%d/%m/%Y"))
    write(p, body)

    # Gracias
    p = {"path": "/gracias/", "noindex": True, "noform": True, "title": "Consulta enviada | Estudio J, C & S", "description": "Recibimos tu consulta.", "schemas": []}
    body = """<section class="section thanks"><div class="container container--narrow">
  <p class="kicker">Consulta enviada</p>
  <h1>Gracias. <em>Recibimos tu consulta.</em></h1>
  <p class="lead">Un abogado del estudio va a revisarla y te vamos a contactar a la brevedad. Si es urgente, escribinos por WhatsApp.</p>
  <div class="btn-row">{w}<a class="btn btn--outline" href="/">Volver al inicio</a></div>
</div></section>""".format(w=btn_wa("Escribir por WhatsApp"))
    write(p, body)

    # 404
    p = {"path": "/404.html", "noindex": True, "noform": True, "title": "Página no encontrada | Estudio J, C & S", "description": "La página que buscás no existe.", "schemas": []}
    body = """<section class="section thanks"><div class="container container--narrow">
  <p class="kicker">Error 404</p>
  <h1>No encontramos <em>esta página.</em></h1>
  <p class="lead">Puede que la dirección haya cambiado. Estas son algunas secciones que te pueden servir:</p>
  <ul class="link-list">{links}</ul>
  <div class="btn-row" style="margin-top:32px"><a class="btn btn--primary" href="/">Ir al inicio</a>{w}</div>
</div></section>""".format(links="".join('<li><a href="{}">{}</a></li>'.format(url_area(k), e(a["nombre"])) for k, a in AREAS.items()),
                            w=btn_wa("WhatsApp", "outline"))
    write(p, body)


def build_sitemap():
    prio = {"/": "1.0"}
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    today = date.today().isoformat()
    for p in PAGES:
        if p.get("noindex"):
            continue
        path = p["path"]
        pr = prio.get(path)
        if pr is None:
            if path.strip("/") in [a["slug"] for a in AREAS.values()]:
                pr = "0.9"
            elif path.strip("/") in SERVICIOS:
                pr = "0.9"
            elif path.startswith("/informacion-juridica/"):
                pr = "0.6"
            else:
                pr = "0.5"
        lastmod = p.get("article") or today
        lines.append("  <url><loc>{}{}</loc><lastmod>{}</lastmod><priority>{}</priority></url>".format(SITE, path, lastmod, pr))
    lines.append("</urlset>")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nAllow: /\nDisallow: /gracias/\nDisallow: /enviar.php\n\nSitemap: {}/sitemap.xml\n".format(SITE))


def main():
    build_home()
    for k in AREAS:
        build_area(k)
    for slug in SERVICIOS:
        build_servicio(slug)
    build_estudio()
    build_contacto()
    build_blog()
    for a in ARTICULOS:
        build_articulo(a)
    build_simple()
    build_sitemap()
    print("Generadas {} páginas en {}".format(len(PAGES), os.path.normpath(OUT)))


if __name__ == "__main__":
    main()
