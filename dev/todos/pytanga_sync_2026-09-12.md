# pytanga Sync — 2026-09-12 (1.17.0 → 2.3.0)

Update the tutorials from pytanga **1.17.0** (the current `extra.tanga_version`
marker in `mkdocs.yml`) to **2.3.0**. This spans **8 changelogs**. See
`dev/workflows/tutorial-update.md` for the overall process.

## Changelogs to process (since 1.17.0)

| # | Version | Changelog file | Since | Scope |
|---|---------|----------------|-------|-------|
| 1 | 2.2.0 | `2026/09/12_541f8f7d.md` | 2.2.0 | AffineExpression solve · `HDirection(x,y,z)` · `display_snapshot` inline default |
| 2 | 2.1.0 | `2026/09/10_fd4465bb.md` | 2.1.0 | Jupyter `Visualizer` singleton · named-scene reset · `PortConflictMode` |
| 3 | 2.0.0 | `2026/09/09_c331b359.md` | 2.0.0 | `install_info` · `LogView` timestamps · export fixes |
| 4 | 2.0.0-rc4 | `2026/09/08_7184d679.md` | 1.17.0 | HTML export CSS refactor (`delivery="cdn"`) |
| 5 | 2.0.0-rc3 | `2026/09/07_c059c59e.md` | 1.17.0 | CDN/offline delivery · `column`/`custom` table column types |
| 6 | 2.0.0-rc2 | `2026/09/06_a175b015.md` | 1.17.0 | CSV delimiter/decimal · SplitView/TableView fixes |
| 7 | 2.0.0-rc1 | `2026/09/05_6ced30c0.md` | 1.17.0 | Native `TableView` · `space_dim` · 2D `stretch` · `SdfCompose` |
| 8 | 2.0.0 | `2026/09/03_58f34cb0.md` | 1.17.0 | **Scene/layout/overlay model · `add_*` removal · display views** |

All changelogs live under `.dep-docs/pytanga/changelog/`.

## Chapter map

- **Part I — Visualization**: `tutorials/visualization/` — 21 chapters
  (`01_quick_tour` … `21_sdf_viewer`).
- **Part II — Geometric Algebra & Core**: `tutorials/algebra/` — 17 chapters
  (`01_quick_tour` … `17_visualizing_algebra_entities`).

## Steps

- [x] 1. Read `2026/09/12_541f8f7d.md` (v2.2.0) → record `### v2.2.0`.
- [x] 2. Read `2026/09/10_fd4465bb.md` (v2.1.0) → record `### v2.1.0`.
- [x] 3. Read `2026/09/09_c331b359.md` (v2.0.0) → record `### v2.0.0`.
- [x] 4. Read `2026/09/08_7184d679.md` (v2.0.0-rc4) → record `### v2.0.0-rc4`.
- [x] 5. Read `2026/09/07_c059c59e.md` (v2.0.0-rc3) → record `### v2.0.0-rc3`.
- [x] 6. Read `2026/09/06_a175b015.md` (v2.0.0-rc2) → record `### v2.0.0-rc2`.
- [x] 7. Read `2026/09/05_6ced30c0.md` (v2.0.0-rc1) → record `### v2.0.0-rc1`.
- [x] 8. Read `2026/09/03_58f34cb0.md` (v2.0.0) → record `### v2.0.0`.
- [x] 9. Consolidate → unified update list (below).
- [x] 10. Rewrite Viz 16 · Controls (`add_*` + runtime value API → `*View` + `set_layout` + `view.set_value`; add display views + menus).
- [x] 11. Create new chapter 17 · Tables (native `TableView`).
- [x] 12. Update Viz 15 · Visualizer app (`add_*` → `*View` + `set_layout`).
- [x] 13. Update Viz 18 → 19 · Responsive computation (`add_slider` → `SliderView`).
- [ ] 14. Update Viz 14 · Split views (scene/layout/overlay model) — non-breaking enhancement (deferred).
- [ ] 15. Update Viz 06 · Multi-scene (`viz.scene(name, space_dim=…)`) — non-breaking enhancement (deferred).
- [x] 16. SDF smooth CSG + `SdfCompose` — verified already covered in the SDF viewer tutorial; tuple form remains valid.
- [ ] 17. Update Viz 09/10 (2D `stretch` + `set_space_dim`) — non-breaking enhancement (deferred).
- [ ] 18. Update Viz 19 → 20 · Export (`delivery=` modes) — non-breaking enhancement (deferred).
- [ ] 19. Update Viz 03/04 (Jupyter singleton + `PortConflictMode`) — non-breaking enhancement (deferred).
- [ ] 20. Update Viz 07/21 (unified transform args + `Transform.from_operator`) — non-breaking enhancement (deferred).
- [x] 21. Update Algebra 14 · Expression (`bind`/`evaluate`).
- [x] 22. Renumber 17–21 → 18–22 (folders, nav, cross-references) + insert new 17.
- [x] 23. Update `mkdocs.yml` → `extra.tanga_version: "2.3.0"`.
- [x] 24. Author branch changelog `docs/changelog/2026-09-12_feat-tanga-2-3-0.md`.
- [x] 25. Validate: `uv run mkdocs build --strict` + `uv run python tools/execute_notebooks.py --dry-run`.

