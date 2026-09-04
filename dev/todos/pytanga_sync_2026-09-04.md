# pytanga Sync — 2026-09-04 (1.11.0 → 1.17.0)

Update the tutorials from pytanga **1.11.0** (the current `extra.tanga_version`
marker in `mkdocs.yml`) to **1.17.0**. This spans **12 changelogs**, so the work is
split into one step per changelog: each step reads exactly one changelog and records
a per-changelog analysis. A final step consolidates all analyses into the unified
update plan.

See `dev/workflows/tutorial-update.md` for the overall process.

## Changelogs to process (since 1.11.0)

| # | Version | Changelog file | Since | Scope |
|---|---------|----------------|-------|-------|
| 1 | 1.11.1 | `2026-08-30_83af75c1.md` | 1.11.0 | docs GA/viz restructure · `update_label` fix |
| 2 | 1.12.0 | `2026-08-31_3ea3a8ab.md` | 1.11.1 | viz: scene-scoped `alert`/`confirm`/`update_control` · `Visualizer.scene` · `fit_view2d` · `drag_anchor` · breaking `port`/`host`/`open_browser` |
| 3 | 1.13.0 | `2026-08-31_7848e4a2.md` | 1.12.0 | viz: scrollable panes · breaking banner `on_close` · control registry refactor |
| 4 | 1.14.0 | `2026-09-01_cada3cce.md` | 1.13.0 | viz: `on_click` handler · drag/click fixes |
| 5 | 1.14.1 | `2026-09-01_f6125a1e.md` | 1.14.0 | viz: 2D `fit_camera` pane fix · camera-fit refactor |
| 6 | 1.14.2 | `2026-09-01_2cf2de71.md` | 1.14.1 | viz: table editing · undo/redo · row deletion |
| 7 | 1.15.0 | `2026-09-01_0dcaf306.md` | 1.14.1 | viz: menus · dialogs · `GroupView` overlays · `EAnchor` · breaking control groups |
| 8 | 1.16.0 | `2026-09-01_412e5f48.md` | 1.15.0 | viz: CSS theme system · runtime switching · themed export · custom themes |
| 9 | 1.17.0-rc1 | `2026-09-02_951a9a19.md` | 1.16.0 | core: stacked merge · integer axis labels · `project_onto` · breaking `project_to`/`.labels`/`Variable.label` |
| 10 | 1.17.0-rc2 | `2026-09-02_868c81bb.md` | 1.17.0-rc1 | viz: `FileChooserDialog` · dialog sizing · breaking `FileChooserView` |
| 11 | 1.17.0-rc3 | `2026-09-02_d1203c2d.md` | 1.17.0-rc2 | viz: flow layout · `SpacerView` · control size floors |
| 12 | 1.17.0 | `2026-09-02_8ac6344a.md` | 1.17.0-rc3 | core: `DataArray` · counting-axis reduction · `RndMV` · breaking legacy bindings · `random_mv` removed |

All changelogs live under `.dep-docs/pytanga/changelog/`.

## Chapter map (for the analysis)

- **Part I — Visualization**: `tutorials/visualization/` — 21 chapters
  (`01_quick_tour` … `21_sdf_viewer`); plan: `dev/todos/tutorial/viz/tutorial_overview.md`.
- **Part II — Geometric Algebra & Core**: `tutorials/algebra/` — 17 chapters
  (`01_quick_tour` … `17_visualizing_algebra_entities`); plan:
  `dev/todos/tutorial/algebra/tutorial_overview.md`.

## Analysis questions (answer per changelog)

For each changelog, record under its `### vX.Y.Z` section:

1. **Affected chapters** — which existing viz/algebra chapters use an API that
   changed, and what must change in each.
2. **New content** — does any new feature warrant a **new** chapter/notebook, or
   should it extend an existing chapter?
3. **Breaking changes** — any breaking change that invalidates current tutorial code
   (and how to fix it).
4. **Renumbering** — would a new chapter shift the existing numbering?

