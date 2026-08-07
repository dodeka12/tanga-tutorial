#!/usr/bin/env python3
"""PGA3 visualizer example: display a plane and a line in 3D."""

from pytanga.basis import BasisPGA3
from pytanga.geometry import Direction, Line, Plane, Point, Geometry
from pytanga.viz import Visualizer


def main() -> None:
    # Create the visualizer with PGA3 (OPNS) mode enabled
    P3 = BasisPGA3()
    viz = Visualizer(opns=True, title="PGA3 — Plane & Line")
    geo = Geometry(P3)

    # Define a plane: the XY-plane (z=0) with normal pointing up (0, 0, 1)
    plane = geo.create(Plane(
        point=Point(-1, 0, 0),
        normal=Direction(1, 1, 0),
    ))
    plane.show("Plane")

    viz.add(plane, color="#4488ff", opacity=0.4, label="XY Plane")

    # Define a line passing through (1, 0, 0) pointing along the y-axis
    line = geo.create(Line(
        origin=Point(1, 0, 0),
        direction=Direction(0, 1, 0),
    ))
    line.show("line")

    viz.add(line, color="#ff4444", label="Line")

    point = plane ^ line
    point.show("point")
    viz.add(point, color="#B818B2")

    # Start the server; opens browser and blocks until Ctrl+C
    viz.run()


if __name__ == "__main__":
    main()