---
description: Resume a long-running task safely from its durable checkpoint and reconcile repository/SHA drift before mutation.
---

Read `AGENTS.md` and invoke `checkpoint-resume`.

Load the checkpoint and referenced artifacts, compare repository/branch/HEAD/dirty state, detect drift, identify stale approvals/validation, and remain read-only until inconsistencies are reconciled.

Return checkpoint validity, current fingerprint, still-valid artifacts, open findings, ordered next steps, recommended next agent, and mutation ownership.
