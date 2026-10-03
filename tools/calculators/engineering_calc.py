#!/usr/bin/env python3
import argparse, json
from bend import bend_allowance,outside_setback,bend_deduction
from mass import rectangular_plate_mass_kg
from cost import price_from_margin,price_from_markup
from tolerance import worst_case,rss
from thermal import required_airflow_m3h
from gasket import compression_percent
from stiffness import rectangular_second_moment_mm4,cantilever_end_load_deflection_mm,simply_supported_center_load_deflection_mm

def main():
    ap=argparse.ArgumentParser(description='Mechanical AI deterministic calculator')
    sp=ap.add_subparsers(dest='cmd',required=True)
    b=sp.add_parser('bend'); [b.add_argument('--'+x,type=float,required=True) for x in ('t','r','angle','k')]
    m=sp.add_parser('mass'); [m.add_argument('--'+x,type=float,required=True) for x in ('w','h','t','density')]
    c=sp.add_parser('price'); c.add_argument('--cost',type=float,required=True); g=c.add_mutually_exclusive_group(required=True); g.add_argument('--margin',type=float); g.add_argument('--markup',type=float)
    q=sp.add_parser('airflow'); [q.add_argument('--'+x,type=float,required=True) for x in ('heat','dt')]
    t=sp.add_parser('tolerance'); t.add_argument('--nominal',type=float,default=0.0); t.add_argument('--plusminus',type=float,nargs='+',required=True); t.add_argument('--method',choices=['worst','rss'],default='worst')
    gk=sp.add_parser('gasket'); gk.add_argument('--free',type=float,required=True); gk.add_argument('--compressed',type=float,required=True)
    st=sp.add_parser('beam'); st.add_argument('--load',type=float,required=True); st.add_argument('--length',type=float,required=True); st.add_argument('--e',type=float,required=True); st.add_argument('--width',type=float,required=True); st.add_argument('--depth',type=float,required=True); st.add_argument('--support',choices=['cantilever','simply-supported'],required=True)
    a=ap.parse_args()
    if a.cmd=='bend':
        out={'BA_mm':bend_allowance(a.t,a.r,a.angle,a.k),'OSSB_mm':outside_setback(a.t,a.r,a.angle),'BD_mm':bend_deduction(a.t,a.r,a.angle,a.k),'evidence':'CALCULATED','warning':'K-factor is caller-supplied and must be production-validated.'}
    elif a.cmd=='mass': out={'mass_kg':rectangular_plate_mass_kg(a.w,a.h,a.t,a.density),'evidence':'CALCULATED','warning':'Density is caller-supplied.'}
    elif a.cmd=='price': out={'price':price_from_margin(a.cost,a.margin) if a.margin is not None else price_from_markup(a.cost,a.markup),'evidence':'CALCULATED'}
    elif a.cmd=='airflow': out={'airflow_m3h':required_airflow_m3h(a.heat,a.dt),'evidence':'CALCULATED','warning':'First-pass sensible-heat balance only; fan pressure/recirculation/filter losses are not modelled.'}
    elif a.cmd=='tolerance':
        fn=worst_case if a.method=='worst' else rss
        out={'nominal':a.nominal,'plusminus':fn(a.plusminus),'method':a.method,'evidence':'CALCULATED','warning':'RSS requires a justified statistical basis; worst-case is deterministic.'}
    elif a.cmd=='gasket': out={'compression_percent':compression_percent(a.free,a.compressed),'evidence':'CALCULATED','warning':'Compare with the exact gasket supplier compression window; this does not establish an IP rating.'}
    else:
        I=rectangular_second_moment_mm4(a.width,a.depth)
        d=cantilever_end_load_deflection_mm(a.load,a.length,a.e,I) if a.support=='cantilever' else simply_supported_center_load_deflection_mm(a.load,a.length,a.e,I)
        out={'I_mm4':I,'deflection_mm':d,'evidence':'CALCULATED','warning':'Simple beam idealization only; broad sheet panels/doors may require plate/shell/FEA or physical test.'}
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
