# Tutorial 1.0.0 Sync — 2026-08-22 Changelog

Driven by `.dep-docs/pytanga/changelog/2026-08-22_fae3c1e.md` ("Changes since
version 0.13.0"). Unlike the 2026-08-18 viz overhaul, this changelog mixes a small
set of **core-algebra breaking changes** with a second wave of **`pytanga.viz`
additions**. The algebra/geometry breaking changes are already applied to the
implemented notebooks; the remaining work is (a) small polish to the algebra plan
and `07_pga3`, (b) folding the new viewer features into the viz plan, and (c)
planning a new algebra chapter for the `pytanga.expression` symbolic subsystem — a
pre-existing gap introduced in 0.11.0 (not a 1.0.0 change).

The authoritative changelog deltas that matter here:

| Area | Change |
|------|--------|
| Breaking | `meet()`/`join()` **inverted** for `BasisPGA2`/`BasisPGA3`: `meet` = intersection (outer product), `join` = union (regressive product `⋆(⋆A ∧ ⋆B)`). All other algebras keep the previous semantics. |
| Breaking | `BasisPGA2`/`BasisPGA3` rename `e0_inv` → `e0_recip` (it is the reciprocal, `e0 · e0_recip = 1`). |
| Breaking | `Visualizer.animate()` **no longer opens the viewer** — `show()` is now the single display entry point. |
| New | `show()` works in Jupyter via a `jupyter` option (`None` auto-detect / `True` notebook / `False` browser tab). |
| New | Idempotent `display()` / `show()` in Jupyter (keyed by `viewer_name`, notebook cell id, or scene name). |
| New | Scene context managers — `with viz:` and `with viz.scene("name"):`. |
| New | `animate(auto_clear=True)` — per-frame flush + auto-remove of objects added after the loop began. |
| New | `viz(...)` callable shorthand for `new()` (returns a `VizObjectRef`). |
| New | `enable_server_stop_key()` (default Ctrl+Q); `viz.scene(name, enable_server_stop_key=True)`. |
| New | Operator viz reworked: `GeneralRotor` renders like `Rotor` (disc arc + torus + axis line) displaced to its origin; `Motor` renders a displaced rotation + translation arrow along the screw axis. |
| Refactor | `Motor` normalized to a **screw form** (`GeneralRotor` about a displaced axis + axial `Translator`); `analyze(motor)` returns a `GeneralRotor`. |
| New | Jupyter examples `interactive.ipynb`, `animation.ipynb`, `export.ipynb` + `demo_multi_scene.py`. |

---

## Status: already done

- `tutorials/algebra/07_pga3/07_pga3.ipynb` — `meet()`/`join()` semantics swapped
  (§6 + §10 + §11 summary), `e0_inv` → `e0_recip` (§2 + §9 + §11), re-executed.
- `tutorials/algebra/01_quick_tour/01_quick_tour.ipynb` — re-executed (the stale
  `e0_inv` blade name was only in a saved output).
- `tutorials/algebra/03_basis_classes/03_basis_classes.ipynb` — markdown + code
  `e0_inv` → `e0_recip`, re-executed.
- `dev/todos/tutorial/algebra/tutorial_overview.md` — §7 `e0_inv` → `e0_recip`.
- Confirmed no other notebook calls `join()`/`meet()` on `PGA2`/`PGA3`; `05` uses
  P3 and `06` uses N3, whose semantics are unchanged.

---

## 1. Remaining changes to the already-created tutorial files

### 1.1 `tutorials/algebra/07_pga3/07_pga3.ipynb` — §5 incidence (optional)

- The changelog now documents PGA2/3 incidence as `A.dual() ^ B.dual() == 0`.
  §5 currently teaches `point ^ plane == 0`, which is still correct (the outer
  product is unchanged) and is verified by the re-executed output.
- **Optional:** add one sentence + one line to §5 showing the equivalent dual
  form, e.g. `(P_on.dual() ^ plx.dual()).is_zero`, to match the new docs.
- Re-execute only if the source changes.

---

## 2. Remaining changes to the algebra plan

`dev/todos/tutorial/algebra/tutorial_overview.md`

### 2.1 §7 PGA 3D — round out the `join()`/`meet()` description (optional)

- The abstract currently gives only the `meet()` (intersection) examples. Add the
  `join()` (union) examples now demonstrated in the notebook:
  - "the meet of two planes is their intersection line, the meet of three planes
    their intersection point; the join of two points is the line through them, and
    the join of a line and a point is their spanning plane."
- Optionally add the incidence convention `A.dual() ^ B.dual() == 0`.

### 2.2 §14 Geometry Submodule — note the Motor screw form

- In the operator list sentence (or a short note), record that `Motor` is now
  normalized to a **screw form** — a `GeneralRotor` about a displaced axis plus an
  axial `Translator` — and that `analyze(motor)` therefore returns a
  `GeneralRotor` (not a `Motor`).

### 2.3 §16 Visualizing Algebra Entities — operator rendering

- Note that `GeneralRotor` renders like `Rotor` displaced to its origin and that
  `Motor` renders a displaced rotation plus a translation arrow along the screw
  axis (mirrors viz plan §11, below).

### 2.4 New tutorial — Expression subsystem (`pytanga.expression`)

The `pytanga.expression` package (introduced in 0.11.0, 2026-08-20) has no tutorial
chapter yet. Add one to Part I covering the symbolic layer:

- **`Variable`** — a named slot with a fixed `BladeMask` (its "type"); re-exported
  as `from pytanga import Variable`.
- **`Expression`** — a reduced product tensor (one axis per variable occurrence +
  one output axis), built by combining variables with constants/other variables via
  the geometric `*`, inner `|`, and outer `^` products.
- **`AffineExpression`** — a sum of `Expression` terms that could not be merged.

Content to cover (see `.dep-docs/pytanga/py/expression/usage.md`):

- Building: `v * a`, `v | a`, `v ^ a`, `v * w`, scalar scale, repeated `v * v`.
- Evaluation/binding: `e(V1=x)`, batched `e(V1=[x0, x1])`, nested cross-product
  batching, counting-axis labels via `(label, list)`.
- Partial evaluation → Jacobians (`e(V1=x)` leaves a tensor over the remaining vars).
- `+`/`-` term merging vs `AffineExpression`; distributing `*`, `~`, `2 * f`, `-f`.
- Involutions (`~e`, `e.conj()`), `inv(name)`, `lstsq(rhs=...)`, `svd()`, `.tensor`.
- Limits: `MAX_DEGREE` (4) repeated occurrences per term, ~12 live variables per
  process, read-only stacked partial expressions.

Prerequisites / cross-references: depends on `BladeMask` (§10) and
`MVLabeledTensor` (§13); complements the solver (§11). Recommend placing it after
§13 Tensor Operations (before Geometry) — renumber the following chapters
(Geometry, Custom Algebras, Visualizing) and update the parent overview's folder
list plus the §1 quick-tour reference. Point to the `py/examples/expression/`
scripts (`equation_demo.py`, `polynomial_demo.py`, `line_fitting_p3.py`,
`variable_rotor.py`, `solve_ax_b.py`, `variable_rotor_entity.py`).

---

## 3. Remaining changes to the visualization plan

`dev/todos/tutorial/viz/tutorial_overview.md` — fold the new viewer features into
the relevant chapters and update the one breaking change.

### 3.1 §2 Getting Started with the Viewer

- State that `show()` is the **single display entry point**; add its `jupyter`
  option (`None` auto-detect, `True` notebook inline, `False` browser tab).
- Add inline `display()` for Jupyter, and the **idempotent** `show()`/`display()`
  behavior (repeated calls in one cell flush into the already-open viewer, keyed by
  `viewer_name`, the notebook cell id, or the scene name).
- Add the `display()` hint-when-server-not-running behavior in Jupyter.
- (Optional) note the scene title also sets the browser-tab title (truncated to 40
  chars).

### 3.2 §3 Interactive Scenes and Multi-Scene Management

- Add the **scene context managers**: `with viz:` and `with viz.scene("name"):`
  (reset scene on entry, `show()` on entry, flush on exit; `Visualizer` and
  `VizSceneHandle` implement `__enter__`/`__exit__`).
- Add `enable_server_stop_key()` (default Ctrl+Q) and
  `viz.scene(name, enable_server_stop_key=True)`; note it is opt-in and disabled by
  default.

### 3.3 §4 Scene Graphs, Groups, and Transforms

- Add the **`viz(...)` callable shorthand** for `new()` — `viz(Point(1, 2, 3),
  color="...")` returns a `VizObjectRef` (equivalent to `viz.new(...)`), enabling
  the concise pre-create + update animation pattern.

### 3.4 §9 Animation

- Update for the **breaking change**: `animate()` no longer opens the viewer — call
  `show()` first (or use `with viz:`), then drive the loop with `animate()`.
- Add `animate(auto_clear=True)` (each frame flushes, then removes objects added
  after the loop began; objects added *before* the loop persist).
- (Optional) note the loop now restarts cleanly after a browser `q` stop.

### 3.5 §10 Export and Publishing

- Confirm the glTF entry point is `export_glb()` (there is no `export_gltf`); the
  current "glTF/GLB with `export_glb()`" wording is already correct.
- `SceneExporter` still exists (deprecated) for MP4/video capture — keep the
  deprecation note, and optionally align the section with the restructured library
  export docs (`html` / `gltf` / `video-image`).

### 3.6 §11 Visualizing GA Entities and Operators

- Update the operator rendering description:
  - `GeneralRotor` renders with the same rotor visualization as `Rotor` (disc arc,
    torus, axis line), displaced to its origin.
  - `Motor` renders a displaced rotation (general rotor) plus a translation arrow
    along the screw axis.

### 3.7 Optional additions

- Reference the new Jupyter examples (`interactive.ipynb`, `animation.ipynb`,
  `export.ipynb`) and the multi-scene script (`demo_multi_scene.py`) where the
  corresponding chapters are taught.

---

## 4. Parent overview

`dev/todos/tutorial/tutorial_overview.md` — **no changes** (high-level, no stale API
references).

---

## 5. Validation

- Re-execute any notebook whose source changed (only `07_pga3` if §1.1 is taken):
  `.venv/bin/jupyter nbconvert --to notebook --execute --inplace <path>`.
- Grep `tutorials/` + `dev/todos/` for `e0_inv` → zero matches; confirm `e0_recip`
  is used in `01`, `03`, `07` and the algebra plan.
- Confirm every notebook has zero `output_type: "error"` cells.
- Re-read the viz plan cross-references after edits to ensure the `#…` anchors
  still resolve (chapter numbering is unchanged this time).

---

## 6. Suggested order of work

1. Viz plan §3.4 (§9 Animation) — the only remaining *breaking* change to document.
2. Viz plan §3.1 / §3.2 / §3.3 / §3.6 — the headline new features.
3. Viz plan §3.5 / §3.7 — export review + example pointers.
4. Algebra plan §2.1–2.3 — polish (Motor screw form + operator rendering + join
   examples).
5. Algebra plan §2.4 — plan and write the new expression-subsystem chapter
   (`Variable` / `Expression` / `AffineExpression`).
6. `07_pga3` §5 incidence note (§1.1, optional).
7. Run the §5 validation pass.

