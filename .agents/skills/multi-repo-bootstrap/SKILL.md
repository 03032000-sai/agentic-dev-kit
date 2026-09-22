---
name: multi-repo-bootstrap
description: Safely establish a multi-repository working set, inventory independent Git state, discover cross-repo contracts, and elect an anchor for shared artifacts.
---

# Multi-Repo Bootstrap

## Inputs
User-supplied repository URLs/paths, optional branches, and optional aliases.

## Clone/attach rules
For each repository:
1. derive/validate a safe name;
2. resolve destination beneath `repos/`;
3. block path traversal;
4. refuse to overwrite a non-empty destination;
5. preserve existing independent Git history;
6. verify origin, branch, HEAD SHA, and working-tree state.

Confirm mutation plans before cloning/checking out.

## Inventory
Maintain `docs/multi-repo/inventory.json` with name, path, source URL, requested/current branch, HEAD SHA, and role.

## Cross-repo discovery
Identify confirmed/inferred:
- API/event contracts;
- shared schemas/libraries;
- data ownership;
- deploy-order dependencies;
- coordinated migrations;
- integration tests;
- compatibility/version constraints.

## Anchor repository
Elect the repository that owns the shared contract, dependency root, or strongest inbound relationship. Put shared artifacts under that repo's `docs/cross-repo/`. Do not create a separate docs repo by default.

## Git invariant
Every mutation targets exactly one Git repository. Never treat wrapper + sub-repos as one history.

## Output
Inventory, dependency graph, integration checklist, anchor decision, source SHAs, and unresolved cross-repo risks.
