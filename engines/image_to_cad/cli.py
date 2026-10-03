#!/usr/bin/env python3
import argparse, json
from .pipeline import process_image

def main():
    ap=argparse.ArgumentParser(description='Image-to-CAD draft geometry reconstruction')
    ap.add_argument('image'); ap.add_argument('--out',default='image-cad-output')
    ap.add_argument('--ref-p1',nargs=2,type=float); ap.add_argument('--ref-p2',nargs=2,type=float); ap.add_argument('--ref-mm',type=float)
    a=ap.parse_args(); ref=None
    if a.ref_p1 and a.ref_p2 and a.ref_mm: ref={'p1_px':a.ref_p1,'p2_px':a.ref_p2,'distance_mm':a.ref_mm}
    r=process_image(a.image,reference=ref,out_dir=a.out); print(json.dumps(r['validation'],ensure_ascii=False,indent=2))
if __name__=='__main__': main()
