# Sitio web — Estudio J, C & S

Sitio estático (HTML, CSS y JavaScript sin dependencias) pensado para Hostinger,
con foco en SEO local, generación de consultas y velocidad de carga.

- `sitio/` → la carpeta que se publica (subir su contenido a `public_html`).
- `tools/` → generador y contenido editable (no se sube al hosting).

## Estructura del sitio

| Sección | URL |
|---|---|
| Inicio | `/` |
| Derecho Civil y Comercial | `/derecho-civil-y-comercial/` |
| · Accidentes de tránsito | `/accidentes-de-transito/` |
| · Seguros | `/seguros/` |
| · Daños y perjuicios | `/danos-y-perjuicios/` |
| · Constitución de sociedades | `/constitucion-de-sociedades/` |
| · Constitución de SAS | `/constitucion-de-sas/` |
| · Planes de ahorro | `/planes-de-ahorro/` |
| · Cheques sin fondos | `/cheques-sin-fondos/` |
| Derecho Laboral | `/derecho-laboral/` |
| · Despidos | `/despidos/` |
| · ART y accidentes de trabajo | `/art-accidentes-de-trabajo/` |
| Derecho de Familia | `/derecho-de-familia/` |
| · Sucesiones | `/sucesiones/` |
| Consorcios y Expensas | `/consorcios-y-expensas/` |
| · Expensas | `/expensas/` |
| · Cobro de expensas | `/cobro-de-expensas/` |
| El Estudio | `/el-estudio/` |
| Contacto | `/contacto/` |
| Información jurídica | `/informacion-juridica/` (6 categorías y 12 artículos) |
| Política de Privacidad, Gracias, 404 | `/politica-de-privacidad/`, `/gracias/`, `/404.html` |

Cada página de servicio tiene título y descripción SEO propios, H1 único,
breadcrumbs, preguntas frecuentes, enlaces internos, llamadas a la acción y un
formulario con el motivo de consulta ya seleccionado. Datos estructurados:
`LegalService`, `Service`, `FAQPage`, `BreadcrumbList`, `BlogPosting`.

## Publicar en Hostinger

1. Subí **todo el contenido** de `sitio/` a `public_html`, incluido el archivo
   oculto `.htaccess`.
2. Las consultas del formulario se envían a `info@estudiojcs.com.ar`, usando esa
   misma casilla como remitente (configurable en `sitio/enviar.php`). Al
   responder el email, la respuesta va directo a quien hizo la consulta.
3. Con el SSL activo, habilitá la redirección a HTTPS en `.htaccess`.
4. Enviá `https://estudiojcs.com.ar/sitemap.xml` en Google Search Console.
5. Creá o actualizá el Perfil de Empresa de Google con los mismos datos de
   contacto (clave para el SEO local).

## Editar contenido

Los textos están en:

- `tools/contenido_servicios.py` → áreas, servicios, preguntas frecuentes y
  motivos del formulario.
- `tools/contenido_articulos.py` → artículos de Información jurídica.
- `tools/build.py` → datos de contacto, equipo, inicio, El Estudio y plantillas.

Después de editar, regenerá el sitio:

```
python3 tools/build.py
```

### Agregar un servicio

Sumá una entrada en `SERVICIOS` (su `slug` será la URL) y agregá ese slug a la
lista `servicios` del área correspondiente en `AREAS`. Se crean automáticamente
la página, el enlace en el menú, el sitemap y los datos estructurados.

### Agregar un artículo

Sumá un elemento a `ARTICULOS`. Para enlazar un servicio dentro del texto usá
`{{s:slug-del-servicio|texto}}`; para otro artículo, `{{a:slug|texto}}`.

### Equipo

Hoy se muestra un bloque genérico con los apellidos de los socios. Para pasar
a perfiles individuales, completá la lista `EQUIPO` en `tools/build.py`; las
fotos van en `sitio/assets/img/equipo/` (ideal `.webp`, 800 × 1000 px).

### Foto del hero

Guardá la imagen en `sitio/assets/img/hero.webp` y en `tools/build.py` cambiá
`HERO_FOTO = None` por `HERO_FOTO = "/assets/img/hero.webp"`.

### Campañas y medición

- Google Tag Manager está activo con el contenedor `GTM-NWPZN5J3` (`GTM_ID` en `tools/build.py`).
- El sitio envía al `dataLayer` los eventos `consulta_enviada`,
  `contacto_whatsapp`, `contacto_telefono` y `contacto_email`.
- La página `/gracias/` permite medir conversiones de formularios.
- Los parámetros `utm_*` y `gclid` de las campañas se guardan y llegan en el
  email de cada consulta.
- Para una landing con motivo preseleccionado: `/contacto/?motivo=Sucesión`.

## Datos del estudio

- Dirección: Lavelle y Talcahuano, Ciudad Autónoma de Buenos Aires (se muestra
  en contacto, pie de página, Política de Privacidad y datos estructurados).
- Equipo: bloque genérico con los apellidos de los socios. Para mostrar perfiles
  individuales, completá la lista `EQUIPO` (ver más arriba).
- Hero: composición con el monograma del logo.

Tipografías: Bodoni Moda y Hanken Grotesk (SIL Open Font License), alojadas en
el propio sitio.
