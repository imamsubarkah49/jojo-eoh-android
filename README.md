# JoJo's Bizarre Adventure: Eyes of Heaven — Android port

Unofficial Android/ARM64 port of **JoJo's Bizarre Adventure: Eyes of Heaven**
(PS4, `CUSA04909`), built on the Android stack from
[zFitness/gow3_android](https://github.com/zFitness/gow3_android): FEXCore for
x86-64 guest code, the shadPS4 GNM → Vulkan renderer, Turnip, and the existing
Kotlin/Compose launcher.

> **No game files are included.** You need your own dump of `CUSA04909`
> (base + update 01.00 or 01.06). This project is not affiliated with Bandai
> Namco or CyberConnect2.

## Status

This is the first port commit, not a finished build.

- **Baseline:** the same game already runs on the generic Bachata S4 Android
  stack at **25–30 fps on a Poco F5** (Snapdragon 7+ Gen 2 / Adreno 725 / 12 GB).
  That is the performance bar this port has to beat.
- **Done in this fork:** source imported, JoJo identity accepted by the
  launcher, GOW3-only hooks disabled for `CUSA04909`, and the import table
  expanded from a public CUSA04909 shadPS4 log.
- **Not done yet:** first boot with a real dump, the dump-dependent
  `--check-imports` pass, GPU correctness, and on-device performance.

The next milestone is not “write more scaffolding”; it is:

```bash
python scripts/prepare.py <CUSA04909>
python scripts/link_modules.py <CUSA04909>
out/gow3-probe out/boot-linked.bin --app0 <CUSA04909> --check-imports
```

and then removing the first `STOP:`/missing-import line that a real dump
produces.

## What changed from `gow3_android`

| File | Change |
|---|---|
| `src/jojo_import_names.inc` | 84 additional `NID#library → symbol` entries extracted from a public CUSA04909 shadPS4 log |
| `src/jojo_stubs.inc` | 79 optional Np/dialog/voice/JPEG/PNG imports mapped to existing generic handlers |
| `src/runtime.c` | Includes the JoJo import-name table |
| `src/runtime_services.c` | Includes the JoJo stub table; adds `jojo_unsupported` |
| `src/runtime_rtc.c` | `sceRtcParseDateTime`, `sceRtcParseRFC3339`, Windows FILETIME conversions; wires `sceRtcGetCurrentTick` |
| `src/probe.c` | JoJo title fallback; GOW3 cheat hooks skipped for CUSA04909 |
| `patches/JoJo_Eyes_of_Heaven_CUSA04909.xml` | Empty compatibility profile (no byte writes yet) |
| `android-launcher/.../PatchCatalog.kt` | Accepts `CUSA04909` 01.00 / 01.06 |
| `android-launcher/.../strings.xml` | JoJo app name/about/folder text |
| `run.py` | Defaults to `../CUSA04909`; accepts `JOJO_GAME_DIR` |

The import coverage report is in [`docs/jojo-imports.md`](docs/jojo-imports.md).
It lists the 84 system imports and the 67 native imports that the log resolved
but the GOW3 table did not name.

## Build

Use the upstream Android build flow (Linux/WSL2, Android NDK, submodules):

```bash
git submodule update --init --recursive
bash tools/android/build_bionic_deps.sh
bash tools/android/build_bionic.sh
cd android-launcher && ./gradlew :app:assembleDebug
```

The upstream GOW3 README is preserved as [`README.gow3.md`](README.gow3.md) for
the build details and the Android runtime layout. Native binary/library names
still use the upstream `gow3-*` prefix in this first commit; renaming them is
mechanical and is deliberately separate from the runtime work.

## First run with your own dump

1. Put the decrypted `CUSA04909` folder (with `eboot.bin`, `sce_module`,
   `sce_sys`) next to the port, or set `JOJO_GAME_DIR`.
2. Prepare the image with the existing `prepare.py` / `link_modules.py`.
3. Run the probe with `--check-imports` before trying to boot. This is the
   authoritative list of missing functions for *your* eboot version.
4. Boot with `--cpu-only` first to separate CPU/runtime problems from GPU
   problems, then with the GPU enabled.

Do not trust the public log as a complete list: it is a shadPS4 report, not a
dump of your executable. Your `--check-imports` output wins.

## Legal

GPL-2.0-or-later, like the upstream port. Third-party components keep their own
licenses. Do not distribute game files, decrypted executables, firmware, or
patches derived from someone else's dump. Keep the project clearly unofficial.
