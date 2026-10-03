# Compact Knowledge Bundle — 09-documentation-cost-quotation.md


---

## SOURCE FILE: `knowledge/10-engineering-documentation.md`

---
id: mai-knowledge-engineering-documentation
title: Technical and Engineering Documentation (Teknik Doküman Üretimi)
category: documentation
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [company document templates, customer document requirements]
maturity: implemented
source_ids: []
---

# Technical and Engineering Documentation (Teknik Doküman Üretimi)

## 1. Principles
1. **One purpose per document.** A reader should know in the first lines what the document is for and what to do with it.
2. **Facts, calculations, assumptions and open items are separated** (see the evidence labels below).
3. **Traceable**: document number, revision, date, author, approval, referenced drawings/standards with edition.
4. **Reproducible**: another engineer can repeat the calculation from the stated inputs.
5. **No invented data.** Missing information appears as an explicit "OPEN ITEM", never as a plausible number.

Evidence labels used everywhere in this library: `[FACT-SUPPLIED]`, `[CALCULATED]`, `[SOURCE-BACKED]`, `[PRACTICE]` (engineering practice), `[ESTIMATE]`, `[ASSUMPTION]`, `[OPEN]`.

## 2. Document types and minimum content
| Document | Purpose | Minimum sections |
|---|---|---|
| Design description (tasarım tanımı) | Explain a design for review | Scope, requirements, concept, key calculations, risks, open items |
| Technical specification (teknik şartname) | Define requirements for a supplier | Scope, normative references, requirements (shall/should), acceptance, deliverables |
| Datasheet (teknik veri föyü) | Product facts | Identification, dimensions, materials, ratings, environment, weight, standards |
| Work instruction (iş talimatı) | Perform a task consistently | Purpose, scope, tools/PPE, steps (numbered), checks, records |
| Inspection plan / report (muayene) | Prove conformity | Item, requirement, method, instrument, result, accept/reject, signature |
| Assembly instruction (montaj talimatı) | Build a product | Parts list, torque values, sequence, drawings |
| Test procedure / report (deney) | Verify a requirement | Objective, setup, pass criteria, steps, results, deviations |
| FAT/SAT (fabrika/saha kabul testi) | Customer acceptance | Test list, criteria, witnesses, punch list |
| User/maintenance manual | Safe use and service | Safety, transport, installation, operation, maintenance, spare parts |
| Calculation note (hesap föyü) | Support a decision | Inputs, method, formulas, results, checks, conclusion |
| BOM / cut list | What to buy/cut | Item, description, material, quantity, revision |
| Quotation technical annex | Scope of supply | Included, excluded, assumptions, drawings, delivery |

## 3. Requirement language
`shall` = mandatory; `should` = recommended; `may` = permitted. Each requirement has an identifier and is verifiable (a test, inspection or document check). "Fast", "robust", "sufficient" are not requirements.

## 4. Writing style for Turkish engineering documents
- Short sentences; one instruction per step; imperative mood in procedures ("Parçayı sabitleyin.").
- Use the established term the reader knows; give the English term once in brackets when it helps.
- Consistent units (mm, kg, N·m); numbers with units; decimal comma or point consistent in the whole document (Turkish documents normally use a decimal comma; **state the convention when the document goes abroad**).
- Do not use vague words ("yaklaşık", "uygun") without a value or range.
- Tables for parameters; numbered steps for procedures; diagrams referenced by number.

## 5. Standard document skeleton
```text
Title · Document no. · Revision · Date · Author / Reviewer / Approver
1 Purpose and scope
2 Definitions and references (with edition)
3 Inputs and assumptions
4 Method / description
5 Results
6 Verification and checks
7 Open items and risks
8 Revision history
```

## 6. Calculation notes
Show the governing formula, the symbols, the units, the input values with source, the result with the number of significant digits that the inputs justify, and the check (order of magnitude, alternative method). Example format:

> **Weight of plate** `m = L·W·T·ρ = 1.0 × 2.0 × 0.003 m³ × 7850 kg/m³ = 47.1 kg` [CALCULATED] — density from the material certificate/standard [SOURCE-BACKED]; cutting, hardware and coating not included [ASSUMPTION].

## 7. Review checklist
Numbers consistent between text, tables and drawings · units · references with edition · revision history · all open items listed · no confidential data of other customers · spelling of part numbers · pagination and document number on every page.

