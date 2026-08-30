# Viz API Sync — 2026-08-26 Changelogs (1.5.0 + 1.6.0 + 1.7.0)

Driven by three consecutive changelogs that postdate the last sync
(`viz_api_sync_2026-08-25.md`, which covered "Since 1.3.0" = v1.4.0):

| Changelog | Version | Content |
|-----------|---------|---------|
| `2026-08-26_a074adb3.md` ("Since 1.4.0") | v1.5.0 | `ActPoint` drag lifecycle + label support · `clear(add_axes=, add_grid=)` |
| `2026-08-26_d870e5be.md` ("Since 1.5.0") | v1.6.0 | `flush_async`/`flush(wait=True)` · banners/dialogs · compute offload · slider `on_press`/`on_release` · file chooser |
| `2026-08-26_c798944f.md` ("Since 1.6.0") | v1.7.0 | Six extra viz-only entities + mesh/SDF styles · `partialDisk`/`regularPolygon` SDF primitives · `SdfStyle.antialias` |

All three are `pytanga.viz`-only; there are no geometric-algebra core changes
(nothing touches `Algebra`/`MV`, the basis classes, geometry `create`/`analyze`,
solver, matrix, tensor, expression, or BladeMask). The new entities live in
`pytanga.geometry` but are viz-only (no multivector representation), like the
existing `Cylinder`/`Arc`.

## Authoritative changelog deltas

| Area | Change |
|------|--------|
| New | `ActPoint` / `ActSceneObject` `on_drag_start=` / `on_drag_end=` drag-lifecycle callbacks (return value ignored — pure notifications) |
| New | `ActPoint` label support (`viz.add(ActPoint(...), label=...)`, incl. `label_style`, `attach_to`, `parent_id`) |
| New | `clear(add_axes=, add_grid=)` re-add options on `Visualizer` / `VizSceneHandle` |
| New | `flush_async()` (awaitable) + `flush(wait=True)` (blocking, sync scripts only) |
| New | Banners/dialogs: `show_banner` / `alert` / `confirm` (modal `dismissable=False`, per-scene `scene_name=`), `remove_banner` / `clear_banners`, `show_banner_async` |
| New | Compute offload: `submit_user` / `run_user` / `run_user_sync` (and `Visualizer.run_blocking`) |
| New | Slider `on_press` / `on_release` events (in addition to `on_change`) |
| New | File chooser: `add_file_chooser` / `open_file_chooser` / `FileChooserView` (backend-driven modal file browser) |
| New | Viz-only entities `Disk` / `PartialDisk` / `Box` / `Ellipsoid` / `Ellipse` / `RegularPolygon` (+ `regular_polygon()` factory) |
| New | Mesh styles `DiskStyle`/`PartialDiskStyle`/`BoxStyle`/`EllipsoidStyle`/`EllipseStyle`/`RegularPolygonStyle` + SDF styles `SdfDiskStyle`/… |
| New | SDF entity mappings (`Disk`→`cappedCylinder`, `Box`→`box`, `Ellipsoid`/`Ellipse`→`ellipsoid`) + `partialDisk`/`regularPolygon` primitives; `SdfStyle.antialias` |
| Fix | 2D pointer interaction (stale camera + orthographic drag scale); removing an entity now removes its attached labels |

## 1. Adapt existing chapters (viz plan)

| Chapter | Change |
|---------|--------|
| Intro | add controls / banners / responsive to the coverage list; SDF-viewer ref 16 → 19 |
| Conventions | expand the viz-only entity list to 8 entries; refs 15 → 18, 16 → 19 |
| 1 Quick Tour | add Controls / Banners & Dialogs / Responsive Computation bullets; Export ref 14 → 17 |
| 2 Getting Started | add `flush_async()` / `flush(wait=True)` note → ch 16 |
| 3 SDF Objects | add the six `Sdf*Style` classes + `antialias` + entity→SDF mappings |
| 4 Multi-Scene | add `clear(add_axes=, add_grid=)` |
| 6 Styles & Colors | add the six viz-only entities + their `*Style` classes + slab `thickness` |
| 10 Interaction | add `on_drag_start`/`on_drag_end` + `ActPoint` label support |
| 12 Split Views | add `FileChooserView`; link to ch 14 |
| 13 VisualizerApp | reframe as the overview hub linking ch 14 / 15 / 16 |
| 19 SDF Viewer | note `antialias` + new SDF entities are in the *standard* viewer's SDF path (ch 3) |

## 2. New chapters

| New | Chapter | Scope |
|-----|---------|-------|
| 14 | Controls and Input | all panel controls (`add_slider` incl. `on_press`/`on_release`, `add_dropdown`, `add_button`, `add_group`) + file chooser + view controls (`SliderView`/`DropdownView`/`ButtonView`/`FileChooserView`) + removal |
| 15 | Banners and Dialogs | `alert` / `show_banner` / `confirm`, modal, alignment, global vs per-scene, auto-hide vs removal, `show_banner_async` |
| 16 | Responsive Computation | `flush_async()` / `flush(wait=True)` + `submit_user`/`run_user` offload + the "Calculating… banner → offload → done callback" pattern |

## 3. Renumbering (viz plan)

Inserting three chapters after 13 shifts Export/GA/SDF up by three:

| Old | New |
|-----|-----|
| 14 Export | 17 |
| 15 Visualizing GA Entities | 18 |
| 16 SDF Viewer | 19 |
| — | 14 (Controls), 15 (Banners), 16 (Responsive) |

## 4. Parent overview + Part I

- `dev/todos/tutorial/tutorial_overview.md` — add `14_controls/`, `15_banners_dialogs/`,
  `16_responsive_computation/` and renumber `14_export` → `17_export`,
  `15_ga_entities` → `18_ga_entities`, `16_sdf_viewer` → `19_sdf_viewer`; update the
  Part II description, the `visualization/` bullet, and the "runs through" note.
- `dev/todos/tutorial/tutorial_overview.md` (pre-existing fix) — add
  `17_visualizing_algebra_entities/` to the `algebra/` layout (the plan already had a
  17th chapter); drop the stale "plus `21_custom_algebras`" clause (Custom Algebras
  has been `16_custom_algebras/` since the 1.1.0/1.4.0 renumbering) and add
  "visualizing algebra entities" to the `algebra/` bullet.
- `dev/todos/tutorial/algebra/tutorial_overview.md` — add a "Note on viz-only
  entities" to Chapter 15 (Geometry Submodule): the geometry submodule also carries
  rendering-only dataclasses (`Cylinder`, `Arc`, `Disk`, `PartialDisk`, `Box`,
  `Ellipsoid`, `Ellipse`, `RegularPolygon`) with no multivector representation.

## 5. Validation

- Grep the plans for `#…` anchors; confirm chapter numbers are consistent and no
  stale `#14-export`, `#15-visualizing-ga`, `#16-sdf-viewer` references remain.
- Confirm new API names match the installed 1.7.0 surface (`on_drag_start`,
  `on_drag_end`, `clear(add_axes=, add_grid=)`, `flush_async`, `flush(wait=True)`,
  `show_banner`/`alert`/`confirm`, `submit_user`/`run_user`, `on_press`/`on_release`,
  `add_file_chooser`/`open_file_chooser`, `Disk`/`PartialDisk`/`Box`/`Ellipsoid`/
  `Ellipse`/`RegularPolygon`, `regular_polygon`, `SdfStyle.antialias`, …).
- Existing `tutorials/algebra/01…08` notebooks: no changes required (only
  `display_snapshot`/`export_snapshot`/`.show()` are used; none of the changed APIs
  appear, and there are no breaking changes).