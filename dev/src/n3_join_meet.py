# SPDX-License-Identifier: Apache-2.0
# Copyright 2021 Christian Perwass

"""Explore ``join()`` / ``meet()`` blade operations in ``BasisN3``.

N3 (conformal 3D, G(5, 0b10000)) uses the **full 5D pseudoscalar** as its
dual, so ``join`` / ``meet`` follow the standard CGA complement
(OPNS <-> IPNS).  This script builds a representative set of N3 entities
and prints, for a curated list of pairs, the result of ``join()`` and
``meet()`` together with its grade and its ``geo.analyze()`` reading.

Run with::

    uv run python dev/src/n3_join_meet.py
"""

from pytanga.basis import BasisN3
from pytanga.geometry import (
    Circle,
    Direction,
    Geometry,
    Line,
    Plane,
    Point,
    PointPair,
    Space,
    Sphere,
)

N3 = BasisN3()
geo = Geometry(N3)  # OPNS by default (N3.opns == True)


def describe(label: str, mv) -> str:
    """Return 'grade k: analyze(mv)' for a multivector, tolerating failures."""
    grades = mv.grades if mv.grades else [0]
    try:
        result = geo.analyze(mv)
        return f"{label}: grade {grades} -> {result!r} ({type(result).__name__})"
    except Exception as exc:  # noqa: BLE001 - report rather than crash
        return f"{label}: grade {grades} -> <analyze error: {type(exc).__name__}>"


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n  {title}\n{'=' * 68}")


# ── 1. The entities (all in OPNS) ────────────────────────────────
entities = {
    "Point P (1,2,3)": Point(1, 2, 3),
    "Point Q (-1,0,2)": Point(-1, 0, 2),
    "Direction d (0,1,0)": Direction(0, 1, 0),
    "PointPair PP": PointPair(point_a=Point(-2, 0, 0), point_b=Point(2, 0, 0)),
    "Line L (x-axis)": Line(origin=Point(0, 0, 0), direction=Direction(1, 0, 0)),
    "Circle C (r=2, z=0)": Circle(center=Point(0, 0, 0), normal=Direction(0, 0, 1), radius=2.0),
    "Plane pl0 (z=0)": Plane(point=Point(0, 0, 0), normal=Direction(0, 0, 1)),
    "Plane plY (y=0)": Plane(point=Point(0, 0, 0), normal=Direction(0, 1, 0)),
    "Sphere S1 (r=2)": Sphere(center=Point(0, 0, 0), radius=2.0),
    "Sphere S2 (c=(1,0,0), r=1.5)": Sphere(center=Point(1, 0, 0), radius=1.5),
    "Space I": Space(),
}

mvs = {name: geo.create(e) for name, e in entities.items()}

hr("1. Entity grades (OPNS)")
for name, mv in mvs.items():
    print(f"  {name:34s} -> grade {mv.grades}")

# ── 2. join() / meet() between pairs ─────────────────────────────
pairs = [
    ("Point P (1,2,3)", "Point Q (-1,0,2)"),
    ("Point P (1,2,3)", "Direction d (0,1,0)"),
    ("Point P (1,2,3)", "PointPair PP"),
    ("Sphere S1 (r=2)", "Sphere S2 (c=(1,0,0), r=1.5)"),
    ("Sphere S1 (r=2)", "Plane pl0 (z=0)"),
    ("Sphere S2 (c=(1,0,0), r=1.5)", "Plane pl0 (z=0)"),
    ("Plane pl0 (z=0)", "Plane plY (y=0)"),
    ("Line L (x-axis)", "Plane pl0 (z=0)"),
    ("Line L (x-axis)", "Plane plY (y=0)"),
    ("Circle C (r=2, z=0)", "Plane plY (y=0)"),
    ("Circle C (r=2, z=0)", "Sphere S1 (r=2)"),
    ("Sphere S1 (r=2)", "Space I"),
]

hr("2. join() and meet() in OPNS (full-5D dual)")
for an, bn in pairs:
    A, B = mvs[an], mvs[bn]
    try:
        j = N3.join(A, B)
        print("  " + describe(f"join({an!r}, {bn!r})", j))
    except Exception as exc:  # noqa: BLE001
        print(f"  join({an!r}, {bn!r}) -> <error: {type(exc).__name__}: {exc}>")
    try:
        m = N3.meet(A, B)
        print("  " + describe(f"meet({an!r}, {bn!r})", m))
    except Exception as exc:  # noqa: BLE001
        print(f"  meet({an!r}, {bn!r}) -> <error: {type(exc).__name__}: {exc}>")

# ── 3. IPNS sanity check: circle = wedge of two IPNS spheres ─────
hr("3. IPNS: circle = S1_ipns ^ S2_ipns (wedge of two IPNS spheres)")
N3.opns = False
s1_ipns = geo.create(Sphere(center=Point(0, 0, 0), radius=2.0))
s2_ipns = geo.create(Sphere(center=Point(1, 0, 0), radius=1.5))
print(describe("S1 (IPNS)", s1_ipns))
print(describe("S2 (IPNS)", s2_ipns))
circle_ipns = N3.op(s1_ipns, s2_ipns)
print(describe("S1 ^ S2 (IPNS)", circle_ipns))
N3.opns = True

print("\nDone.")
