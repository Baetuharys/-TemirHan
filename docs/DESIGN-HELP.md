# Design Help — What to ask when you are stuck

You do **not** need to know the correct engineering term first. Describe the symptom, attach a screenshot/drawing/photo if available, and say what the part is supposed to do.

## Fast command palette for ChatGPT / Claude
These are conversational shortcuts, not software commands. The AI should interpret them through `skills/operating-system`.

| Command | Use it for | Example |
|---|---|---|
| `/intake` | Turn a vague problem into requirements | `/intake yeni IP hedefli elektrik kabini` |
| `/design` | Generate/compare design paths | `/design kapı çok esniyor, nasıl stiffener koymalıyım?` |
| `/review` | Review CAD/drawing/DFM | `/review bu teknik resmi üretim açısından kontrol et` |
| `/bend` | Bend/K/flat-pattern reasoning | `/bend 2 mm DC01, 90°, elimde bu bend table var...` |
| `/enclosure` | Cabinet/IP/gasket/thermal | `/enclosure kapı conta hattını kontrol et` |
| `/gdt` | Datum/tolerance/GD&T | `/gdt bu delik paterni için datum stratejisi kur` |
| `/imagecad` | Estimate/reconstruct geometry from image | `/imagecad bu resmi DXF taslağına çevirmek için ne eksik?` |
| `/solidworks` | Workflow/UI/modeling | `/solidworks bu parçayı sac metal olarak nasıl kurarım?` |
| `/macro` | Safe SolidWorks macro scaffold | `/macro tüm çizimlerden PDF export etmek istiyorum` |
| `/calc` | Deterministic calculation | `/calc 3 mm 1000x500 çelik sac ağırlığı` |
| `/cost` | Manufacturing cost breakdown | `/cost lazer+büküm+kaynak maliyetini kur` |
| `/quote` | RFQ/quotation document | `/quote bu BOM için müşteri teklifi taslağı` |
| `/source` | Verify a standard/software/source fact | `/source ISO 5459 güncel edition nedir?` |
| `/release` | Production release gate | `/release bu DXF/drawing paketi üretime hazır mı?` |

## Best minimum input
If you know them, give: purpose, material/thickness, main dimensions, quantity, environment/IP target, manufacturing route/shop, SolidWorks version/language, and what is currently failing. Missing items may remain unknown.

## What a good answer should do
1. Restate the actual design problem.
2. Separate known facts from assumptions.
3. Give 2–4 viable paths only when there is a real trade-off.
4. Explain manufacturing/assembly/service impact.
5. Use deterministic calculations where possible.
6. Say what must be measured, sourced or tested before release.
7. Finish with one concrete next action.
