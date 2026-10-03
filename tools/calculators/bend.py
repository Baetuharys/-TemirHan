"""Deterministic bend geometry. Inputs are mm/degrees. K-factor is an INPUT, not a material constant."""
import math

def _positive(name,v,allow_zero=False):
    if v < 0 or (not allow_zero and v == 0): raise ValueError(f"{name} must be {'>=0' if allow_zero else '>0'}")

def bend_allowance(t_mm:float, r_mm:float, angle_deg:float, k_factor:float)->float:
    _positive('thickness',t_mm); _positive('radius',r_mm,True)
    if not 0 < angle_deg < 180: raise ValueError('angle_deg must be between 0 and 180')
    if not 0 < k_factor < 1: raise ValueError('k_factor must be between 0 and 1')
    return math.radians(angle_deg)*(r_mm+k_factor*t_mm)

def outside_setback(t_mm:float, r_mm:float, angle_deg:float)->float:
    _positive('thickness',t_mm); _positive('radius',r_mm,True)
    if not 0 < angle_deg < 180: raise ValueError('angle_deg must be between 0 and 180')
    return (r_mm+t_mm)*math.tan(math.radians(angle_deg)/2)

def bend_deduction(t_mm:float, r_mm:float, angle_deg:float, k_factor:float)->float:
    return 2*outside_setback(t_mm,r_mm,angle_deg)-bend_allowance(t_mm,r_mm,angle_deg,k_factor)

def flat_length_outside(outside_segments_mm, bends):
    """bends is iterable of dicts: t_mm,r_mm,angle_deg,k_factor. One BD is subtracted per bend."""
    return sum(float(x) for x in outside_segments_mm)-sum(bend_deduction(**b) for b in bends)
