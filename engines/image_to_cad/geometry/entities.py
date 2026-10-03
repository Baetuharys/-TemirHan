from dataclasses import dataclass, field, asdict
import math

@dataclass(frozen=True)
class Point:
    x: float
    y: float

@dataclass
class Line:
    p1: Point
    p2: Point
    confidence: float = 1.0
    source: str = "detected"
    def length(self): return math.hypot(self.p2.x-self.p1.x,self.p2.y-self.p1.y)
    def angle_deg(self): return math.degrees(math.atan2(self.p2.y-self.p1.y,self.p2.x-self.p1.x))%180
    def midpoint(self): return Point((self.p1.x+self.p2.x)/2,(self.p1.y+self.p2.y)/2)

@dataclass
class Circle:
    center: Point
    radius: float
    confidence: float = 1.0
    source: str = "detected"

@dataclass
class Constraint:
    type: str
    entity_ids: list[int]
    confidence: float
    note: str = ""

@dataclass
class GeometryModel:
    lines: list[Line] = field(default_factory=list)
    circles: list[Circle] = field(default_factory=list)
    constraints: list[Constraint] = field(default_factory=list)
    units: str = "px"
    mm_per_px: float|None = None
    provenance: dict = field(default_factory=dict)

    def to_dict(self):
        def point(p): return {'x':p.x,'y':p.y}
        return {
          'units':self.units,'mm_per_px':self.mm_per_px,'provenance':self.provenance,
          'lines':[{'p1':point(x.p1),'p2':point(x.p2),'confidence':x.confidence,'source':x.source} for x in self.lines],
          'circles':[{'center':point(x.center),'radius':x.radius,'confidence':x.confidence,'source':x.source} for x in self.circles],
          'constraints':[asdict(x) for x in self.constraints]
        }
