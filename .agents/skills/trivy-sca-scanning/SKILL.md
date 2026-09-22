---
name: trivy-sca-scanning
description: Run and interpret Trivy software-composition-analysis (SCA) dependency CVE scans. Use when invoking an SCA scan runner, parsing Trivy results, handling the "zero packages scanned" false-clean hard-stop, or reading CVE findings.
---

# Trivy SCA Scanning

## Overview
SCA is performed by a scan runner that invokes a Trivy binary against dependency manifests (`pom.xml`, `package.json`, `requirements.txt`, etc.) and emits: the raw Trivy JSON results (each vuln carries CWE IDs, CVSS, severity), and a deduplicated CVE snapshot (the handoff contract the remediation step consumes).

## Critical Behavior — the False-Clean Hard-Stop
The scan runner HARD-STOPS when it returns `success=False` or `packages_scanned == 0`. Zero packages means Trivy failed to parse manifests — this is a false clean, not a pass. Write an error sentinel file when this happens. **Never work around it** — do not query a public package registry as a fallback, fabricate a zero-CVE result, or downgrade the error to a warning.

## When to Use This Skill
- Running an SCA scan and validating package coverage.
- Diagnosing `packages_scanned == 0` (missing/unsupported manifest, bad target path).
- Reading CVE counts from the findings summary — never load the full raw results file into context; read the deduplicated/summarized view.
- Confirming the pre-staged Trivy binary (or however it is wired into the build) is available.

## Do NOT apply this skill when
- Fixing/upgrading dependencies (use `transitive-dependency-remediation`).
- Enriching CVEs with KEV/EPSS (use `vuln-enrichment-prioritization`).
- Editing SAST/Semgrep rules (use `semgrep-sast-rules`).

## Workflow
1. Confirm Trivy availability (`trivy --version`); fail fast if missing.
2. Invoke the scan runner against the target directory.
3. If `success=False` or `packages_scanned == 0` → stop, explain the false-clean, point to the error sentinel.
4. Inspect severity counts via the findings summary (bounded read, not the raw results file).
5. Confirm the raw results file and the deduplicated snapshot exist on disk.

## Example
```python
res = run_sca_scan(target_dir="/repo", reports_dir="/repo/reports")
if not res["success"] or res["packages_scanned"] == 0:
    raise RuntimeError("Trivy false-clean: no packages parsed — see the SCA error sentinel")
```
