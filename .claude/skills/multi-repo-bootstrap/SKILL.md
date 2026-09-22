---
name: multi-repo-bootstrap
description: Onboard multiple Git repositories into a shared multi-repo workspace before any cross-repo engineering workflow begins.
---

# Multi-Repo Bootstrap

1. Resolve target repositories from user-supplied URLs (optionally `<url>#<branch>` or an alias).
2. Multi-Repo Bootstrapper runs preflight checks (path-traversal-safe destination, no overwrite of a non-empty checkout) and confirms the clone plan with the user.
3. Clone each repository into `repos/<name>/` and verify `.git`, origin, and current branch.
4. Write/update the canonical manifest at `docs/multi-repo/inventory.json`.
5. Cross-Repo Discovery scans all cloned repos and builds the dependency graph, integration checklist, and elects an anchor repo.
6. Hand off to the requested engineering workflow (e.g. `brownfield-bootstrap`, `incremental-design-build`) scoped to the relevant sub-repo(s).

Never force-clone, force-checkout, or discard local changes in an existing sub-repo. Do not assume a repo exists — always resolve from the manifest or fresh user input.
