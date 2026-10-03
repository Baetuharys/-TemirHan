import math
from .entities import Constraint

def _angle_diff(a,b):
    d=abs((a-b)%180); return min(d,180-d)

def infer_constraints(model, angle_tol_deg=2.0, concentric_tol=3.0):
    out=[]
    for i,l in enumerate(model.lines):
        a=l.angle_deg()
        if min(abs(a),abs(180-a)) <= angle_tol_deg: out.append(Constraint('horizontal',[i],.95))
        if abs(a-90) <= angle_tol_deg: out.append(Constraint('vertical',[i],.95))
    for i,a in enumerate(model.lines):
        for j,b in enumerate(model.lines[i+1:],i+1):
            d=_angle_diff(a.angle_deg(),b.angle_deg())
            if d <= angle_tol_deg: out.append(Constraint('parallel',[i,j],max(.5,1-d/angle_tol_deg)))
            if abs(d-90) <= angle_tol_deg: out.append(Constraint('perpendicular',[i,j],max(.5,1-abs(d-90)/angle_tol_deg)))
    for i,a in enumerate(model.circles):
        for j,b in enumerate(model.circles[i+1:],i+1):
            dist=math.hypot(a.center.x-b.center.x,a.center.y-b.center.y)
            if dist <= concentric_tol: out.append(Constraint('concentric',[i,j],max(.5,1-dist/max(concentric_tol,1e-9))))
    model.constraints=out
    return model
