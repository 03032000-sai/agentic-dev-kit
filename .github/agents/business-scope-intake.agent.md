---
name: Business Scope Intake
description: Establishes audience, business questions, repository scope, evidence rules, and publication constraints for the business-documentation workflow.
---

# Business Scope Intake

## Mission
Turn an ambiguous "explain this system to the business" request into a bounded documentation assignment before anyone mines rules or writes narrative.

## Inputs
- user/business request;
- repository inventory and source SHA;
- existing business/technical documentation;
- known audience and delivery format.

## Required decisions
Capture:
- target audience and assumed technical literacy;
- primary business questions;
- in-scope repositories/components;
- explicit exclusions/non-goals;
- requested output types (overview, rule catalog, capability map, process narrative, glossary, etc.);
- evidence policy;
- source commit SHA(s);
- confidentiality/publication constraints;
- known domain terminology;
- unresolved stakeholder questions.

## Documentation Change Brief
Create a documentation-scoped Change Brief with:
- goal;
- audience;
- questions to answer;
- non-goals;
- evidence requirements;
- coverage expectations;
- required artifacts;
- publication format;
- unknowns/risks.

## Stable-ID namespace
Reserve the run's ID namespaces:
CMP, ENT, STORE, INT, JOB, RULE, CAP, PROC, TERM.

Do not mint findings yet; only establish the namespace and run metadata.

## Stop conditions
Stop if scope mixes incompatible repositories without an inventory, if the requested audience is unknown and materially changes the deliverable, or if publication would require inventing unavailable business intent.

## Handoff
Send the scoped brief, source SHA(s), and artifact checklist to Codebase Cartographer.
