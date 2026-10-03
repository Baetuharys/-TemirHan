#!/usr/bin/env python3
"""Build a compact provider knowledge pack, plus ChatGPT instructions."""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist/chatgpt-knowledge"
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)

groups = {
    "01-sheet-metal-materials.md": [
        "knowledge/01-sheet-metal-fundamentals.md", "knowledge/02-bending-and-flat-pattern.md", "knowledge/15-materials-reference.md"
    ],
    "02-solidworks.md": [
        "knowledge/03-solidworks-sheet-metal.md", "knowledge/04-solidworks-turkish-ui-and-terminology.md", "knowledge/13-solidworks-macros-api.md"
    ],
    "03-enclosures-ip-thermal-sealing.md": [
        "knowledge/05-enclosures-ip-ik.md", "knowledge/18-enclosure-thermal-management.md",
        "knowledge/24-sealing-gaskets-and-ingress-details.md", "knowledge/29-electrical-enclosure-layout-and-serviceability.md"
    ],
    "04-drawing-gdt-tolerances-quality.md": [
        "knowledge/06-technical-drawing.md", "knowledge/07-gdt-and-tolerancing.md",
        "knowledge/17-tolerance-stack-and-fits.md", "knowledge/26-metrology-inspection-and-quality-planning.md"
    ],
    "05-image-and-image-to-cad.md": [
        "knowledge/08-image-dimension-estimation.md", "knowledge/20-image-to-cad-geometry-reconstruction.md"
    ],
    "06-cad-manufacturing-dfma-finishing.md": [
        "knowledge/09-cad-engineering-practice.md", "knowledge/14-welding-fasteners-finishing.md",
        "knowledge/19-manufacturing-process-selection-and-dfma.md", "knowledge/25-corrosion-finishing-and-material-compatibility.md"
    ],
    "07-mechanical-design-stiffness-hardware.md": [
        "knowledge/16-design-troubleshooting-and-decision-support.md", "knowledge/22-structural-stiffness-and-load-paths.md",
        "knowledge/23-joints-fasteners-hinges-and-hardware.md", "knowledge/30-engineering-sanity-checks-and-calculation-discipline.md"
    ],
    "08-requirements-release-supplier-change.md": [
        "knowledge/21-requirements-risk-and-release.md", "knowledge/27-bom-revision-pdm-and-change-control.md",
        "knowledge/28-supplier-fabricator-rfq-and-handoff.md"
    ],
    "09-documentation-cost-quotation.md": [
        "knowledge/10-engineering-documentation.md", "knowledge/11-quotation-and-commercial.md", "knowledge/12-cost-analysis.md"
    ],
}
for out_name, rels in groups.items():
    parts = [f"# Compact Knowledge Bundle — {out_name}\n"]
    for rel in rels:
        p = ROOT / rel
        parts += [f"\n---\n\n## SOURCE FILE: `{rel}`\n", p.read_text(encoding="utf-8")]
    (OUT / out_name).write_text("\n".join(parts), encoding="utf-8")
for rel in [
    "reference/glossary-sacmetal.md",
    "reference/standards-map.md",
    "reference/solidworks-ui-labels.csv",
    "sources/registry.md",
]:
    p = ROOT / rel
    if p.exists(): shutil.copy(p, OUT / p.name)
(OUT / "00-INSTRUCTIONS-COPY.txt").write_text(
    (ROOT / "training/system-prompts/chatgpt-custom-gpt-instructions.md").read_text(encoding="utf-8"), encoding="utf-8"
)
print(f"Built compact ChatGPT pack: {len(list(OUT.iterdir()))} files")
