# Data Governance for AI Training and Use

## Never put into prompts, knowledge files, datasets or evals
- Customer drawings, models, DXF files or part numbers that identify a customer
- Customer or supplier names, prices, contracts, quotations, order numbers
- Personal data (names, phone, e-mail, ID numbers, IBAN)
- Credentials, API keys, internal URLs
- Proprietary standards text you are not licensed to redistribute (paraphrase and cite instead)

## Allowed
Synthetic examples you wrote; textbook formulas; public, generic engineering knowledge; your own anonymised parts with dimensions changed and identifiers removed; standards **references** (number, edition, topic).

## Before using a real case
1. Get written permission if the data is not yours.
2. Remove every identifier; change dimensions beyond recognition; remove logos and title blocks.
3. Replace names with generic roles ("müşteri", "tedarikçi").
4. Have a second person review.
5. Record provenance (`provenance: synthetic | own-anonymised | public`).

## Provider settings
Check the privacy/data-use settings of each AI product (history, training opt-out, retention) and use business/enterprise offerings when handling sensitive work. Policies change; verify at the time of use.

## Licensing
Add a LICENSE file before publishing the repository. Content derived from standards must not copy protected text.

## Review gate
`python training/scripts/validate_dataset.py` blocks obvious identifiers (e-mail, phone, IBAN) but cannot detect confidential drawings or names. Human review is mandatory for every new record.
