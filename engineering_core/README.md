# Engineering Core Data Model

This package gives ChatGPT/Claude/tools a **shared representation of engineering facts** instead of passing unstructured prose between steps.

The core rule is simple: **every important value carries provenance**. A thickness can be `SUPPLIED`; mass can be `CALCULATED`; a gasket compression can be `SOURCE-BACKED`; a photo dimension can be `ESTIMATED`; unresolved inputs remain `UNKNOWN`.

Use this model when a workflow moves between image analysis, calculations, SolidWorks automation, drawing review, costing and quotation. The model is intentionally small and serializable so it can be mirrored into JSON, tool calls or future APIs.

`release_gate()` does not certify a design. It only prevents the software from silently converting assumptions into release-quality facts.
