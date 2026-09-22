---
name: multi-repo-bootstrap
description: Safely establish a multi-repository working set, inventory independent Git state, discover cross-repo contracts, and elect an anchor for shared artifacts.
---

# Multi-Repo Bootstrap

Validate each user-supplied repo destination under `repos/`, refuse destructive overwrite, preserve independent Git histories, and inventory origin/branch/HEAD SHA.

Discover cross-repo APIs/events/schemas/libraries/data ownership/deploy order/integration tests. Elect an anchor repo for shared `docs/cross-repo/` artifacts. Every Git mutation targets exactly one repo. Return inventory, dependency graph, integration checklist, anchor decision, source SHAs, and risks.
