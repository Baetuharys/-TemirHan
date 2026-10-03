# Release v3.0.0 — 2026-10-02

## Release goal
Turn the supplied knowledge/skill repos and Image→CAD scaffold into one maintainable mechanical-engineering AI platform that is useful for daily design questions while remaining explicit about evidence and production verification.

## Merge policy
- **SV2.0.0**: base knowledge/training/provider structure.
- **Claude v2.0.0**: salvage unique deterministic calculators, detailed references, examples and CAD-review material that SV2 dropped.
- **Image-to-CAD Geometry Engine**: retain architecture intent, replace empty pipeline with an executable 2D baseline.
- **v3 additions**: source governance, common engineering data model, real retrieval, project profiles, agents/workflows, deterministic design tools, broader mechanical-design knowledge and stricter release gates.

## Internal release evidence
- Repository validator: must pass.
- Dataset validator: 47 SFT / 20 preference / 63 eval.
- Gold harness: 49/49 supplied responses, 14 eval cases skipped because no gold response is intentionally stored.
- RAG retrieval regression: pass.
- Calculator regression: pass.
- Image→CAD synthetic regression: pass.
- Provider exports rebuild successfully.

## Not claimed
This release does not claim certification, production validation of every rule, a real SolidWorks execution environment, verified Turkish labels for every command, or general 3D reconstruction from arbitrary photos.
