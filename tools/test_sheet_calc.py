import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sheet_calc import *

def close(a, b, tol=1e-3): assert abs(a - b) < tol, (a, b)

# 90 deg, t=2, R=2, K=0.4  -> BA = (pi/2)*2.8
close(bend_allowance(2, 2, 90, 0.4), math.pi / 2 * 2.8)
close(outside_setback(2, 2, 90), 4.0)
close(bend_deduction(2, 2, 90, 0.4), 8 - math.pi / 2 * 2.8)
# U channel 100 + 30 + 30 outside, two 90 deg bends
close(flat_length_outside([100, 30, 30], 2, 2, 2, 90, 0.4), 160 - 2 * (8 - math.pi / 2 * 2.8))
# plate 500x300x2 aluminium 2660 kg/m3 -> 798.0 g ; 4 holes d10 -> 796.3 g
close(blank_mass_kg(500 * 300, 2, 2660) * 1000, 798.0, 0.05)
close(blank_mass_kg(500 * 300, 2, 2660, [10] * 4) * 1000, 796.33, 0.05)
# density sensitivity 2660 vs 2700
close(blank_mass_kg(500 * 300, 2, 2700) * 1000, 810.0, 0.05)
total, by = cost_rollup([("a", 10, "SUPPLIED"), ("b", 5, "ASSUMED"), ("c", 2.5, "CALCULATED")])
close(total, 17.5); close(by["ASSUMED"], 5)
print("ok: sheet_calc tests passed")
