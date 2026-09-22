---
description: Run the complete governed Stage 0 / Gate A / Gate B / Gate C engineering loop.
---

Read `AGENTS.md`, then invoke the `incremental-design-build` skill for the user's requirement.

Do not jump directly to code for a substantial change.

Required behavior:
1. establish fresh Stage 0 context;
2. create/confirm Change Brief + mechanical Definition of Done;
3. establish safe branch/checkpoint state;
4. use progressive disclosure;
5. run the agent-alignment round;
6. produce System Design and fresh Gate A critique;
7. produce Implementation Design and fresh Gate B critique;
8. implement in bounded slices with local validation/checkpoints;
9. run clean-context validation when warranted;
10. run fresh Gate C critique;
11. produce traceability and PR-ready Git handoff.

If a gate fails, route back to the responsible stage. If checkpoint/context integrity fails, stop mutation and operate read-only.

At every pause report current stage, current gate, artifacts produced, deterministic evidence, open findings/risks, checkpoint state, and recommended next agent/action.
