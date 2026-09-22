# Principles

## AI is a reasoner, not the final authority
Use AI for exploration, synthesis, planning, implementation assistance, and critique. Use deterministic systems for compilation, tests, schemas, policy gates, static analysis, security scans, and release criteria.

## Separation of responsibilities
A single context that designs, implements, validates, and approves its own work accumulates assumptions and confirmation bias. Split responsibilities when the task is large enough to justify it.

## Progressive disclosure
Start from structure and metadata, then expand only the branches of information needed for the task.

## Fresh-context critique
A critic should receive the artifact, requirements, and necessary evidence without inheriting all of the author's narrative.

## Unknown is a first-class outcome
If evidence is unavailable, say `unknown`.

## Human control
Human approval belongs in the architecture when an operation can be destructive, expensive, security-sensitive, irreversible, or production-impacting.
