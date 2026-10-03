# Engineering Content Maturity Model — v3

Structural type (module/master/blueprint/skill/adapter) and engineering maturity are separate axes.

| Level | Meaning | What it does **not** mean |
|---|---|---|
| `PLANNED` | scope identified | no usable content yet |
| `DRAFT` | initial content exists | not reviewed or tested |
| `IMPLEMENTED` | usable content/tool exists with basic tests/examples | not source- or shop-validated |
| `SOURCE-REVIEWED` | release-relevant external claims traced to current official/supplier sources | not validated against a specific factory/project |
| `DOMAIN-REVIEWED` | reviewed by a competent engineer/domain owner | not proven in production |
| `TESTED` | eval/regression/tool tests pass against defined cases | not production validation |
| `PRODUCTION-VALIDATED` | used/verified on real controlled project/shop data with recorded evidence | not universal certification |

Never write “Complete” merely because a file exists. `PRODUCTION-VALIDATED` is project/process specific and may need to expire after software, tooling, supplier or standard changes.
