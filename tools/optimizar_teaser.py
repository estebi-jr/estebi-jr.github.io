#!/usr/bin/env python3
"""Deja un proyecto listo para assets/ del portafolio.

Uso:
  python3 tools/optimizar_teaser.py teaser.mp4 <id> [--shots 1.png 2.png ...] [--icon icono.png] [--crf 23]

Genera:
  assets/teasers/<id>.mp4   H.264, sin audio, faststart (empieza a verse antes de terminar de bajar)
  assets/teasers/<id>.jpg   póster = primer cuadro, para que el loop no salte al empezar
  assets/shots/<id>/N.webp  capturas a 442×960, en el orden en que las pases
  assets/icons/<id>.webp    ícono a 256px (el CSS redondea las esquinas)

Necesita ffmpeg y Pillow (pip install pillow). Si el MP4 pasa de 8 MB, sube --crf (25 o 26).
"""
import argparse
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def run(cmd):
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('video', type=pathlib.Path)
    ap.add_argument('id', help='id del proyecto: minúsculas, sin espacios (ej. ojala, nota-7)')
    ap.add_argument('--shots', nargs='*', type=pathlib.Path, default=[])
    ap.add_argument('--icon', type=pathlib.Path)
    ap.add_argument('--crf', type=int, default=23)
    a = ap.parse_args()

    teasers = ROOT / 'assets' / 'teasers'
    teasers.mkdir(parents=True, exist_ok=True)
    mp4, jpg = teasers / f'{a.id}.mp4', teasers / f'{a.id}.jpg'
    run(['ffmpeg', '-v', 'error', '-y', '-i', str(a.video), '-an', '-c:v', 'libx264', '-preset', 'veryfast',
         '-crf', str(a.crf), '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(mp4)])
    run(['ffmpeg', '-v', 'error', '-y', '-i', str(a.video), '-frames:v', '1', '-q:v', '4', str(jpg)])
    mb = mp4.stat().st_size / 1e6
    print(f'{mp4.relative_to(ROOT)}  {mb:.1f} MB' + ('  (sobre 8 MB: prueba --crf 25)' if mb > 8 else ''))
    print(f'{jpg.relative_to(ROOT)}')

    if a.shots or a.icon:
        try:
            from PIL import Image
        except ImportError:
            sys.exit('Falta Pillow: pip install pillow')
    if a.shots:
        out = ROOT / 'assets' / 'shots' / a.id
        out.mkdir(parents=True, exist_ok=True)
        for n, src in enumerate(a.shots, 1):
            dst = out / f'{n}.webp'
            Image.open(src).convert('RGB').resize((442, 960), Image.LANCZOS).save(dst, 'WEBP', quality=82, method=6)
            print(dst.relative_to(ROOT))
    if a.icon:
        out = ROOT / 'assets' / 'icons'
        out.mkdir(parents=True, exist_ok=True)
        dst = out / f'{a.id}.webp'
        im = Image.open(a.icon).convert('RGBA')
        w, h = im.size
        # Si el ícono trae esquinas transparentes, las rellena con su propio fondo para que no queden negras
        bg = im.crop((int(w * .11), int(h * .11), int(w * .89), int(h * .89))).resize((w, h), Image.LANCZOS)
        bg.alpha_composite(im)
        bg.convert('RGB').resize((256, 256), Image.LANCZOS).save(dst, 'WEBP', quality=90, method=6)
        print(dst.relative_to(ROOT))


if __name__ == '__main__':
    main()
