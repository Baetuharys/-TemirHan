import math, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/calculators'))
from bend import *
from mass import *
from cost import *
from tolerance import *
from thermal import *
def close(a,b,tol=1e-6): assert abs(a-b)<=tol,(a,b)
def test_all():
    close(bend_allowance(2,2,90,.4),math.pi/2*2.8)
    close(bend_deduction(2,2,90,.4),8-math.pi/2*2.8)
    close(rectangular_plate_mass_kg(1000,2000,3,7850),47.1,1e-8)
    close(price_from_margin(132.36,.20),165.45,1e-8)
    assert worst_case([10,20],[.1,.2])['plus_minus']==.30000000000000004
    close(rss([10,20],[.1,.2])['plus_minus'],math.sqrt(.05))
    close(required_airflow_m3h(100,10),29.8507462687,1e-6)
if __name__=='__main__': test_all(); print('ok: calculators')

from gasket import compression_percent
from stiffness import rectangular_second_moment_mm4, cantilever_end_load_deflection_mm
assert abs(compression_percent(10, 7.5)-25.0) < 1e-9
I = rectangular_second_moment_mm4(20, 10)
assert abs(I - 1666.6666666667) < 1e-6
assert cantilever_end_load_deflection_mm(100, 100, 200000, I) > 0
