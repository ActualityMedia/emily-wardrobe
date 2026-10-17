"""Build the small images the Kindle Fire version uses.

The full-size renders in ../wardrobe are up to 700x700 RGBA. Decoding ~40 of
them at once costs ~80 MB of bitmap memory, which is too much for the
Fire 7 (5th gen) tablet's 1 GB, shared with Fire OS itself. This writes 256 px, palette-reduced copies to
kindle/img. Re-run it after adding items to wardrobe-data.js:

    python3 kindle/build_assets.py
"""
import json
import os
import re
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "img")
MAX_PX = 256


def wardrobe_images():
    src = open(os.path.join(ROOT, "wardrobe-data.js"), encoding="utf-8").read()
    data = json.loads(re.search(r"window\.WARDROBE\s*=\s*(\[.*\])", src, re.S).group(1))
    return sorted({item["image"] for item in data})


def shrink(src, dst):
    im = Image.open(src).convert("RGBA")
    im.thumbnail((MAX_PX, MAX_PX), Image.LANCZOS)
    im = im.quantize(colors=256, method=Image.FASTOCTREE, dither=Image.FLOYDSTEINBERG)
    im.save(dst, optimize=True)


def main():
    os.makedirs(OUT, exist_ok=True)
    before = after = 0
    for rel in wardrobe_images():
        src = os.path.join(ROOT, rel)
        dst = os.path.join(OUT, os.path.basename(rel))
        shrink(src, dst)
        before += os.path.getsize(src)
        after += os.path.getsize(dst)
    print("%d images: %.1f MB -> %.1f MB" % (len(wardrobe_images()), before / 1e6, after / 1e6))


if __name__ == "__main__":
    sys.exit(main())
