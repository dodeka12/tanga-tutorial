# Viz API Sync — 2026-08-18 Changelog

Driven by `.dep-docs/pytanga/changelog/2026-08-18_95486fd.md` (cumulative "since
0.9.2"). The changelog is almost entirely a **`pytanga.viz` API overhaul**; the
core algebra/geometry API (used by the two implemented tutorials) is unchanged.

This plan fixes the already-written tutorial/plan content that now references
**removed or deprecated** names, folds the **new features** into the
`dev/todos/viz/tutorial_overview.md` plan (adding a chapter where the material
is too large for an existing one), and refreshes the stale root `README.md`.

The authoritative old→new mapping (from the library's `visualizer.md`) is:

| Old | New |
|-----|-----|
| `start()` | `start_server()` + `open_browser()` (i.e. `show()`) |
| `stop()` | `stop_server()` |
| `run()` | `show()` + `wait()` |
| `display_static()` | `display_snapshot()` |
| `export_html()` | `export_snapshot()` |
| `export_figure_html()` | `export_figure(path=None)` |
| `open_figure()` | `open_snapshot()` |
| `export_animated_html()` | `export_snapshot(animation=rec)` |
| `export_animated_figure()` | `export_figure(animation=rec)` |
| `SceneExporter` | `viz` / `viz.scene(name)` |
| `default_styles` | `viz.styles.kind` (`viz.styles[Kind]`) |
| `default_label_style` / `default_label_styles` | `viz.styles.label_base` / `viz.styles.label_kind` |
| `default_annotation_style` | `viz.styles.annotation` |
| `default_act_point_style` | `viz.styles.act_point` |
| `default_tex_label_style` | `viz.styles.tex_label_kind` |
| `Axis.label_at_major` | `Axis.show_value_labels` |
| `Axis.label_format` | `Axis.value_format` |
| `Axis.label_size` | removed → `AxisStyle.value_style` (`font_size`) |

---

## 1. Fix breaking changes (plans + code)

### 1.1 `tutorials/algebra/03_basis_classes/03_basis_classes.ipynb`

The only implemented tutorial that uses the viewer. It calls the renamed
`display_static()`.

- Markdown cell ("The `pytanga.viz` viewer renders …" section): change the
  `` `display_static()` `` mention to `` `display_snapshot()` ``.
- Code cell (3D scene): `viz.display_static()` → `viz.display_snapshot()`.
- Code cell (2D scene): `viz2.display_static()` → `viz2.display_snapshot()`.
- Re-execute the notebook to regenerate the now-stale embedded HTML outputs:
  `uv run jupyter nbconvert --to notebook --execute --inplace tutorials/algebra/03_basis_classes/03_basis_classes.ipynb`

> `tutorials/algebra/02_algebra_core/02_algebra_core.ipynb` has no viz usage —
> no changes.

### 1.2 `dev/todos/algebra/tutorial_overview.md`

Replace all **6 × `SceneExporter`** references (in the quick tour and the
per-tutorial "Visual Examples" notes) with `export_snapshot()`. E.g.:

- "Export via `SceneExporter`." → "Export via `export_snapshot()`."
- "Output self-contained HTML via `SceneExporter`." → "Output self-contained HTML
  via `export_snapshot()`."

No serving/style/axis names are referenced in this part, so nothing else changes here.

### 1.3 `dev/todos/viz/tutorial_overview.md`

- **Conventions (bullet 3):** "configured once via `default_styles`" →
  "configured once via `viz.styles` defaults (per-kind `viz.styles[...]`, master
  template `viz.global_styles`)".
- **Chapter 1 quick tour — Scenes bullet:** "open the interactive Three.js viewer
  with `run()`" → "with `show()` (`show()` + `wait()` to block)".
- **Chapter 1 quick tour — Visual Examples:** "Export via `SceneExporter`" →
  "Export via `export_snapshot()`".
- **Chapter 2 (Getting Started):** rewrite the run-mode sentence —
  blocking `run()` → `show()` + `wait()`; non-blocking
  `start()`/`flush()`/`stop()` → `start_server()`/`flush()`/`stop_server()`.
- **Chapter 4 (Styles):** "the `default_styles` override mechanism, and how to set
  `default_label_style`" → "the `viz.styles` override mechanism (per-kind
  `viz.styles[...]`, `viz.global_styles`, `set_default_color()`), and how to set
  label defaults via `viz.styles.label_base` / `viz.styles.label_kind`".
- **Chapter 9 (Export):** replace `SceneExporter` with the consolidated API —
  `export_snapshot()` / `export_glb()` / `export_figure()` / `open_snapshot()` /
  `display_snapshot()`; animated export via `animation=` +
  `start_animation_recording()`; note `SceneExporter` is deprecated.

---

## 2. Incorporate new features (and add a chapter)

The new viz features are too large to squeeze into the existing chapters. They
break into one substantial new chapter plus small extensions to four existing
chapters.

### 2.1 New chapter — "Scene Graphs, Groups, and Transforms"

Insert as **new Chapter 4**, directly after "Interactive Scenes and Multi-Scene
Management" (keeps the *structure/organization* topics together before the
*appearance* chapters). Anchor: `#4-scene-graphs-groups-and-transforms`.

**Abstract (draft):**

