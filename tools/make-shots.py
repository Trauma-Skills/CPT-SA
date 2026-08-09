#!/usr/bin/env python3
"""Derive the published walkthrough screenshots from the raw captures.

Three sets exist, and only the last two are committed:

    docs/img/raw/     native window captures, gitignored (see .gitignore)
    docs/img/         cropped to the action, downscaled for the web
    docs/img/focus/   the same crop, with the control that matters ringed

Run from anywhere:  python3 tools/make-shots.py

Coordinates below are in *raw pixel space* (the captures are Retina, so roughly
2x the logical window). If a shot is retaken at a different window size, its
numbers need redoing — `--grid` writes a ruled copy of each raw into
docs/img/.grid/ to make that quick.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "docs" / "img" / "raw"
CROP_OUT = ROOT / "docs" / "img"
FOCUS_OUT = ROOT / "docs" / "img" / "focus"

MAX_WIDTH = 1600  # ~2.5x the 640px measure the page renders these at

# The mark is a ring and nothing else: no dimming veil, so the surrounding UI
# is never degraded. It has to be baked into the PNG rather than drawn in CSS
# because Markdown has no CSS — this is the image README.md and any other plain
# renderer shows. The page animates it by cross-fading this file against the
# plain crop, which reads as the ring breathing.
VEIL = None  # set to (r, g, b, a) to dim everything outside the marks again
RING = (125, 58, 68)  # the page's own plum (--care), so the mark belongs to
#                       the design rather than sitting on top of it
PAD = 16  # breathing room between a control and the ring around it
RADIUS = 16
RING_W = 5  # ~2px once the crop is scaled down to page width


# crop: (left, top, right, bottom) in raw pixels
# focus: rectangles inside the same raw space; [] means "no overlay needed"
SHOTS: dict[str, dict] = {
    "02-project-or-folder.png": {
        "crop": (684, 400, 2248, 1230),
        "focus": [
            (898, 806, 1139, 863),  # Chat / Cowork toggle
            (1800, 807, 2015, 861),  # Opus 5
            (835, 911, 1130, 963),  # Project or folder
        ],
    },
    "03-create-new-project.png": {
        "crop": (728, 437, 2212, 1193),
        "focus": [(844, 986, 1314, 1039)],  # Create new project
    },
    "04-create-project.png": {
        "crop": (620, 300, 2200, 1500),
        "focus": [(943, 1075, 1171, 1120)],  # Use a folder
    },
    "05-folder.png": {
        "crop": (423, 409, 2399, 1404),
        "focus": [
            (1181, 498, 1641, 546),  # the folder itself
            (524, 1266, 701, 1312),  # New Folder
        ],
    },
    "06-folder-permissions.png": {
        "crop": (700, 380, 2250, 1330),
        "focus": [(1376, 1030, 1612, 1094)],  # Always allow
    },
    "07-project-details.png": {
        "crop": (873, 276, 2037, 1586),
        "focus": [(1683, 1427, 1925, 1483)],  # Create project
    },
    "08-automatic-approve.png": {
        "crop": (291, 189, 1833, 960),
        "focus": [(695, 752, 1149, 803)],  # Automatically approve
    },
    # Retaken 2026-08-10 at a tighter framing than the other raws (1456x882,
    # already composer-centred), so the crop is the full frame.
    "09-paste.png": {
        "crop": (0, 0, 1456, 882),
        "focus": [
            (100, 205, 875, 255),  # the pasted install message
            (1305, 315, 1367, 377),  # send
        ],
    },
}


def downscale(img: Image.Image) -> Image.Image:
    if img.width <= MAX_WIDTH:
        return img
    h = round(img.height * MAX_WIDTH / img.width)
    return img.resize((MAX_WIDTH, h), Image.LANCZOS)


def with_focus(img: Image.Image, rects: list[tuple[int, int, int, int]]) -> Image.Image:
    """Mark `rects`: a ring around each, and optionally a veil over the rest."""
    out = img.convert("RGBA")

    if VEIL:
        mask = Image.new("L", out.size, 255)  # 255 = veil applies here
        carve = ImageDraw.Draw(mask)
        for r in rects:
            carve.rounded_rectangle(pad(r), radius=RADIUS, fill=0)

        veil = Image.new("RGBA", out.size, VEIL[:3] + (0,))
        veil.putalpha(mask.point(lambda v: v * VEIL[3] // 255))
        out = Image.alpha_composite(out, veil)

    if RING:
        ring = ImageDraw.Draw(out)
        for r in rects:
            ring.rounded_rectangle(pad(r), radius=RADIUS, outline=RING + (255,), width=RING_W)
    return out.convert("RGB")


def pad(r: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return (r[0] - PAD, r[1] - PAD, r[2] + PAD, r[3] + PAD)


def rebase(r: tuple[int, int, int, int], crop: tuple[int, int, int, int]):
    return (r[0] - crop[0], r[1] - crop[1], r[2] - crop[0], r[3] - crop[1])


def grid(raw: pathlib.Path, name: str) -> None:
    """Write a ruled copy of a raw capture, for working out new coordinates."""
    out_dir = CROP_OUT / ".grid"
    out_dir.mkdir(parents=True, exist_ok=True)
    img = Image.open(raw).convert("RGB")
    d = ImageDraw.Draw(img)
    for x in range(0, img.width, 100):
        heavy = x % 500 == 0
        d.line([(x, 0), (x, img.height)], fill=(255, 0, 0) if heavy else (255, 170, 170), width=2 if heavy else 1)
        if heavy:
            d.text((x + 6, 6), str(x), fill=(255, 0, 0))
    for y in range(0, img.height, 100):
        heavy = y % 500 == 0
        d.line([(0, y), (img.width, y)], fill=(0, 0, 255) if heavy else (170, 170, 255), width=2 if heavy else 1)
        if heavy:
            d.text((6, y + 6), str(y), fill=(0, 0, 255))
    img.save(out_dir / name)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid", action="store_true", help="also write ruled raws to docs/img/.grid/")
    args = ap.parse_args()

    if not RAW.is_dir():
        print(f"no raw captures at {RAW}", file=sys.stderr)
        return 1

    FOCUS_OUT.mkdir(parents=True, exist_ok=True)
    missing = []

    for name, spec in SHOTS.items():
        src = RAW / name
        if not src.exists():
            missing.append(name)
            continue
        if args.grid:
            grid(src, name)

        raw = Image.open(src).convert("RGB")
        box = spec["crop"]
        cropped = raw.crop(box)

        downscale(cropped).save(CROP_OUT / name, optimize=True)

        rects = [rebase(r, box) for r in spec["focus"]]
        focused = with_focus(cropped, rects) if rects else cropped
        downscale(focused).save(FOCUS_OUT / name, optimize=True)

        w, h = downscale(cropped).size
        print(f"{name:32} {raw.width}x{raw.height} -> {w}x{h}" + ("" if rects else "  (no overlay)"))

    for name in missing:
        print(f"missing raw capture: {name}", file=sys.stderr)
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
