# Implementation Design — EXAMPLE-RATE-LIMIT

This sample intentionally uses generic paths.

| IMP ID | File / Module | Change |
|---|---|---|
| IMP-001 | api/middleware | invoke rate-limit decision after tenant identity |
| IMP-002 | rate_limit/service | implement decision contract |
| IMP-003 | config | bind tenant/default quota configuration |
| IMP-004 | tests/unit | allow/throttle/config tests |
| IMP-005 | tests/integration | tenant isolation test |

## Validation
| VAL ID | Requirement | Evidence |
|---|---|---|
| VAL-001 | REQ-001 | unit + tenant-isolation integration test |
| VAL-002 | REQ-002 | throttled response contract test |
| VAL-003 | REQ-003 | metric emission assertion |

## Rollback
Disable the integration point/configuration and redeploy the prior known-good candidate. Exact mechanism depends on the host repository.
