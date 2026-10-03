---
id: mai-knowledge-solidworks-turkish-ui
title: SolidWorks Turkish Interface and Terminology
category: solidworks-turkish
evidence: unverified-ui-labels
last_reviewed: 2026-10-02
verify_before_release: [every Turkish UI label against a Turkish installation]
maturity: implemented
source_ids: []
---

# SolidWorks Turkish Interface and Terminology

## 1. The honest status
The Turkish **UI labels** in this library are **not verified** against an installed Turkish SolidWorks. A made-up button name is worse than none, so the library treats labels in three confidence levels:

| Level | Meaning | How the AI writes it |
|---|---|---|
| **V** (verified) | Copied from a screenshot or text supplied by a user with the stated SolidWorks version | Use the Turkish label as shown |
| **C** (common) | Widely used core term, high confidence, still unverified for the specific version | Use it, add "(ekranda farklı görünebilir)" if the step matters |
| **U** (unverified) | Not checked | Write the English command name; put `[doğrulanmadı]` next to any Turkish guess |

Machine-readable file: `reference/solidworks-ui-labels.csv` (EN command, TR label, level, version, source, note). Anyone can fill it from screenshots.

## 2. Three layers that must never be mixed
1. **UI path** — what to click (language and version dependent).
2. **Feature / property name** — what appears in the FeatureManager tree or in custom properties (language dependent; a property created in a Turkish session keeps its Turkish name).
3. **API name** — macro/API identifiers are **always English** (`ModelDoc2`, `FeatureManager`, `CustomPropertyManager`).

## 3. Core terms with level C (confidence: common)
| English | Turkish | Level |
|---|---|---|
| Part | Parça | C |
| Assembly | Montaj | C |
| Drawing | Teknik resim | C |
| Sketch | Eskiz | C |
| Feature / FeatureManager | Özellik / Özellik Yöneticisi | C |
| Dimension | Ölçü | C |
| Configuration | Konfigürasyon | C |
| Rebuild | Yeniden oluştur | U |
| Sheet metal | Sac levha | C (trade term); menu label U |
| Flat pattern | Açınım / Düz açınım | C (trade term); feature label U |

Everything else is U until verified. Do **not** extend this table without evidence.

## 4. How the AI should answer a SolidWorks question in Turkish
1. Ask once for the **SolidWorks version** and whether the UI is Turkish.
2. Give the English command name first when the Turkish label is U: "**Edge Flange** (Kenar Flanşı olabilir — ekranda doğrula)".
3. Tell the user how to find the command without knowing the label: type the English or Turkish word in the command search box, or right-click the feature in the tree.
4. Offer a screenshot request when the label matters: "Menünün ekran görüntüsünü gönderirsen Türkçe adı kayda geçiririm."
5. Never write a menu path as if it were certain when it is U.

Example answer (U-level command):
> Sac levha parçada kenarı bükmek için **Edge Flange** komutunu kullan. Türkçe arayüzde adı sürüme göre değişebilir; komut arama kutusuna "flanş" veya "edge" yazarak bulabilirsin. Ekranda gördüğün adı yazarsan sonraki adımlarda onu kullanırım.

## 5. Capture protocol (how to verify labels quickly)
1. Open a Turkish SolidWorks; note the version (Help → About).
2. For each command: screenshot of the toolbar tooltip *and* of the PropertyManager title.
3. Fill one row in `reference/solidworks-ui-labels.csv`: `en_command, tr_label, level=V, version, source=screenshot, note`.
4. Run `python scripts/validate_reference.py` to check the CSV.
5. Re-run the evaluation set (`training/eval`) to confirm the AI uses V rows correctly.

## 6. Turkish technical writing policy (summary)
Order of preference: exact UI label → standard term → established shop term → Öztürkçe word where it is already in real use and unambiguous → coined words only as marked suggestions. Full rules: `docs/terminology-policy.md`. Glossary: `reference/glossary-sacmetal.md`.
