# Architecture

`agentic-dev-kit` is a repository-native agent operating system. There is no required orchestration server. The repository itself carries the policies, specialist roles, skills, prompts, contracts, and loops that coding assistants invoke from chat.

## Cross-tool architecture

```mermaid
flowchart TB
    U[Engineer]

    subgraph ENTRY[Chat surfaces]
      GHC[GitHub Copilot]
      CC[Claude Code]
      CX[OpenAI Codex]
    end

    subgraph POLICY[Canonical repository policy]
      A[AGENTS.md]
      C[CLAUDE.md]
      CI[Copilot instructions]
    end

    subgraph ROLES[Specialist roles]
      B[Bootstrap / Discovery]
      SD[System Designer]
      ID[Implementation Designer]
      IMP[Implementer]
      CR[Fresh Critics]
      OP[Local / Clean Operators]
      GM[Git Manager]
    end

    subgraph CONTROL[Deterministic control plane]
      CB[Change Brief + DoD]
      GA[Gate A]
      GB[Gate B]
      GC[Gate C]
      CP[Durable Checkpoints]
      EV[Tests / Builds / Scans / Evidence]
    end

    U --> ENTRY
    ENTRY --> POLICY
    POLICY --> ROLES
    ROLES --> CONTROL
    CONTROL --> ROLES
```

## Repository layout

```text
.
├── AGENTS.md
├── CLAUDE.md
├── .agents/
│   ├── skills/
│   └── checkpoints/            # optional runtime state; normally gitignored
├── .claude/
│   ├── agents/
│   └── skills/
├── .github/
│   ├── agents/
│   ├── prompts/
│   ├── instructions/
│   └── copilot-instructions.md
└── docs/
    ├── contracts/
    ├── workflows/
    └── ...
```

## Separation of powers

```mermaid
flowchart LR
    R[Requirement] --> BOOT[Bootstrapper]
    BOOT --> SD[System Designer]
    SD --> C1[Fresh Critic]
    C1 -->|pass| ID[Implementation Designer]
    ID --> C2[Fresh Critic]
    C2 -->|pass| IMP[Implementer]
    IMP --> OP[Local Operator]
    OP --> CLEAN[Clean-Repo Operator]
    CLEAN --> C3[Fresh Critic]
    C3 -->|pass| GM[Git Manager]
    GM --> H[Human PR / Merge Decision]

    C1 -->|blocking| SD
    C2 -->|blocking| ID
    C3 -->|blocking| IMP
```

## Artifact hierarchy

The canonical artifacts are:
1. Change Brief + mechanical Definition of Done;
2. current-state evidence map;
3. system design;
4. Gate A findings;
5. implementation design;
6. Gate B findings;
7. implementation diff;
8. validation evidence;
9. Gate C findings;
10. PR-ready summary and residual-risk register.

## Context strategy

```mermaid
flowchart LR
    I[Instructions] --> M[Indexes / manifests]
    M --> T[Targeted files]
    T --> D[Dependency chase]
    D --> S[Compact evidence summary]
    S --> CP[Checkpoint]
    CP --> N[Fresh next stage / critic]
```

The framework intentionally avoids carrying every raw file and every prior model thought into every later stage.
