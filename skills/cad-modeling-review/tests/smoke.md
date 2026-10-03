# Smoke test: CAD review

**Prompt:** "Bu modeli teknik resme geçmeden kontrol et." (feature tree screenshot)

**Pass if** it produces classified findings and asks for what it cannot see; it does not declare the model correct.
**Fail if** it says 'looks good' without findings or questions.
