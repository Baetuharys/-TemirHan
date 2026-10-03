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
