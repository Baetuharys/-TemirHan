# Case: Sheet-Metal Cost → Quotation

## Scenario
A customer requests a quotation for a sheet-metal part/assembly. The engineering data includes material, laser cutting, marking, bending, welding, assembly, and finishing, but some rates are unknown.

## Required skill chain
`cost-analysis` → `quotation-generator` → `technical-document-generator`

## Required behavior
- Separate physical quantities from commercial rates.
- Identify missing machine/hour, labor, finishing, and overhead inputs.
- Keep customer-facing assumptions and exclusions explicit.
- Avoid turning an engineering estimate into a falsely exact price.
