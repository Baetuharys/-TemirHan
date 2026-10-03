"""Mass calculations. Density must be supplied or source-backed by the caller."""
import math

def blank_mass_kg(area_mm2:float, thickness_mm:float, density_kg_m3:float, circular_holes_mm=())->float:
    if area_mm2 <= 0 or thickness_mm <= 0 or density_kg_m3 <= 0: raise ValueError('area, thickness and density must be >0')
    removed=sum(math.pi*(float(d)/2)**2 for d in circular_holes_mm)
    if removed >= area_mm2: raise ValueError('removed hole area must be smaller than blank area')
    return (area_mm2-removed)*thickness_mm*1e-9*density_kg_m3

def rectangular_plate_mass_kg(width_mm:float,height_mm:float,thickness_mm:float,density_kg_m3:float)->float:
    return blank_mass_kg(width_mm*height_mm,thickness_mm,density_kg_m3)
