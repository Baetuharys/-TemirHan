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
