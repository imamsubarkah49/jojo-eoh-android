#!/usr/bin/env python3
"""Compare the imports a public JoJo EoH shadPS4 log resolves with the NIDs the
gow3-derived runtime already names.

This is a coverage scan, not proof that every named NID has a working
implementation. It separates native modules (libc, libSceLibcInternal,
libSceFios2) from the system libraries the port has to emulate.
"""
from __future__ import annotations

import argparse
import collections
import re
from pathlib import Path

INC_RE = re.compile(r'\{"([^"#]+)#([^"]+)","([^"]+)"\}')
LOG_RE = re.compile(
    r'Stub resolved\s+(\S+)\s+as\s+(\S+)\s+\(lib:\s*([^,]+),\s*mod:\s*([^)]+)\)'
)
NATIVE_LIBS = {'libc', 'libSceLibcInternal', 'libSceFios2'}


def read_inc(path: Path) -> dict[tuple[str, str], str]:
    text = path.read_text(encoding='utf-8', errors='replace')
    return {(nid, lib): name for nid, lib, name in INC_RE.findall(text)}


def read_log(path: Path) -> list[tuple[str, str, str, str]]:
    text = path.read_text(encoding='utf-8', errors='replace')
    return LOG_RE.findall(text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('log', type=Path)
    parser.add_argument('--inc', type=Path, default=Path('src/import_names.inc'))
    parser.add_argument('--out', type=Path, default=Path('docs/jojo-imports.md'))
    args = parser.parse_args()

    known = read_inc(args.inc)
    rows = read_log(args.log)
    unique = {}
    for nid, name, lib, mod in rows:
        unique[(nid, lib.strip())] = name

    by_lib = collections.Counter(lib for _, lib in unique)
    missing = [(nid, lib, name) for (nid, lib), name in unique.items()
               if (nid, lib) not in known]
    missing_hle = [item for item in missing if item[1] not in NATIVE_LIBS]
    missing_native = [item for item in missing if item[1] in NATIVE_LIBS]

    lines = [
        '# JoJo EoH import coverage',
        '',
        f'Source log: `{args.log.as_posix()}`',
        f'Known NIDs in `{args.inc.as_posix()}`: **{len(known)}**',
        f'Unique imports in the log: **{len(unique)}**',
        f'Imports with no matching NID: **{len(missing)}** '
        f'({len(missing_hle)} system/HLE, {len(missing_native)} native)',
        '',
        '## Imports by library',
        '',
        '| Library | Unique imports |',
        '|---|---:|',
    ]
    for lib, count in by_lib.most_common():
        lines.append(f'| `{lib}` | {count} |')

    lines += [
        '',
        '## Missing system NIDs (need an HLE implementation or a deliberate stub)',
        '',
        '| NID | Library | Symbol |',
        '|---|---|---|',
    ]
    for nid, lib, name in sorted(missing_hle, key=lambda x: (x[1], x[2])):
        lines.append(f'| `{nid}` | `{lib}` | `{name}` |')

    lines += [
        '',
        '## Missing native NIDs (libc / libc internal / Fios2)',
        '',
        'These are normally supplied by the game\'s bundled `libc.prx` or '
        '`libSceFios2.prx`; a missing name here usually means the linker did '
        'not see the module, not that the game needs a new runtime function.',
        '',
        '| NID | Library | Symbol |',
        '|---|---|---|',
    ]
    for nid, lib, name in sorted(missing_native, key=lambda x: (x[1], x[2])):
        lines.append(f'| `{nid}` | `{lib}` | `{name}` |')

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'wrote {args.out} ({len(unique)} imports, {len(missing_hle)} missing HLE)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
