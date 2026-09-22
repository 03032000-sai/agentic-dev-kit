---
description: Checkpoint and compact a long-running workflow before context quality degrades, preserving only decision-relevant state.
---

Read `AGENTS.md` and invoke `context-governance`.

If active context is approaching 80% or contains substantial stale exploration, write/verify the durable checkpoint first. Preserve Change Brief/DoD, approved artifacts, evidence references, open findings, validation state, key decisions, and ordered next steps.

Then produce a compact resume packet for the next session/agent. Do not continue mutable work if checkpoint persistence is unavailable or untrusted.
