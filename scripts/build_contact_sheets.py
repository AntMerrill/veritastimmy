#!/usr/bin/env python3
"""Build labeled contact-sheet grids from a directory of screenshots.

Corrupt/unreadable files (known issue: ~50 of 486 phone screenshots came
off the phone mangled via ifuse, see project_ifuse_iphone_copy_unreliable)
are detected and skipped rather than aborting the whole run. Every skip is
logged to <out_dir>/skipped.txt with the reason. A manifest.tsv in the
output dir maps each sheet file to the images placed on it, in order.

Usage:
    python3 scripts/build_contact_sheets.py <input_dir> <out_dir> \
        [--cols 4] [--rows 6] [--thumb-width 220] [--pattern '*.png']
"""
import argparse
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError

DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})_tb(?:-(\d+))?\.\w+$")


def sort_key(path: Path):
    m = DATE_RE.match(path.name)
    if not m:
        return (path.name, 0)
    date, idx = m.groups()
    return (date, int(idx) if idx else 0)


def load_verified(path: Path):
    """Return an opened Image, or None if the file is corrupt/unreadable."""
    try:
        with Image.open(path) as probe:
            probe.verify()
    except (UnidentifiedImageError, OSError, ValueError, SyntaxError) as e:
        return None, str(e)
    try:
        im = Image.open(path)
        im.load()
        return im.convert("RGB"), None
    except (UnidentifiedImageError, OSError, ValueError, SyntaxError) as e:
        return None, str(e)


def build_sheets(input_dir: Path, out_dir: Path, pattern: str, cols: int, rows: int, thumb_w: int):
    out_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(input_dir.glob(pattern), key=sort_key)
    if not files:
        print(f"No files matching {pattern!r} in {input_dir}", file=sys.stderr)
        return

    per_sheet = cols * rows
    label_h = 22
    pad = 6

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    except Exception:
        font = ImageFont.load_default()

    skipped = []
    manifest = []
    good = []

    for f in files:
        im, err = load_verified(f)
        if im is None:
            skipped.append((f.name, err))
            continue
        ratio = thumb_w / im.width
        thumb = im.resize((thumb_w, int(im.height * ratio)))
        im.close()
        good.append((f.name, thumb))

    thumb_h = max((t.height for _, t in good), default=0)
    sheet_w = cols * thumb_w + (cols + 1) * pad
    sheet_h = rows * (thumb_h + label_h) + (rows + 1) * pad

    for sheet_idx in range(0, len(good), per_sheet):
        chunk = good[sheet_idx : sheet_idx + per_sheet]
        sheet = Image.new("RGB", (sheet_w, sheet_h), "white")
        draw = ImageDraw.Draw(sheet)
        for i, (name, thumb) in enumerate(chunk):
            r, c = divmod(i, cols)
            x = pad + c * (thumb_w + pad)
            y = pad + r * (thumb_h + label_h + pad)
            sheet.paste(thumb, (x, y))
            draw.text((x, y + thumb_h + 2), name, fill="black", font=font)
        out_name = f"sheet_{sheet_idx // per_sheet:03d}.jpg"
        sheet.save(out_dir / out_name, quality=88)
        for name, _ in chunk:
            manifest.append((out_name, name))

    with open(out_dir / "manifest.tsv", "w") as f:
        f.write("sheet\tfilename\n")
        for sheet_name, img_name in manifest:
            f.write(f"{sheet_name}\t{img_name}\n")

    with open(out_dir / "skipped.txt", "w") as f:
        for name, err in skipped:
            f.write(f"{name}\t{err}\n")

    n_sheets = (len(good) + per_sheet - 1) // per_sheet
    print(f"{len(good)} images placed across {n_sheets} sheets in {out_dir}")
    print(f"{len(skipped)} skipped as corrupt/unreadable -> {out_dir / 'skipped.txt'}")
    print(f"manifest -> {out_dir / 'manifest.tsv'}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input_dir", type=Path)
    p.add_argument("out_dir", type=Path)
    p.add_argument("--pattern", default="*.png")
    p.add_argument("--cols", type=int, default=4)
    p.add_argument("--rows", type=int, default=6)
    p.add_argument("--thumb-width", type=int, default=220)
    args = p.parse_args()
    build_sheets(args.input_dir, args.out_dir, args.pattern, args.cols, args.rows, args.thumb_width)


if __name__ == "__main__":
    main()
