#!/usr/bin/env python3
"""Deterministic structural and parity checks for agentic-dev-kit."""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

required_files = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    "docs/architecture.md",
    "docs/principles.md",
    "docs/USAGE.md",
    "docs/contracts/change-brief.md",
    "docs/contracts/checkpoints.md",
    "docs/contracts/evidence.md",
    "docs/contracts/gates.md",
    "docs/contracts/agent-handoffs.md",
    "docs/workflows/incremental-design-build-loop.md",
    "docs/workflows/brownfield-preloop.md",
    "docs/workflows/context-governance.md",
    "docs/workflows/agent-alignment.md",
    ".agents/templates/change-brief.md",
    ".agents/templates/checkpoint.yaml",
    ".agents/templates/system-design.md",
    ".agents/templates/implementation-design.md",
    ".agents/templates/critic-findings.md",
    ".agents/templates/traceability.md",
]

required_roles = {
    "repo-bootstrapper",
    "repo-analyst",
    "system-designer",
    "implementation-designer",
    "implementer",
    "local-operator",
    "clean-repo-operator",
    "git-manager",
    "traceability-analyst",
    "project-traceability",
    "docs-code-aligner",
    "security-reviewer",
    "design-critic",
    "implementation-plan-critic",
    "implementation-critic",
    "map-critic",
    "findings-critic",
    "implementation-executor",
    "git-repo-manager",
}

required_prompts = {
    "incremental-design-build",
    "feature-development",
    "bugfix",
    "brownfield-bootstrap",
    "knowledge-discovery",
    "reverse-engineer-design",
    "docs-code-alignment",
    "safe-refactor",
    "security-remediation",
    "release-readiness",
    "multi-repo-bootstrap",
    "business-docs-loop",
    "skill-scaffolding",
    "bootstrap-repo",
    "system-design",
    "implementation-design",
    "gate-a-review",
    "gate-b-review",
    "gate-c-review",
    "local-validate",
    "clean-validate",
    "git-handoff",
    "agent-alignment",
    "resume-checkpoint",
    "context-compact",
    "project-traceability",
    "design-test-oracles",
    "observability-evidence",
    "replay-debugging",
}

required_eval_skills = {
    "incremental-design-build",
    "bugfix",
    "business-docs-loop",
    "security-remediation",
    "safe-refactor",
    "release-readiness",
    "semgrep-sast-rules",
    "trivy-sca-scanning",
    "frontmatter-indexer",
    "skill-scaffolding",
}

frontmatter_re = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def fail(message: str) -> None:
    errors.append(message)


