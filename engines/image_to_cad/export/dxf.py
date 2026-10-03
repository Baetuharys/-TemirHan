def write_r12_dxf(model, path):
    """Dependency-free ASCII DXF writer for LINE/CIRCLE."""
    rows = [
        "0", "SECTION", "2", "HEADER", "9", "$INSUNITS", "70", "4" if model.units == "mm" else "0",
        "0", "ENDSEC", "0", "SECTION", "2", "ENTITIES",
    ]

    def add(*values):
        rows.extend(str(v) for v in values)

    for line in model.lines:
        add(
            "0", "LINE", "8", "GEOMETRY",
            "10", f"{line.p1.x:.6f}", "20", f"{-line.p1.y:.6f}", "30", "0",
            "11", f"{line.p2.x:.6f}", "21", f"{-line.p2.y:.6f}", "31", "0",
        )
    for circle in model.circles:
        add(
            "0", "CIRCLE", "8", "GEOMETRY",
            "10", f"{circle.center.x:.6f}", "20", f"{-circle.center.y:.6f}", "30", "0",
            "40", f"{circle.radius:.6f}",
        )
    add("0", "ENDSEC", "0", "EOF")
    from pathlib import Path
    Path(path).write_text("\n".join(rows) + "\n", encoding="ascii")
