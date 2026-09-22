#!/usr/bin/env python3
"""Mirror canonical .agents/skills into .claude/skills."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents" / "skills"
TARGET = ROOT / ".claude" / "skills"

if not SOURCE.exists():
    raise SystemExit("Missing canonical .agents/skills")

TARGET.mkdir(parents=True, exist_ok=True)
source_names = {p.name for p in SOURCE.iterdir() if p.is_dir()}

for existing in TARGET.iterdir():
    if existing.is_dir() and existing.name not in source_names:
        shutil.rmtree(existing)

for skill_dir in SOURCE.iterdir():
    if not skill_dir.is_dir():
        continue
    destination = TARGET / skill_dir.name
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(skill_dir, destination)

print(f"Synced {len(source_names)} skills to .claude/skills")
