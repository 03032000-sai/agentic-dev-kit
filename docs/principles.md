# Engineering Principles

## 1. Deterministic control around non-deterministic reasoning

Models are strong at ambiguity, synthesis, design exploration, code generation, and critique. They are not the final authority for correctness. Every substantial workflow therefore wraps model reasoning with deterministic contracts, tests, scanners, evidence, and explicit gates.

## 2. Separation of powers

The framework deliberately separates:
- discovery;
- system design;
- implementation design;
- implementation;
- local validation;
- clean-context validation;
- critique;
- Git lifecycle;
- human approval.

An author should not be the only verifier of its own work.

## 3. Progressive disclosure

Large repositories are not loaded wholesale. Agents first inspect instructions, indexes, manifests, and metadata; then read task-relevant files and follow dependencies only when required. This preserves reasoning quality and reduces accidental scope expansion.

## 4. Fresh-context criticism

Critics review the requirement, artifact, and authoritative evidence without inheriting the author's full reasoning history. This reduces confirmation bias and forces the artifact to stand on its own.

## 5. Evidence classes

Claims are tagged as `confirmed`, `documented`, `inferred`, or `unknown`. Unknowns are preserved, not papered over. Documentation cannot promote inference into fact merely because the wording sounds confident.

## 6. Mechanical Definition of Done

Acceptance criteria should be translated into observable checks whenever possible: tests, build outputs, schema validation, scanner results, exact files/artifacts, or reproducible commands. "Looks correct" is not a Definition of Done.

## 7. Durable state over conversational memory

Long workflows checkpoint branch/SHA, decisions, artifacts, validation, findings, risks, and next steps. If durable state is unavailable, mutation stops rather than relying on uncertain conversational memory.

## 8. Local success is weaker than clean reproducibility

A warm working tree may contain caches, generated files, environment residue, or unstated assumptions. Clean-context validation is required when release risk warrants it.

## 9. Least privilege by agent role

Read-only agents stay read-only. Git agents do not edit product logic. Implementers do not merge. Critics do not silently fix the artifacts they review. Tool access follows responsibility.

## 10. Human authority at irreversible boundaries

The framework automates reasoning and repetitive engineering work, but leaves irreversible or high-risk actions under explicit human control.
