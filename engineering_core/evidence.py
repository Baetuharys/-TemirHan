from dataclasses import dataclass, asdict
from enum import Enum
from typing import Any, Optional

class EvidenceTag(str, Enum):
    SUPPLIED = "SUPPLIED"
    CALCULATED = "CALCULATED"
    SOURCE_BACKED = "SOURCE-BACKED"
    PRACTICE = "PRACTICE"
    ASSUMED = "ASSUMED"
    ESTIMATED = "ESTIMATED"
    UNKNOWN = "UNKNOWN"

@dataclass
class EvidenceValue:
    value: Any = None
    tag: EvidenceTag = EvidenceTag.UNKNOWN
    unit: Optional[str] = None
    source_id: Optional[str] = None
    confidence: Optional[float] = None
    note: Optional[str] = None

    def validate(self) -> list[str]:
        issues=[]
        if self.tag == EvidenceTag.SOURCE_BACKED and not self.source_id:
            issues.append("SOURCE-BACKED value requires source_id")
        if self.tag == EvidenceTag.ESTIMATED and self.confidence is None:
            issues.append("ESTIMATED value should carry confidence")
        if self.confidence is not None and not 0 <= self.confidence <= 1:
            issues.append("confidence must be in [0,1]")
        return issues

    def to_dict(self):
        d=asdict(self); d['tag']=self.tag.value; return d
