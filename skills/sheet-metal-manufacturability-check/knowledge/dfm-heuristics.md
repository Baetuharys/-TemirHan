# DFM heuristics (PRACTICE: starting points, replace with the shop's rules)

These are commonly used multiples; they vary by material, tooling and machine. Treat every number as a question to the shop, never as a limit.

| Topic | Common starting heuristic | Why it matters |
|---|---|---|
| Hole diameter (laser) | not smaller than about 1 x thickness | small holes pit or distort |
| Hole edge distance | about 1.5-2 x thickness minimum | tear-out, distortion |
| Hole to bend line | about 2-2.5 x thickness + bend radius | hole elongation |
| Minimum flange length | about 3-4 x thickness (+ radius) | die support |
| Bend relief | depth >= radius + thickness, width >= thickness (or per CAD default) | tearing at corners |
| Slot/notch width | about 1 x thickness | thermal distortion, tool strength |
| Bend radius vs thickness | material and grain dependent; aluminium tempers crack at small radii | cracks on the outside |

## Order of questions to the shop
1. Material availability and thickness tolerance.
2. Smallest bend radius and tool set they use for this thickness.
3. Their bend table or K-factor.
4. Their minimum flange and hole-to-bend rule.
5. Coating thickness and masking practice.
