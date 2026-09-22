---
name: trivy-sca-scanning
description: Run and interpret Trivy dependency/CVE scans with a fail-closed posture.
---

# Trivy SCA Scanning
Run Trivy against the dependency manifest/lockfile, not just the source tree, so transitive dependencies are included. Treat zero packages scanned as a hard failure, not a clean result — a misconfigured scan must never be reported as "no vulnerabilities found." Classify findings by actual reachability where evidence permits, not severity alone. Re-run after any remediation to confirm the specific CVE is gone, not just that the scan succeeded.