## 8. AI behaviour for document generation
1. Ask for audience, purpose, language, and template if the document is formal.
2. Produce a **skeleton first** for long documents; confirm, then fill.
3. Insert `[OPEN]` for any missing mandatory data.
4. Never fabricate standard clauses, test results, signatures, certificate numbers or customer names.
5. For Word/PDF output: follow the file-creation procedures of the runtime; keep the content source in Markdown so that revisions are diffable.


---

## SOURCE FILE: `knowledge/11-quotation-and-commercial.md`

---
id: mai-knowledge-quotation-commercial
title: Quotation and Commercial Documents (Teklif Dokümanı)
category: commercial
evidence: business-practice
last_reviewed: 2026-10-02
verify_before_release: [current tax rates, current Incoterms edition, company terms, legal review for contracts]
maturity: implemented
source_ids: []
---

# Quotation and Commercial Documents (Teklif Dokümanı)

> This file is practical guidance, not legal or tax advice. Tax rates, legal terms and contract wording must be checked with the company's finance/legal staff.

## 1. What a good quotation does
It makes the buyer's decision easy and protects the seller from misunderstanding: what is included, what is not, at what price, until when, under which conditions.

## 2. Structure
1. Header: company, quotation number, date, validity period, revision, contact person.
2. Customer details and reference (RFQ number, drawing numbers, revisions).
3. **Scope of supply** — per item: description, drawing/part number + revision, material and thickness, finish, quantity.
4. **Price table** — unit price, quantity, line total, currency, price basis (per piece / per lot), tooling or one-off costs listed separately.
5. **Assumptions and exclusions** — e.g. "material price valid for order within X days", "tolerances per ISO 2768-m", "finish colour RAL ...", "no testing included", "transport excluded".
6. **Commercial terms** — delivery time (from order/from drawing approval/from material receipt), Incoterms 2020 term and named place, payment terms, validity, tax treatment, warranty, packaging, minimum order quantity.
7. **Technical annex** — drawings, flat patterns, tolerances, inspection and certificates (3.1 etc.) if requested.
8. Revision history and approval.

## 3. Pricing logic (see `12-cost-analysis.md`)
Quote price = **cost** + **margin** (state which: *markup on cost* or *margin on price* — they are different: a 20 % markup is a 16.7 % margin). Consider quantity breaks (setup amortisation), material volatility (price validity window or surcharge clause), and risk items (new process, tight tolerance).

## 4. Incoterms 2020 (short)
EXW (ex works), FCA (free carrier), CPT, CIP, DAP (delivered at place), DPU, DDP (delivered duty paid) for any mode; FAS, FOB, CFR, CIF for sea/inland waterway only. State the term **with a named place**, e.g. "DAP Istanbul". Confirm the current edition.

## 5. Tax and currency notes (Türkiye)
- VAT (KDV) rate and exemptions depend on the product, customer and current law; **check the current rate before issuing**. Write prices "KDV hariç" (excl. VAT) unless the company policy says otherwise.
- Currency: state it; for long validity add an exchange-rate clause (rate at invoice date or a fixed rate up to a date).
- Export: tax treatment differs; check with finance.

## 6. Typical commercial clauses (examples, not legal text)
- Validity: "Bu teklif düzenleme tarihinden itibaren 15 gün geçerlidir." (set according to material volatility)
- Payment: advance %, balance on delivery, or net X days.
- Changes: drawings changes after order → price and lead-time review.
- Tolerance of quantity: ±x % for coated or nested production if agreed.
- Intellectual property: customer drawings remain customer property.

## 7. Risk and clarification list before quoting
Missing drawing revision · conflicting material/thickness · unclear finish spec · tolerances tighter than process capability · unspecified annual volume · inspection and certificate requirements · packaging and logistics · penalty clauses. Convert them to **questions to the customer**, not silent assumptions.

## 8. Email cover template (Turkish)
> Konu: Teklif No TKL-XXXX – [Parça/Proje adı]
> Merhaba [Ad Soyad],
> [RFQ/Resim no]'ya istinaden teklifimizi ekte sunuyoruz. Teklif; [kapsam özeti] kalemlerini, [teslim süresi] teslim süresini ve [geçerlilik] geçerlilik süresini içermektedir. Varsayımlar ve hariç tutulan kalemler teklifin 5. bölümünde belirtilmiştir. Çizim revizyonu [Rev X] baz alınmıştır.
> Sorularınız için bana ulaşabilirsiniz.
> Saygılarımla,

## 9. AI behaviour
1. Ask for: items, quantities, drawings, material, finish, delivery, payment, validity, currency.
2. Pull prices only from supplied data or a stated cost model; mark rates as **illustrative** if they are not supplied.
3. Never invent customer names, prior orders, certifications or legal clauses.
4. Provide the quotation as a structured table first, then the narrative text.
5. List **assumptions and exclusions** every time.


