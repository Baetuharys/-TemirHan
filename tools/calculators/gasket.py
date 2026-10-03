"""Deterministic gasket geometry helpers. Supplier limits still govern release."""

def compression_percent(free_thickness_mm: float, compressed_thickness_mm: float) -> float:
    if free_thickness_mm <= 0:
        raise ValueError('free thickness must be > 0')
    if compressed_thickness_mm < 0:
        raise ValueError('compressed thickness must be >= 0')
    return (free_thickness_mm-compressed_thickness_mm)/free_thickness_mm*100.0


def compressed_thickness_mm(free_thickness_mm: float, compression_percent_value: float) -> float:
    if free_thickness_mm <= 0:
        raise ValueError('free thickness must be > 0')
    if not 0 <= compression_percent_value < 100:
        raise ValueError('compression percent must be in [0,100)')
    return free_thickness_mm*(1-compression_percent_value/100.0)
