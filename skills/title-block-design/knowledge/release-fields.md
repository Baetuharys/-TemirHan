# Sheet-metal title-block field strategy

The title block should expose production-critical information without duplicating data that can be linked from model properties.

## Candidate fields
- Part number / drawing number
- Part name / description
- Material
- Sheet thickness
- Revision number
- Revision date
- Main assembly / parent assembly reference when reliably available
- Drawing scale and units
- General tolerance reference
- Surface finish/coating where applicable

## Design rule
Prefer a single authoritative source for each field. If a value is model-driven, link it to the corresponding Custom Property or configuration-specific property rather than manually typing a second copy.

## Release check
Verify that displayed values match the released model/configuration and that revision data is intentionally updated.
