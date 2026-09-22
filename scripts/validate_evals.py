#!/usr/bin/env python3
"""Validate repository-native skill eval fixtures."""
from __future__ import annotations

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
errors: list[str] = []
count = 0

for eval_path in sorted(SKILLS.glob("*/evals/eval.json")):
    count += 1
    skill_dir = eval_path.parents[1].name
    try:
        data = json.loads(eval_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{eval_path.relative_to(ROOT)} invalid JSON: {exc}")
        continue

    if data.get("skill") != skill_dir:
        errors.append(f"{eval_path.relative_to(ROOT)} skill must equal directory name '{skill_dir}'")

    if not isinstance(data.get("version"), int) or data["version"] < 1:
        errors.append(f"{eval_path.relative_to(ROOT)} needs integer version >= 1")

    positives = data.get("positive_cases")
    negatives = data.get("negative_cases")
    required = data.get("required_behaviors")
    forbidden = data.get("forbidden_behaviors")

    if not isinstance(positives, list) or not positives:
        errors.append(f"{eval_path.relative_to(ROOT)} needs positive_cases")
    if not isinstance(negatives, list) or not negatives:
        errors.append(f"{eval_path.relative_to(ROOT)} needs negative_cases")
    if not isinstance(required, list) or len(required) < 2:
        errors.append(f"{eval_path.relative_to(ROOT)} needs >=2 required_behaviors")
    if not isinstance(forbidden, list) or len(forbidden) < 1:
        errors.append(f"{eval_path.relative_to(ROOT)} needs forbidden_behaviors")

    ids: set[str] = set()
    for group_name, cases, expected_trigger in [
        ("positive_cases", positives or [], True),
        ("negative_cases", negatives or [], False),
    ]:
        for case in cases:
            if not isinstance(case, dict):
                errors.append(f"{eval_path.relative_to(ROOT)} {group_name} entries must be objects")
                continue
            cid = case.get("id")
            prompt = case.get("prompt")
            trigger = case.get("must_trigger")
            if not cid or not isinstance(cid, str):
                errors.append(f"{eval_path.relative_to(ROOT)} case missing string id")
            elif cid in ids:
                errors.append(f"{eval_path.relative_to(ROOT)} duplicate case id: {cid}")
            else:
                ids.add(cid)
            if not prompt or not isinstance(prompt, str):
                errors.append(f"{eval_path.relative_to(ROOT)} case {cid!r} missing prompt")
            if trigger is not expected_trigger:
                errors.append(
                    f"{eval_path.relative_to(ROOT)} case {cid!r} must_trigger should be {expected_trigger}"
                )

if count == 0:
    errors.append("no skill eval fixtures found")

if errors:
    print("EVAL VALIDATION FAILED")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print("EVAL VALIDATION PASSED")
print(f" - eval fixtures: {count}")
