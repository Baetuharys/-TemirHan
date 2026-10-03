import math

def validate_geometry(model, min_line_length=None, min_hole_diameter=None):
    issues=[]; warnings=[]
    for i,l in enumerate(model.lines):
        if l.length() <= 1e-9: issues.append(f'line {i}: zero length')
        if min_line_length is not None and model.units=='mm' and l.length()<min_line_length:
            warnings.append(f'line {i}: {l.length():.3f} mm below caller-supplied minimum {min_line_length} mm')
    for i,c in enumerate(model.circles):
        if c.radius<=0: issues.append(f'circle {i}: radius <=0')
        if min_hole_diameter is not None and model.units=='mm' and 2*c.radius<min_hole_diameter:
            warnings.append(f'circle {i}: diameter {2*c.radius:.3f} mm below caller-supplied minimum {min_hole_diameter} mm')
    if model.units!='mm': warnings.append('geometry is still pixel-space; do not use as manufacturing dimensions')
    return {'pass':not issues,'issues':issues,'warnings':warnings}
