# Architecture — Mechanical AI Engineering v3

```text
User / CAD / drawing / image / project data
                    |
                    v
          Operating System / Intake
                    |
        +-----------+-----------+
        |                       |
        v                       v
   Skills / Agents        Deterministic Tools
        |                       |
        +-----------+-----------+
                    |
                    v
        Knowledge + RAG Retrieval
                    |
                    v
             Source Registry
                    |
                    v
          Verification / Release Gate
                    |
        +-----------+-----------+
        |                       |
        v                       v
   ChatGPT/Claude/...      Engineering outputs
```

## Source of truth
- `knowledge/`: human-readable domain knowledge.
- `sources/`: source/provenance metadata, not copyrighted standard text.
- `skills/`: task contracts and workflows.
- `engineering_core/`: shared evidence/data model and release validation.
- `tools/`: deterministic arithmetic/engineering helpers.
- `engines/`: larger executable engines such as image→CAD.
- `rag/`: local retrieval baseline over generated chunks.
- `training/`: behavior datasets, evaluation and provider-neutral prompts.
- `adapters/`: thin runtime/provider instructions.
- `dist/`: generated artifacts only; never the source of truth.

## Why this split matters
Facts change independently from behavior. A source edition may change without rewriting a skill; a better workflow may change without retraining factual knowledge. Calculations should be code when deterministic. Project/shop capability stays in `project-profiles/`, not as universal knowledge.

## Engineering trust model
`SUPPLIED → CALCULATED / SOURCE-BACKED → verified project evidence` is stronger than `PRACTICE → ASSUMED → ESTIMATED → UNKNOWN`. Release validation blocks unresolved assumptions where they affect manufacturing intent.

## Image→CAD boundary
The engine currently performs 2D preprocessing, line/circle detection, scale calibration, basic geometric constraints, JSON/SVG/DXF export and first-pass manufacturing checks. It is not a general 3D inverse-CAD solver and does not claim native `.SLDPRT` generation yet.