## Per-changelog analyses

### v2.2.0 (`2026/09/12_541f8f7d.md`)

- **Affected**: Algebra 14 · Expression / 11 · Equation solving — `AffineExpression`
  counting-axis reduction + `.lstsq()`/`.svd()`/`.inv()`. Viz 03/19 —
  `display_snapshot()`/`display_row(mode="static")` now default `delivery="inline"`.
- **Breaking**: none.
- **New content**: extend Algebra 14/11 with `AffineExpression` solve; extend Viz 03/19 export notes.
- **Renumbering**: none.

### v2.1.0 (`2026/09/10_fd4465bb.md`)

- **Affected**: Viz 03 · Jupyter notebooks — Jupyter-scoped `Visualizer` singleton,
  `PortConflictMode` (`CANCEL`/`AUTO`/`KILL`/`ASK`), named-scene re-run reset. Viz 04 —
  `port_conflict_mode=` default (`AUTO` under Jupyter).
- **Breaking**: none.
- **New content**: extend Viz 03 with singleton/port-conflict/re-run semantics.
- **Renumbering**: none.

### v2.0.0 (`2026/09/09_c331b359.md`)

- **Affected**: Viz 16/new 17 — `LogView` timestamps (`show_date`/`show_utc_offset`).
  Viz 19 — animated-export Loop/frame-0 fixes.
- **Breaking**: none.
- **New content**: extend display-views coverage.
- **Renumbering**: none.

### v2.0.0-rc4 (`2026/09/08_7184d679.md`)

- **Affected**: Viz 19 · Export — standalone HTML exports inline only base + token shell;
  `delivery="cdn"` references theme shell from jsDelivr.
- **Breaking**: none (internal CSS packing).
- **New content**: none required.
- **Renumbering**: none.

### v2.0.0-rc3 (`2026/09/07_c059c59e.md`)

- **Affected**: Viz 19 · Export — `delivery="inline"`/`"offline"`/`"cdn"`. Viz 16/new 17 —
  `column` (from-column enum) and `custom` (`on_enum_options`) table column types.
- **Breaking**: none.
- **New content**: extend table coverage.
- **Renumbering**: none.

### v2.0.0-rc2 (`2026/09/06_a175b015.md`)

- **Affected**: Viz 16/new 17 — `to_csv`/`from_csv` `delimiter`/`decimal_separator`.
  Viz 14 — `SplitView` fills flow containers.
- **Breaking**: none.
- **New content**: extend table persistence coverage.
- **Renumbering**: none.

### v2.0.0-rc1 (`2026/09/05_6ced30c0.md`)

- **Affected**: Viz 16/new 17 — native `TableView` (column types/editors, persistence,
  sorting, zoom/resize, row/column control, selection-relative insert/delete, editable
  columns). Viz 09/10 — 2D camera `stretch` modes + `set_space_dim`. Viz 05/21 —
  `SdfCompose`. Viz 07/20 — unified transform arguments.
- **Breaking**: 2D camera `uniform` → `stretch` (no tutorial uses `uniform=`; new content only).
- **New content**: table chapter; camera stretch; SDF combine; space-dim switch.
- **Renumbering**: none (table chapter folded here unless a dedicated chapter is added).

### v2.0.0 (`2026/09/03_58f34cb0.md`)

