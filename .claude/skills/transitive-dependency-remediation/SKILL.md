---
name: transitive-dependency-remediation
description: Remediate vulnerable indirect dependencies using ecosystem-native controls and resolved-graph verification.
---

# Transitive Dependency Remediation

## Principle
Change the dependency graph with the smallest compatible intervention. Do not fork/vendor merely because the vulnerable package is indirect.

## Ecosystem patterns
### Maven/Gradle
Use dependency management/constraints/platform controls or an upstream direct dependency upgrade. Verify with the resolved dependency tree.

### npm/pnpm/yarn
Use supported overrides/resolutions only when appropriate; prefer an upstream package upgrade when it naturally resolves the transitive. Verify the lockfile and resolved tree.

### Python
Prefer an upstream dependency update or a constraints/lock resolution compatible with the project tooling. Verify the resolved environment/lock graph, not only `requirements*.txt`.

### .NET
Use central package management/direct package override only when compatible with repository conventions; verify the transitive graph.

## Version choice
Prefer the lowest compatible version that fixes the vulnerability unless repository policy says otherwise. Avoid unrelated major-version churn.

## Evidence
Record:
- original dependency path;
- remediation mechanism;
- new resolved path/version;
- SCA rescan result;
- tests/build result.

A manifest edit without resolved-graph evidence is incomplete.
