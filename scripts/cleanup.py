#!/usr/bin/env python3
"""Remove leftover generated images from the previous yanzhi-baogai run.

AI previews and before/after comparison images contain a person's face. They are
stored only in a local ``generated-images/`` directory (git-ignored) and must
never be committed to GitHub. This script is called at the START of every skill
run so that last time's images are automatically cleared.

Usage:
    python scripts/cleanup.py
    python scripts/cleanup.py --dir generated-images
    python scripts/cleanup.py --dry-run
    python scripts/cleanup.py --keep 1        # keep the newest image
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp"}
KEEP_FILES = {".gitkeep", "README.md"}


def cleanup(directory: Path, dry_run: bool = False, keep: int = 0) -> int:
    if not directory.exists():
        print(f"[cleanup] nothing to clean: {directory} does not exist")
        return 0

    images = sorted(
        (
            p
            for p in directory.iterdir()
            if p.is_file()
            and p.suffix.lower() in IMAGE_SUFFIXES
            and p.name not in KEEP_FILES
        ),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )

    targets = images[keep:] if keep > 0 else images
    if not targets:
        print(f"[cleanup] no leftover images in {directory}")
        return 0

    for p in targets:
        if dry_run:
            print(f"[cleanup] would remove: {p.name}")
        else:
            try:
                p.unlink()
                print(f"[cleanup] removed: {p.name}")
            except OSError as exc:
                print(f"[cleanup] FAILED to remove {p.name}: {exc}", file=sys.stderr)

    verb = "would remove" if dry_run else "removed"
    print(f"[cleanup] {verb} {len(targets)} image(s) from {directory}")
    return len(targets)


def main() -> None:
    parser = argparse.ArgumentParser(description="Clear previous run's generated images.")
    parser.add_argument(
        "--dir",
        default="generated-images",
        help="image directory to clean (default: generated-images)",
    )
    parser.add_argument("--dry-run", action="store_true", help="list files without deleting")
    parser.add_argument(
        "--keep",
        type=int,
        default=0,
        help="keep the newest N images instead of deleting all (default: 0)",
    )
    args = parser.parse_args()

    cleanup(Path(args.dir), dry_run=args.dry_run, keep=max(0, args.keep))


if __name__ == "__main__":
    main()
