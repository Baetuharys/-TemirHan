# End-to-End Release Integration Test

Scenario: a sheet-metal part is modeled in SolidWorks and must be released for laser, marking, bending, welding/fasteners, and assembly.

Expected chain:
1. engineering-task-intake
2. solidworks-sheet-metal-workflow
3. sheet-metal-manufacturability-check
4. flat-pattern-workflow
5. technical-drawing-review
6. solidworks-dxf-release-check / laser-dxf-marking-workflow
7. sheet-metal-weld-fastener-review
8. weight-analysis / cost-analysis
9. technical-document-generator
10. sheet-metal-release-workflow

Pass criteria: identity/revision consistency, explicit assumptions, process mapping, DXF verification, and a final release checklist.
