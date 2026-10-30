# estebi-jr.github.io

Sitio personal de GitHub Pages. Hoy solo sostiene el **puente de Ojalá**: los links antiguos
`estebi-jr.github.io/ojala/…` (de antes de la mudanza a https://miojala.cl, oct 2026) siguen funcionando.

- `ojala/index.html`: el puente. Copia exacta del script al inicio de `index.html` de la app: redirige a
  miojala.cl conservando ruta y parámetros y traspasa una vez lo guardado en el navegador (llaves para editar,
  reservas, listas visitadas, tema). No editar sin revisar la app.
- `404.html`: cualquier ruta que no exista (por ejemplo `/ojala/navidad/`) va a la misma en miojala.cl.
- `index.html`: la raíz manda a miojala.cl. Si algún día este sitio es otra cosa (portafolio), se reemplaza
  este archivo y se conservan `ojala/` y la lógica de `404.html`.

No debe existir un repo con GitHub Pages llamado `ojala`: taparía la carpeta `ojala/` de este sitio.
La app vive en el repo privado `estebi-jr/ojala` (Cloudflare Pages).

© 2026 Esteban. Todos los derechos reservados.
