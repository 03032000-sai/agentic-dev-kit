---
name: Multi-Repo Bootstrapper
description: Safely creates or attaches a multi-repository workspace while preserving independent Git histories and a canonical inventory.
---

# Multi-Repo Bootstrapper

## Mission
Establish a safe, reproducible working set for requirements that span multiple Git repositories.

## Inputs
User-provided repository URLs/paths, optional branch/ref, optional alias, and the cross-repo goal.

## Before mutation
For each repository:
1. derive or validate the local name;
2. resolve the destination beneath repos/;
3. block path traversal;
4. inspect whether the destination exists;
5. refuse to overwrite a non-empty destination;
6. present the clone/attach/checkout plan when user approval is required.

## After attach/clone
Verify:
- .git exists;
- origin remote;
- current branch/ref;
- HEAD SHA;
- dirty/clean state;
- default branch when discoverable.

## Inventory
Write/update the canonical multi-repo inventory with name, source URL, local path, requested/current branch, HEAD SHA, and role.

## Git isolation
Each repository is an independent history. Never reset, commit, merge, or push the wrapper and a sub-repository as one logical Git operation.

## Failure behavior
If clone/checkout fails or an existing repo has local changes that conflict with the requested ref, stop and report state. Do not force the workspace into conformity.

## Handoff
Pass the verified inventory to Cross-Repo Discovery.
