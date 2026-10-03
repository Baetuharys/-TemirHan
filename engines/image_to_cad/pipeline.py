"""Image → detected primitives → inferred constraints → optional calibration → validation/export."""
from pathlib import Path
import json
from .preprocessing.image import preprocess
from .detection.primitives import detect_primitives
from .geometry.constraints import infer_constraints
from .calibration.scale import ScaleCalibration, apply_scale
from .validation.manufacturing import validate_geometry
from .export.dxf import write_r12_dxf
from .export.svg import write_svg


def process_image(image_path, *, reference=None, out_dir=None, detection=None, manufacturing_limits=None):
    image_path = Path(image_path)
    detection = detection or {}
    manufacturing_limits = manufacturing_limits or {}
    prep = preprocess(image_path, threshold=detection.get("threshold"), invert=detection.get("invert", False))
    model = detect_primitives(
        prep["edges"],
        min_line_length=detection.get("min_line_length", 30),
        max_line_gap=detection.get("max_line_gap", 8),
        hough_threshold=detection.get("hough_threshold", 35),
        detect_circles=detection.get("detect_circles", True),
    )
    model.provenance = {
        "input": str(image_path),
        "geometry_tag": "ESTIMATED",
        "warning": "Computer-vision reconstruction requires CAD review before manufacturing.",
    }
    infer_constraints(model)
    if reference:
        cal = ScaleCalibration.from_reference(
            reference["p1_px"], reference["p2_px"], reference["distance_mm"],
            source=reference.get("source", "user-reference"),
            confidence=reference.get("confidence", 1.0),
        )
        apply_scale(model, cal)
    validation = validate_geometry(model, **manufacturing_limits)
    report = {"geometry": model.to_dict(), "validation": validation, "release_status": "DRAFT-REVIEW-REQUIRED"}
    if out_dir:
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "geometry.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_svg(model, out / "geometry.svg")
        write_r12_dxf(model, out / "geometry.dxf")
    return report
