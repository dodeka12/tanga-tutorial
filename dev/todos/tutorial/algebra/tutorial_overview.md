# TanGA Tutorial Series — Part I: Geometric Algebra & Core

This plan covers the geometric-algebra foundation of **pytanga**: the `Algebra`
and `MV` types, the eight basis classes, the geometry submodule, the numerical
building blocks (solver, matrix, tensor, blade mask), and a closing chapter on
visualizing algebra entities with `pytanga.viz`.

It is the first of two tutorial parts. The companion plan,
[Part II — Visualization](../viz/tutorial_overview.md), teaches the viewer from
scratch (no geometric-algebra background required) and contains only a basic
introduction to visualizing GA entities, deferring the GA detail back to this
plan.

---

## Conventions (shared with Part II)

- Create algebras from a **basis class** (e.g. `E3 = BasisE3()`,
  `PGA = BasisPGA3()`) rather than the generic `Algebra(dim, sig, dtype)`
  constructor. The generic `Algebra` class is introduced in
  [Tutorial 3](#3-algebra-and-multivectors--the-core) and reserved for custom
  algebras (see [Tutorial 16](#16-custom-algebras-and-advanced-patterns)).
- **Geometric entities and operators are created through the `pytanga.geometry`
  submodule**, not on the basis classes. The recommended pattern is the
  `Geometry` convenience class, which maps between geometry and multivectors
  with a single `geo(...)` call (`geo(entity)` → `MV`, `geo(mv)` → entity):

  ```python
  from pytanga.geometry import Geometry

  geo = Geometry(BasisE3())     # binds an algebra; OPNS/IPNS read from algebra.opns
  mv = geo(entity)              # Entity/Operator → MV
  result = geo(mv)              # MV → Entity/Operator
  ```

  (`geo.create(entity)` and `geo.analyze(mv)` are the explicit equivalents of
  `geo(entity)` and `geo(mv)`.)

- The OPNS/IPNS interpretation is an **algebra property** (`algebra.opns`,
  mutable, default `True`), read automatically by creation and analysis — there
  are no per-call `opns=` overrides. The standalone `analyze()` / `create()`
  functions (and their `*_entity` / `*_operator` variants) read the same flag.

---

## 1. Algebra Quick Tour

**Format:** Jupyter notebook

**Abstract:** A rapid, example-driven tour through pytanga's geometric-algebra side
only. Glance at each major algebra area — not to master it, but to see the big picture
and know where to dive deeper. Each section ends with a reference to the tutorial that
covers the topic in full. For a tour of the viewer itself, see
[Part II](../viz/tutorial_overview.md).

Sections:

- **Algebra & Multivectors** — Create an algebra, build multivectors from strings,
  compute the geometric product, inner product and outer product, extract grades. add a tabel of all available GA operations and how to excute them in pytanga → [Tutorial 3](#3-algebra-and-multivectors--the-core)
- **Basis Classes** — Use `BasisE3` and `BasisPGA3` for named blades; glimpse the 2D
  basis classes. → [Tutorial 4](#4-the-eight-basis-classes)
- **Rotors & Motions** — Build a rotor with the geometry submodule's `Rotor` and rotate
  a vector with the sandwich product. → [Tutorial 5](#5-euclidean-3d-g30--vectors-bivectors-rotors)
- **Geometry Submodule** — Create a `Point`, `Line`, and `Sphere` with the `Geometry`
  convenience class; round-trip with `analyze()`. → [Tutorial 15](#15-geometry-submodule--algebra-independent-entities)
- **Equation Solving** — Solve `A * X = B` for an unknown multivector with `solve()`. →
  [Tutorial 12](#12-equation-solving--from-ga-to-linear-systems)

**Visual Examples:** Use `pytanga.viz.Visualizer` to render conformal-algebra
(`BasisN3`) entities — a sphere with its center and radius, a circle as a
sphere–sphere intersection, and a point pair — giving an immediate, visual sense of
what the conformal model produces. Export via `export_snapshot()`. Do not explain the
Visualizer API; reference [Part II](../viz/tutorial_overview.md).

---

## 2. Algebra and Multivectors — The Core

**Format:** Jupyter notebook

**Abstract:** Introduce the `Algebra` class and the `MV` (multivector) type. Cover
constructing an algebra from dimension, signature, and dtype; calling the algebra to
create multivectors from strings, dicts, and tuples; coefficient access and display.
Introduce the geometric, outer, and inner products; addition, scalar multiplication,
reverse, involution, and inversion. Show grade extraction, blade iteration, and
`prune()`.

---

## 3. The Eight Basis Classes

**Format:** Jupyter notebook

**Abstract:** Present the eight pre-built `Algebra` subclasses that expose named basis
blades as attributes. Four are for 3D geometry and four for 2D:

| 3D Classes | Description |
|------------|-------------|
| `BasisE3` | Euclidean 3D — G(3,0) |
| `BasisP3` | Projective 3D — G(4,0) |
| `BasisN3` | Null/Conformal 3D — G(5,0)⊕[B₁,0,0,0] |
| `BasisPGA3` | Plane-based Geometric Algebra 3D |

| 2D Classes | Description |
|------------|-------------|
| `BasisE2` | Euclidean 2D — G(2,0) |
| `BasisP2` | Projective 2D — G(3,0) |
| `BasisN2` | Null/Conformal 2D — G(4,0)⊕[B₁,0,0,0] |
| `BasisPGA2` | Plane-based Geometric Algebra 2D |

For each, show the algebra signature, the named blade attributes, and a short
geometric example. Geometric entities and operators are created through the
`pytanga.geometry` submodule (see
[Tutorial 15](#15-geometry-submodule--algebra-independent-entities)), not on the
basis classes. Compare the algebras side by side — when to use which, how their basis
elements encode different geometric meanings, and the entity/operator coverage matrix
across all eight. Include the three patterns for accessing named blades (explicit
assignment, attribute access, namespace injection).

**Note:** The 2D classes (`BasisE2`/`P2`/`N2`/`PGA2`) work with the same geometry
entity and operator types as 3D — the `z` component is simply always 0. In N2, a
"sphere" is a circle (the conformal model uses 3 points to define a sphere, which
in 2D results in a circle). E2 has no points — only directions and rotors.

**Visual Examples:** Use `pytanga.viz.Visualizer` to produce standalone HTML figures
comparing a common geometric object (e.g. a point and a line) across the four 3D
algebras, and a second figure showing the 2D counterparts with
`Visualizer(space_dim=2)`. Do not explain the Visualizer API in detail; reference
[Part II](../viz/tutorial_overview.md) for setup instructions.

---

## 4. Euclidean 3D (G(3,0)) — Vectors, Bivectors, Rotors

**Format:** Jupyter notebook

**Abstract:** Deep dive into `BasisE3`. Build vectors and bivectors from coordinates and
from the geometric product of basis vectors. Compute the outer product to form
bivectors, use the inner product for metric relationships. Construct rotors from
angle-axis pairs using the geometry submodule's `Rotor` operator (via `geo()`),
apply them with the versor/sandwich product `R * v * ~R`, compose multiple rotations,
and verify results. Cover the pseudoscalar, Hodge dual via the signed dual operator,
and the correspondence between bivectors and rotation planes.

**Visual Examples:** Use `pytanga.viz.Visualizer` to produce standalone HTML figures
illustrating key concepts — vectors and their outer-product bivector as an oriented
plane, the cross product as the Hodge dual of the outer product, and a rotor applied
to a vector with before/after comparison. Do not explain the Visualizer API in detail;
reference [Part II](../viz/tutorial_overview.md) for setup instructions.

---

## 5. Projective 3D (G(4,0)) — Homogeneous Coordinates

**Format:** Jupyter notebook

**Abstract:** Deep dive into `BasisP3`. Introduce the homogeneous (projective)
embedding where a fourth basis vector `e4` carries the origin. Show how points,
directions, lines, and planes are represented as blades. Demonstrate perspective
projection, translation via projective rotors, and the relationship between
projective and Euclidean entities. Highlight the geometry submodule's `Geometry`
class and the `analyze()`/`create()` pipeline as shortcuts for working with P3
entities. Note that translation goes through the geometry pipeline
(`geo(Translator(...))`); all P3 entities and operators are created via the
`pytanga.geometry` submodule.

**Visual Examples:** Produce standalone HTML figures via `pytanga.viz.Visualizer`
showing a P3 point, a P3 line (as a bivector), and a plane in projective space. Use
`export_snapshot()` to export self-contained HTML. Do not explain the Visualizer API;
reference [Part II](../viz/tutorial_overview.md).

---

## 6. Conformal / Null 3D (G(5,0)⊕[B₁,0,0,0]) — Spheres, Circles, Point Pairs

**Format:** Jupyter notebook

**Abstract:** Deep dive into `BasisN3`. Explain the null-vector embedding (`e0`, `e∞`),
IPNS vs OPNS representations, and how spheres, circles, point pairs, lines, and planes
emerge as blades. Build a sphere from a center and radius, extract center and radius
from a sphere. Construct circles as intersections of spheres. Show the distinction
between IPNS entities (as `analyze` output) and OPNS constructions. Introduce N3
operators: rotors, translators, dilators, and the inversion operator.

**Visual Examples:** Use `pytanga.viz.Visualizer` to produce standalone HTML figures
of a sphere, a circle (as sphere–sphere intersection), a point pair, an imaginary
circle (`ImagCircle` — dotted wireframe, dual of a real point pair), an imaginary
sphere (`ImagSphere`), and the effect of applying a dilator (scaling) and a
translator (displacement). Output self-contained HTML via `export_snapshot()`. Do not
explain the Visualizer API; reference [Part II](../viz/tutorial_overview.md).

---

## 7. PGA 3D — Plane-Based Geometric Algebra

**Format:** Jupyter notebook

**Abstract:** Deep dive into `BasisPGA3`. Explain the single-null-vector embedding used
in PGA3 (related to N3 but with a single `e0` with `e0² = 0`). Build points, lines, and
planes as blades. Construct Euclidean motions — translators, rotors, and motors — and
apply them to entities via the sandwich product. Show how PGA3 unifies rotations,
translations, and reflections in a single algebraic framework. Demonstrate the
Gunn/Dorst null embedding (`e0`, `e0_inv`) and construct entities and motions through
the `pytanga.geometry` submodule.

**Visual Examples:** Produce standalone HTML figures via `pytanga.viz.Visualizer`
showing a plane, a line (intersection of two planes), a point (intersection of three
planes), and a motor applied to a point (combined rotation + translation). Export
self-contained HTML via `export_snapshot()`. Do not explain the Visualizer API; reference
[Part II](../viz/tutorial_overview.md).

---

## 8. Duality and Complements

**Format:** Jupyter notebook

**Abstract:** Cover the three dual/conjugate operations in pytanga: the unsigned
bitwise complement (`~MV`), the signed Clifford dual (`MV.dual()`), and the left dual
(`MV.ldual()`). Explain the mathematical meaning of each, when to use each one, and
how they interact across the eight basis algebras. Include practical use cases: mapping
between IPNS and OPNS, computing the regressive product via duality, and extracting
normals/orthogonal complements.

**Visual Examples:** Use `pytanga.viz.Visualizer` to produce standalone HTML figures
illustrating the geometric meaning of duality: a bivector (oriented plane) and its
Hodge dual vector (normal direction), and the IPNS/OPNS duality of a sphere in N3.
Export self-contained HTML via `export_snapshot()`. Do not explain the Visualizer API;
reference [Part II](../viz/tutorial_overview.md).

---

## 9. Modulus Arithmetic with Integer Algebras

**Format:** Jupyter notebook

**Abstract:** Demonstrate integer-valued algebras with modular arithmetic. Create an
`Algebra` with `dtype="int64"` and a modulus, explain the `hmod` half-space modular
reduction, and show how multiple moduli can coexist on the same algebra (NTRU-style
pattern). Cover the relationship between `solve_mod` and modular GA equations, and
discuss use cases in cryptography and exact symbolic computation.

---

## 10. BladeMask — Labelling Subspaces

**Format:** Jupyter notebook / Python script

**Abstract:** Introduce `BladeMask`, the foundational type that labels matrix rows,
tensor axes, and solver dimensions. Cover construction from blade IDs, string
expressions, grade filters, `from_mv`, and `from_array`. Demonstrate O(1) membership
testing (`bid in mask`), position lookup (`index()`), blade name listing (`names()`),
and set operations (`union`, `intersection`). Explain algebra affinity — masks from
different algebras cannot be mixed. Show how to derive `product_blade_mask` and
`inverse_blade_mask` for a given product.

---

## 11. Equation Solving — From GA to Linear Systems

**Format:** Jupyter notebook

**Abstract:** Teach the `solve`, `solve_lsq`, and `solve_mod` free functions. Start
with finding the multiplicative inverse of a multivector (`A * X = 1`). Move to
solving for an unknown multivector in product equations (`A ∘ X = Y`), over-determined
systems with `solve_lsq`, and modular systems with `solve_mod`. Explain the automatic
blade mask derivation pipeline — how the solver infers the unknown's subspace from the
inputs. Cover the `EProduct` and `EInv` enums that control which GA product is used
and whether involutions are applied.

---

## 12. Matrix Operations — Multivectors Meet NumPy

**Format:** Jupyter notebook

**Abstract:** Bridge geometric algebra and linear algebra with `MVMatrix` and
`MVProductMatrix`. Create column vectors of multivector coefficients labelled by a
`BladeMask`. Build product matrices with `product_matrix()`. Convert between `MV` and
NumPy arrays via `to_matrix` and `from_matrix`. Show batched operations on multiple
multivectors stored as columns of an `MVMatrix`. Demonstrate how the product matrix
encodes any GA product as a linear map.

---

## 13. Tensor Operations — Labelled Einsum for Multivectors

**Format:** Jupyter notebook

**Abstract:** Introduce `MVTensor` (N-D tensor with `BladeMask`-labelled axes) and
`MVLabeledTensor` (label-driven arithmetic). Show slicing, factories, scalar ops, and
NumPy interop. Demonstrate label-driven contractions — the `*` operator infers Einsum
summations from shared axis labels, `+`/`-` broadcast over non-matching labels, and
arrow syntax (`"ij->ji"`) reorders axes. Build the product tensor with
`product_tensor()` and use it for bulk product computation. Show `iter_labels` for
per-element computation along a labelled axis.

---

## 14. Geometry Submodule — Algebra-Independent Entities

**Format:** Jupyter notebook

**Abstract:** Cover the complete `pytanga.geometry` data model. Introduce entity types
(`Point`, `Direction`, `Line`, `Plane`, `Circle`, `Sphere`, `PointPair`, `Space`,
`ImagCircle`, `ImagSphere`, `ImagPointPair`) and operator types (`ReflectionPlane`
(alias `Reflection`), `ReflectionLine`, `ReflectionPoint`, `Inversion`, `Rotor`,
`Translator`, `Dilator`, `Motor`, `GeneralRotor`). Show the entity/operator coverage
matrices across all eight algebras (E3, P3, PGA3, N3, E2, P2, PGA2, N2). Present the
`Geometry` convenience class as the recommended pattern — bind an algebra once (with an
optional `seed` for reproducible random generation) and call `geo(entity)` /
`geo.analyze(mv)` / `geo(obj)` without repeating the algebra on every call; the
OPNS/IPNS interpretation is read from the algebra's `opns` flag (mutable, default
`True`). Cover MV-accepting constructors (`Point(mv)`, `Plane(mv)`, …), factory
helpers (`Line.from_points`, `Plane.from_corner_and_span`), the typed analyzers
(`analyze_point`, `analyze_line`, …), and random entity generators (`RndPoint`,
`RndDirection`, `Uniform`, `Normal`). Cover the standalone `analyze()` / `create()` /
`analyze_entity()` / `analyze_operator()` / `create_entity()` / `create_operator()`
functions as a stateless alternative. Demonstrate the bidirectional pipeline:
`analyze()` extracts geometric meaning from a multivector; `create()` constructs a
multivector from a geometric description. Show round-trip examples proving consistency
across all eight algebras. Highlight algebra independence — the same `Point` object can
be created in E3, P3, N3, PGA3, or their 2D counterparts.

**Note on `HPoint`:** The homogenized point type `HPoint` (and `HDirection`) is used
internally by the visualizer and `PointPath` for trails and FIFO-capped paths. It
exposes its own analyzer/constructor (`analyze_hpoint`, `HPoint(mv)`). Its
visualization-oriented uses are the only reason it exists; it is introduced in
[Part II — Animation](../viz/tutorial_overview.md) when discussing `PointPath`.

**Visual Examples:** Use `pytanga.viz.Visualizer` to produce standalone HTML figures
of each entity type created via `geo()` and fed to the Visualizer. Show
round-trip validation: create an MV from a geometry entity, re-analyze it with
`geo.analyze()`, and verify the resulting entity matches the original — all visually
confirmed in 3D. Export self-contained HTML via `export_snapshot()`. Do not explain the
Visualizer API; reference [Part II](../viz/tutorial_overview.md).

---

## 15. Custom Algebras and Advanced Patterns

**Format:** Jupyter notebook

**Abstract:** Go beyond the eight built-in basis classes. Construct custom algebras with
arbitrary dimension and signature (up to 31 dimensions). Show how to assign names to
blades manually, create ad-hoc basis classes, and integrate custom algebras with
`BladeMask`, the solver pipeline, and the geometry submodule (where supported). Cover
sparse blade encoding, performance considerations, and the `constexpr`-friendly C++
template engine behind the scenes.

---

## 16. Visualizing Algebra Entities

**Format:** Jupyter notebook

**Abstract:** Close the part by picturing everything built so far. Feed the
`Geometry`-created entities and operators from the preceding chapters — points,
directions, lines, planes, spheres, circles, point pairs, rotors, translators, motors,
and reflections — into `pytanga.viz.Visualizer`, and show how raw multivectors are
analyzed on the way into the viewer (honoring the algebra's `opns` flag). The focus
here is on *what* each GA object looks like and how to map it to the viewer. The
viewer's general tooling — scenes, axes/grid/camera, labels, interaction, animation,
and export — lives in [Part II](../viz/tutorial_overview.md); that part also contains a
basic introduction to visualizing GA entities and operators for readers who skipped
this plan.