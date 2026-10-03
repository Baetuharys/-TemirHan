# Case: SolidWorks-to-DXF Production Release

## Scenario
A sheet-metal model has a flat pattern and drawing. A DXF must be released to laser production.

## Required skill chain
`solidworks-sheet-metal-workflow` → `flat-pattern-workflow` → `solidworks-dxf-release-check` → `laser-dxf-marking-workflow`

## Required behavior
- Verify the correct configuration/body and flat pattern.
- Verify units/scale and orientation.
- Check geometry cleanliness and duplicate/open entities.
- Check cut/mark separation.
- Link drawing revision to released manufacturing data.
- Produce a release checklist rather than assuming export success equals production readiness.
