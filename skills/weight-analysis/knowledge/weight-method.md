# Weight method

## Relationships
- Solid: `m = V x rho`.
- Flat blank: `m = (A_blank - sum(A_holes)) x t x rho`. A circle hole of diameter d removes `pi x d^2 / 4`.
- Assembly: `m_total = sum(parts) + hardware + coating + welds`; keep each as its own line.

## Unit conversions
- `1 mm^3 = 1e-9 m^3`. With rho in kg/m^3: `m[kg] = V[mm^3] x 1e-9 x rho`.
- `g/cm^3 x 1000 = kg/m^3`.

## Where the numbers go wrong
1. Density from memory instead of a source (differences of 1-2% between sources are normal for aluminium alloys).
2. Thickness tolerance: for a 2 mm sheet a thickness deviation shifts mass by the same percentage.
3. CAD material assignment: the mass-properties dialog uses the density of the material assigned to the part; a custom or default material changes the answer.
4. Configurations: the flat-pattern configuration and the formed configuration have different volumes only through the bend model; use the one that matches the question.
5. Finish: powder or zinc coating adds mass that is not in the base-metal density.
