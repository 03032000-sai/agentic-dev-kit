---
description: Prepare a validated change for safe commit/PR handoff under the single-writer Git contract.
agent: git-manager
---

Read `AGENTS.md`.

Inspect branch, HEAD/base, status, staged/unstaged diff, checkpoint, validation, critic findings, and residual risks. Confirm repository mutation ownership has been handed to Git Manager.

Stage only reviewed paths if authorized, summarize the staged diff, and propose commit/PR text. Do not reset/clean/rewrite history/force push/push/merge without explicit authorization for that action.
