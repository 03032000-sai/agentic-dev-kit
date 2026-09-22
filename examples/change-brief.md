# Change Brief — EXAMPLE-RATE-LIMIT

## Goal
Add tenant-aware request rate limiting to a public API without changing authentication semantics.

## Non-goals
- redesign authentication;
- change API response schemas outside the new rate-limit response;
- introduce a new external datastore.

## Requirements
| ID | Requirement |
|---|---|
| REQ-001 | Enforce an independently configurable limit per tenant. |
| REQ-002 | Return a deterministic throttled response when the limit is exceeded. |
| REQ-003 | Emit observable allow/throttle counters. |

## Mechanical Definition of Done
| ID | Check | Expected evidence |
|---|---|---|
| DOD-001 | unit tests cover allow + throttle | passing test output |
| DOD-002 | integration test proves tenant isolation | passing integration result |
| DOD-003 | metrics exist for allow/throttle | metric assertion / smoke evidence |

## Risks
- incorrect tenant keying could cause cross-tenant interference;
- retry behavior could amplify request volume.

## Open questions
- exact default quota is a product/configuration decision.
