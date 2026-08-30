# Inline Visualizations — Implementation Plan

> **Status:** plan only — not yet implemented.

## Goal

Every scene that a tutorial intends to show must be embedded **inline** via
`display_snapshot()`, so it renders directly in the built HTML docs. mkdocs-jupyter
renders a notebook's `text/html` output verbatim, so `display_snapshot()`'s
`<iframe src="data:text/html;base64,…">` shows up in the published site.

Standalone HTML files written by `export_snapshot(path)` are **build artifacts** and
must never be the *only* way a scene is surfaced — `_output/` is gitignored and the
docs do not link to it.

## Background

- `display_snapshot()` → inline `<iframe>` in the cell's `text/html` output (what the
  docs show).
- `export_snapshot(path)` → writes a standalone HTML file (not shown in docs).
- The book is built with `execute: false` (mkdocs-jupyter), so **saved notebook
  outputs** are what get rendered. After editing a notebook, it must be **run** so the
  new iframe output is saved into the `.ipynb`.

## Audit (`display_snapshot` / `export_snapshot` counts per notebook)

### Visualization

| Notebook | display | export | action |
|---|---|---|---|
| 01_quick_tour | 11 | 3 | add intro scene (below) |
| 02_use_cases | 2 | 3 | ok |
| 03_jupyter | 8 | 2 | ok |
| 04_getting_started | 2 | 3 | ok |
| 05_sdf_objects | 6 | 2 | ok |
| 06_multi_scene | 0 | 3 | **add display** |
| 07_scene_graphs | 5 | 1 | ok |
| 08_styles_colors | 5 | 2 | ok |
| 09_axes_grid_camera | 3 | 8 | ok |
| 10_coordinate_system | 7 | 3 | ok |
| 11_labels | 9 | 2 | ok |
| 12_interaction | 4 | 2 | ok |
| 13_animation | 4 | 3 | ok |
| 14_split_views | 0 | 0 | **add display** |
| 15_visualizer_app | 0 | 0 | **add display** |
| 16_controls | 0 | 0 | **add display** |
| 17_banners_dialogs | 0 | 0 | **add display** |
| 18_responsive_computation | 0 | 0 | **add display** |
| 19_export | 4 | 10 | ok (export is the topic) |
| 20_ga_entities | 4 | 2 | ok |
| 21_sdf_viewer | 0 | 0 | **add display** |

### Geometric Algebra

| Notebook | display | export | action |
|---|---|---|---|
| 01_quick_tour | 2 | 0 | ok |
| 02_algebra_core | 0 | 0 | consider |
| 03_basis_classes | 3 | 0 | ok |
| 04_euclidean_e3 | 3 | 0 | ok |
| 05_projective_p3 | 2 | 1 | ok |
| 06_conformal_n3 | 2 | 2 | ok |
| 07_pga3 | 2 | 2 | ok |
| 08_duality | 2 | 2 | ok |
| 09_modulus | 0 | 0 | consider |
| 10_blade_mask | 0 | 0 | consider |
| 11_equation_solving | 0 | 0 | consider |
| 12_matrix | 0 | 0 | consider |
| 13_tensor | 0 | 0 | consider |
| 14_expression | 0 | 0 | consider |
| 15_geometry | 0 | 1 | **add display** |
| 16_custom_algebras | 0 | 0 | consider |
| 17_visualizing_algebra_entities | 0 | 8 | **add display (primary issue)** |

## Tasks

### 1. Intro scene for the Visualization quick tour

Add a simple, attractive opening scene to
`tutorials/visualization/01_quick_tour/01_quick_tour.ipynb` (first code cell):

- Two intersecting spheres.
- Texture labels on them showing a math formula (KaTeX), e.g. `r² = x² + y² + z²`.

Use `display_snapshot()` so it renders inline at the top of the page.

### 2. Convert export-only scenes to inline

For each notebook where scenes are currently only `export_snapshot()`-ed, add a
matching `display_snapshot()` call so the scene is visible inline:

- `tutorials/algebra/17_visualizing_algebra_entities/17_visualizing_algebra_entities.ipynb`
  (8 exports, 0 displays — the whole point of the tutorial is to show entities).
- `tutorials/algebra/15_geometry/15_geometry.ipynb` (1 export).
- `tutorials/visualization/06_multi_scene/06_multi_scene.ipynb` (3 exports).

### 3. Add inline scenes where a tutorial currently shows nothing

Review and add `display_snapshot()` examples where they add value:

- Visualization: `14_split_views`, `15_visualizer_app`, `16_controls`,
  `17_banners_dialogs`, `18_responsive_computation`, `21_sdf_viewer`.
- Algebra (only where a visual helps — many of these are numeric/API and may not need
  a viewer): `02_algebra_core`, `09_modulus`, `10_blade_mask`, `11_equation_solving`,
  `12_matrix`, `13_tensor`, `14_expression`, `16_custom_algebras`.

### 4. Re-execute edited notebooks

After editing, run each changed notebook (Jupyter with `pytanga` installed) so the
`display_snapshot()` iframe output is saved into the `.ipynb`. mkdocs renders saved
outputs (`execute: false`); it does not run the notebooks.

### 5. Rebuild and verify

```bash
uv run mkdocs build --strict
```

Then confirm `<iframe src="data:text/html;base64,…">` is present in the relevant
pages under `site/` (grep for `<iframe` in the changed tutorial pages).

## Validation checklist

- [ ] No tutorial relies on `export_snapshot()` alone for a scene that should be shown.
- [ ] `01_quick_tour` opens with the two-spheres intro scene.
- [ ] `17_visualizing_algebra_entities` shows entities inline.
- [ ] `mkdocs build --strict` succeeds with no `_hooks`/`README` warnings.
- [ ] Inline iframes render in `site/**/index.html`.
