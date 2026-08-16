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