# Default workflow — Weight Analysis

1. Identify what is wanted: blank mass, finished part mass, assembly mass, shipping mass.
2. Pick density with a stated source (`knowledge/15`); never assume stainless = steel.
3. Compute `m = V·ρ` (V in m³, ρ in kg/m³) or `m = A·T·ρ`; show the substituted numbers.
4. Subtract cut-outs; add hardware, welds, coating separately and label them estimates.
5. Compare with CAD mass properties; explain differences (density, configuration, coating).
6. Apply order-of-magnitude check (kg/m² per mm: steel ≈ 7.85).
7. Give result with units and an uncertainty note.

## Gate before output
- Units consistent (mm vs m).
- Density grade matches the real grade.
- Blank vs finished mass is not confused.