## Steps

- [x] **1.** Read `.dep-docs/pytanga/changelog/2026-08-30_83af75c1.md` (v1.11.1) →
  record `### v1.11.1`.

- [x] **2.** Read `.dep-docs/pytanga/changelog/2026-08-31_3ea3a8ab.md` (v1.12.0) →
  record `### v1.12.0`.

- [x] **3.** Read `.dep-docs/pytanga/changelog/2026-08-31_7848e4a2.md` (v1.13.0) →
  record `### v1.13.0`.

- [x] **4.** Read `.dep-docs/pytanga/changelog/2026-09-01_cada3cce.md` (v1.14.0) →
  record `### v1.14.0`.

- [x] **5.** Read `.dep-docs/pytanga/changelog/2026-09-01_f6125a1e.md` (v1.14.1) →
  record `### v1.14.1`.

- [x] **6.** Read `.dep-docs/pytanga/changelog/2026-09-01_2cf2de71.md` (v1.14.2) →
  record `### v1.14.2`.

- [x] **7.** Read `.dep-docs/pytanga/changelog/2026-09-01_0dcaf306.md` (v1.15.0) →
  record `### v1.15.0`.

- [x] **8.** Read `.dep-docs/pytanga/changelog/2026-09-01_412e5f48.md` (v1.16.0) →
  record `### v1.16.0`.

- [x] **9.** Read `.dep-docs/pytanga/changelog/2026-09-02_951a9a19.md` (v1.17.0-rc1) →
  record `### v1.17.0-rc1`.

- [x] **10.** Read `.dep-docs/pytanga/changelog/2026-09-02_868c81bb.md` (v1.17.0-rc2) →
  record `### v1.17.0-rc2`.

- [x] **11.** Read `.dep-docs/pytanga/changelog/2026-09-02_d1203c2d.md` (v1.17.0-rc3) →
  record `### v1.17.0-rc3`.

- [x] **12.** Read `.dep-docs/pytanga/changelog/2026-09-02_8ac6344a.md` (v1.17.0) →
  record `### v1.17.0`.

- [x] **13. Consolidate** — merged into the "Consolidated update list" below.
  Implemented: breaking-API fixes (`01_quick_tour`, `03_jupyter`, `13_tensor`,
  `14_expression`) and new-feature sections (`12_interaction`, `14_split_views`,
  `15_visualizer_app`, `16_controls`, `17_banners_dialogs`, `15_geometry`).
  Marker set to `1.17.0`; `uv run mkdocs build --strict` passes.

## Per-changelog analyses

### v1.11.1 (`2026-08-30_83af75c1.md`)
- **Affected**: Viz 11 · Labels — `update_label` now updates labels on entity refs.
- **Breaking**: none.
- **New content**: none (upstream docs restructure only).
- **Renumbering**: none.

### v1.12.0 (`2026-08-31_3ea3a8ab.md`)
- **Affected**: Viz 06 · Multi-scene (`Visualizer.scene(name, add_axes=, add_grid=)`, scene-scoped handles); Viz 17 · Banners & dialogs (scene-scoped `alert`/`confirm`/`update_control`); Viz 10 · Coordinate system (`fit_view2d`); Viz 12 · Interaction (`drag_anchor`); Viz 03/04/15 (replace removed `port`/`host`/`open_browser`).
- **Breaking**: `Visualizer`/`VisualizerApp(port=, host=, open_browser=)` removed → use `start_server`/`show`/`run`.
- **New content**: extend existing chapters.
- **Renumbering**: none.

### v1.13.0 (`2026-08-31_7848e4a2.md`)
- **Affected**: Viz 14 · Split views (`scrollable=True`); Viz 17 · Banners & dialogs (banner `on_close` now receives the value); Viz 16 · Controls (`FileChooserView` path/`root=` fixes).
- **Breaking**: banner `on_close` receives the value, not the id.
- **New content**: extend existing.
- **Renumbering**: none.

