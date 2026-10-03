#!/usr/bin/env python3
"""Mechanical AI command entry point. Standard-library core; optional CV deps for image-cad."""
import argparse, subprocess, sys, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run_py(rel,*args):
    return subprocess.call([sys.executable,str(ROOT/rel),*map(str,args)],cwd=ROOT)

def main():
    ap=argparse.ArgumentParser(prog='mai',description='Mechanical AI Engineering Library command line')
    sp=ap.add_subparsers(dest='cmd',required=True)
    sp.add_parser('validate',help='run repository release/integrity checks')
    s=sp.add_parser('search',help='search engineering knowledge (BM25)'); s.add_argument('query'); s.add_argument('-k',type=int,default=5); s.add_argument('--category')
    c=sp.add_parser('calc',help='deterministic engineering calculator'); c.add_argument('calc_args',nargs=argparse.REMAINDER)
    i=sp.add_parser('image-cad',help='draft image→CAD reconstruction'); i.add_argument('image'); i.add_argument('--out',default='image-cad-output'); i.add_argument('--ref-p1',nargs=2,type=float); i.add_argument('--ref-p2',nargs=2,type=float); i.add_argument('--ref-mm',type=float)
    n=sp.add_parser('new-prompt',help='MergenHan-style prompt asset creation'); n.add_argument('kind',choices=['master','module','blueprint']); n.add_argument('slug'); n.add_argument('--category')
    sp.add_parser('rebuild',help='regenerate catalogs, RAG index and provider export packages')
    a=ap.parse_args()
    if a.cmd=='validate': sys.exit(run_py('scripts/validate_all.py'))
    if a.cmd=='search':
        args=[a.query,'-k',a.k];
        if a.category: args += ['--category',a.category]
        sys.exit(run_py('rag/retrieve.py',*args))
    if a.cmd=='calc': sys.exit(run_py('tools/calculators/engineering_calc.py',*a.calc_args))
    if a.cmd=='image-cad':
        cmd=[sys.executable,'-m','engines.image_to_cad.cli',a.image,'--out',a.out]
        if a.ref_p1 and a.ref_p2 and a.ref_mm: cmd += ['--ref-p1',*map(str,a.ref_p1),'--ref-p2',*map(str,a.ref_p2),'--ref-mm',str(a.ref_mm)]
        sys.exit(subprocess.call(cmd,cwd=ROOT))
    if a.cmd=='new-prompt':
        args=[a.kind,a.slug];
        if a.category: args += ['--category',a.category]
        sys.exit(run_py('scripts/new_prompt.py',*args))
    if a.cmd=='rebuild':
        cmds=[['scripts/generate_catalog.py'],['scripts/generate_skill_catalog.py'],['training/scripts/build_rag_chunks.py'],['rag/build_index.py'],['scripts/export_chatgpt.py'],['scripts/export_claude_skills.py']]
        for x in cmds:
            rc=run_py(*x)
            if rc: sys.exit(rc)
        print('Rebuild complete.')
if __name__=='__main__': main()
