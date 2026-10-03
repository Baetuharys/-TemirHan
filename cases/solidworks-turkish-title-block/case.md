# Case: SolidWorks Turkish UI — Sheet-Metal Title Block

## Scenario
A company uses SolidWorks in Turkish. A sheet-metal drawing title block must show revision number/date, description, material, thickness, part identity, and main assembly information.

## Known inputs
- UI language: Turkish
- Domain: sheet-metal technical drawing
- Required outputs: field design and implementation guidance
- User preference: simple title block with more description space

## Required skill chain
`solidworks-turkish-ui` → `title-block-design` → `technical-drawing-review`

## Required behavior
- Separate stable UI facts from version-dependent menu wording.
- Distinguish a property that SolidWorks can expose automatically from one requiring a custom property or manual convention.
- Never invent a property name merely because a field sounds plausible.
- Explain where a custom property would be used when automatic linkage is not guaranteed.
