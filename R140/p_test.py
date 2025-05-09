
from pathlib import Path
from datetime import datetime
import io
import contextlib

import pytest
import t139tg.p as org


# ────────────────────────────────────────────────
# Utilidades auxiliares
# ────────────────────────────────────────────────
class FixedDatetime(datetime):
    """Devuelve siempre la misma marca temporal para que los tests sean deterministas."""
    @classmethod
    def now(cls):
        return cls(2025, 1, 2, 3, 4, 5)   # 2025-01-02 03:04:05


def make_file(folder: Path, name: str, data: bytes = b"x") -> Path:
    path = folder / name
    path.write_bytes(data)
    return path


def run_organize(src: Path, dest: Path, now_cls=datetime):
    """Organiza un archivo capturando stdout."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        result = org.organize_file(src, dest, now_fn=now_cls.now)
    return result, buf.getvalue()


# ────────────────────────────────────────────────
# Tests parametrizados
# ────────────────────────────────────────────────
@pytest.mark.parametrize(
    "filename,subdir,ext",
    [
        ("informe.pdf",        "pdf",          ".pdf"),
        ("README",             "sin_extension",""),
        ("FOTO.JPG",           "jpg",          ".JPG"),
        ("diseño de logo.png", "png",          ".png"),
    ],
)
def test_organiza_archivo(tmp_path, filename, subdir, ext):
    src_dir = tmp_path / "Downloads"
    dst_dir = tmp_path / "Organizado"
    src_dir.mkdir(); dst_dir.mkdir()

    original = make_file(src_dir, filename)
    target, salida = run_organize(original, dst_dir, FixedDatetime)

    timestamp = FixedDatetime.now().strftime("%Y%m%d_%H%M%S")
    esperado  = dst_dir / subdir / f"{Path(filename).stem}__{timestamp}{ext}"

    assert target == esperado and target.exists()
    assert not original.exists()
    assert f"✔ {Path(filename).name}" in salida


# ────────────────────────────────────────────────
# Casos límite
# ────────────────────────────────────────────────
def test_ignora_directorios(tmp_path):
    src_dir = tmp_path / "Downloads"; dst_dir = tmp_path / "Organizado"
    src_dir.mkdir(); dst_dir.mkdir()
    carpeta = src_dir / "Subcarpeta"; carpeta.mkdir()

    already_seen = set()
    org.scan_once(src_dir, dst_dir, already_seen)

    assert not any(dst_dir.rglob("*")), "No debería mover directorios"


def test_evitar_colision(tmp_path):
    src_dir = tmp_path / "Downloads"
    dst_dir = tmp_path / "Organizado"
    src_dir.mkdir(); dst_dir.mkdir()

    f1 = make_file(src_dir, "dup.txt", b"uno")
    class T1(FixedDatetime): pass
    t1, _ = run_organize(f1, dst_dir, T1)

    f2 = make_file(src_dir, "dup.txt", b"dos")
    class T2(FixedDatetime):
        @classmethod
        def now(cls):             # +1 s
            return cls(2025, 1, 2, 3, 4, 6)

    t2, _ = run_organize(f2, dst_dir, T2)

    assert t1.exists() and t2.exists()
    assert t1.name != t2.name



def test_crea_subcarpeta_si_no_existe(tmp_path):
    src_dir = tmp_path / "Downloads"; dst_dir = tmp_path / "Organizado"
    src_dir.mkdir(); dst_dir.mkdir()

    archivo = make_file(src_dir, "nuevo.ext")
    run_organize(archivo, dst_dir, FixedDatetime)

    assert (dst_dir / "ext").is_dir(), "La subcarpeta <ext> no se creó"