---

## SOURCE FILE: `knowledge/12-cost-analysis.md`

---
id: mai-knowledge-cost-analysis
title: Sheet-Metal Cost Analysis (Maliyet Analizi)
category: cost
evidence: calculation
last_reviewed: 2026-10-02
verify_before_release: [material prices, machine hour rates, shop overhead, subcontractor quotes]
maturity: implemented
source_ids: []
---

# Sheet-Metal Cost Analysis (Maliyet Analizi)

## 1. Cost model
```text
Part cost = Material + Cutting + Forming (bending) + Joining + Finishing + Hardware
          + Setup/Tooling (amortised) + Inspection + Packaging + Logistics
          + Overhead (genel gider) + Risk allowance
Price     = Cost + Margin
```
All rates in this file are **illustrative, not market data**. Replace them with the shop's numbers.

## 2. Components and drivers
| Component | Formula / driver |
|---|---|
| Material | `mass / nesting yield × price per kg`; mass = `L·W·T·ρ` of the **blank**, not the finished part |
| Nesting yield | usable-sheet utilisation; small parts in big sheets 70–85 %, depends on nesting and remnants |
| Laser cutting | `(cut length / cutting speed + pierces × pierce time) × machine rate`; speed falls with thickness |
| Punching | hits × time per hit × machine rate (+ tool cost if new tools) |
| Bending | `setup / batch + bends × handling time × press brake rate`; setup depends on tooling changes |
| Welding | length or number of tacks × time × rate; grinding after welding |
| Hardware (PEM, nuts, glands, gaskets) | purchase price × quantity + insertion time |
| Finishing | powder coat: area × price per m² (+ masking); galvanizing/anodizing: per kg or per m²; minimum lot charges |
| Inspection | frequency, first-article, certificate requirements |
| Packaging/logistics | per part or per pallet |
| Overhead | percent of direct cost or hourly burden |
| Risk | allowance for new process, tight tolerance, scrap risk |

## 3. Worked example (illustrative rates)
Part: flat blank 300 × 200 mm, 2 mm DC01, 4 holes ⌀10, 2 bends, powder coat, batch 50.
| Item | Calculation | Value |
|---|---|---|
| Mass of blank | 0.300 × 0.200 × 0.002 × 7850 | 0.942 kg |
| Material | 0.942 / 0.75 yield × 40 per kg | 50.24 |
| Cut length | 2×(300+200) + 4×π×10 | 1125.7 mm |
| Laser | (1125.7/2000 + 5 pierces × 0.5 s) × 30 per min | 18.13 |
| Bend setup | 30 min × 24 per min / 50 | 14.40 |
| Bend handling | 2 bends × 0.3 min × 24 | 14.40 |
| Powder coat | 0.12 m² (both faces) × 150 per m² | 18.00 |
| Packaging | — | 3.00 |
| **Direct cost** | | **118.17** |
| Overhead 12 % | | 14.18 |
| **Cost** | | **132.36** |
| Price with 20 % **markup on cost** | cost × 1.20 | 158.83 (margin on price 16.7 %) |
| Price for 20 % **margin on price** | cost / 0.80 (rounded cost 132.36) | 165.45 |

Batch sensitivity of the same part (same rates): batch 10 → cost 196.87; batch 50 → 132.36; batch 200 → 120.26. Setup amortisation is the largest lever on small batches.

## 4. Quick cost-reduction levers (design for manufacturing)
Fewer bends and fewer different bend radii/tools · allow a standard thickness and grade · avoid features that need new tools · nest-friendly shapes (common-line cutting) · loosen tolerances that do not matter · avoid secondary operations (tapping, deburr by hand) · combine parts when function allows · minimise painted area/ masking · standard fasteners.

## 5. Margin vs markup
`markup = (price − cost)/cost`, `margin = (price − cost)/price`. Always label which one the user means.

## 6. Sensitivity and uncertainty
Report ranges: material ± price change, yield ± 5 points, machine time ± 10–20 %. Show the **top 3 drivers**. If a rate is guessed, mark it `[ASSUMPTION]` and list it among the open items.

## 7. Output template
1. Inputs and assumptions table. 2. Cost breakdown table. 3. Unit price and lot price at quantity breaks. 4. Sensitivity (top drivers). 5. Open items (needed rates/prices). 6. Statement: illustrative if rates are not supplied.
