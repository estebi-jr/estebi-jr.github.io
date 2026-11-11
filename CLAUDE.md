# Portafolio esteban.dev — guía para Claude

Este repo es la fuente de verdad del portafolio de Esteban (antes lo era el artefacto de Claude).
GitHub Pages publica `main` en https://estebi-jr.github.io/ un minuto después de cada push.

## Reglas
- Sitio estático: un solo `index.html` + `assets/`. Sin frameworks, sin build, sin dependencias nuevas.
- Contenido solo en el bloque DATOS del `<script>`. Todo texto es `{ es, en }`: cada cambio de copy va en los dos idiomas.
- Diseño monocromo; el color lo ponen teasers, capturas e íconos (`tint`). Colores siempre como tokens en `:root`,
  redefinidos en los dos bloques oscuros. Tipografías: Bricolage Grotesque, Geist, Geist Mono.
- Copy en español chileno neutro, primera persona, frases cortas. Sin emojis en la página.
- Crédito a la IA: los proyectos no dicen "con Claude" ni "con Claude Code". La IA aparece solo en "Cómo trabajo"
  y en la lista de herramientas. Sin detalles internos por proyecto (backends, servicios, "usado en").
- Respetar `prefers-reduced-motion`. El cursor propio solo con mouse.
- No tocar `ojala/`, `404.html` ni el script del `<head>` de `index.html` sin leer el README (puente de Ojalá).

## Antes de hacer push
Probar a 390px y 1440px, en claro y oscuro, en ES y EN (`?lang=en`): consola sin errores, sin scroll horizontal,
y que carguen teasers, capturas e íconos (servir la carpeta con `python3 -m http.server`).

## Agregar o actualizar un proyecto
1. `python3 tools/optimizar_teaser.py teaser.mp4 <id> --shots 1.png 2.png … --icon icono.png`
2. Copiar un bloque de `PROJECTS` en `index.html` y ajustar `id`, `name`, `kind`, `year`, `tint`, textos,
   `stack`, `url`, `icon`, `video`, `poster`, `shots`. El orden del arreglo es el orden en la página y en el iPhone.
3. Proyectos descartados van en `GRAVEYARD` (agregan `cause` y `lesson`).

## Artefacto de Claude (opcional)
https://claude.ai/artifact/6WJkUfKFUgMJ1ZGBBZUdDi es un espejo para ver y comentar dentro de Claude.
Para actualizarlo: publicar el contenido de `index.html` sin `<!doctype>`, `<html>`, `<head>` ni `<body>`
(el artefacto los agrega) y subir los archivos de `assets/` que cambiaron.
