# Brownfield Discovery Workflow

1. Inspect repository root and high-signal metadata.
2. Identify languages, package managers, build/test systems, and deployment configuration.
3. Read repository-level instructions and architecture docs.
4. Locate entry points and dependency boundaries.
5. Trace only code paths relevant to the task.
6. Locate tests that encode current behavior.
7. Record evidence with file paths and symbols.
8. Separate confirmed facts from inference and unknowns.
9. Stop when enough evidence exists for the next engineering stage.

Avoid summarizing the entire repository when the task is narrow.
