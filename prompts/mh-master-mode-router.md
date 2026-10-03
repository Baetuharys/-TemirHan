---
id: mai-master-mode-router
title: Mechanical AI Mode Router
type: master
status: active
version: 1.0.0
summary: Selects the correct operating mode and specialist skills for mechanical engineering, manufacturing, documentation, commercial, and market-intelligence tasks.
tags: [core, routing, engineering, market-intelligence]
depends_on: []
last_reviewed: 2026-10-02
---

# Mode Router

Select one or more modes from `mh-compat/modes/README.md`. Do not load every skill by default.

Priority:
1. intake when requirements are unclear;
2. research / market-intelligence when current external evidence is required;
3. engineering for calculations/design;
4. verification/audit before relying on a result;
5. release before production issue;
6. commercial for pricing/quotation.

Use the specialist skills as the domain layer and keep this router provider-agnostic.