- **Affected**: Viz 16/15/18 — `add_*` facades removed → `*View` + `set_layout`/`viz.add(view)`;
  `control_position` removed → `GroupView(position=…)`; runtime value API removed →
  `Control.set_value`/`undo`/`redo`. Viz 14/06 — scene/layout/overlay model (`add_scene`
  auto-layout, `add_layout`, polymorphic `viz.add`). Viz 05/21 — smooth SDF CSG. Viz 16 —
  display views (`LabelView`/`MarkdownView`/`LogView`/`SeparatorView`/`ToolbarView`).
- **Breaking**: `add_*` facades, `control_position`, `set_control*`/`undo_table`/`redo_table`,
  `controls_define` all removed (major rewrite of Viz 16/15/18).
- **New content**: display views; `Expression.bind()`/`evaluate()` (Algebra 14);
  `Transform.from_operator()` (Viz 07/20).
- **Renumbering**: none.

## Consolidated update list

### 1. Adapt existing chapters

**Part I — Visualization**

| Chapter | Change |
|---------|--------|
| 03 · Jupyter | Jupyter `Visualizer` singleton, `PortConflictMode`, named-scene re-run reset, `display_snapshot` inline default |
| 04 · Getting started | `port_conflict_mode=` default (`AUTO` under Jupyter) |
| 05 · SDF objects | smooth CSG (`smooth_union`/`smooth_intersection`/`smooth_subtract`) + `SdfCompose` |
| 06 · Multi-scene | `viz.scene(name, space_dim=…)` + `LayoutHost → Layout → Scene` hierarchy |
| 07 · Scene graphs | unified `set_transform`/`apply_transform` args + `Transform.from_operator()` |
| 09 · Axes/grid/camera | 2D camera `stretch` modes + `set_space_dim(2|3)` |
| 10 · Coordinate system | `fit_view2d(..., stretch=…)`, `space_dim=2`, `set_space_dim` |
| 14 · Split views | scene/layout/overlay model (`add_layout`/`set_layout`, polymorphic `viz.add`); `SplitView` flow-fill |
| 15 · Visualizer app | `add_*` → `*View` + `set_layout` |
| 16 · Controls | **rewrite**: `add_*` → `*View`; `set_control_value`/`update_control`/`undo_table`/`redo_table` → `Control.set_value`/`.undo`/`.redo`; add display views + `EControlVariant` + `on_press`/`on_release` |
| 18 · Responsive computation | `add_slider` → `SliderView` |
| 19 · Export | `delivery=` (`"cdn"`/`"inline"`/`"offline"`), animated-export Loop fix |
| 20 · GA entities | unified transform args + `Transform.from_operator()` |
| 21 · SDF viewer | smooth CSG + `SdfCompose` |

**Part II — Geometric Algebra & Core**

| Chapter | Change |
|---------|--------|
| 11 · Equation solving | `AffineExpression.lstsq/svd/inv` (verify overlap) |
| 14 · Expression | `Expression.bind()`/`.evaluate()`, `AffineExpression` counting-axis reduction + `.lstsq()`/`.svd()`/`.inv()` |

### 2. New chapters

- **17 · Tables (NEW)** — native `TableView`: column types (`number`/`string`/`bool`/
  enum/`column`/`custom`), editors, keyboard nav, sorting, zoom/resize, undo/redo,
  `add_row`/`add_column`/`insert_row`/`get_cell`/`set_cell`, JSON/CSV persistence with
  `delimiter`/`decimal_separator`. Inserted after Viz 16.

### 3. Renumbering

17 → 18 (banners & dialogs), 18 → 19 (responsive computation), 19 → 20 (export),
20 → 21 (GA entities), 21 → 22 (SDF viewer). Update folder/file stems, `mkdocs.yml` nav,
and intra-tutorial cross-references.

### 4. Parent overview + part plans

Update `dev/todos/tutorial/viz/tutorial_overview.md` (add Tables; note controls rewrite)
and `dev/todos/tutorial/algebra/tutorial_overview.md` (Expression `bind`/`evaluate`).

### 5. Validation

- Grep tutorials for removed APIs: `add_slider|add_button|add_table|add_menu|add_control_group|add_checkbox|add_dropdown|add_text_field|add_text_area|add_color_picker|add_value_edit|add_file_chooser`, `control_position`, `set_control|get_control|set_control_value|set_control_view_value|undo_table|redo_table|update_control|controls_define`, `uniform=`.
- Confirm new names against installed 2.3.0 surface.
- Build gate: `uv run mkdocs build --strict`, `uv run python tools/execute_notebooks.py --dry-run`.
