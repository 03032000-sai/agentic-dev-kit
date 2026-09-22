#!/usr/bin/env python3
"""Deterministic structural checks for agentic-dev-kit."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "AGENTS.md", "CLAUDE.md",
    ".github/copilot-instructions.md",
    "docs/architecture.md", "docs/principles.md",
    "docs/workflows/design-build.md",
    ".agents/skills/repo-discovery/SKILL.md",
    ".agents/skills/architecture-analysis/SKILL.md",
    ".agents/skills/test-planning/SKILL.md",
]
roles = ["repo-analyst","system-designer","implementation-designer","implementer","critic","git-manager"]
errors = []

for rel in required:
    p = ROOT / rel
    if not p.is_file() or p.stat().st_size == 0:
        errors.append(f"missing or empty: {rel}")

fm_re = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
for skill in (ROOT / ".agents" / "skills").glob("*/SKILL.md"):
    text = skill.read_text(encoding="utf-8")
    m = fm_re.search(text)
    if not m:
        errors.append(f"missing frontmatter: {skill.relative_to(ROOT)}")
        continue
    fm = m.group(1)
    if not re.search(r"^name:\s*\S+", fm, re.MULTILINE):
        errors.append(f"missing skill name: {skill.relative_to(ROOT)}")
    if not re.search(r"^description:\s*.+", fm, re.MULTILINE):
        errors.append(f"missing skill description: {skill.relative_to(ROOT)}")

for role in roles:
    if not (ROOT / ".github" / "agents" / f"{role}.agent.md").is_file():
        errors.append(f"missing Copilot agent: {role}")
    if not (ROOT / ".claude" / "agents" / f"{role}.md").is_file():
        errors.append(f"missing Claude agent: {role}")

canon = {p.parent.name for p in (ROOT/".agents/skills").glob("*/SKILL.md")}
claude = {p.parent.name for p in (ROOT/".claude/skills").glob("*/SKILL.md")}
if canon != claude:
    errors.append("Claude skills out of sync; run python3 scripts/sync_skills.py")

if errors:
    print("VALIDATION FAILED")
    for e in errors: print(" -", e)
    sys.exit(1)

print("VALIDATION PASSED")
print(f" - custom roles: {len(roles)}")
print(f" - canonical skills: {len(canon)}")
