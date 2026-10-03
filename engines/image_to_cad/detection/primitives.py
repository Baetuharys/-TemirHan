import math
from ..geometry.entities import Point, Line, Circle, GeometryModel

def _canonical_line(x1,y1,x2,y2):
    a=(float(x1),float(y1)); b=(float(x2),float(y2))
    if a>b: a,b=b,a
    return (*a,*b)

def _dedupe_lines(lines, midpoint_tol=6, angle_tol=2.0):
    kept=[]
    for l in sorted(lines,key=lambda x:x.length(),reverse=True):
        m=l.midpoint(); a=l.angle_deg(); dup=False
        for k in kept:
            km=k.midpoint(); ka=k.angle_deg()
            ad=abs((a-ka)%180); ad=min(ad,180-ad)
            if math.hypot(m.x-km.x,m.y-km.y)<=midpoint_tol and ad<=angle_tol:
                dup=True; break
        if not dup: kept.append(l)
    return kept

def detect_primitives(edges, min_line_length=30, max_line_gap=8, hough_threshold=35, detect_circles=True):
    try:
        import cv2, numpy as np
    except ImportError as e:
        raise RuntimeError('OpenCV and NumPy are required; install requirements.txt') from e
    model=GeometryModel()
    raw=cv2.HoughLinesP(edges,1,np.pi/180,threshold=int(hough_threshold),minLineLength=int(min_line_length),maxLineGap=int(max_line_gap))
    lines=[]
    if raw is not None:
        for x1,y1,x2,y2 in raw[:,0,:]:
            lines.append(Line(Point(float(x1),float(y1)),Point(float(x2),float(y2)),confidence=.75,source='HoughLinesP'))
    model.lines=_dedupe_lines(lines)
    if detect_circles:
        blur=cv2.GaussianBlur(edges,(5,5),1)
        circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,dp=1.2,minDist=20,param1=100,param2=18,minRadius=3,maxRadius=0)
        if circles is not None:
            for x,y,r in circles[0]: model.circles.append(Circle(Point(float(x),float(y)),float(r),confidence=.70,source='HoughCircles'))
    return model
