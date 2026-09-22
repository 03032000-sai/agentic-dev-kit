---
name: vuln-enrichment-prioritization
description: Enrich vulnerability findings with exploitation and reachability evidence without replacing authoritative scanner results.
---

# Vulnerability Enrichment & Prioritization

## Inputs
Start from normalized scanner findings. Enrichment adds context; it does not delete findings.

## Signals
Where available:
- CISA KEV known-exploited status;
- FIRST EPSS probability/percentile;
- OSV/vendor advisories;
- internet/external exposure;
- application reachability;
- privilege/data impact;
- available fixed version;
- compensating controls.

## Priority logic
Use transparent rules such as:
1. known exploited + reachable/exposed;
2. high exploitation probability + reachable;
3. critical/high severity with credible impact;
4. lower-severity or low-reachability findings.

Do not present a model-generated numeric "risk score" as objective truth unless the repository defines a deterministic formula.

## Missing data
If KEV/EPSS/advisory enrichment is unavailable, say so and degrade explicitly to available evidence. Never block remediation solely because enrichment failed.

## Output
For each finding provide scanner severity, enrichment signals, reachability status, priority rationale, recommended action, and unknowns.
