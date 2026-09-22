---
description: Replay a checkpointed or event-driven workflow to isolate the first state divergence without re-triggering unsafe side effects.
---

Read `AGENTS.md` and invoke `replay-debugging`.

Pin the failing run and source SHA, reconstruct the execution timeline from persisted evidence, identify the last known-good checkpoint, replay safely from the earliest reproducible boundary, and compare state transition by transition until the first divergence is found.

Distinguish deterministic replay from nondeterministic model re-execution. Never invent missing history or replay destructive production side effects without approval. Return timeline, divergence evidence, root-cause confidence, and regression oracle.
