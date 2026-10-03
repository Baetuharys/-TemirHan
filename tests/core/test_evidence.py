import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from engineering_core.evidence import EvidenceValue,EvidenceTag
from engineering_core.validation import release_gate
def test():
    assert EvidenceValue(2,EvidenceTag.SUPPLIED,'mm').validate()==[]
    assert EvidenceValue(3,EvidenceTag.SOURCE_BACKED,'mm').validate()
    g=release_gate({'thickness':EvidenceValue(2,EvidenceTag.SUPPLIED,'mm'),'k':EvidenceValue(.4,EvidenceTag.ASSUMED)})
    assert not g['pass'] and any('ASSUMED' in x for x in g['blockers'])
if __name__=='__main__': test(); print('ok: evidence core')
