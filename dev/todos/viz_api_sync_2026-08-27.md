# Viz API Sync — 2026-08-27 Changelog (1.8.0)

Driven by one changelog that postdates the last sync
(`viz_api_sync_2026-08-26.md`, which covered 1.5.0 + 1.6.0 + 1.7.0):

| Changelog | Version | Content |
|-----------|---------|---------|
| `2026-08-27_265517f8.md` ("Since 1.7.0") | v1.8.0 | Four new controls (`add_text_field`/`add_text_area`/`add_color_picker`/`add_checkbox`) · button icons + icon model · tooltips · reusable text editor (`open_editor`) · `ActPoint` `drag_mode` |

Viz-only again — no geometric-algebra core changes, and no breaking changes. The new
controls live on `Visualizer` / `VizSceneHandle` and are also available as control
views in layouts.

## Authoritative changelog deltas

| Area | Change |
|------|--------|
| New | `add_text_field` (single-line text), `add_text_area` (multi-line, `rows`) |
| New | `add_color_picker` (native hex color input), `add_checkbox` (boolean) |
| New | Button icons: `icon=` (rendered before the label) + `icon_only` mode |
| New | Icon model: `family:name` strings, `EIconMaterial` / `EIconUC` enums (Material icons load from Google Fonts; `uc:` glyphs need no font) |
| New | `tooltip=` hover text on every control and the control-group title bar |
| New | `add_group` / `add_control_group` title-bar `icon` + `tooltip` |
| New | `open_editor()` reusable text editor — `on_close(text, event)` receives the edited text (or `None` on discard) |
| New | `ActPoint(..., drag_mode=DragMode.XY_PLANE)` — constrain the unmodified left-button drag to one plane (2D defaults to `XY_PLANE`) |

## 1. Adapt existing chapters (viz plan)

| Chapter | Change |
|---------|--------|
| 1 Quick Tour | broaden the Controls bullet (new controls + icons/tooltips/text editor) |
| 9 Labels & Annotations | cross-ref `open_editor()` → ch 14 |
| 10 Object Interaction | add `ActPoint` `drag_mode=DragMode.XY_PLANE` (and 2D default) |
| 12 Split Views | add the text / color / checkbox control-view counterparts |
| 14 Controls and Input | expand: `add_text_field`/`add_text_area`/`add_color_picker`/`add_checkbox`, icons, tooltips, `open_editor`; add `all_controls.py` example |

## 2. New chapters

None — the 1.8.0 surface is all controls/input, absorbed into the existing
Chapter 14 "Controls and Input" (created in the 1.6.0 sync as the hub for *all*
controls). The chapter grows but remains one coherent "all controls" topic; no split
is warranted.

## 3. Renumbering

None — no chapters inserted or removed.

## 4. Parent overview + Part I

No changes — the top-level `tutorial_overview.md` folder layout and the Part I
(algebra) plan are unaffected (viz-only, additive, no new chapters).

## 5. Validation

- Grep the plans for `#…` anchors; confirm chapter numbers are still consistent.
- Confirm new API names match the installed 1.8.0 surface (`add_text_field`,
  `add_text_area`, `add_color_picker`, `add_checkbox`, `icon`/`icon_only`,
  `EIconMaterial`/`EIconUC`, `tooltip`, `open_editor`, `drag_mode`/`DragMode`).
- Existing `tutorials/algebra/01…08` notebooks: no changes required (only
  `display_snapshot`/`export_snapshot`/`.show()` are used; none of the changed APIs
  appear, and there are no breaking changes).
