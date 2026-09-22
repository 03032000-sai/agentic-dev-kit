---
name: skill-scaffolding
description: Author complete skill + eval pairs covering every tool/technology this project actually uses. Creates a new skill directory with SKILL.md and a matching eval set. Skills + evals only — never creates agents or edits runtime/tool code.
---

# Scaffold Skills + Evals for the Full Tech Surface

You author new skills (and, where the host platform supports it, matching evals) so the workspace's agents have complete, discoverable coverage for every tool and technology this project actually uses. You create skills and evals only — you never create agents and never touch runtime or application code.

## 0) Hard Scope Guardrails (read first)
- Create/edit ONLY under the skills directory (and its matching evals directory, if the platform has one).
- Do NOT create or edit any agent definition file.
- Do NOT edit application source, tests, or tool implementation code. You may READ them for grounding.
- Give every new skill a distinct name that does not collide with an existing skill.
- **report-only mode:** if asked, produce the full set of proposed files as a preview and STOP without writing.

## 1) Templates (copy these shapes exactly)
**Skill** — `<skills-root>/<name>/SKILL.md`, modeled on an existing rich skill in this repo (e.g. `docker-podman-optimizer`):
- Frontmatter: `name`, a discovery-quality `description` (start with a crisp capability line and include a "Use when: …" clause).
- Body: `## Overview`, `## When to Use This Skill`, `## Do NOT apply this skill when`, a concrete workflow/checklist, and short grounded examples citing real repo paths.

**Eval** (if the host platform supports skill evals) — cloned from an existing eval set's shape: set name `<name>-eval`, reference the skill by name, keep the existing config/metrics/graders shape, and point at a `tasks/` directory.

**Eval tasks** — at minimum: two positive-trigger tasks (`should_trigger: true`, text grader contains the skill's key keywords) and one negative-trigger task (an unrelated prompt, `should_trigger: false`, must not contain the skill's keywords).

## 2) Identify Skills to Author
Before writing anything, identify the tech surfaces this repo actually uses that lack a skill yet. Ground every candidate in real files you have read — never invent a skill for a hypothetical stack. Typical discovery sources: dependency manifests (`pyproject.toml`, `package.json`, `pom.xml`, `go.mod`, …), CI/CD config, Dockerfiles, IaC, and any existing skills directory (to avoid duplicating coverage already present).

Group candidates into logical phases (e.g. security tooling, a specific framework/SDK, a cloud platform's services, a backend language/build system, CI/CD) so a large scaffolding run can proceed phase by phase instead of all at once.

## 3) Per-Skill Recipe (repeat for each)
1. Read the cited grounding files for that skill.
2. Write `<skills-root>/<name>/SKILL.md` (Section 1 shape), grounded and specific.
3. Write the matching eval set, if the platform supports it, cloned from the template.
4. Write the eval tasks (2 positive-trigger + 1 negative-trigger) with that skill's keywords.

## 4) Execution Scope
Default to the first logical phase if the invocation names no phase/skill; otherwise run only the named phase(s) or skill(s). Do phases in the order you defined them unless told otherwise.

## 5) Acceptance Checklist (self-verify before finishing)
- Only the skills directory (and its eval directory, if applicable) was created/edited — no agents, no application source, no tool code.
- Each new `SKILL.md` has valid frontmatter with a discovery-quality "Use when: …" description and a name that doesn't collide with an existing skill.
- Each new skill has a matching eval set (if the platform supports evals) referencing it by name, plus 2 positive-trigger + 1 negative-trigger task files.
- Every `SKILL.md` is grounded in real repo files (paths cited), not invented behavior.

## 6) Final Output
Emit a short summary table: skill name, files created, grounding sources used, and any skills deferred to a later phase.
