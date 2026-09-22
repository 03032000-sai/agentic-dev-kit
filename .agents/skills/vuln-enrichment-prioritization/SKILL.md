---
name: vuln-enrichment-prioritization
description: Enrich SAST/SCA findings with exploitability signals and rank remediation priority.
---

# Vulnerability Enrichment & Prioritization
Enrich raw findings with CISA KEV (known-exploited), FIRST EPSS (exploit-prediction score), and OSV advisories before ranking — severity alone is not priority. Rank by actual exploitability and reachability, not CVSS score in isolation. If an enrichment source is unavailable, degrade to severity-only ranking and say so explicitly rather than blocking remediation.
