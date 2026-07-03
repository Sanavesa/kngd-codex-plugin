#!/usr/bin/env python3
"""
package_for_itch.py — zip a zero-build game for itch.io HTML5 upload.

Produces a zip with index.html at the ROOT of the archive (itch requires this),
including assets and any sibling files the game needs. Excludes VCS/editor/build junk
and the output folder itself. No third-party dependencies. Python 3.8+.

Usage:
    python3 package_for_itch.py [GAME_DIR] [-o OUT_ZIP]

Defaults:
    GAME_DIR = current directory
    OUT_ZIP  = <GAME_DIR>/submission/game.zip

itch.io serves games over HTTPS inside an iframe, so a zero-build game (engine from a CDN)
runs there unchanged. This script also warns about the two things that DO differ on itch:
  * http:// subresources  -> blocked as mixed content (itch is https)
  * https:// CDN links    -> load fine on itch (it's online); the note just flags them
"""

import argparse
import os
import re
import sys
import zipfile

EXCLUDE_DIRS = {".git", "node_modules", "__pycache__", ".vscode", ".idea",
                ".cache", "dist", "build", "submission"}
EXCLUDE_FILES = {".DS_Store", "Thumbs.db", "AGENTS.md", "PROGRESS.md"}
SCAN_EXTS = (".html", ".htm", ".js", ".mjs", ".css")

# subresource-ish attributes/refs where a URL scheme matters on itch
HTTP_MIXED = re.compile(r"""["'(=]\s*(http://[^"')\s]+)""", re.I)
HTTPS_CDN = re.compile(r"""["'(=]\s*(https://[^"')\s]+)""", re.I)


def human(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} B"
        n /= 1024


def collect(game_dir, out_abs):
    files = []
    for dirpath, dirnames, filenames in os.walk(game_dir):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for name in filenames:
            if name in EXCLUDE_FILES or name.lower().endswith(".zip"):
                continue
            full = os.path.join(dirpath, name)
            if os.path.abspath(full) == out_abs:
                continue
            files.append(full)
    return files


def scan_schemes(game_dir, files):
    mixed, cdns = [], set()
    for full in files:
        if not full.lower().endswith(SCAN_EXTS):
            continue
        rel = os.path.relpath(full, game_dir)
        try:
            with open(full, "r", encoding="utf-8", errors="replace") as fh:
                for i, line in enumerate(fh, 1):
                    for m in HTTP_MIXED.finditer(line):
                        mixed.append((rel, i, m.group(1)))
                    for m in HTTPS_CDN.finditer(line):
                        cdns.add(m.group(1).split("?")[0])
        except OSError:
            pass
    return mixed, sorted(cdns)


def main(argv):
    ap = argparse.ArgumentParser(description="Package a zero-build game for itch.io")
    ap.add_argument("game_dir", nargs="?", default=os.getcwd())
    ap.add_argument("-o", "--out", default=None, help="output zip path")
    args = ap.parse_args(argv[1:])

    game_dir = os.path.abspath(args.game_dir)
    if not os.path.isdir(game_dir):
        print(f"error: not a directory: {game_dir}", file=sys.stderr)
        return 2

    out = args.out or os.path.join(game_dir, "submission", "game.zip")
    out = os.path.abspath(out)
    out_abs = out

    # index.html must be at the game root -> it becomes the zip root entry
    if not os.path.isfile(os.path.join(game_dir, "index.html")):
        nested = []
        for dp, dn, fn in os.walk(game_dir):
            dn[:] = [d for d in dn if d not in EXCLUDE_DIRS]
            if "index.html" in fn and os.path.abspath(dp) != game_dir:
                nested.append(os.path.relpath(os.path.join(dp, "index.html"), game_dir))
        print("ERROR: no index.html at the game root.", file=sys.stderr)
        if nested:
            print(f"       Found index.html deeper in: {', '.join(nested)}", file=sys.stderr)
            print("       itch needs index.html at the ROOT of the zip. Point this script at "
                  "that folder, or move the game up.", file=sys.stderr)
        return 1

    files = collect(game_dir, out_abs)
    mixed, cdns = scan_schemes(game_dir, files)

    os.makedirs(os.path.dirname(out), exist_ok=True)
    total_raw = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for full in sorted(files):
            arc = os.path.relpath(full, game_dir)   # index.html at zip root
            zf.write(full, arc)
            try:
                total_raw += os.path.getsize(full)
            except OSError:
                pass

    zip_size = os.path.getsize(out)

    print(f"packaged {len(files)} file(s) -> {out}")
    print(f"  uncompressed: {human(total_raw)}   zip: {human(zip_size)}")
    print(f"  index.html is at the zip root: yes")

    warned = False
    if mixed:
        warned = True
        print("\n  [WARN] http:// subresources are BLOCKED on itch (mixed content). Switch to https:// or vendor locally:")
        for rel, ln, url in mixed[:12]:
            print(f"         {rel}:{ln}  {url}")
    if cdns:
        print("\n  [note] game loads from these CDNs (expected — Phaser/three.js load this way):")
        for u in cdns[:12]:
            print(f"         {u}")
        print("         These load fine on itch (it's online). Keep every URL https:// and pin the "
              "engine version so a new release can't change the game.")
    if zip_size > 500 * 1024 * 1024:
        warned = True
        print(f"\n  [WARN] zip is {human(zip_size)} — over itch's practical size; trim assets.")
    elif zip_size > 100 * 1024 * 1024:
        print(f"\n  [note] zip is {human(zip_size)} — large for an HTML5 jam entry; consider trimming.")

    print("\nNext: upload this zip to itch, tick \"This file will be played in the browser\".")
    if mixed and warned:
        print("Fix the mixed-content WARN(s) first, or the game will fail to load resources on itch.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
