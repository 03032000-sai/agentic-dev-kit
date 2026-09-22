---
name: git-safety
description: Enforce branch isolation, single-writer commit ownership, explicit staging, and human approval for destructive or publication Git operations.
---

# Git Safety

## Invariants
- substantial mutable work happens on a dedicated feature/fix branch;
- inspect branch/status/diff before mutation;
- never discard uncommitted work to make the workflow convenient;
- exactly one role owns mutable repository work at a time;
- Git Manager is the sole role that creates commits;
- push/merge/history rewrite require explicit authorization.

## Safe operations
Inspect status, diff, log, remotes, and branch relationships. Create/switch a branch only when it will not overwrite work. Stage explicit reviewed paths and summarize the staged diff before commit.

## Prohibited without explicit approval
- reset --hard;
- clean -fd;
- checkout/restore that discards work;
- rebase/history rewrite;
- force push;
- default/protected-branch merge;
- push merely because a commit succeeded.

## Pre-commit evidence
Record branch, HEAD/base, staged paths, staged diff summary, validation status, unresolved findings/risks, and proposed message.

## Multi-repo
Identify the exact repository before every Git mutation. Never stage/commit across wrapper and sub-repositories as one operation.
