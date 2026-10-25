#!/usr/bin/env python3
"""Package the JoJo port's changed/new files relative to the upstream Android tag.

The result is meant to be uploaded over a fork of zFitness/gow3_android, which
already has the FEX/GPU submodules. It deliberately contains no .git directory
and no build outputs.
"""
from __future__ import annotations

import hashlib
import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT.parent / 'vendor' / 'gow3_android-2.1.7-bionic-v4'
OUT = ROOT.parent / 'jojo-port-changed-files.zip'


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if not UPSTREAM.is_dir():
        raise SystemExit(f'upstream source not found: {UPSTREAM}')
    changed: list[Path] = []
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if rel.parts[0] in {'.git', 'out', '.local-deps'}:
            continue
        if path.suffix in {'.pyc'} or '__pycache__' in rel.parts:
            continue
        upstream = UPSTREAM / rel
        if not upstream.is_file() or digest(path) != digest(upstream):
            changed.append(rel)

    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as archive:
        for rel in changed:
            archive.write(ROOT / rel, rel.as_posix())
    print(f'{OUT} ({OUT.stat().st_size:,} bytes, {len(changed)} files)')
    for rel in changed:
        print(rel.as_posix())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
