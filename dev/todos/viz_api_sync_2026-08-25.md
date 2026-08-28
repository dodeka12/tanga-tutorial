# Viz API Sync — 2026-08-25 Changelogs (1.2.0 + 1.3.0 + 1.4.0)

Driven by three consecutive changelogs that postdate the last sync
(`viz_api_sync_2026-08-24.md`, which covered "Since 1.0.0" and "Since 1.0.1"):

| Changelog | Version | Content |
|-----------|---------|---------|
| `2026-08-25_c6f85e08.md` ("Since 1.1.0") | v1.2.0 | `CoordinateSystem` inner data group + `vline`/`hline`/`line`/`point` annotation helpers |
| `2026-08-25_88f3e3d9.md` ("Since 1.2.0") | v1.3.0 | Per-frame camera playback in animated export · default 2D orthographic camera · export honors live camera |
| `2026-08-25_cbc7adc7.md` ("Since 1.3.0") | v1.4.0 | SDF viewer (`SdfVisualizer`) + SDF objects in the standard viewer |

All three are `pytanga.viz`-only; there are no geometric-algebra core changes (the
PGA `dual`/`undual` sign fixes were already flagged to Part I in the previous sync).

## Authoritative changelog deltas

| Area | Change |
|------|--------|
| New | `CoordinateSystem.data_group` + `to_data(x, y)` (plots/drawings in data coords) |
| New | `vline`/`hline`/`line`/`point` annotation helpers (create-or-update by `name`, `remove_*`, `label`/`label_style`) |
| New | Per-frame camera playback in animated HTML export (`AnimationRecording` snapshots camera each frame) |
| New | Default 2D view uses a top-down orthographic camera |
| New | HTML export honors the full live-scene camera config |
| New | `SdfVisualizer` (WebGL2 ray-marched viewer) + primitive library + `Composed` + per-object CSG + lighting + overlays |
| New | SDF objects in the standard viewer: `SdfStyle` marker, per-entity `Sdf*Style`, `SdfObject`+`ECompose` operators, `Composed`, `SdfGroup`, per-object materials |

## 1. Adapt existing chapters (viz plan)

| Chapter | Change |
|---------|--------|
| Intro | mention the two rendering paths (mesh + SDF) |
| Conventions | add the SDF rendering bullet; renumber refs 14→15, 7→8, 5→6, 11→12 |
| 1 Quick Tour | add SDF Objects section → ch 3; renumber refs |
| 2 Getting Started | ref ch 11 → 12 |
| 7 Axes/Grid/Camera | add default 2D orthographic camera note; ref ch 7 → 8 |
| 8 Coordinate System | add `data_group`/`to_data` + `vline`/`hline`/`line`/`point` helpers |
| 11 Animation | refs ch 7 → 8, ch 12 → 13 |
| 14 Export | add per-frame camera playback + live-camera/orthographic note |

## 2. New chapters

| New | Chapter | Scope |
|-----|---------|-------|
| 3 | SDF Objects in the Standard Viewer | `SdfStyle` + per-entity `Sdf*Style`, `SdfObject` + `ECompose` operators, `Composed`, `SdfGroup`, per-object materials, limitations (prominent, early — the main supported SDF route) |
| 16 | SDF Viewer (SdfVisualizer) | short, early-stage/experimental note; primitives, `Composed`, per-object CSG, entity mapping, lighting, overlays, update loop |

## 3. Renumbering (viz plan)

Inserting Chapter 3 shifts old 3–14 up by one; Chapter 16 is appended:

| Old | New |
|-----|-----|
| 3–14 | 4–15 |
| — | 3 (SDF Objects) |
| — | 16 (SDF Viewer) |

## 4. Parent overview + Part I

- `dev/todos/tutorial/tutorial_overview.md` — add `03_sdf_objects/` and `16_sdf_viewer/`
  to the `visualization/` layout (renumbering 03–14 → 04–15), update the Part II
  description, the `visualization/` bullet, and the "runs through 14_ga_entities" note.
- `dev/todos/tutorial/algebra/tutorial_overview.md` — add `MV.undual()` (the inverse
  right dual, `dual(undual(A)) == A`) and the PGA3/PGA2 Hodge-star sign fix note to
  Chapter 8 "Duality and Complements" (a 1.0.x gap folded in now).

## 5. Validation

- Grep the viz plan for `#…` anchors; confirm chapter numbers are consistent and no
  stale `[Chapter N]`/`(#N-…)` references remain.
- Confirm new API names match the installed 1.4.0 surface (`SdfVisualizer`, `SdfStyle`,
  `SdfObject`, `ECompose`, `Composed`, `SdfGroup`, `DirectionalLight`, `set_member_transform`,
  `data_group`, `to_data`, `vline`, `hline`, `AnimationRecording`, …).
