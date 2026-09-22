# System Design — EXAMPLE-RATE-LIMIT

## Boundary
The existing API authentication boundary remains unchanged. Rate limiting occurs after tenant identity is established and before protected business work begins.

~~~mermaid
flowchart LR
    C[Client] --> A[Authentication]
    A --> T[Tenant Identity]
    T --> R[Rate-Limit Decision]
    R -->|allow| B[Business Handler]
    R -->|throttle| X[429 Response]
    R --> M[Metrics]
~~~

## Contract
Input: authenticated tenant identity + request classification.

Output: ALLOW or THROTTLE plus optional retry metadata.

## Invariants
- one tenant's traffic cannot consume another tenant's quota;
- authentication failures are never transformed into rate-limit responses;
- a throttled request must not execute protected business work.

## Failure behavior
A dependency/configuration failure must follow an explicitly approved fail-open/fail-closed policy; this example leaves that decision open for Gate A resolution.

## Gate A
The unresolved dependency-failure policy is BLOCKING until explicitly decided.