> Organize scenes as node hierarchies. Build parent/child hierarchies with
> `VizGroup` (empty `THREE.Group` nodes) and create entities inside groups with
> `viz.new(...)` / `group.new(...)`. Use the `VizObjectRef` handle to mutate nodes
> by reference — replace `.entity`, adjust `.style` / `.color` / `.opacity`, and
> manage labels via `.label_ids` / `.labels` / `update_label()`. Cover per-object
> transforms (`translate`, `rotate`, `scale_by`, `set_transform`) and
> operator-based `transform` (`Rotor` / `Motor` / `Translator` / `Dilator`) with
> aspect-scoped `full` / `style` / `transform` updates for cheap in-place group
> animation. Introduce the `content` aspect — replacing an entity's geometry
> (same kind) mutates the three.js mesh in place, preserving transform, parent,
> style, and id mapping. Cover overlay nodes via `attach_to` (overlay follows a
> referenced scene node in the CSS plane).

**Visual Examples:** nested groups (`demo_nested_groups.py`), a two-link arm /
double pendulum built from nested groups with midpoint line labels, and a
`VizObjectRef`-driven drag/update loop (`demo_drag_point.py`,
`demo_scene_graph.py`).

> **Split option (only if this chapter gets too large):** separate "Transforms &
> Overlays" into its own chapter (12 total). Recommended for now: keep as one
> chapter; split later if the material outgrows it.

### 2.2 Extend existing chapters

- **Chapter 5 — Styles and Colors** (was 4): add the unified `VizStyles` holder
  (`viz.styles` main scene vs `viz.global_styles` master template, `viz.styles[Kind]`
  sugar, assign vs `merge`) and `CylinderLineStyle` (world-unit cylinder lines vs
  the default screen-space `Line2` fat lines).
- **Chapter 6 — Axes, Grid, and Camera** (was 5): add `AxisStyle.label_style`
  (axis *name* label) vs `AxisStyle.value_style` (numeric value labels), and
  `Axis.show_value_labels` / `Axis.value_format`.
- **Chapter 7 — Labels, Titles, and Annotations** (was 6): add per-entity label
  anchors `LabelStyle.along` (scalar / 2-/3-tuple fraction along the entity) and
  screen-plane `LabelStyle.rotation`.
- **Chapter 9 — Animation** (was 8): add the `Visualizer.animate()` frame loop
  (generator yielding once per frame, paces to `fps`, clean `stop()` on exit) as
  the recommended scripted-animation driver, alongside `animate_to` / `Timeline` /
  `PointPath` and the `content`-aspect in-place updates.

### 2.3 Renumber chapters and fix cross-references

The insertion shifts chapters 4–10 by one:

| Old | New |
|-----|-----|
| 4 Styles and Colors | 5 |
| 5 Axes, Grid, and Camera | 6 |
| 6 Labels, Titles, and Annotations | 7 |
| 7 Object Interaction and Active Objects | 8 |
| 8 Animation | 9 |
| 9 Export and Publishing | 10 |
| 10 Visualizing GA Entities and Operators | 11 |

Update every intra-document reference accordingly, including the Chapter 1 quick
tour bullets (Styles → 5, Axes/Grid/Camera → 6, Labels → 7, Interaction → 8,
Animation → 9, Export → 10, and a **new** "Scene Graphs & Transforms → 4" bullet)
and the Conventions reference to "[Chapter 10] visualizing GA entities" →
"[Chapter 11]".

---

## 3. Update `README.md`

The root README is stale (predates the new two-part tutorial layout and the
testpypi dependency). Fix:

- **Running Tutorials:** replace "open `01_e3_basics.ipynb`" with the real
  structure — `uv run jupyter notebook tutorials/`, then open
  `tutorials/algebra/…` (Part I) or `tutorials/visualization/…` (Part II); list
  the implemented notebooks (02, 03) explicitly.
- **Repository Structure:** replace the flat `tutorials/01_e3_basics.ipynb` sketch
  with the actual layout (`tutorials/algebra/`, `tutorials/visualization/`,
  `dev/todos/`, `.dep-docs/`, `.dep-examples/`, `examples/`).
- **Running Examples:** mention all three scripts
  (`examples/basic_algebra.py`, `examples/pga3_intro.py`,
  `examples/pga3_visualizer.py`).
- **"Later: Installing tanga-py from PyPI":** update to reflect the current
  `pyproject.toml` (tanga-py `0.11.0rc1` from the TestPyPI index via
  `[tool.uv.sources]`, `prerelease = "allow"`), replacing the stale
  `path = "../tanga", editable = true` guidance.
- Optionally add a short pointer to `dev/todos/` for the tutorial series plans.

---

## 4. Validation

- Re-execute `03_basis_classes.ipynb` (`uv run jupyter nbconvert --to notebook
  --execute --inplace …`) and confirm it runs clean and renders inline.
- Grep `tutorials/` + `dev/todos/` for the deprecated names and confirm zero
  remaining references: `display_static`, `SceneExporter`, `default_styles`,
  `default_label_style`, `default_annotation_style`, `open_figure`,
  `export_animated_`, the `run()` / `start()` / `stop()` serving aliases,
  `label_at_major`, `label_format`, `label_size`.
- Confirm the renumbered cross-references in `viz/tutorial_overview.md` still
  point at the right anchors (no broken `#…-…` links).

---

## 5. Suggested order of work

1. Fix `03_basis_classes.ipynb` and re-execute (smallest, unblocks validation).
2. Fix `dev/todos/algebra/tutorial_overview.md` (mechanical `SceneExporter` swap).
3. Fix `dev/todos/viz/tutorial_overview.md` breaking changes (§1.3).
4. Restructure the viz plan (§2): add Chapter 4, extend chapters, renumber.
5. Update `README.md` (§3).
6. Run the §4 validation pass.