### v1.14.0 (`2026-09-01_cada3cce.md`)
- **Affected**: Viz 12 · Interaction — `on_click` on `ActSceneObject`/`ActPoint`; ideal-point drag/click fixes.
- **Breaking**: none.
- **New content**: extend Interaction.
- **Renumbering**: none.

### v1.14.1 (`2026-09-01_f6125a1e.md`)
- **Affected**: Viz 14 · Split views / 10 · Coordinate system / 19 · Export — 2D `fit_camera` fits the pane; internal camera-fit unification.
- **Breaking**: none.
- **New content**: none (bug fix).
- **Renumbering**: none.

### v1.14.2 (`2026-09-01_2cf2de71.md`)
- **Affected**: Viz 16 · Controls — table spreadsheet editing, row deletion, undo/redo (`undo_table`/`redo_table`).
- **Breaking**: none.
- **New content**: extend Controls.
- **Renumbering**: none.

### v1.15.0 (`2026-09-01_0dcaf306.md`)
- **Affected**: Viz 16 · Controls (`EControlVariant`, `GroupView` icon/`icon_only`, `EAnchor`, unified control groups); Viz 17 · Banners & dialogs (`Dialog` overlay); Viz 15/14 (menu system, `add_menu`, `serialize_layout(overlay=...)`).
- **Breaking**: control groups are now `GroupView` overlays (legacy fixed-panel groups removed).
- **New content**: menus + dialogs — extend Controls (16) and Banners & dialogs (17).
- **Renumbering**: none (extend).

### v1.16.0 (`2026-09-01_412e5f48.md`)
- **Affected**: Viz 15 · Visualizer app (`Visualizer.theme`/`set_theme`, `list_themes`, auto-reload); Viz 19 · Export (`theme=` on exports); Viz 08 · Styles & colors (custom themes).
- **Breaking**: none.
- **New content**: CSS theme system — extend Visualizer app (15) + Styles & colors (08).
- **Renumbering**: none.

### v1.17.0-rc1 (`2026-09-02_951a9a19.md`)
- **Affected**: Algebra 14 · Expression system (stacked merge, integer `Variable` labels, constant `Expression(A)`); Algebra 13 · Tensor operations (`MVLabeledTensor.labels` → `tuple[AxisLabel, ...]`, integer axis labels); Algebra 10 · BladeMask (`project_onto`); Algebra 02 (`project_to` removed).
- **Breaking**: `MVLabeledTensor.labels` structured; `Variable.label` int; `project_to` removed → `project_onto`.
- **New content**: extend Expression (14) + Tensor (13).
- **Renumbering**: none.

### v1.17.0-rc2 (`2026-09-02_868c81bb.md`)
- **Affected**: Viz 16 · Controls (`FileChooserView` listing-only → compose with `TextFieldView`+`ButtonView`); Viz 17 · Banners & dialogs (`FileChooserDialog`, dialog `width`/`height` + resize).
- **Breaking**: `FileChooserView` no longer renders a path field/"Browse".
- **New content**: extend Controls (16) + Banners & dialogs (17).
- **Renumbering**: none.

### v1.17.0-rc3 (`2026-09-02_d1203c2d.md`)
- **Affected**: Viz 14 · Split views — flow layout (`gap`/`align`/`justify`, `Size.fr(n)`), `SpacerView`, control size floors.
- **Breaking**: none.
- **New content**: extend Split views (14).
- **Renumbering**: none.

### v1.17.0 (`2026-09-02_8ac6344a.md`)
- **Affected**: Algebra 14 · Expression system (`DataArray`, counting-axis reduction, `Expression.__call__` legacy forms removed); Algebra 15 · Geometry submodule (`RndMV`, fixed components in `RndPoint`/`RndDirection`; `pytanga.random_mv` removed); Algebra 13 · Tensor operations (`DataArray` labels).
- **Breaking**: legacy `Expression.__call__` binding forms removed; `pytanga.random_mv` removed → `pytanga.geometry.RndMV`.
- **New content**: extend Expression (14) + Geometry (15).
- **Renumbering**: none.

