# Change Brief Contract

A Change Brief is the stable task contract shared across agents. It is created during Stage 0 and updated only when scope, constraints, or approved decisions materially change.

```yaml
change_id:
title:

goal:
problem_statement:

non_goals: []

requirements:
  - id: R1
    statement:
    source:
    priority:

constraints:
  technical: []
  compatibility: []
  security: []
  operational: []

definition_of_done:
  - id: D1
    check:
    evidence_expected:

acceptance_criteria:
  - id: A1
    criterion:
    maps_to: [R1, D1]

risks:
  - id:
    description:
    mitigation:

approved_design_decisions: []

validation_plan:
  commands: []
  environments: []
  clean_context_required: false

open_questions: []
```

## Rules

- Requirements and non-goals are both binding.
- Definition-of-Done items should be mechanically verifiable whenever possible.
- If implementation discovers a requirement conflict, update the brief only after the conflict is surfaced and resolved.
- Agents must not silently widen scope.
- Critics review the artifact against this brief, not against what they imagine the user intended.
