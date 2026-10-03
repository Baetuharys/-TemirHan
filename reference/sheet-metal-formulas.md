# Sheet-metal formulas (check the K-factor source before use)

Symbols: T = thickness, R = inside bend radius, θ = bend angle (angle the flange is turned,
90° for a right-angle bend), K = K-factor (neutral-axis position ÷ T).

- Bend allowance: `BA = θ(rad) × (R + K·T)`   with θ(rad) = θ(°) × π / 180
- Outside setback: `OSSB = (R + T) × tan(θ/2)`
- Bend deduction: `BD = 2 × OSSB − BA`
- Flat length of a part = sum of flat segments + sum of BA (or − sum of BD when dimensions are outside-to-outside)
- Weight: `m = V × ρ`  (keep V in m³ and ρ in kg/m³, or mm³ and kg/mm³; never mix)

K-factor is **not a constant**. It depends on material, thickness, radius, tooling and
method. Use the shop's bend table, the SolidWorks gauge table, or a test bend.
Typical textbook range is 0 < K < 0.5; a number outside the supplier's data is an assumption.

Approximate densities (state the source in any real calculation):
carbon steel ≈ 7850 kg/m³ · stainless 304 ≈ 7900–8000 kg/m³ · aluminium 5052 ≈ 2680 kg/m³.
