---
name: vuln-enrichment-prioritization
description: Enrich scanner findings with CISA KEV, FIRST EPSS, and OSV data and produce exploitability-ranked artifacts. Use when running enrichment before/after a fix, tuning the KEV > EPSS >= 0.70 > severity priority order, handling the non-blocking degraded/partial fallback, or reading the prioritized findings output.
---

# Vulnerability Enrichment & Prioritization

## Overview
Enrichment augments SAST and SCA findings with: **CISA KEV** — is this CVE actively exploited? **FIRST EPSS** — probability of exploitation in the next 30 days. **OSV** — aliases, references, CVSS scores.

Signature (illustrative): `run_enrichment(scanner_input_path, scanner_type, reports_dir, phase="after", offline_only=False, timeout_seconds=15)` where `scanner_type` is `"trivy"` or `"semgrep"` and `phase` is `"before"` or `"after"`.

## Non-Blocking Contract
Enrichment never fails the workflow. If external APIs are unavailable it still returns `success=True` and marks findings `enrichment_status="degraded"|"partial"`. Scanner findings remain the source of truth — enrichment only augments prioritization. Use `offline_only=True` to rely on cache with no live calls.

## Prioritization Order (highest first)
1. `kev_flag=true` (CISA KEV — actively exploited)
2. EPSS score, with `>= 0.70` treated as High
3. Severity rank: Critical > High > Medium > Low

Artifacts: raw enrichment output, the prioritized findings file, a summary, and run stats, plus phase-labeled variants (`*.before.json` / `*.after.json`).

## When to Use This Skill
- Running enrichment after a scan (call twice: `phase="before"` then `phase="after"`).
- Tuning the priority order or the EPSS High threshold.
- Handling degraded/offline runs gracefully.
- Producing the prioritized file the ATT&CK mapper reads.

## Do NOT apply this skill when
- Mapping to ATT&CK/CWE/CAPEC/D3FEND (use `mitre-attack-mapping`).
- Running the underlying scans (use `trivy-sca-scanning` / `semgrep-sast-rules`).
- You would make enrichment blocking — it must always degrade gracefully.

## Workflow
1. Ensure the scan produced its raw results file.
2. Call the enrichment step with the scan output, scanner type, reports directory, and phase.
3. On degraded APIs, continue — check `degraded_count` / `enrichment_status`.
4. Read the prioritized findings file for the ranked list (bounded reads only).

## Example
```python
run_enrichment(
    scanner_input_path="reports/trivy-results.json",
    scanner_type="trivy",
    reports_dir="reports",
    phase="before",
)
```
