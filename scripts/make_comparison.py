#!/usr/bin/env python3
"""Build a before/after comparison image for a yanzhi-baogai diagnosis.

Takes the user's original photo and the AI ceiling preview, and produces a
single side-by-side image with score labels and an explicit AI notice.

Usage:
    python scripts/make_comparison.py \
        --before path/to/original.jpg \
        --after path/to/preview.png \
        --output generated-images/yanzhi-before-after.png \
        --current 7.4 --ceiling 8.0

Requires Pillow (pip install pillow). Output is written locally only and is
git-ignored -- never commit personal photos to GitHub.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("[make_comparison] Pillow is required: pip install pillow")


BG = (250, 248, 245)
INK = (34, 30, 28)
SUB = (110, 100, 95)
ACCENT = (198, 92, 62)
CARD = (255, 255, 255)
NOTICE_BG = (245, 238, 232)


def load_font(size: int):
    candidates = [
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
        "/System/Library/Fonts/PingFang.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


def fit(img: Image.Image, target_h: int) -> Image.Image:
    ratio = target_h / img.height
    resample = getattr(Image, "Resampling", Image).LANCZOS
    return img.resize((max(1, int(img.width * ratio)), target_h), resample)


def build(before: Path, after: Path, output: Path, current: str, ceiling: str) -> None:
    left = Image.open(before).convert("RGB")
    right = Image.open(after).convert("RGB")

    panel_h = 900
    left = fit(left, panel_h)
    right = fit(right, panel_h)

    gap = 48
    pad = 48
    top = 150
    bottom = 150
    width = left.width + gap + right.width + pad * 2
    height = top + panel_h + bottom

    canvas = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(canvas)

    title_font = load_font(46)
    sub_font = load_font(26)
    label_font = load_font(32)
    notice_font = load_font(22)

    title = "颜值上限 · 前后对比"
    tw = draw.textlength(title, font=title_font)
    draw.text(((width - tw) / 2, 38), title, font=title_font, fill=INK)

    subtitle = f"当前 {current}   →   上限 {ceiling}   ·   提升 {round(float(ceiling) - float(current), 1):+.1f}"
    sw = draw.textlength(subtitle, font=sub_font)
    draw.text(((width - sw) / 2, 100), subtitle, font=sub_font, fill=SUB)

    left_x, right_x = pad, pad + left.width + gap
    canvas.paste(left, (left_x, top))
    canvas.paste(right, (right_x, top))

    # Corner labels
    draw.rounded_rectangle(
        (left_x + 16, top + 16, left_x + 232, top + 70), radius=14, fill=(0, 0, 0)
    )
    draw.text((left_x + 30, top + 28), "原始照片", font=label_font, fill=(255, 255, 255))

    draw.rounded_rectangle(
        (right_x + 16, top + 16, right_x + 236, top + 70), radius=14, fill=ACCENT
    )
    draw.text((right_x + 30, top + 28), "AI 上限预览", font=label_font, fill=(255, 255, 255))

    # Center arrow
    arrow_x = left_x + left.width + gap / 2
    arrow_y = top + panel_h / 2
    draw.ellipse(
        (arrow_x - 38, arrow_y - 38, arrow_x + 38, arrow_y + 38), fill=CARD
    )
    draw.polygon(
        [
            (arrow_x - 14, arrow_y - 16),
            (arrow_x + 16, arrow_y),
            (arrow_x - 14, arrow_y + 16),
        ],
        fill=ACCENT,
    )

    notice = "本图含 AI 生成画面 · 分数为娱乐向参考，非客观评价"
    nw = draw.textlength(notice, font=notice_font)
    draw.rounded_rectangle(
        ((width - nw) / 2 - 24, height - 96, (width + nw) / 2 + 24, height - 46),
        radius=12,
        fill=NOTICE_BG,
    )
    draw.text(((width - nw) / 2, height - 86), notice, font=notice_font, fill=SUB)

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)
    print(f"[make_comparison] saved: {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build before/after comparison image.")
    parser.add_argument("--before", required=True, help="original photo path")
    parser.add_argument("--after", required=True, help="AI preview image path")
    parser.add_argument("--output", required=True, help="output image path")
    parser.add_argument("--current", default="7.0", help="current score, e.g. 7.4")
    parser.add_argument("--ceiling", default="8.0", help="ceiling score, e.g. 8.0")
    args = parser.parse_args()

    before, after = Path(args.before), Path(args.after)
    for p in (before, after):
        if not p.exists():
            sys.exit(f"[make_comparison] input not found: {p}")

    build(before, after, Path(args.output), args.current, args.ceiling)


if __name__ == "__main__":
    main()
