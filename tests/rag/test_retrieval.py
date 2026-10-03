import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from rag.build_index import build
from rag.retrieve import search
def test():
    idx=build(out_path=ROOT/'rag/index.json')
    r=search('K faktörü bend deduction açınım',k=5,index=idx)
    assert r and any('bending' in str(x.get('source','')).lower() or 'flat' in str(x.get('source','')).lower() for x in r),r[:2]
    r2=search('IP65 enclosure gasket',k=5,index=idx)
    assert r2
if __name__=='__main__': test(); print('ok: rag retrieval')
