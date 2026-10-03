---
id: mai-skill-engineering-source-verification
title: Engineering Source Verification
type: skill
status: active
version: 1.0.0
summary: Verify standards, software documentation and supplier claims before they become release-critical engineering facts. Tracks edition/status/provenance and flags drafts, replacements and version-specific APIs.
tags: [sources, standards, provenance, verification]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, available drawings/CAD/images/data, constraints, desired decision or deliverable
output_contract: evidence-labelled engineering analysis, risks, unresolved inputs, verification actions, next step
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: engineering-source-verification
description: Verify standards, software documentation and supplier claims before they become release-critical engineering facts. Tracks edition/status/provenance and flags drafts, replacements and version-specific APIs.
---
# Engineering Source Verification

## Trigger
Use when a claim depends on a standard edition, SolidWorks API/UI behavior, supplier datasheet or any external technical source.

## Workflow
1. Classify the claim: project-supplied, standard, software doc, supplier data or practice.
2. Resolve the governing source and edition/version.
3. Check lifecycle status and whether a newer edition/draft exists.
4. Record source ID and distinguish public metadata from licensed content.
5. If the exact requirement cannot be verified, mark it UNKNOWN instead of paraphrasing memory.
6. Return claim, source, status, limitations and next verification action.

## Knowledge to load
- `sources/README.md`
- `knowledge/21-requirements-risk-and-release.md`

## Output discipline
- Distinguish facts, calculations, practice, assumptions, estimates and unknowns.
- Do not upgrade a draft analysis into a certification or release claim.
- Prefer a concrete next action over generic advice.
