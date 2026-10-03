---
id: mai-skill-solidworks-macro-generator
title: SolidWorks Macro Generator
type: skill
status: active
version: 0.2.0
summary: Design, generate, explain, and debug SolidWorks VBA macro workflows with explicit assumptions and API verification points.
tags: [solidworks, macro, vba, api, automation]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-source-validation, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: desired automation, document type, SolidWorks version when known, inputs/outputs, existing code if debugging
output_contract: macro code, usage, assumptions, API/version risks, test procedure
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: solidworks-macro-generator
description: Generate cautious SolidWorks API macros (VBA) with read-first design, null checks, no invented API members and a test-on-copy protocol. Use for SolidWorks makro, otomasyon, özel özellik, toplu işlem.
---
# SolidWorks Macro Generator
## Workflow
1. Convert the request into inputs, actions, outputs, and failure cases.
2. Identify Part, Assembly, Drawing, and configuration context.
3. Choose the smallest API surface needed.
4. Generate code with clear names and error handling.
5. Explain how to run it.
6. Provide a small test procedure before production use.
7. Mark version-sensitive API calls for documentation verification.
## Rules
- Never claim an unverified API member exists.
- Do not hide destructive operations.
- Preserve the user's intent during debugging and isolate the failing operation.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/13-solidworks-macros-api.md`
- `knowledge/03-solidworks-sheet-metal.md`
