from .evidence import EvidenceTag, EvidenceValue

BLOCKING_FOR_RELEASE={EvidenceTag.UNKNOWN, EvidenceTag.ASSUMED}

def release_gate(values: dict[str, EvidenceValue]) -> dict:
    blockers=[]; warnings=[]
    for name,v in values.items():
        blockers.extend(f"{name}: {x}" for x in v.validate())
        if v.tag in BLOCKING_FOR_RELEASE:
            blockers.append(f"{name}: {v.tag.value}")
        elif v.tag == EvidenceTag.ESTIMATED:
            warnings.append(f"{name}: ESTIMATED; validate before manufacturing")
        elif v.tag == EvidenceTag.PRACTICE:
            warnings.append(f"{name}: PRACTICE; verify against shop/project requirements")
    return {"pass":not blockers,"blockers":blockers,"warnings":warnings}
