from dataclasses import dataclass, field, asdict
from typing import Optional
from .evidence import EvidenceValue, EvidenceTag

@dataclass
class MaterialSpec:
    grade: EvidenceValue = field(default_factory=EvidenceValue)
    standard: EvidenceValue = field(default_factory=EvidenceValue)
    density_kg_m3: EvidenceValue = field(default_factory=EvidenceValue)
    finish: EvidenceValue = field(default_factory=EvidenceValue)

@dataclass
class Bend:
    angle_deg: EvidenceValue = field(default_factory=EvidenceValue)
    inside_radius_mm: EvidenceValue = field(default_factory=EvidenceValue)
    direction: EvidenceValue = field(default_factory=EvidenceValue)
    k_factor: EvidenceValue = field(default_factory=EvidenceValue)

@dataclass
class Hole:
    kind: str = "round"
    x_mm: EvidenceValue = field(default_factory=EvidenceValue)
    y_mm: EvidenceValue = field(default_factory=EvidenceValue)
    diameter_mm: EvidenceValue = field(default_factory=EvidenceValue)
    width_mm: EvidenceValue = field(default_factory=EvidenceValue)
    length_mm: EvidenceValue = field(default_factory=EvidenceValue)

@dataclass
class CostLine:
    name: str
    amount: EvidenceValue
    category: str = "other"

@dataclass
class SheetMetalPart:
    part_id: str
    revision: str = "A"
    description: str = ""
    material: MaterialSpec = field(default_factory=MaterialSpec)
    thickness_mm: EvidenceValue = field(default_factory=EvidenceValue)
    bends: list[Bend] = field(default_factory=list)
    holes: list[Hole] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    source_files: list[str] = field(default_factory=list)
    release_status: str = "DRAFT"

    def validate_release(self) -> list[str]:
        issues=[]
        if self.thickness_mm.tag == EvidenceTag.UNKNOWN or self.thickness_mm.value is None:
            issues.append("thickness is unresolved")
        if self.material.grade.tag == EvidenceTag.UNKNOWN or not self.material.grade.value:
            issues.append("material grade is unresolved")
        for i,b in enumerate(self.bends,1):
            if b.angle_deg.value is None: issues.append(f"bend {i}: angle missing")
            if b.inside_radius_mm.value is None: issues.append(f"bend {i}: inside radius missing")
            if b.k_factor.tag in (EvidenceTag.ASSUMED, EvidenceTag.ESTIMATED, EvidenceTag.UNKNOWN):
                issues.append(f"bend {i}: K-factor not production-validated")
        return issues

    def to_dict(self):
        def conv(x):
            if isinstance(x, EvidenceValue): return x.to_dict()
            if hasattr(x,'__dataclass_fields__'):
                return {k:conv(v) for k,v in asdict(x).items()}
            if isinstance(x,list): return [conv(v) for v in x]
            if isinstance(x,dict): return {k:conv(v) for k,v in x.items()}
            return x
        # asdict loses EvidenceValue types, so build explicitly
        return {
            'part_id':self.part_id,'revision':self.revision,'description':self.description,
            'material':{
                'grade':self.material.grade.to_dict(),'standard':self.material.standard.to_dict(),
                'density_kg_m3':self.material.density_kg_m3.to_dict(),'finish':self.material.finish.to_dict()},
            'thickness_mm':self.thickness_mm.to_dict(),
            'bends':[{k:getattr(b,k).to_dict() for k in ('angle_deg','inside_radius_mm','direction','k_factor')} for b in self.bends],
            'holes':[{**{'kind':h.kind}, **{k:getattr(h,k).to_dict() for k in ('x_mm','y_mm','diameter_mm','width_mm','length_mm')}} for h in self.holes],
            'notes':self.notes,'source_files':self.source_files,'release_status':self.release_status,
        }
