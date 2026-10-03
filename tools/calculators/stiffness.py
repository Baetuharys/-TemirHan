"""Simple beam idealizations for first-pass reasoning only.

Do not use these functions as a plate/shell or enclosure certification model.
E is N/mm^2, loads N, lengths mm; output deflection is mm.
"""

def rectangular_second_moment_mm4(width_mm: float, depth_mm: float) -> float:
    if width_mm <= 0 or depth_mm <= 0:
        raise ValueError('section dimensions must be > 0')
    return width_mm*depth_mm**3/12.0


def cantilever_end_load_deflection_mm(load_n: float, length_mm: float, e_mpa: float, i_mm4: float) -> float:
    if length_mm <= 0 or e_mpa <= 0 or i_mm4 <= 0:
        raise ValueError('length, E and I must be > 0')
    return load_n*length_mm**3/(3.0*e_mpa*i_mm4)


def simply_supported_center_load_deflection_mm(load_n: float, length_mm: float, e_mpa: float, i_mm4: float) -> float:
    if length_mm <= 0 or e_mpa <= 0 or i_mm4 <= 0:
        raise ValueError('length, E and I must be > 0')
    return load_n*length_mm**3/(48.0*e_mpa*i_mm4)
