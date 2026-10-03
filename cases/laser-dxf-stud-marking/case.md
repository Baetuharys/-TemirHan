# Case: Laser DXF — Stud/PEM Marking Without Cutting

## Scenario
A flat pattern contains locations for stud fasteners. The laser file must contain visible marking information, but the marked geometry must not be interpreted as a through-cut.

## Known inputs
- Manufacturing process: laser cutting
- Output: DXF
- Requirement: marking visible to downstream process
- Critical risk: sketch geometry may be interpreted as cutting geometry

## Required skill chain
`laser-dxf-marking-workflow` → `solidworks-dxf-release-check` → `sheet-metal-release-workflow`

## Required behavior
1. Separate design intent from DXF geometry.
2. Determine whether the CAM/postprocessor supports separate marking entities/layers.
3. Prefer an explicit CUT/MARK process mapping over assuming that a circle is automatically a mark.
4. Treat CAM as the final manufacturing interpretation layer.
5. Provide a verification checklist before release.
