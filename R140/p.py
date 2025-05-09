#!/usr/bin/env python3
"""
Auto-organizador de descargas
-------------------------------------------
• Vigila una carpeta mediante sondeos periódicos.
• Cuando detecta un archivo nuevo:
    – Crea una subcarpeta con el nombre de la extensión (pdf, jpg, …).
    – Mueve allí el archivo y le añade un sello temporal al nombre.
Ejemplo:
    python organize_downloads_no_watchdog.py --source ~/Downloads --dest ~/Organizado -i 2
Ctrl-C para terminar.
"""
from __future__ import annotations

import argparse
import shutil
import time
from datetime import datetime
from pathlib import Path


def organize_file(src_path: Path, dest_dir: Path, *, now_fn=datetime.now) -> Path:
    """
    Mueve `src_path` a `dest_dir/<ext>/nombre__AAAAMMDD_HHMMSS.ext`.
    Devuelve la ruta destino.
    """
    if not src_path.is_file():
        raise ValueError(f"'{src_path}' no es un archivo")

    ext = src_path.suffix.lower().lstrip(".") or "sin_extension"
    category_dir = dest_dir / ext
    category_dir.mkdir(parents=True, exist_ok=True)

    timestamp = now_fn().strftime("%Y%m%d_%H%M%S")
    new_name = f"{src_path.stem}__{timestamp}{src_path.suffix}"
    target_path = category_dir / new_name

    # Evitar colisiones poco probables:
    counter = 1
    while target_path.exists():
        target_path = category_dir / f"{src_path.stem}__{timestamp}_{counter}{src_path.suffix}"
        counter += 1

    shutil.move(src_path, target_path)
    print(f"✔ {src_path.name} → {target_path.relative_to(dest_dir)}")
    return target_path


def scan_once(source_dir: Path, dest_dir: Path, seen: set[Path]):
    """
    Recorre `source_dir`; para cada archivo que aún no esté en `seen`
    lo organiza y lo añade al conjunto.
    """
    for entry in source_dir.iterdir():
        if entry.is_file() and entry not in seen:
            organize_file(entry, dest_dir)
            seen.add(entry)


def main():
    parser = argparse.ArgumentParser(description="Organiza automáticamente la carpeta de descargas.")
    parser.add_argument("--source", default="~/Downloads", help="Carpeta a vigilar (por defecto ~/Downloads)")
    parser.add_argument("--dest",   default="~/Organizado", help="Carpeta destino (por defecto ~/Organizado)")
    parser.add_argument("-i", "--interval", type=float, default=1.0, help="Segundos entre sondeos (1.0)")
    args = parser.parse_args()

    source_dir = Path(args.source).expanduser()
    dest_dir   = Path(args.dest).expanduser()
    source_dir.mkdir(parents=True, exist_ok=True)
    dest_dir.mkdir(parents=True, exist_ok=True)

    print(f"📂 Observando: {source_dir}")
    print(f"📦 Destino:    {dest_dir}\nCtrl+C para detener.\n")

    already_seen = set(source_dir.iterdir())  # Ignorar lo que ya existe

    try:
        while True:
            scan_once(source_dir, dest_dir, already_seen)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\n⏹  Detenido por el usuario.")


if __name__ == "__main__":
    main()