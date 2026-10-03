from dataclasses import dataclass
import math
from ..geometry.entities import Point, Line, Circle, GeometryModel

@dataclass
class ScaleCalibration:
    mm_per_px: float
    source: str
    confidence: float = 1.0

    @classmethod
    def from_reference(cls,p1_px,p2_px,real_distance_mm,source='user-reference',confidence=1.0):
        dx=float(p2_px[0])-float(p1_px[0]); dy=float(p2_px[1])-float(p1_px[1])
        pix=math.hypot(dx,dy)
        if pix<=0 or real_distance_mm<=0: raise ValueError('reference distances must be >0')
        return cls(float(real_distance_mm)/pix,source,float(confidence))

def apply_scale(model:GeometryModel,cal:ScaleCalibration)->GeometryModel:
    s=cal.mm_per_px
    model.lines=[Line(Point(l.p1.x*s,l.p1.y*s),Point(l.p2.x*s,l.p2.y*s),l.confidence,l.source) for l in model.lines]
    model.circles=[Circle(Point(c.center.x*s,c.center.y*s),c.radius*s,c.confidence,c.source) for c in model.circles]
    model.units='mm'; model.mm_per_px=s
    model.provenance['scale']={'tag':'CALCULATED','source':cal.source,'confidence':cal.confidence,'mm_per_px':s}
    return model
