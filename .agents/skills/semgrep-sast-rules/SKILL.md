---
name: semgrep-sast-rules
description: Author, extend, and debug Semgrep SAST rules and Tier-1 autofix templates. Use when writing or editing SAST rule YAML, adding taint-mode rules, defining fix autofix templates, tuning severities, or diagnosing why a SAST scan misses or false-positives a finding.
---

# Semgrep SAST Rules

## Overview
A SAST layer runs Semgrep against the target codebase, auto-detects the project stack, and selects the matching rule YAML — typically a shared rule set plus per-stack rule files (one per language/framework). Scan output is a raw results file plus a deduplicated findings snapshot that downstream remediation agents consume.

## Rule Conventions (match the existing file)
- Rule id encodes language + weakness, e.g. `java-command-injection`, `java-sql-injection-taint`. Keep this `<lang>-<weakness>[-taint]` convention.
- Two flavors per weakness: a fast `patterns:` rule and a precise `mode: taint` rule with `pattern-sources` (e.g. `$REQ.getParameter(...)`) and `pattern-sinks` (e.g. `Runtime.getRuntime().exec(...)`).
- `severity: ERROR` (Critical/High), `WARNING` (Medium), `INFO` (Low). These map into the Critical/High/Medium/Low buckets used by the severity gate — never invent new severity strings.
- `languages:` must match the stack (e.g. `[java]`, `[python]`, `[javascript]`).

## When to Use This Skill
- Adding a new weakness rule (SQLi, command injection, SSRF, XXE, weak crypto, etc.).
- Adding a `fix:` autofix template so a finding is Tier-1 (template) remediable.
- Adding a per-stack rule file for a newly supported language.
- Reducing false positives via `pattern-not`, `metavariable-pattern`, or taint sanitizers.
- Adding `metadata.cwe` to a rule so findings carry a first-class CWE.

## Do NOT apply this skill when
- Running a scan or reading results — that's the scan runner's job, not rule editing.
- Editing SCA/dependency logic (use `trivy-sca-scanning` / `transitive-dependency-remediation`).
- Changing the underlying scanner tooling itself — this skill edits rule YAML only.

## Workflow
1. Read the target rule file(s) and find the closest existing rule to mirror.
2. Write the fast `patterns:` rule; add a `mode: taint` companion for injection classes.
3. Where a safe mechanical rewrite exists, add a `fix:` template (Tier-1 autofix).
4. Add `metadata: { cwe: [...] }` for standards mapping.
5. Validate locally: `semgrep --config <file> --validate`, then run the scan against a fixture and confirm the finding appears in the deduplicated snapshot.
6. Confirm severities land in the expected severity-gate bucket.

## Example
```yaml
- id: python-ssrf-taint
  mode: taint
  pattern-sources:
    - pattern: flask.request.args.get(...)
  pattern-sinks:
    - pattern: requests.get(...)
  message: Untrusted input reaches an outbound HTTP request (SSRF)
  languages: [python]
  severity: ERROR
  metadata:
    cwe: ["CWE-918"]
```
