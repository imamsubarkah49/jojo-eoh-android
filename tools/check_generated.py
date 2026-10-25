#!/usr/bin/env python3
"""Sanity-check the generated JoJo import tables before a native build."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def entries(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding='utf-8')
    return re.findall(r'\{"([^"]+)","([^"]+)"\}', text)


def main() -> int:
    base = entries(ROOT / 'src/import_names.inc')
    jojo = entries(ROOT / 'src/jojo_import_names.inc')
    stubs = re.findall(
        r'\{"([^"]+)",\s*(\w+)\}',
        (ROOT / 'src/jojo_stubs.inc').read_text(encoding='utf-8'),
    )
    services = (ROOT / 'src/runtime_services.c').read_text(encoding='utf-8')
    rtc = (ROOT / 'src/runtime_rtc.c').read_text(encoding='utf-8')

    base_nids = {nid for nid, _ in base}
    jojo_nids = [nid for nid, _ in jojo]
    dup_base = sorted(set(jojo_nids) & base_nids)
    dup_jojo = sorted({nid for nid in jojo_nids if jojo_nids.count(nid) > 1})

    defined = set(re.findall(r'static\s+ABI\s+\w+\s+(\w+)\s*\(', services))
    table_names = set(re.findall(r'\{"(sce[^"]+)"\s*,', services))
    missing_handlers = sorted({handler for _, handler in stubs if handler not in defined})
    duplicate_table = sorted({name for name, _ in stubs} & table_names)

    rtc_names = set(re.findall(r'\{"(sceRtc[^"]+)"\s*,', rtc))
    missing_rtc = sorted({name for _, name in jojo if name.startswith('sceRtc') and name not in rtc_names})

    problems = []
    if dup_base:
        problems.append(f'duplicate NIDs already in import_names.inc: {len(dup_base)}')
    if dup_jojo:
        problems.append(f'duplicate NIDs inside jojo_import_names.inc: {len(dup_jojo)}')
    if missing_handlers:
        problems.append(f'stub handlers not defined in runtime_services.c: {missing_handlers}')
    if duplicate_table:
        problems.append(f'stub symbols already in runtime_services.c: {duplicate_table}')
    if missing_rtc:
        problems.append(f'RTC symbols not in runtime_rtc.c: {missing_rtc}')

    print(f'base NIDs: {len(base)}')
    print(f'jojo NIDs: {len(jojo)}')
    print(f'jojo stubs: {len(stubs)}')
    if problems:
        print('\n'.join(problems))
        return 1
    print('OK: no duplicate NIDs, all stub handlers defined, all RTC symbols wired')
    return 0


if __name__ == '__main__':
    sys.exit(main())
