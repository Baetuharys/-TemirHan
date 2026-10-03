# Topic Coverage Map — v3.0.0

Status follows `docs/maturity-model.md`; “file exists” never means “engineering complete”.

| # | Topic | Primary assets | Eval | Maturity / open condition |
|---:|---|---|---|---|
| 1 | Sheet-metal fundamentals & DFM | knowledge/01, manufacturability skill | ev-034–035 | IMPLEMENTED — shop capability profile required |
| 2 | Bending / K / flat pattern | knowledge/02, bend/flat skills, calculators | ev-001–004,045,057 | TESTED arithmetic — production bend data remains shop-specific |
| 3 | SolidWorks sheet metal | knowledge/03, SW workflow/DXF skills | ev-023–024 | IMPLEMENTED — installed version verification |
| 4 | SolidWorks Turkish UI | knowledge/04, UI-label CSV | ev-021–022 | IMPLEMENTED — real Turkish-installation verification open |
| 5 | Cabinets / enclosure architecture | knowledge/05,16,18,29 + patterns | ev-008–013,046,050,062 | IMPLEMENTED — project geometry/test required |
| 6 | IP / IK | knowledge/05,24, source registry | ev-008–013,059 | SOURCE-REVIEWED metadata — rating only by applicable test |
| 7 | Gaskets / ingress details | knowledge/24, gasket pattern/calculator | ev-059 | TESTED calculation behavior — exact supplier data required |
| 8 | Enclosure thermal | knowledge/18, airflow calculator | ev-049–050 | TESTED first-pass heat balance — real curves/pressure losses open |
| 9 | Electrical-enclosure mechanical layout | knowledge/29 | ev-062 | IMPLEMENTED — electrical safety values must come from governing authority |
| 10 | Technical drawing | knowledge/06, drawing/title-block skills | ev-014–015 | IMPLEMENTED — company/customer drawing rules required |
| 11 | GD&T / datums | knowledge/07,17,26 | ev-016–018,047–048,061 | SOURCE-REVIEWED metadata; domain review recommended |
| 12 | Tolerance stack / fits | knowledge/17, calculator | ev-047–048 | TESTED for 1-D math; statistical basis/project stack still required |
| 13 | Metrology / inspection | knowledge/26, metrology skill | ev-061 | IMPLEMENTED — gauge capability/sampling plan project-specific |
| 14 | Visual dimension estimation | knowledge/08 | ev-019–020 | TESTED abstention/scale behavior; manufacturing use requires measurement |
| 15 | Image → CAD | knowledge/20, executable engine | ev-051–052,055 | IMPLEMENTED + synthetic test; real-photo benchmark pending |
| 16 | CAD engineering / model hygiene | knowledge/09, cad-modeling-review | ev-044 | IMPLEMENTED |
| 17 | Design troubleshooting | knowledge/16, design-troubleshooter | ev-046 | IMPLEMENTED |
| 18 | Structural stiffness / load paths | knowledge/22, stiffness skill/calculator | ev-058 | IMPLEMENTED — plate/shell/FEA/physical verification as applicable |
| 19 | Joints / fasteners / hinges / hardware | knowledge/23 + knowledge/14 | ev-060 | IMPLEMENTED — manufacturer data/load case required |
| 20 | Welding / fasteners / finishing | knowledge/14 + references | ev-042–043 | IMPLEMENTED — WPS/manufacturer/process data required |
| 21 | Corrosion / coating compatibility | knowledge/25 | future domain eval | IMPLEMENTED — environment and supplier process required |
| 22 | Materials / mass | knowledge/15, mass calculator | ev-005–007,036,040 | TESTED arithmetic — certified properties need source |
| 23 | Manufacturing route / DFMA | knowledge/19, process-selection skill | ev-056 | IMPLEMENTED — supplier capability profile required |
| 24 | Supplier / RFQ handoff | knowledge/28, handoff skill | ev-063 | IMPLEMENTED |
| 25 | BOM / revision / PDM / change | knowledge/27, release workflow | release cases | IMPLEMENTED — organization PDM policy required |
| 26 | Engineering documentation | knowledge/10, templates | ev-041 | IMPLEMENTED |
| 27 | Quotation | knowledge/11, quotation skill | ev-030–031 | IMPLEMENTED — company/legal/tax terms external |
| 28 | Cost analysis | knowledge/12, cost calculator | ev-027–029 | TESTED arithmetic — current rates remain supplied inputs |
| 29 | SolidWorks macros/API | knowledge/13, macro skill | ev-025–026 | SOURCE-REVIEWED selected 2026 docs; real SolidWorks execution pending |
| 30 | Requirements / risk / release | knowledge/21, skills + agents | ev-055,057 | IMPLEMENTED |
| 31 | Engineering sanity checks | knowledge/30, tools | multi-category | IMPLEMENTED |
| 32 | Sources / provenance | sources/, verification skill | ev-053–054 | SOURCE-REVIEWED registry metadata; lifecycle re-check required |
| 33 | Project/fabricator profiles | project-profiles/ | behavior/SFT | IMPLEMENTED — user must populate real shop values |
| 34 | RAG/retrieval | training/rag + rag/ BM25 | retrieval regression | TESTED lexical baseline; semantic reranker optional |
| 35 | AI training/evaluation/adapters | training/, adapters/ | all | IMPLEMENTED — real model runs recorded separately |

## Highest-value real-world validation still needed
1. Populate a real fabricator profile: materials, machines, tooling, preferred radii, bend table, weld/finish limits and rates.
2. Capture Turkish SolidWorks screenshots/version to promote UI labels from unverified to verified.
3. Run macro regression in a controlled SolidWorks installation on copies of test parts/drawings.
4. Build an Image→CAD benchmark with real images/drawings and ground-truth CAD/error metrics.
5. Add company drawing/title-block/quotation/revision conventions.
6. Run the 63 eval cases against the target ChatGPT/Claude configuration and record results.
