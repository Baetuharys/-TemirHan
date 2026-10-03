# Case: 5754 Aluminum Weight Analysis

## Scenario
A sheet-metal part is modeled in SolidWorks. The user needs its mass to match the production expectation and wants the material density treated as a controlled input.

## Known inputs
- Material family: EN AW-5754 aluminum
- Geometry source: SolidWorks model
- Required result: mass/weight estimate or verification
- Critical requirement: density must not be silently invented

## Required skill chain
`material-property-research` → `weight-analysis` → `technical-drawing-review`

## Required behavior
1. Identify exact alloy/temper/product-form information available.
2. Identify density source and whether it is a nominal or source-specific value.
3. Use model volume and density consistently.
4. State unit system.
5. If geometry or material state is incomplete, stop short of false precision.
6. Report the verification path for reconciling CAD mass with expected production mass.
