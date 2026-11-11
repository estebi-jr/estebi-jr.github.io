# estebi-jr.github.io

Portafolio de Esteban (**esteban.dev**): todas mis apps en un solo lugar, con teasers, capturas y la historia de cada una.
Sitio estático: un solo `index.html` (HTML + CSS + JS, sin frameworks ni build) más `assets/`.

En vivo: https://estebi-jr.github.io/

## Estructura
- `index.html`: el portafolio. Todo el contenido vive en el bloque **DATOS** al inicio del `<script>`
  (`PROFILE`, `PROJECTS`, `GRAVEYARD`, `STEPS`, `PROCESS_DEMO`, `TOOLS`, `BANNER`, `UI`), en español e inglés.
- `assets/teasers/<id>.mp4` + `<id>.jpg`: teaser y póster de cada proyecto.
- `assets/shots/<id>/1.webp…`: capturas (442×960).
- `assets/icons/<id>.webp`: ícono de cada app para el iPhone del hero (256px).
- `assets/brand/`: favicon e ícono para iPhone. `assets/og-image.png`: imagen al compartir el link.
- `tools/optimizar_teaser.py`: deja un video, sus capturas y su ícono listos para `assets/`.

## Puente de Ojalá (no tocar sin revisar la app)
Los links antiguos `estebi-jr.github.io/ojala/…` (de antes de la mudanza a https://miojala.cl, oct 2026) siguen funcionando.
- `ojala/index.html`: el puente. Copia exacta del script al inicio de `index.html` de la app: redirige a
  miojala.cl conservando ruta y parámetros y traspasa una vez lo guardado en el navegador. No editar sin revisar la app.
- `404.html`: cualquier ruta que no exista (por ejemplo `/ojala/navidad/`) va a la misma en miojala.cl.
- `index.html`: el script al inicio del `<head>` manda a miojala.cl los links de la raíz con ruta de la app (`#/l/…`).
  Los links del portafolio usan `#id` sin barra (ej. `/#ojala`), así que no se cruzan.

No debe existir un repo con GitHub Pages llamado `ojala`: taparía la carpeta `ojala/` de este sitio.
La app vive en el repo privado `estebi-jr/ojala` (Cloudflare Pages).

© 2026 Esteban. Todos los derechos reservados.
