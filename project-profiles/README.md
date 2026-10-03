# Project / Fabricator Profiles

The library becomes much more useful when it knows **your real shop and project constraints**. Do not repeatedly ask the AI to guess them. Copy `example-fabricator-profile.yaml`, fill only what you know, and attach it with the project.

High-value fields:
- SolidWorks version and UI language;
- preferred drawing standard and units;
- stocked materials/thicknesses;
- laser/punch limits and minimum preferred features;
- press-brake tooling, bend table/K-factor source and validated bend deductions;
- welding processes and preferred joint styles;
- PEM/fastener families actually stocked;
- finishing suppliers and process constraints;
- enclosure target, environment, gasket/lock/hinge families;
- costing rates and quotation rules;
- customer/project-specific mandatory standards.

Unknown fields stay `null`. Never populate a missing shop value from a rule of thumb and then treat it as production data.

Use one profile per shop/site when capability differs. Project-specific overrides belong in a project profile rather than changing the shared knowledge base.
