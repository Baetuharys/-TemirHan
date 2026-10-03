# Flat length hand-check

Symbols: t thickness, R inside radius, theta bend angle (turned angle, 90 deg for a right-angle bend), K K-factor.

- Bend allowance: `BA = theta(rad) x (R + K x t)`
- Outside setback: `OSSB = (R + t) x tan(theta/2)`
- Bend deduction: `BD = 2 x OSSB - BA`
- Outside-to-outside lengths: `L_flat = sum(outside segments) - n_bends x BD`
- Inside-to-inside or mid-line lengths use their own formulas; convert to outside first.

## Worked check: U-channel
Outside dimensions 100 (web) + 30 + 30 (flanges), t = 2, R = 2, two 90 deg bends, K = 0.4 (ASSUMED).
BA = 4.398, OSSB = 4.000, BD = 3.602 -> `L_flat = 160 - 2 x 3.602 = 152.796 mm`.
If the shop's K is 0.35, BA drops to 4.241 and L_flat becomes 153.11 mm (+0.31 mm): K matters at this level of precision.

## When the difference to CAD is large
1. Different bend model (K-factor vs bend table vs deduction).
2. Radius mismatch (inside vs outside).
3. Segment measured to a different reference (mid-line vs outside).
4. Angle recorded as the included angle (90 deg interior = 90 deg turned here; but a 60 deg included angle is a 120 deg turned angle).
