---
id: mai-blueprint-market-intelligence
title: Market Intelligence & Potential Customer Research
type: blueprint
status: active
version: 1.1.0
summary: Blueprint for evidence-based market, competitor, project and potential-customer research.
tags: [market-intelligence, market-research, business-development]
depends_on: [mai-module-context-audit, mai-module-source-validation, mai-module-uncertainty-management, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: geography, sector/capability, company criteria, project/time window, desired output
output_contract: structured company/project findings with evidence, dates, uncertainty and research gaps
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Market Intelligence & Potential Customer Research

## Scope
Research public market signals relevant to mechanical/sheet-metal business development in Türkiye and requested nearby markets.

## Workflow
1. Define geography, sector, capability and time window.
2. Discover candidates across multiple source classes.
3. Verify identity and business role.
4. Research projects, contracts, investments and procurement signals.
5. Research public customer/partner relationships.
6. Build company dossiers.
7. Identify potential customer fit from evidence-backed signals.
8. Report sources, dates, evidence grades and unknowns.

## Required checks
- No unsupported customer or contract claims.
- No silent geography expansion.
- Current claims require current sources.
- Important claims should be corroborated where practical.
- Facts, source-reported claims and inference must be visibly separated.
