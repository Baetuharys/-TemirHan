# Mechanical AI Library v1.0 Release Contract

## Purpose
This document defines what "stable" means for the library. Stability means the repository structure, validation rules, provider-agnostic skill contract, and documented workflows are ready for reuse. It does not mean that every engineering result is automatically correct without project-specific inputs.

## Stable architecture
```text
Knowledge
   ↓
Prompt / Module / Blueprint
   ↓
Skill
   ↓
Workflow
   ↓
Adapter
   ↓
ChatGPT / Claude
```

## Skill contract
A reusable skill should:
1. identify the actual engineering requirement;
2. separate supplied facts, calculations, estimates, engineering practice, assumptions, and source-dependent claims;
3. identify missing inputs that can materially change the result;
4. avoid fabricating dimensions, material data, standards, machine capabilities, software paths, API behavior, or production parameters;
5. perform relevant verification checks;
6. return a usable result plus assumptions, uncertainty, verification items, and next action.

## Release gates
- Metadata valid.
- Dependency graph valid.
- No unresolved internal prompt IDs.
- Turkish mirrors complete for current prompt catalog.
- Core integration tests present.
- Case regression suite present.
- Adapter guidance present.
- README and changelog identify the current release.

## Engineering evidence levels
Use these labels consistently:
- **Provided fact:** explicitly supplied by the user/project/source.
- **Calculated:** derived from stated inputs and a stated relationship.
- **Source-backed:** supported by a cited standard, manufacturer document, datasheet, or other identified source.
- **Engineering practice:** a practical convention that is not being presented as a mandatory standard requirement.
- **Estimate:** approximate result with stated uncertainty.
- **Assumption:** temporary input used because a required value was not supplied.

## Final release behavior
When a downstream manufacturing decision depends on a missing input, the workflow must stop at that gate or clearly mark the assumption. It must not silently convert an assumption into a fact.
