from __future__ import annotations

from pathlib import Path
from collections.abc import Iterator

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}


def iter_images(path: str | Path) -> Iterator[Path]:
    """Yield image paths from a file or directory tree."""
    p = Path(path)
    if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES:
        yield p
    elif p.is_dir():
        for child in sorted(p.rglob("*")):
            if child.is_file() and child.suffix.lower() in IMAGE_SUFFIXES:
                yield child
