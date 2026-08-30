# TanGA Tutorial Series — Overview

This document is the entry point to the **pytanga** tutorial series, which is split
into two independent parts. Each part has its own planning document with the full,
ordered list of tutorials.

> **Convention (both parts):** Create algebras from a **basis class**
> (e.g. `E3 = BasisE3()`, `PGA = BasisPGA3()`) rather than the generic
> `Algebra(dim, sig, dtype)` constructor. Geometric entities and operators are
> created through the `pytanga.geometry` submodule — not on the basis classes —
> with the `Geometry` convenience class as the recommended pattern. Map between
> geometry and multivectors with the single `geo(...)` call — `geo(entity)` builds
> an `MV`, `geo(mv)` re-analyzes one back into an entity. The OPNS/IPNS
> interpretation is an **algebra property** (`algebra.opns`, mutable, default
> `True`), read automatically; there are no per-call `opns=` overrides.

---

## Part I — Visualization

Teaches the `pytanga.viz` viewer from scratch — no geometric-algebra background
required. Covers scenes, SDF objects, styles, axes/grid/camera, plotting with
`CoordinateSystem`, labels, object interaction, animation, split views & layouts,
the `VisualizerApp` (with its controls, banners/dialogs, and responsive-computation
tooling), and export, using geometry dataclasses as plain 3D data. It
closes with a basic chapter on visualizing GA entities and operators (deferring the
GA detail to Part II) and a short chapter on the experimental `SdfVisualizer`.

**Plan:** [dev/todos/viz/tutorial_overview.md](viz/tutorial_overview.md)

---

## Part II — Geometric Algebra & Core

Covers the algebra and multivector foundations, the eight basis classes, the
geometry submodule, and the numerical tooling (solver, matrix, tensor, blade mask),
plus an introduction to **visualizing** algebra entities and operators with
`pytanga.viz`.

**Plan:** [dev/todos/algebra/tutorial_overview.md](algebra/tutorial_overview.md)

---

## Tutorials Folder Layout

The tutorial notebooks live under `tutorials/`, organized into two main subfolders
that mirror the two parts of this series. Each subfolder numbers its tutorials
independently, starting at `01`.

```
tutorials/
├── README.md
├── algebra/             # Part II — Geometric Algebra & Core
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
│   ├── 14_expression/
│   ├── 15_geometry/
│   ├── 16_custom_algebras/
│   └── 17_visualizing_algebra_entities/
└── visualization/       # Part I — Visualization
    ├── README.md
    ├── 01_quick_tour/
    ├── 02_getting_started/
    ├── 03_sdf_objects/
    ├── 04_multi_scene/
    ├── 05_scene_graphs/
    ├── 06_styles_colors/
    ├── 07_axes_grid_camera/
    ├── 08_coordinate_system/
    ├── 09_labels/
    ├── 10_interaction/
    ├── 11_animation/
    ├── 12_split_views/
    ├── 13_visualizer_app/
    ├── 14_controls/
    ├── 15_banners_dialogs/
    ├── 16_responsive_computation/
    ├── 17_export/
    ├── 18_ga_entities/
    └── 19_sdf_viewer/
```

- **`algebra/`** — Part II tutorials: the algebra quick tour, installation, the
  algebra/multivector core, the basis classes, the 3D deep dives (E3, P3, N3,
  PGA3), duality, modulus arithmetic, the numerical tooling (BladeMask, solver,
  matrix, tensor), the expression system, the geometry submodule, custom
  algebras, and a closing chapter on visualizing algebra entities.
- **`visualization/`** — Part I tutorials: the viewer quick tour, getting started,
  SDF objects in the standard viewer, multi-scene management, scene graphs, styles,
  axes/grid/camera, the `CoordinateSystem` plotting helper, labels, object
  interaction, animation, split views & layouts, and the `VisualizerApp` (plus its
  detail chapters: controls & the file chooser, banners/dialogs, and responsive
  computation), closed by export, a basic chapter on visualizing GA
  entities/operators, and a short chapter on the experimental `SdfVisualizer`.

> Each subfolder numbers its tutorials from `01` and opens with its own quick tour —
> `algebra/01_quick_tour` (the algebra) and `visualization/01_quick_tour` (the viewer).
> `algebra/` runs from `01` through `17_visualizing_algebra_entities`.
> `visualization/` restarts at `01` and runs through `19_sdf_viewer`. Each folder
> also carries a `README.md`
> (`tutorials/README.md`, `tutorials/algebra/README.md`,
> `tutorials/visualization/README.md`).