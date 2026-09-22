# Agent Handoff Contract

A handoff is a constrained transfer of responsibility, not a dump of the entire conversation.

## Required envelope

```yaml
from_role:
to_role:
task:
current_stage:

change_brief:
approved_upstream_artifacts: []

authoritative_evidence:
  - path:
    purpose:

constraints: []
non_goals: []
open_findings: []

authority:
  may:
  may_not:

expected_output:
validation_expected:
checkpoint_path:
```

## Handoff rules

1. Pass artifacts and evidence, not the author's full reasoning transcript.
2. The receiving role must reject an incomplete or unsafe handoff rather than silently filling critical gaps.
3. Critics receive fresh context: requirement + artifact + minimum authoritative evidence.
4. Implementers must receive approved system and implementation design when those gates apply.
5. Git Manager receives the actual diff/validation state, not a prose claim that "everything passed."
