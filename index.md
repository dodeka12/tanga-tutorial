# TanGA Tutorial

Tutorials for the [TanGA](https://github.com/dodeka12/tanga) geometric algebra
library.

This book walks through the **pytanga** Python package in two parts:

- **Visualization** — teaches the `pytanga.viz` viewer from scratch, no
  geometric-algebra background required.
- **Geometric Algebra & Core** — covers the `Algebra` and `MV` types, the
  basis classes, the geometry submodule, and the numerical tooling.

## Conventions

Throughout the tutorials, algebras are created from a **basis class** (for
example `E3 = BasisE3()`) rather than the generic `Algebra(dim, sig, dtype)`
constructor. Geometric entities and operators are created through the
`pytanga.geometry` submodule — not on the basis classes — with the `Geometry`
convenience class as the recommended pattern. The OPNS/IPNS interpretation is an
**algebra property** (`algebra.opns`, default `True`).

## Running the tutorials live

Each notebook page has a power button at the top that connects to a local
Jupyter server, letting you run the cells in place. See the
[repository README](https://github.com/dodeka12/tanga-tutorial) for setup.

## Where to start

Use the navigation on the left, or begin with the
[Visualization quick tour](tutorials/visualization/01_quick_tour/01_quick_tour.ipynb).
For the underlying geometric algebra, start with the
[Algebra quick tour](tutorials/algebra/01_quick_tour/01_quick_tour.ipynb).