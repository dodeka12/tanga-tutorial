# TanGA Tutorial Series — Overview

This document is the entry point to the **pytanga** tutorial series, which is split
into two independent parts. Each part has its own planning document with the full,
ordered list of tutorials.

> **Convention (both parts):** Create algebras from a **basis class**
> (e.g. `E3 = BasisE3()`, `PGA = BasisPGA3()`) rather than the generic
> `Algebra(dim, sig, dtype)` constructor. Geometric entities and operators are
> created through the `pytanga.geometry` submodule — not on the basis classes —
> with the `Geometry` convenience class as the recommended pattern. The OPNS/IPNS
> interpretation is an **algebra property** (`algebra.opns`, mutable, default
> `True`), read automatically; there are no per-call `opns=` overrides.

---

## Part I — Geometric Algebra & Core

Covers the algebra and multivector foundations, the eight basis classes, the
geometry submodule, and the numerical tooling (solver, matrix, tensor, blade mask),
plus an introduction to **visualizing** algebra entities and operators with
`pytanga.viz`.

**Plan:** [dev/todos/algebra/tutorial_overview.md](algebra/tutorial_overview.md)

---

## Part II — Visualization

Teaches the `pytanga.viz` viewer from scratch — no geometric-algebra background
required. Covers scenes, styles, axes/grid/camera, labels, object interaction,
animation, and export, using geometry dataclasses as plain 3D data. It ends with a
single, basic chapter on visualizing GA entities and operators that defers the GA
detail to Part I.

**Plan:** [dev/todos/viz/tutorial_overview.md](viz/tutorial_overview.md)

---

## Tutorials Folder Layout

The tutorial notebooks live under `tutorials/`, organized into two main subfolders
that mirror the two parts of this series. Each subfolder numbers its tutorials
independently, starting at `01`.

```
tutorials/
├── README.md
├── algebra/             # Part I — Geometric Algebra & Core
│   ├── README.md
│   ├── 01_quick_tour/
│   ├── 02_algebra_core/
│   ├── 03_basis_classes/
│   ├── 04_euclidean_e3/
│   ├── 05_projective_p3/
│   ├── 06_conformal_n3/
│   ├── 07_pga3/
│   ├── 08_duality/
│   ├── 09_modulus/
│   ├── 10_blade_mask/
│   ├── 11_equation_solving/
│   ├── 12_matrix/
│   ├── 13_tensor/
│   ├── 14_geometry/
│   └── 15_custom_algebras/
└── visualization/       # Part II — Visualization
    ├── README.md
    ├── 01_quick_tour/
    ├── 02_viz_scenes/
    ├── 03_viz_labels/
    ├── 04_viz_animation/
    ├── 05_viz_export/
    └── 06_end_to_end/
```

- **`algebra/`** — Part I tutorials: the algebra quick tour, installation, the
  algebra/multivector core, the basis classes, the 3D deep dives (E3, P3, N3,
  PGA3), duality, modulus arithmetic, the numerical tooling (BladeMask, solver,
  matrix, tensor), the geometry submodule, and custom algebras.
- **`visualization/`** — Part II tutorials: a viewer quick tour, scenes, labels,
  animation, and export, closed by `06_end_to_end` — a cross-cutting capstone that ties
  algebra, geometry, solving, and visualization together.

> Each subfolder numbers its tutorials from `01` and opens with its own quick tour —
> `algebra/01_quick_tour` (the algebra) and `visualization/01_quick_tour` (the viewer).
> `algebra/` keeps its original numbers (`01`–`15`, plus `21_custom_algebras`, the
> "Custom Algebras" chapter that still carries its old flat-layout number).
> `visualization/` restarts at `01`; its old flat-layout numbers `16`–`20` become
> `02`–`06` after the new `01_quick_tour`. Each folder also carries a `README.md`
> (`tutorials/README.md`, `tutorials/algebra/README.md`,
> `tutorials/visualization/README.md`).