## Consolidated update list

### 1. Adapt existing chapters

**Part I — Visualization**

| Chapter | Change |
|---------|--------|
| 02 · Use cases / 04 · Getting started / 15 · Visualizer app | Replace removed `Visualizer(port/host/open_browser)` with `start_server`/`show`/`run` (1.12.0) |
| 06 · Multi-scene | `Visualizer.scene(name, add_axes=, add_grid=)` + scene-scoped handles (1.12.0) |
| 08 · Styles & colors | UI theme system: `register_theme`/`copy_theme`, custom themes (1.16.0) |
| 10 · Coordinate system | `fit_view2d`; `add_axes`/`add_grid` opt-out (1.12.0); 2D pane `fit_camera` (1.14.1) |
| 11 · Labels | `update_label` on entity refs (1.11.1) |
| 12 · Interaction | `on_click` + `drag_anchor` + ideal-point drag/click fixes (1.12.0, 1.14.0) |
| 14 · Split views | `scrollable=True` (1.13.0); flow layout/`Size.fr`/`SpacerView` (1.17.0-rc3); 2D pane aspect (1.14.1); overlay mounts (1.15.0) |
| 15 · Visualizer app | `VisualizerApp` flags + `run(timeout=)` (1.12.0); menus (1.15.0); themes (1.16.0) |
| 16 · Controls | `EControlVariant`/`GroupView`/unified control groups (1.15.0 breaking); table undo/redo (1.14.2); `FileChooserView` listing-only (1.17.0-rc2 breaking) |
| 17 · Banners & dialogs | `Dialog` overlay (1.15.0); `FileChooserDialog` + sizing (1.17.0-rc2); scene-scoped `alert`/`confirm` (1.12.0); banner `on_close` value (1.13.0) |
| 19 · Export | theme-aware export `theme=` (1.16.0); 2D export resize (1.14.2) |

**Part II — Geometric Algebra & Core**

| Chapter | Change |
|---------|--------|
| 02 · Algebra & multivectors | `project_to` → `project_onto` (1.17.0-rc1) |
| 10 · BladeMask | `project_onto` with `BladeMask` (1.17.0-rc1) |
| 13 · Tensor operations | `MVLabeledTensor.labels` structured; integer axis labels (1.17.0-rc1); `DataArray` (1.17.0) |
| 14 · Expression system | stacked merge, integer `Variable` labels, `Expression(A)`, `DataArray` + counting-axis reduction (1.17.0-rc1, 1.17.0); `Expression.__call__` legacy forms removed (1.17.0) |
| 15 · Geometry submodule | `RndMV` + fixed components; `pytanga.random_mv` removed (1.17.0) |

### 2. New chapters

None required — all 1.12.0–1.17.0 surface extends existing chapters. (Optional: give
"menus" a dedicated section under Viz 15/16 and "themes" under Viz 08/15 rather than
a new numbered chapter.)

### 3. Renumbering

None.

### 4. Parent overview + part plans

- Update the `dev/todos/tutorial/viz/tutorial_overview.md` abstracts for the affected
  chapters (menus, dialogs, themes, table undo/redo).
- Note: the viz plan lists 19 chapters but the nav has 21 (`02 · Use cases`,
  `03 · Jupyter notebooks` are missing from the plan) — reconcile while editing.

### 5. Validation

- Grep tutorials for removed APIs: `project_to`, `random_mv`, `Visualizer(port=`,
  `open_browser=`, `host=`.
- Confirm new API names (`project_onto`, `RndMV`, `DataArray`, `MenuView`,
  `add_menu`, `Dialog`, `show_dialog`, `FileChooserDialog`, `set_theme`,
  `register_theme`, `copy_theme`) against the installed 1.17.0 surface.
- Likely untouched: viz 01/05/07/09/13/18/20/21 and most of algebra
  01/03–09/11/12/16/17 (verify the removed-API grep returns nothing there).
