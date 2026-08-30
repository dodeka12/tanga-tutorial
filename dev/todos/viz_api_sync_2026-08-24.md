# Viz API Sync — 2026-08-24 Changelog (1.1.0rc2)

Driven by `.dep-docs/pytanga/changelog/2026-08-24_d31afff.md` ("Since 1.0.1",
i.e. `v1.1.0rc2`) and `.dep-docs/pytanga/changelog/2026-08-24_b7423f2.md`
("Since 1.0.0", i.e. `v1.0.1`). The previous sync
(`tutorial_1_0_0_sync_2026-08-24.md`) covered 1.0.0, so these two changelogs are
the outstanding delta for Part II.

The changes are almost entirely **new `pytanga.viz` features** — there is no
breaking change to the existing Part II plan content. The core-algebra changes
(PGA `dual`/`undual` Hodge-star sign fixes, blade-name sign parsing) belong to
Part I and are out of scope here.

## Authoritative changelog deltas

| Area | Change |
|------|--------|
| New | Split views (`SplitView` panes) and the `View` hierarchy (`View`/`SplitView`/`StackView`/`SceneView`/`SpacerView`/`Size`), `show(layout=…)`/`run(layout=…)` |
| New | `StackView` + HTML control views (`SliderView`/`ButtonView`/`DropdownView`), `GroupView` (titled stack / scene overlay) |
| New | Server multi-scene subscription (one WebSocket, many scenes) |
| New | Per-pane cameras — `SceneView(scene, camera=…)`, `Visualizer.set_view_camera(view, camera)` |
| New | Viz-only entities `Cylinder` / `Arc` + `CylinderStyle` / `ArcStyle` |
| New | `CoordinateSystem` plotting helper (`Scale`/`LinearScale`/`LogScale`, `plot`, `add_plot`/`update_plots`, …) |
| New | `VisualizerApp` shutdown (`request_shutdown()`, `enable_server_stop_key` forwarding, blocking `run()`) — from 1.0.1 |

## 1. Adapt existing chapters (viz plan)

| Chapter | Change |
|---------|--------|
| Conventions | add bullets: `CoordinateSystem`; viz-only `Cylinder`/`Arc`; the `View` hierarchy via `show(layout=…)` |
| 1 Quick Tour | add Plotting → ch 7, Split Views & Layouts → ch 11, Interactive Apps → ch 12; renumber the rest |
| 2 Getting Started | note `show()`/`run()` accept `layout=`; viz-only entities exist |
| 3 Multi-Scene | add multi-scene subscription + layout pointer |
| 5 Styles | add `Cylinder`/`Arc` + `CylinderStyle`/`ArcStyle` |
| 6 Axes/Grid/Camera | add `ticks`/`line_positions_*`, `span_u`/`span_v`, `Point()`/`Direction()` args; `CoordinateSystem` pointer |
| 9 Animation | drop the `VisualizerApp` sentence → pointer to ch 12; add live-plot trails pointer |

## 2. New chapters (the larger topics)

| New | Chapter | Scope |
|-----|---------|-------|
| 7 | Coordinate System and Plotting | `CoordinateSystem`, scales, placement, `plot`/`to_local`/`to_world`/`transform`, live trails, in-place updates |
| 11 | Split Views, Layouts, and Control Views | `View` hierarchy, `Size`, splitters, `SceneView` overlays + per-pane cameras, `set_view_camera`, control views, `show(layout=…)` |
| 12 | Interactive Applications (VisualizerApp) | lifecycle, panel controls, scene-scoped controls, handler contract, layout apps, `request_shutdown()`/Ctrl+Q |

## 3. Renumbering

| Old | New | Title |
|-----|-----|-------|
| 1–6 | 1–6 | unchanged |
| — | 7 | Coordinate System and Plotting |
| 7 | 8 | Labels, Titles, and Annotations |
| 8 | 9 | Object Interaction and Active Objects |
| 9 | 10 | Animation |
| — | 11 | Split Views, Layouts, and Control Views |
| — | 12 | Interactive Applications (VisualizerApp) |
| 10 | 13 | Export and Publishing |
| 11 | 14 | Visualizing GA Entities and Operators |

## 4. Parent overview

`dev/todos/tutorial/tutorial_overview.md` — replace the stale 6-chapter
`visualization/` folder layout with the 14-chapter layout; update the Part II
description and the numbering note.

## 5. Out of scope (flag for Part I)

- `BasisPGA3`/`BasisPGA2` `dual`/`undual` sign fixes and blade-name sign parsing
  (`e31` → `-e13`) — algebra tutorials (`07_pga3`, the algebra plan's duality
  chapter).

## 6. Validation

- Grep the viz plan for `#…` anchors after renumbering; confirm no broken links.
- Confirm the removed `VisualizerApp` sentence now points to ch 12.
- Confirm new-feature names match the 1.1.0rc2 docs (`SplitView`, `CoordinateSystem`,
  `Cylinder`, `Arc`, `set_view_camera`, `request_shutdown`, …).
