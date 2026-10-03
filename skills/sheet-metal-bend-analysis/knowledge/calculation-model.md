# Bend calculation model

## Scope
Use this knowledge when the task asks for bend allowance, flat length, bend deduction, K-factor, or a check of a bend result.

## Core distinction
- Bend allowance (BA): length assigned to the neutral-axis arc inside the developed flat length.
- Bend deduction (BD): quantity deducted from the sum of outside flange dimensions to obtain developed length, under the selected dimensioning convention.
- K-factor: ratio locating the neutral axis through the thickness, `K = t_neutral / t`.

## Minimum inputs
Material/condition, thickness `t`, inside radius `R`, bend angle/convention, flange dimensions, and either validated K-factor data or a shop/SolidWorks bend table. Tooling and machine practice can materially change the result.

## Calculation relationship
For a 90° bend expressed with the bend angle in radians, a common first-order relation is:
`BA = theta * (R + K*t)`
This is a model, not a universal production constant. Confirm the convention used by the CAD system and the fabrication process before releasing a flat pattern.

## Verification
Compare calculated development against a controlled sample, bend table, test coupon, or the approved shop method when production accuracy matters.
