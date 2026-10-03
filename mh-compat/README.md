# MergenHan Compatibility Layer

This layer imports the useful structural patterns from the reviewed MergenHan architecture without making the mechanical library provider-dependent.

## Adopted patterns
- lifecycle: module → master → blueprint → skill → adapter
- separate maturity from structural type
- provider-agnostic core + runtime adapters
- metadata/frontmatter discipline
- catalog generation and validation
- explicit dependency graph
- localization mirror
- missing-link and metadata checks
- reusable templates and command-oriented creation flow

## Deliberately not copied
- unrelated domain prompts
- provider-specific behavior in core skills
- branding or identity-specific content
- commands that do not improve engineering/market workflows
