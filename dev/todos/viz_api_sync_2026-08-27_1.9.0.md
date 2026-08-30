# Viz API Sync — 2026-08-27 Changelog (1.9.0)

Driven by one changelog that postdates the last sync
(`viz_api_sync_2026-08-27.md`, which covered 1.8.0):

| Changelog | Version | Content |
|-----------|---------|---------|
| `2026-08-27_0041385d.md` ("Since 1.8.0") | v1.9.0 | In-place control value updates (`set_control_value`/`set_control_view_value`) · value-edit stepper (`add_value_edit`/`ValueEditView`) · breaking: control `default` → `value` |

Viz-only again — no geometric-algebra core changes. The one breaking change
(`default` → `value`) is confined to the controls surface, so it only affects the viz
plan's Chapter 14 (plus its control-view references in Chapters 1 and 12).

## Authoritative changelog deltas

| Area | Change |
|------|--------|
| New | `set_control_value` / `set_control_view_value` (plus `VizSceneHandle.set_control_value`) — update a control's value after creation via a lightweight `control_update` message, preserving panel collapse/drag/focus state |
| New | `update_control(..., value=...)` routes through `set_control_value` |
| New | `add_value_edit` / `ValueEditView` — numeric stepper (`min`/`max`/`step`/`digits`, up/down buttons, arrow-key/scroll-wheel stepping, `editable=True`) |
| Breaking | Control value field `default` → `value` everywhere (dataclasses, view classes, `add_*` APIs, `"value"` wire field; no alias kept) |

## 1. Adapt existing chapters (viz plan)

| Chapter | Change |
|---------|--------|
| 1 Quick Tour | broaden the Controls bullet (value-edit stepper + in-place `set_control_value`) |
| 12 Split Views | add `ValueEditView` to the control-view list |
| 14 Controls and Input | `default` → `value`; add `add_value_edit`/`ValueEditView`; add `set_control_value`/`set_control_view_value`/`update_control(..., value=...)` + the breaking-rename note; update `all_controls.py` example; fix `add_group`/`remove_group` → `add_control_group`/`remove_control_group` |

## 2. New chapters

None — the 1.9.0 surface is all controls/input, absorbed into the existing
Chapter 14 "Controls and Input".

## 3. Renumbering

None — no chapters inserted or removed.

## 4. Parent overview + Part I

No changes — the top-level `tutorial_overview.md` folder layout and the Part I
(algebra) plan are unaffected (viz-only, additive, no new chapters).

## 5. Validation

- Grep the plans for `#…` anchors; confirm chapter numbers are still consistent.
- Confirm new API names match the installed 1.9.0 surface (`set_control_value`,
  `set_control_view_value`, `add_value_edit`, `ValueEditView`, `value=`,
  `update_control(..., value=...)`).
- Confirm no `default=` control references remain in the plans.
- Existing `tutorials/algebra/01…08` notebooks: no changes required (only
  `display_snapshot`/`export_snapshot`/`.show()` are used; none of the changed APIs
  appear, and the breaking change is controls-only).
