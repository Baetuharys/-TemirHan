def write_svg(model, path, padding=10):
    xs, ys = [], []
    for line in model.lines:
        xs += [line.p1.x, line.p2.x]
        ys += [line.p1.y, line.p2.y]
    for circle in model.circles:
        xs += [circle.center.x - circle.radius, circle.center.x + circle.radius]
        ys += [circle.center.y - circle.radius, circle.center.y + circle.radius]
    if not xs:
        xs, ys = [0, 100], [0, 100]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    width = max(maxx - minx, 1) + 2 * padding
    height = max(maxy - miny, 1) + 2 * padding
    body = []
    for line in model.lines:
        body.append(
            f'<line x1="{line.p1.x-minx+padding:.3f}" y1="{line.p1.y-miny+padding:.3f}" '
            f'x2="{line.p2.x-minx+padding:.3f}" y2="{line.p2.y-miny+padding:.3f}" stroke="black" fill="none"/>'
        )
    for circle in model.circles:
        body.append(
            f'<circle cx="{circle.center.x-minx+padding:.3f}" cy="{circle.center.y-miny+padding:.3f}" '
            f'r="{circle.radius:.3f}" stroke="black" fill="none"/>'
        )
    text = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.3f} {height:.3f}">'
        f'<!-- units: {model.units} -->' + "".join(body) + "</svg>\n"
    )
    from pathlib import Path
    Path(path).write_text(text, encoding="utf-8")
