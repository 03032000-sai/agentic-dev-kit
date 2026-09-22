#!/usr/bin/env python3
"""Build a deterministic index of repository-native agentic assets."""
from __future__ import annotations

from argparse import ArgumentParser
from hashlib import sha256
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)

SPECS = [
    ("copilot-agent", ".github/agents/*.agent.md"),
    ("copilot-prompt", ".github/prompts/*.prompt.md"),
    ("copilot-instruction", ".github/instructions/*.instructions.md"),
    ("canonical-skill", ".agents/skills/*/SKILL.md"),
    ("claude-agent", ".claude/agents/*.md"),
    ("claude-skill", ".claude/skills/*/SKILL.md"),
]


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FM.search(text)
    if not match:
        raise ValueError(f"missing frontmatter: {path.relative_to(ROOT)}")
    values: dict[str, str] = {}
    for raw in match.group(1).splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def fallback_name(kind: str, path: Path) -> str:
    name = path.name
    for suffix in (".agent.md", ".prompt.md", ".instructions.md", ".md"):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
            break
    if name == "SKILL":
        name = path.parent.name
    return name


def build_index() -> dict:
    assets: list[dict] = []
    namespace_seen: set[tuple[str, str]] = set()

    for kind, pattern in SPECS:
        for path in sorted(ROOT.glob(pattern)):
            if not path.is_file():
                continue
            fm = parse_frontmatter(path)
            name = fm.get("name") or fallback_name(kind, path)
            description = fm.get("description")
            apply_to = fm.get("applyTo")

            namespace = (kind, name)
            if namespace in namespace_seen:
                raise ValueError(f"duplicate asset name in {kind}: {name}")
            namespace_seen.add(namespace)

            content = path.read_bytes()
            item = {
                "type": kind,
                "name": name,
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": sha256(content).hexdigest(),
            }
            if description:
                item["description"] = description
            if apply_to:
                item["applyTo"] = apply_to
            assets.append(item)

    assets.sort(key=lambda x: (x["type"], x["name"], x["path"]))
    return {
        "schema_version": 1,
        "asset_count": len(assets),
        "assets": assets,
    }


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path, help="Write JSON to this path; stdout when omitted.")
    args = parser.parse_args()

    try:
        payload = build_index()
    except Exception as exc:
        print(f"ASSET INDEX FAILED: {exc}", file=sys.stderr)
        return 1

    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"

    if args.output:
        output = args.output
        if not output.is_absolute():
            output = ROOT / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
        print(f"ASSET INDEX PASSED: {payload['asset_count']} assets -> {output}")
    else:
        sys.stdout.write(rendered)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
