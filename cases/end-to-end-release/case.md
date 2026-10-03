# Case: End-to-End Sheet-Metal Release

## Scenario
A sheet-metal enclosure component moves from CAD through drawing, DXF, laser, marking, bending, welding/fasteners, assembly, cost, and documentation.

## Required chain
`engineering-task-intake` → `solidworks-sheet-metal-workflow` → `technical-drawing-review` → `solidworks-dxf-release-check` → `laser-dxf-marking-workflow` → `sheet-metal-weld-fastener-review` → `cost-analysis` → `technical-document-generator`

## Required behavior
At every handoff, identify what information is consumed by the next process, what has been verified, and what remains an assumption.

## Release principle
A downstream artifact must not silently inherit an unresolved upstream uncertainty.
