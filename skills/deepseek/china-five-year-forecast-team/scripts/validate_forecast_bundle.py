#!/usr/bin/env python3
"""Validate the required China five-year forecast report bundle."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


REQUIRED = {
    "00-experiment-and-sources.md": 1200,
    "01-structural-report.md": 2500,
    "02-industry-career-report.md": 2500,
    "03-resident-life-report.md": 2500,
    "04-skeptic-external-report.md": 2500,
    "05-synthesis-report.md": 4000,
    "forecast-registry.csv": 1,
}

EXPERT_HEADINGS = [
    "## 一、总体判断",
    "## 二、支持依据",
    "## 四、P01—P12详细预测",
    "## 六、最强反方与失败条件",
    "## 七、2031年验证",
]

SYNTHESIS_HEADINGS = [
    "## 一、综合判断",
    "## 二、四位专家的共同结论",
    "## 三、四位专家的关键分歧",
    "## 四、P01—P12综合预测",
    "## 五、支持这些判断的主要因果链",
    "## 六、外部因素如何传导到普通人",
    "## 七、最可能推翻报告的变化",
    "## 八、2031年验证与评分",
]


def validate_markdown(path: Path, minimum: int, headings: list[str], errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    compact_length = len("".join(text.split()))
    if compact_length < minimum:
        errors.append(f"{path.name}: content too short ({compact_length} < {minimum})")
    for heading in headings:
        if heading not in text:
            errors.append(f"{path.name}: missing heading {heading!r}")
    for number in range(1, 13):
        item = f"P{number:02d}"
        if item not in text:
            errors.append(f"{path.name}: missing forecast item {item}")
    if text.count("http") < 6:
        errors.append(f"{path.name}: fewer than six direct source links")


def validate_registry(path: Path, errors: list[str]) -> None:
    required_columns = [
        "id",
        "structural",
        "industry_career",
        "resident_life",
        "skeptic_external",
        "ensemble",
        "direction",
        "disagreement",
        "target_date",
    ]
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != required_columns:
            errors.append(
                f"{path.name}: columns must be exactly {','.join(required_columns)}"
            )
            return
        rows = list(reader)
    if len(rows) != 12:
        errors.append(f"{path.name}: expected 12 rows, found {len(rows)}")
    ids = [row.get("id") for row in rows]
    expected_ids = [f"P{number:02d}" for number in range(1, 13)]
    if ids != expected_ids:
        errors.append(f"{path.name}: ids must run from P01 through P12 in order")
    for row in rows:
        for column in [
            "structural",
            "industry_career",
            "resident_life",
            "skeptic_external",
            "ensemble",
        ]:
            try:
                value = float(row[column])
            except (TypeError, ValueError):
                errors.append(f"{path.name}: {row.get('id')} has invalid {column}")
                continue
            if not 0 <= value <= 1:
                errors.append(
                    f"{path.name}: {row.get('id')} {column} must be between 0 and 1"
                )


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_forecast_bundle.py <bundle-directory>", file=sys.stderr)
        return 2

    bundle = Path(sys.argv[1]).expanduser().resolve()
    errors: list[str] = []
    if not bundle.is_dir():
        print(f"bundle directory does not exist: {bundle}", file=sys.stderr)
        return 2

    for filename in REQUIRED:
        if not (bundle / filename).is_file():
            errors.append(f"missing required file: {filename}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    for filename, minimum in REQUIRED.items():
        path = bundle / filename
        if filename.startswith(("01-", "02-", "03-", "04-")):
            validate_markdown(path, minimum, EXPERT_HEADINGS, errors)
        elif filename == "05-synthesis-report.md":
            validate_markdown(path, minimum, SYNTHESIS_HEADINGS, errors)
        elif filename == "00-experiment-and-sources.md":
            text = path.read_text(encoding="utf-8")
            if len("".join(text.split())) < minimum:
                errors.append(f"{filename}: content too short")
            for required_term in ["信息截止", "实际执行", "预测终点", "模型", "来源"]:
                if required_term not in text:
                    errors.append(f"{filename}: missing metadata term {required_term}")
        elif filename == "forecast-registry.csv":
            validate_registry(path, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: forecast bundle validated at {bundle}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