def frontmatter(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        fail(f"cannot read {path.relative_to(ROOT)}: {exc}")
        return None
    match = frontmatter_re.search(text)
    if not match:
        fail(f"missing frontmatter: {path.relative_to(ROOT)}")
        return None
    return match.group(1)


def require_frontmatter_fields(path: Path, fields: tuple[str, ...]) -> None:
    fm = frontmatter(path)
    if fm is None:
        return
    for field in fields:
        if not re.search(rf"^{re.escape(field)}:\s*.+", fm, re.MULTILINE):
            fail(f"missing {field} in frontmatter: {path.relative_to(ROOT)}")


for rel in required_files:
    path = ROOT / rel
    if not path.is_file():
        fail(f"missing required file: {rel}")
    elif path.stat().st_size == 0:
        fail(f"empty required file: {rel}")

if (ROOT / "AGENTS.md").is_file() and (ROOT / "AGENTS.md").stat().st_size < 5000:
    fail("AGENTS.md is unexpectedly shallow (<5 KB)")
if (ROOT / "README.md").is_file() and (ROOT / "README.md").stat().st_size < 5000:
    fail("README.md is unexpectedly shallow (<5 KB)")

readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
mermaid_marker = chr(96) * 3 + "mermaid"
if readme.count(mermaid_marker) < 6:
    fail("README.md must contain at least 6 Mermaid architecture/workflow diagrams")

gh_agents = ROOT / ".github" / "agents"
claude_agents = ROOT / ".claude" / "agents"

gh_stems: set[str] = set()
for path in gh_agents.glob("*.agent.md"):
    stem = path.name.removesuffix(".agent.md")
    gh_stems.add(stem)
    require_frontmatter_fields(path, ("name", "description"))
    if path.stat().st_size < 300:
        fail(f"agent appears too shallow: {path.relative_to(ROOT)}")

claude_stems: set[str] = set()
for path in claude_agents.glob("*.md"):
    stem = path.stem
    claude_stems.add(stem)
    require_frontmatter_fields(path, ("name", "description"))
    if path.stat().st_size < 300:
        fail(f"agent appears too shallow: {path.relative_to(ROOT)}")

missing = sorted(required_roles - gh_stems)
if missing:
    fail(f"missing required GitHub agents: {', '.join(missing)}")
missing = sorted(required_roles - claude_stems)
if missing:
    fail(f"missing required Claude agents: {', '.join(missing)}")

if gh_stems != claude_stems:
    fail(
        "GitHub/Claude agent sets differ: "
        f"github_only={sorted(gh_stems - claude_stems)}, "
        f"claude_only={sorted(claude_stems - gh_stems)}"
    )

canonical_root = ROOT / ".agents" / "skills"
claude_root = ROOT / ".claude" / "skills"

canonical_skills = {p.name for p in canonical_root.iterdir() if p.is_dir()} if canonical_root.exists() else set()
claude_skills = {p.name for p in claude_root.iterdir() if p.is_dir()} if claude_root.exists() else set()

if canonical_skills != claude_skills:
    fail(
        "Claude skills out of sync: "
        f"canonical_only={sorted(canonical_skills - claude_skills)}, "
        f"claude_only={sorted(claude_skills - canonical_skills)}"
    )

skill_names_seen: dict[str, Path] = {}
for skill_name in sorted(canonical_skills):
    skill_md = canonical_root / skill_name / "SKILL.md"
    if not skill_md.is_file():
        fail(f"missing SKILL.md: {skill_name}")
        continue
    require_frontmatter_fields(skill_md, ("name", "description"))
    fm = frontmatter(skill_md)
    if fm:
        match = re.search(r"^name:\s*(\S+)", fm, re.MULTILINE)
        if match:
            declared = match.group(1).strip()
            if declared in skill_names_seen:
                fail(
                    f"duplicate skill name '{declared}': "
                    f"{skill_names_seen[declared].relative_to(ROOT)} and {skill_md.relative_to(ROOT)}"
                )
            skill_names_seen[declared] = skill_md

    canonical_files = {
        p.relative_to(canonical_root / skill_name)
        for p in (canonical_root / skill_name).rglob("*")
        if p.is_file()
    }
    claude_files = {
        p.relative_to(claude_root / skill_name)
        for p in (claude_root / skill_name).rglob("*")
        if p.is_file()
    }
    if canonical_files != claude_files:
        fail(f"skill file-set mismatch for {skill_name}; run scripts/sync_skills.py")
        continue
    for rel in canonical_files:
        a = canonical_root / skill_name / rel
        b = claude_root / skill_name / rel
        if a.read_bytes() != b.read_bytes():
            fail(f"skill mirror content mismatch: {skill_name}/{rel}")

prompt_dir = ROOT / ".github" / "prompts"
prompt_stems: set[str] = set()
for path in prompt_dir.glob("*.prompt.md"):
    prompt_stems.add(path.name.removesuffix(".prompt.md"))
    require_frontmatter_fields(path, ("description",))

missing_prompts = sorted(required_prompts - prompt_stems)
if missing_prompts:
    fail(f"missing required workflow prompts: {', '.join(missing_prompts)}")

compatibility_aliases = {"repository-discovery"}
expected_eval_skills = canonical_skills - compatibility_aliases
for skill in sorted(expected_eval_skills):
    path = canonical_root / skill / "evals" / "eval.json"
    if not path.is_file():
        fail(f"missing required eval fixture: {path.relative_to(ROOT)}")
        continue
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid eval JSON {path.relative_to(ROOT)}: {exc}")
        continue
    if payload.get("skill") != skill:
        fail(f"eval skill name mismatch: {path.relative_to(ROOT)}")

depth_minimums = {
    ".agents/skills/incremental-design-build/SKILL.md": 3000,
    "docs/workflows/incremental-design-build-loop.md": 3500,
    ".agents/skills/business-docs-loop/SKILL.md": 1200,
    ".agents/skills/security-remediation/SKILL.md": 1200,
}
for rel, minimum in depth_minimums.items():
    path = ROOT / rel
    if path.is_file() and path.stat().st_size < minimum:
        fail(f"critical workflow regressed below expected depth ({minimum} bytes): {rel}")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print("VALIDATION PASSED")
print(f" - GitHub/Claude agents: {len(gh_stems)}")
print(f" - canonical/mirrored skills: {len(canonical_skills)}")
print(f" - GitHub workflow prompts: {len(prompt_stems)}")
print(f" - required eval fixtures: {len(expected_eval_skills)}")
print(f" - README Mermaid diagrams: {readme.count(mermaid_marker)}")
