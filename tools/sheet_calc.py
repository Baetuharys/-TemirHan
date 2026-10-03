#!/usr/bin/env python3
"""Deterministic sheet-metal helper calculations. Standard library only.
Every function returns plain numbers; units are mm, degrees, kg unless the name says otherwise.

CLI examples
  python tools/sheet_calc.py bend --t 2 --r 2 --angle 90 --k 0.4
  python tools/sheet_calc.py mass --area-mm2 150000 --t 2 --density 2660 --holes 4:10
  python tools/sheet_calc.py flat --outside 100 30 30 --bends 2 --t 2 --r 2 --angle 90 --k 0.4
"""
import argparse, math

def bend_allowance(t, r, angle_deg, k):
    return math.radians(angle_deg) * (r + k * t)

def outside_setback(t, r, angle_deg):
    return (r + t) * math.tan(math.radians(angle_deg) / 2)

def bend_deduction(t, r, angle_deg, k):
    return 2 * outside_setback(t, r, angle_deg) - bend_allowance(t, r, angle_deg, k)

def flat_length_outside(segments, n_bends, t, r, angle_deg, k):
    """Sum of outside-to-outside segment lengths minus one bend deduction per bend."""
    return sum(segments) - n_bends * bend_deduction(t, r, angle_deg, k)

def blank_mass_kg(area_mm2, t_mm, density_kg_m3, hole_diameters_mm=()):
    holes = sum(math.pi * (d / 2) ** 2 for d in hole_diameters_mm)
    vol_mm3 = (area_mm2 - holes) * t_mm
    return vol_mm3 * 1e-9 * density_kg_m3            # mm3 -> m3

def cost_rollup(lines):
    """lines: list of (name, amount, tag). Returns total and total by tag."""
    by = {}
    for _, amt, tag in lines:
        by[tag] = by.get(tag, 0.0) + amt
    return sum(by.values()), by

def _main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("bend"); [b.add_argument(f"--{x}", type=float, required=True) for x in ("t", "r", "angle", "k")]
    f = sub.add_parser("flat"); f.add_argument("--outside", type=float, nargs="+", required=True)
    f.add_argument("--bends", type=int, required=True); [f.add_argument(f"--{x}", type=float, required=True) for x in ("t", "r", "angle", "k")]
    m = sub.add_parser("mass"); m.add_argument("--area-mm2", type=float, required=True); m.add_argument("--t", type=float, required=True)
    m.add_argument("--density", type=float, required=True, help="kg/m3, state the source"); m.add_argument("--holes", default="", help="count:diameter, e.g. 4:10")
    a = ap.parse_args()
    if a.cmd == "bend":
        print(f"BA={bend_allowance(a.t,a.r,a.angle,a.k):.3f}  OSSB={outside_setback(a.t,a.r,a.angle):.3f}  BD={bend_deduction(a.t,a.r,a.angle,a.k):.3f}")
    elif a.cmd == "flat":
        print(f"flat length = {flat_length_outside(a.outside,a.bends,a.t,a.r,a.angle,a.k):.3f} mm (K is an input; state its source)")
    else:
        holes = []
        if a.holes:
            n, d = a.holes.split(":"); holes = [float(d)] * int(n)
        print(f"mass = {blank_mass_kg(a.area_mm2,a.t,a.density,holes)*1000:.1f} g (density input: {a.density} kg/m3)")

if __name__ == "__main__":
    _main()
