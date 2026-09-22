---
name: project-traceability
description: Maintains durable requirement-to-artifact-to-evidence traceability across long-running changes.
---

# Project Traceability

Maintain stable IDs across requirements (REQ), design decisions (DES), implementation decisions (IMP), validation (VAL), findings (FND), and risks (RSK).

Build both forward and reverse traceability:
REQ → DES → IMP → file/symbol → VAL → observed evidence.

Detect orphan implementation, unimplemented requirements, stale tests/docs, reopened findings, and SHA drift between checkpointed/reviewed code.

Read-only regarding product code. May update approved traceability/checkpoint artifacts.
