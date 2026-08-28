# Algebra Tutorials — Fix Plan (basis-class-first convention)

This plan corrects the `tutorials/algebra/` notebooks so they follow the series
convention: build **float64** algebras from the `BasisXX` classes, reserve the
generic `Algebra(dim, sig, dtype)` constructor for integer and custom algebras,
and never pass a generic `Algebra` into the `Geometry` submodule.

## Context

- The eight basis classes — `BasisE2`, `BasisE3`, `BasisP2`, `BasisP3`,
  `BasisN2`, `BasisN3`, `BasisPGA2`, `BasisPGA3` — are served by prebuilt
  (cached) C++ bindings for the float64 signatures `(2,0)`, `(3,0)`, `(4,0)`,
  `(4,8)`, `(5,16)`. They require **no** toolchain.
- **Integer dtypes:** the `BasisXX` classes are **not** usable with
  `dtype="int64"/"int32"` for display — their display basis constructs the
  scalar as `multivector({0: 1.0})`, and the integer backends reject the float
  (`TypeError: set(): incompatible function arguments`). Integer/modular
  algebras must use the generic `Algebra(dim, sig, dtype="int64")` constructor
  (tutorials 09, 11). Verified: `Algebra(3, 0, dtype="int64",
  modulus=101)("e1").show("x")` works, `BasisE3(dtype="int64")("e1").show("x")`
  raises.
- A generic `Algebra(dim, sig, dtype)` with a non-basis `(dim, sig)` combination
  is **compiled on first use** and requires a C++ toolchain (CMake + compiler).
  On this machine it is available via `uv run python`.
- The `Geometry` submodule only accepts the known `BasisXX` classes:
  `Geometry(Algebra(...))` constructs, but `create(...)` raises
  `ValueError: Unknown basis type: Algebra` (and `analyze(...)` returns `None`).
  Custom (generic) algebras can be used with the numerical core (`Algebra` /
  `MV` / `BladeMask` / solver / matrix / tensor / expression) but **not** with
  `Geometry` (no `create()` / `analyze()` / `Visualizer`).

## Conventions to enforce

1. Float64 algebras: use `BasisE3()` / `BasisN3()` / … as the entry point
   (tutorials 10, 12, 13, 14, 15, 17).
2. Integer/modular algebras: use `Algebra(dim, sig, dtype="int64", modulus=…)`
   (tutorials 09, 11) — the `BasisXX` classes break on integer dtypes.
3. Generic `Algebra(dim, sig, dtype)` with an arbitrary signature appears
   **only** in Tutorial 16 to show that custom algebras are possible.
4. Do not feed a generic `Algebra` into `Geometry`; keep custom-algebra
   demonstrations on the numerical core only.
5. Execute notebooks with `uv run python`.

## Progress

- [x] 09 — no change (keep `Algebra(3, 0, dtype="int64", …)`; verified)
- [x] 11 — no change (keep `Algebra(3, 0, dtype="int64")`; verified)
- [x] 15 — rewrite for full entity/operator coverage (cached basis classes)
- [x] 16 — add toolchain + Geometry warnings (keep generic `Algebra`)
- [x] 17 — rewrite for full entity/operator visualization (cached basis classes)

## Changes

### 09 — Modulus (`09_modulus/09_modulus.ipynb`)

- No change. Keep `Algebra(3, 0, dtype="int64", modulus=…)` and
  `Algebra(3, 0, dtype="int64")`. Integer algebras require the generic
  constructor because the `BasisXX` display basis is broken for integer dtypes.

### 11 — Equation Solving (`11_equation_solving/11_equation_solving.ipynb`)

- No change. Keep `Algebra(3, 0, dtype="int64")` for the `solve_mod` cell.

### 15 — Geometry (`15_geometry/15_geometry.ipynb`)

- Rewrite for the complete data model, using cached basis classes:
  - Entities: `Point`, `Direction`, `Line`, `Plane`, `Circle`, `Sphere`,
    `PointPair`, `Space` (mention `ImagCircle`/`ImagSphere`/`ImagPointPair`).
  - Operators: `ReflectionPlane`, `ReflectionLine`, `ReflectionPoint`,
    `Inversion`, `Rotor`, `Translator`, `Dilator`, `Motor`, `GeneralRotor`.
  - `Geometry` pipeline: `geo(entity)` / `geo(mv)`, plus `create` / `analyze` /
    `which_entity` / `which_operator`.
  - Typed constructors (`Point(mv)`, `Plane(mv)`, …), factories
    (`Line.from_points`, `Plane.from_corner_and_span`), typed analyzers
    (`analyze_point`, `analyze_line`, …).
  - Random generators (`RndPoint`, `RndDirection`, `Uniform`, `Normal`).
  - Standalone functions (`analyze` / `create` / `*_entity` / `*_operator`).
  - Round-trip coverage across the four 3D basis algebras (E3, P3, PGA3, N3);
    2D models shown sharing signatures.
  - Visualizer figures + `export_snapshot`.
- Re-execute with `uv run python`.

### 16 — Custom Algebras (`16_custom_algebras/16_custom_algebras.ipynb`)

- Keep the generic `Algebra` usage (this is the custom-algebra chapter).
- Add a prominent warning: non-basis `(dim, sig)` combinations compile on first
  use and require a C++ toolchain; `G(4,0)` and `G(4,8)` are precompiled,
  (P3 and N2/PGA2 signatures), while `G(5,0)` compiles.
- Add a note that generic `Algebra` cannot be used with `Geometry` (numerical
  core only).
- Re-execute.

### 17 — Visualizing Algebra Entities (`17_visualizing_algebra_entities/17_visualizing_algebra_entities.ipynb`)

- Expand to the full entity/operator set using cached basis classes:
  points/directions/lines/planes (E3, P3, PGA3), spheres/circles/point pairs
  (N3), rotors/translators/motors/reflections (E3, N3, PGA3).
- Raw-MV -> viewer analysis honoring `opns`.
- `GeneralRotor` / `Motor` rendering notes.
- Re-execute with `uv run python`.

## Execution notes

- Run with `uv run python` so cached algebras load and any custom-algebra demo
  compiles.
- Keep `MV.show()` output plain (non-ANSI) to match the existing committed
  notebooks.
- Validate: zero `output_type: "error"` cells and valid nbformat.

## Order of work

1. 09 -> 11 — done (no change; `Algebra` is required for integer dtypes).
2. 15 -> 17 (full-coverage rewrites).
3. 16 (toolchain warning + Geometry note).
4. Validate all and commit per tutorial.
