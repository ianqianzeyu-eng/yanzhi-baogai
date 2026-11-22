#!/usr/bin/env python3
"""Compute current / ceiling scores and rank improvement levers for yanzhi-baogai.

Usage:
    python scripts/score.py --input examples/sample-input.json
    cat input.json | python scripts/score.py

Input JSON:
{
  "scores": {"bones": 7.0, "features": 7.5, "skin": 6.5,
             "headwear": 5.0, "style": 5.5, "camera": 4.5},
  "ceiling_scores": {"headwear": 8.0, "style": 8.0, "camera": 8.5},
  "notes": {"bones": "正面照，三庭大致均衡"}
}

Output: JSON with current, ceiling, gap, per-dimension details and top_levers.
All scores are entertainment-only estimates, not objective judgments.
"""

import argparse
import json
import sys

WEIGHTS = {
    "bones": 0.35,
    "features": 0.20,
    "skin": 0.10,
    "headwear": 0.15,
    "style": 0.10,
    "camera": 0.10,
}

LABELS = {
    "bones": "骨相比例",
    "features": "五官与表情",
    "skin": "皮肤与状态",
    "headwear": "头面修饰",
    "style": "穿搭与色彩",
    "camera": "镜头与光影",
}

# How far a factor can realistically move with non-medical changes.
DEFAULT_UPLIFT = {
    "bones": 0.0,
    "features": 0.0,
    "skin": 0.8,
    "headwear": 2.5,
    "style": 2.5,
    "camera": 3.0,
}
CEILING_CAP = 9.0

DISCLAIMER = "娱乐向参考，受拍摄角度与光线影响，不构成客观评价或效果承诺。"


def clamp_score(value, field):
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{field} must be a number, got {value!r}")
    if not 0.0 <= number <= 10.0:
        raise ValueError(f"{field} must be between 0 and 10, got {number}")
    return round(number, 1)


def compute(payload):
    scores = payload.get("scores")
    if not isinstance(scores, dict):
        raise ValueError("Input must contain a 'scores' object")

    unknown = set(scores) - set(WEIGHTS)
    if unknown:
        raise ValueError(f"Unknown score keys: {sorted(unknown)}")
    missing = set(WEIGHTS) - set(scores)
    if missing:
        raise ValueError(f"Missing score keys: {sorted(missing)}")

    current_scores = {k: clamp_score(v, k) for k, v in scores.items()}
    ceiling_input = payload.get("ceiling_scores", {}) or {}
    if not isinstance(ceiling_input, dict):
        raise ValueError("'ceiling_scores' must be an object")
    unknown_ceiling = set(ceiling_input) - set(WEIGHTS)
    if unknown_ceiling:
        raise ValueError(f"Unknown ceiling score keys: {sorted(unknown_ceiling)}")

    ceiling_scores = {}
    for key in WEIGHTS:
        default = min(CEILING_CAP, current_scores[key] + DEFAULT_UPLIFT[key])
        ceiling_scores[key] = clamp_score(ceiling_input.get(key, default), key)
        if ceiling_scores[key] < current_scores[key]:
            raise ValueError(f"ceiling_scores.{key} cannot be lower than current score")

    notes = payload.get("notes", {}) or {}
    dimensions = []
    for key, weight in WEIGHTS.items():
        delta = round(ceiling_scores[key] - current_scores[key], 1)
        dimensions.append({
            "key": key,
            "label": LABELS[key],
            "weight": weight,
            "current": current_scores[key],
            "ceiling": ceiling_scores[key],
            "delta": delta,
            "weighted_gain": round(delta * weight, 3),
            "note": notes.get(key, ""),
        })

    current = round(sum(d["current"] * d["weight"] for d in dimensions), 1)
    ceiling = round(sum(d["ceiling"] * d["weight"] for d in dimensions), 1)
    gap = round(ceiling - current, 1)

    levers = sorted(
        [d for d in dimensions if d["delta"] > 0],
        key=lambda d: (-d["weighted_gain"], d["key"]),
    )

    return {
        "current": current,
        "ceiling": ceiling,
        "gap": gap,
        "dimensions": dimensions,
        "top_levers": [
            {"key": d["key"], "label": d["label"], "gain": d["weighted_gain"],
             "from": d["current"], "to": d["ceiling"]}
            for d in levers[:3]
        ],
        "disclaimer": DISCLAIMER,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="Path to input JSON file; reads stdin if omitted")
    args = parser.parse_args()

    try:
        if args.input:
            with open(args.input, "r", encoding="utf-8") as handle:
                payload = json.load(handle)
        else:
            payload = json.load(sys.stdin)
        result = compute(payload)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
