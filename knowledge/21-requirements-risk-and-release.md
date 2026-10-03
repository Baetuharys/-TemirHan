---
id: mai-knowledge-requirements-risk-release
title: Requirements, Risk and Engineering Release
category: engineering-governance
evidence: practice
last_reviewed: 2026-10-02
verify_before_release: [requirements baseline, unresolved assumptions, verification plan, revision state]
maturity: implemented
source_ids: []
---

# Requirements, Risk and Engineering Release

## 1. Requirement record
A useful requirement is identifiable, testable and tied to a source. Record: ID, statement, source/customer, priority, verification method, status and affected parts.

Bad: “make it strong.”  Better: “door shall not permanently deform under the project-defined service load; verify by agreed test/analysis.” The actual load must come from the project, not the AI.

## 2. Lightweight design-risk review
For each important requirement capture:
- failure mode;
- effect;
- likely causes;
- current prevention/detection;
- proposed action;
- owner/status.

The repository does not prescribe a universal risk score because company FMEA schemes differ. Use the organization’s method when one exists.

## 3. Assumption register
Every `ASSUMED`, `ESTIMATED` or `UNKNOWN` release-relevant item goes into an assumption register. Each row needs an owner and a closure action. “AI said so” is not closure evidence.

## 4. Release gates
A production release should confirm at minimum:
- material/thickness/finish;
- interfaces and critical dimensions;
- bend model/tooling source where flat size depends on it;
- weld/fastener definition;
- drawing standard and revision;
- DXF layer/entity review;
- ingress/thermal claims phrased correctly;
- unresolved deviations approved;
- BOM and quotation assumptions aligned with the released design.

## 5. Change control
When a design changes, identify affected CAD, drawings, DXF, BOM, cost, quotation, test plan and documentation. A revision is not complete when only the `.SLDPRT` changed.
