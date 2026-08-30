# TanGA Tutorial Series — Part I: Visualization

This plan teaches the **`pytanga.viz` viewer** from scratch — no geometric-algebra
(GA) background required. It covers everything the viewer can do: building scenes,
styling, axes/grid/camera, labels, object interaction, animation, controls,
banners/dialogs, responsive computation, export — and the viewer's two rendering
paths: the standard mesh pipeline and an opt-in ray-marched
**signed-distance-field (SDF)** path (see
[Chapter 3](#3-sdf-objects-in-the-standard-viewer) and
[Chapter 19](#19-sdf-viewer-sdfvisualizer)).

Visualization inputs are drawn from `pytanga.geometry` dataclasses (`Point`,
`Direction`, `Line`, `Plane`, `Sphere`, `Circle`, `PointPair`, …) used as **plain 3D
data**. A reader can follow the entire part without knowing anything about
multivectors or algebras. The GA-entities chapter near the end introduces how GA entities and operators
are visualized, but only at a basic level — it defers the GA theory to
[Part II — Geometric Algebra & Core](../algebra/tutorial_overview.md).

The companion plan is [Part II — Geometric Algebra & Core](../algebra/tutorial_overview.md),
which covers the algebra, basis classes, geometry submodule, and numerical tooling.

---

## Conventions (shared with Part II)

- Entities passed to the viewer are geometry dataclasses from `pytanga.geometry`
  (or raw multivectors, which are analyzed on the way in — see
  [Chapter 18](#18-visualizing-ga-entities-and-operators)).
- Styles are passed to `add()` as `style=...`, as a `color=`/`opacity=` shortcut, or
  configured once via `viz.styles` defaults (per-kind `viz.styles[...]`, master
  template `viz.global_styles`).
- Grid and axes are explicit scene objects (`Axis`, `Grid`, `Axes2D`, `Axes3D`);
  a default set is inserted per scene unless disabled with `add_default_axes=False`
  / `add_default_grid=False`. The `CoordinateSystem` helper composes grid + axes +
  value labels + an optional background plane + plotted `PointPath`s in one
  `VizGroup` (see [Chapter 8](#8-coordinate-system-and-plotting)).
- The viz-only entities `Cylinder`, `Arc`, `Disk`, `PartialDisk`, `Box`,
  `Ellipsoid`, `Ellipse`, and `RegularPolygon` exist purely for rendering and have
  no multivector representation (see [Chapter 6](#6-styles-and-colors)).
- The viewer has two rendering paths: the standard mesh pipeline and an opt-in
  ray-marched signed-distance-field (SDF) path. SDF objects are rendered inside the
  standard viewer via the `SdfStyle` marker / the `SdfObject` model (see
  [Chapter 3](#3-sdf-objects-in-the-standard-viewer)); the separate, experimental
  `SdfVisualizer` is covered in [Chapter 19](#19-sdf-viewer-sdfvisualizer).
- Multiple scenes and control panels can be arranged in a single browser page with
  the `View` hierarchy (`SplitView`, `StackView`, `SceneView`, and the control
  views) opened via `show(layout=...)` (see
  [Chapter 12](#12-split-views-layouts-and-control-views)).

---

## 1. Visualization Quick Tour ✅

**Format:** Jupyter notebook

**Abstract:** A rapid, example-driven tour through the `pytanga.viz` viewer — no
geometric-algebra background required. Glance at each major capability to see the big
picture and know where to dive deeper. Each section ends with a reference to the
chapter that covers the topic in full.

Sections:

- **Scenes** — Create a `Visualizer`, add a `Point`, `Line`, and `Sphere`, and open the
  interactive Three.js viewer with `show()` + `wait()`. → [Chapter 2](#2-getting-started-with-the-viewer)
- **SDF Objects** — Render smooth ray-marched solids in the standard viewer: opt an
  entity into SDF with `SdfStyle`, compose objects with `SdfObject` + the Python CSG
  operators (`+`/`-`/`&`/`^`), and group members into one solid with `SdfGroup`. →
  [Chapter 3](#3-sdf-objects-in-the-standard-viewer)
- **Scene Graphs & Transforms** — Group entities into hierarchies with `VizGroup`, mutate
  them by reference with `VizObjectRef`, and transform them. →
  [Chapter 5](#5-scene-graphs-groups-and-transforms)
- **Styles & Colors** — Give entities color, opacity, wireframe, and point size via the
  per-type style dataclasses. → [Chapter 6](#6-styles-and-colors)
- **Axes, Grid & Camera** — Frame the scene with axes/grid and configure the camera. →
  [Chapter 7](#7-axes-grid-and-camera)
- **Plotting** — Build a full 2D/3D plotting coordinate system (grid, axes, value
  labels, plots) with `CoordinateSystem`. →
  [Chapter 8](#8-coordinate-system-and-plotting)
- **Labels & Annotations** — Add labels, titles, and Markdown/LaTeX annotations. →
  [Chapter 9](#9-labels-titles-and-annotations)
- **Interaction** — Make objects clickable and draggable with the pointer-event
  system. → [Chapter 10](#10-object-interaction-and-active-objects)
- **Animation** — Animate entities with `Visualizer.animate()` (call `show()` first),
  `PointPath`, `animate_to`, and `Timeline`. → [Chapter 11](#11-animation)
- **Split Views & Layouts** — Show several scenes and control panels in one browser
  page with `SplitView`/`SceneView`/`GroupView` and `show(layout=...)`. →
  [Chapter 12](#12-split-views-layouts-and-control-views)
- **Interactive Apps** — Build an interactive `VisualizerApp` with sliders, dropdowns,
  and buttons. → [Chapter 13](#13-interactive-applications-visualizerapp)
- **Controls** — Use every control type (sliders, dropdowns, buttons with icons, text
  fields, text areas, color picker, checkbox, a numeric value-edit stepper, and the
  file chooser), tooltips, in-place value updates (`set_control_value`), and the
  reusable text editor. →
  [Chapter 14](#14-controls-and-input)
- **Banners & Dialogs** — Show status overlays, prompts, and modal dialogs with
  `show_banner()` / `alert()` / `confirm()`. →
  [Chapter 15](#15-banners-and-dialogs)
- **Responsive Computation** — Keep the viewer responsive during long-running work with
  `flush_async()` and compute offload (`submit_user`). →
  [Chapter 16](#16-responsive-computation)
- **Export** — Export self-contained HTML, PNG screenshots, and MP4 video. →
  [Chapter 17](#17-export-and-publishing)

**Visual Examples:** Include a single standalone HTML figure generated by
`pytanga.viz.Visualizer` showing a styled sphere, a line, and a label — a taste of what
the full visualization tutorials cover. Export via `export_snapshot()`.

---

## 2. Getting Started with the Viewer ✅

**Format:** Jupyter notebook

**Abstract:** Create a `Visualizer` (3D by default; 2D with `space_dim=2`), add a few
plain entities (`Point`, `Line`, `Sphere`) via `add()`, and open the interactive
Three.js viewer with `show()` — the single display entry point. `show()` accepts a
`jupyter` option (`None` auto-detects, `True` forces inline notebook display, `False`
forces a browser tab). Cover the two run modes — blocking `show()`/`wait()` vs
non-blocking `start_server()`/`flush()`/`stop_server()` (the awaitable `flush_async()`
and blocking `flush(wait=True)` variants are covered in
[Chapter 16](#16-responsive-computation)) — plus browser tab reuse
(`reuse_existing`), `wait_for_browser`, and the `Ctrl+S` screenshot shortcut. For
inline Jupyter output use `display()`, which (like `show()`) is idempotent within a
cell — repeated calls flush into the already-open viewer, keyed by `viewer_name`, the
cell id, or the scene name — and prints a hint to call `start_server()` when invoked
before the server is running. `show()`/`run()` also accept a `layout=` to open a
split-view page (see [Chapter 12](#12-split-views-layouts-and-control-views)).

---

## 3. SDF Objects in the Standard Viewer ✅

**Format:** Jupyter notebook

**Abstract:** Render smooth, ray-marched **signed-distance-field (SDF) solids**
inside the standard mesh viewer, mixed with normal meshes in the same scene. Opt a
single entity into SDF rendering with the `SdfStyle` marker style
(`viz.add(Sphere(...), style=SdfStyle(color=...))`) and tune it with the per-entity
style dataclasses (`SdfSphereStyle`, `SdfLineStyle` with `thickness`, `SdfCircleStyle`
with `tube_radius`, `SdfPointStyle` with `size`, `SdfCylinderStyle`,
`SdfPlaneStyle`, plus `SdfDiskStyle`/`SdfPartialDiskStyle`/`SdfEllipseStyle`/
`SdfRegularPolygonStyle` with a slab `thickness`, and `SdfBoxStyle`/`SdfEllipsoidStyle`).
Note the `SdfStyle.antialias` knob (an analytic ~1px silhouette edge fade, off by
default). Build composable SDF objects with `SdfObject` (a geometry entity
plus an id and a per-entity style) and combine them with the Python CSG operators —
`+`/`|` (union), `-` (subtract), `&` (intersection), `^` (xor), and the unary `-`/`~`
polarity tags — backed by the `ECompose`/`Combine` node model. Bundle constituents
into a single internally-CSG'd object with `Composed`, and group several members into
one ray-marched solid (cross-object CSG + per-member materials + independent runtime
transforms) with `SdfGroup`, addressing members by id or index via
`set_member_transform(...)`. Note the constraints: WebGL2 required (SDF objects are
skipped on WebGL1), up to 16 members per `SdfGroup`, and no cross-object shadows
(only self-shadowing within an object/group). Frame-by-frame member animation uses
the loop from [Chapter 11](#11-animation); SDF objects also support the same labels,
interaction, and tweening as meshes. The viz-only entities also map to SDF primitives
— `Disk`→`cappedCylinder`, `Box`→`box`, `Ellipsoid`/`Ellipse`→`ellipsoid`, plus the
new `partialDisk`/`regularPolygon` primitives — so every new solid renders via
`SdfObject(...)` too.

**Visual Examples:** `objects.py` (meshes + `SdfStyle` sphere + a `Composed` bead +
tween + interaction), `object_model.py` (per-entity styles, `SdfObject` operators,
`SdfGroup` per-member materials), `group.py` (`SdfGroup` with per-member CSG +
independent member animation).

---

## 4. Interactive Scenes and Multi-Scene Management ✅

**Format:** Jupyter notebook

**Abstract:** Work with scenes. Add to the main scene, create named scenes with
`viz.scene(name)`, and manage each through `VizSceneHandle`. Cover the scene context
managers — `with viz:` and `with viz.scene("name"):` (reset the scene, `show()` on
entry, flush on exit) — plus multi-scene URLs, browser navigation (`navigate_to()`),
`list_browsers()`, viewer identity (`?viewer=` URL parameter), and side-by-side
Jupyter display with `display_row()`. Cover the scene lifecycle (`add`, `update`,
`remove`, `clear`, `flush`) — including `clear(add_axes=, add_grid=)` to re-add the
default axes/grid after clearing — and the `update_style()` method for changing style
properties without rebuilding geometry. Cover the opt-in browser full-server stop key
via `enable_server_stop_key()` (default Ctrl+Q) and
`viz.scene(name, enable_server_stop_key=True)`. A single browser can subscribe to
many scenes over one WebSocket connection — the mechanism behind multi-pane
layouts (see [Chapter 12](#12-split-views-layouts-and-control-views)).

---

## 5. Scene Graphs, Groups, and Transforms ✅

**Format:** Jupyter notebook

**Abstract:** Organize scenes as node hierarchies. Build parent/child hierarchies with
`VizGroup` (empty `THREE.Group` nodes) and create entities inside groups with
`viz.new(...)` / `group.new(...)` — or the callable `viz(...)` shorthand for `new()`,
which returns a `VizObjectRef`. Use the `VizObjectRef` handle to mutate nodes by
reference — replace `.entity`, adjust `.style` / `.color` / `.opacity`, and manage
labels via `.label_ids` / `.labels` / `update_label()`. Cover per-object transforms
(`translate`, `rotate`, `scale_by`, `set_transform`) and operator-based `transform`
(`Rotor` / `Motor` / `Translator` / `Dilator`) with aspect-scoped `full` / `style` /
`transform` updates for cheap in-place group animation. Introduce the `content` aspect
— replacing an entity's geometry (same kind) mutates the three.js mesh in place,
preserving transform, parent, style, and id mapping. Cover overlay nodes via
`attach_to` (overlay follows a referenced scene node in the CSS plane).

**Visual Examples:** nested groups (`demo_nested_groups.py`), a two-link arm / double
pendulum built from nested groups with midpoint line labels, and a
`VizObjectRef`-driven drag/update loop (`demo_drag_point.py`, `demo_scene_graph.py`).

---

## 6. Styles and Colors ✅

**Format:** Jupyter notebook

**Abstract:** Style entities with the per-type style dataclasses (`PointStyle`,
`LineStyle`, `PlaneStyle`, `SphereStyle`, `CircleStyle`, …) and the `Color` enum.
Explain the color/opacity precedence (`add(color=...)` → `style=...` →
`viz.styles` defaults), the `viz.styles` override mechanism (per-kind `viz.styles[...]`,
`viz.global_styles`, `set_default_color()`, assign vs `merge`), and how to set label
defaults via `viz.styles.label_base` / `viz.styles.label_kind`. Cover opacity, wireframe
rendering, point size, screen-space line thickness, and `CylinderLineStyle` (world-unit
cylinder lines). Introduce the viz-only entities — `Cylinder` and `Arc`, plus the
newer `Disk`, `PartialDisk`, `Box`, `Ellipsoid`, `Ellipse`, and `RegularPolygon` (via
the `regular_polygon()` factory) — which have no multivector representation, and their
style classes (`CylinderStyle` / `ArcStyle` / `DiskStyle` / `PartialDiskStyle` /
`BoxStyle` / `EllipsoidStyle` / `EllipseStyle` / `RegularPolygonStyle`). Cover the
shared knobs (`color`, `opacity`, `wireframe`, `wireframe_dash`, `wireframe_color`,
`wireframe_opacity`) and the per-entity slab `thickness` for the flat shapes
(`Disk` / `PartialDisk` / `Ellipse` / `RegularPolygon`); the planar shapes default to
the xy-plane (`normal = +z`), so they work in both 2D and 3D scenes.

---

## 7. Axes, Grid, and Camera ✅

**Format:** Jupyter notebook

**Abstract:** Control scene framing and reference geometry. Cover the `Axis`, `Grid`,
`Axes2D`, and `Axes3D` scene objects (value labels via `Axis.show_value_labels` /
`Axis.value_format`, name/value label styles via `AxisStyle.label_style` /
`AxisStyle.value_style`, plus `GridStyle` / `Axes2DStyle` / `Axes3DStyle`) and the
default axes+grid behaviour
(`add_default_axes` / `add_default_grid`). Cover camera configuration in depth:
auto-fit (`flush(fit_camera=True)`), explicit `CameraConfig3d`, the `View2DConfig` /
`View3dConfig` input specs and their builders (`get_camera_view2d()`,
`get_camera_view3d()`, `get_camera()`), and runtime updates via `set_camera()`.
Explain orbit controls in 3D vs 2D mode, and note that a 2D scene (`space_dim=2`)
without an explicit camera now defaults to a top-down orthographic camera (so
`flush(fit_camera=True)` recenters it correctly). `Axis`/`Grid` also expose explicit
`ticks`/`line_positions_*` placement, the `Plane` renderer honors `span_u`/`span_v`,
and `position`/`normal`/`up` accept `Point()`/`Direction()` objects. For a complete
plotting coordinate system built from these primitives, see
[Chapter 8](#8-coordinate-system-and-plotting).

---

## 8. Coordinate System and Plotting ✅

**Format:** Jupyter notebook

**Abstract:** Turn the viewer into a 2D/3D plotting tool with `CoordinateSystem`, a
helper that builds a complete plotting coordinate system — grid, axes with value
labels, an optional background plane, and plotted `PointPath`s — inside a single
`VizGroup`. Cover the data range (`xlim` / `ylim`), linear and logarithmic scales
(`xscale` / `yscale`, `Scale` / `LinearScale` / `LogScale`, `base`), the external
`size` vs the data range, `align` / `axis_origin` placement, and 3D
`position` / `normal` / `up` (all also accepting `Point()` / `Direction()` objects).
Plot series with `plot()` and map between data and world coordinates with
`to_local()` / `to_world()` / `transform()`. Plots and user drawings are expressed in
data coordinates via the inner data group (`cs.data_group`, `to_data(x, y)`), so
Python-side scaling is only needed for log axes. Add annotations with the
`vline(x, ...)` / `hline(y, ...)` / `line(start, end, ...)` / `point(p, ...)` helpers
(each accepting `(x, y)` tuples or `Point` instances, create-or-update by an optional
`name`, removable with `remove_vline` / `remove_hline` / `remove_line` / `remove_point`,
and labelable via `label` + `label_style`). Register live trails with
`add_plot()` + `update_plots()` (including the auto-scaling `min_x_span` time axis),
and update ranges/scales in place (`cs.xlim = …`, `cs.yscale = "log"`, etc.) without
re-adding objects. Style the parts via `x_style` / `y_style` / `grid_style` /
`plane_style`.

**Visual Examples:** log-log plots (`demo_log_plot.py`), a tilted 3D plane plot
(`demo_plot_3d.py`), and a live pendulum angle-vs-time trail (`demo_pendulum_plot.py`).

---

## 9. Labels, Titles, and Annotations ✅

**Format:** Jupyter notebook

**Abstract:** Enhance visualizations with `Label` dataclasses (local-frame
positioning, per-entity anchors via `LabelStyle.along`, screen-plane rotation via
`LabelStyle.rotation`, custom `LabelStyle`, dynamic `update_label()`), title overlays,
and Markdown annotation panels with LaTeX math (rendered via KaTeX) — the reusable
`open_editor()` overlay for editing annotation text is covered in
[Chapter 14](#14-controls-and-input). Show how to combine clear labelling with
geometric content for presentation-ready figures.

---

## 10. Object Interaction and Active Objects ✅

**Format:** Jupyter notebook

**Abstract:** Make scenes interactive. Use the pointer-event system
(`InteractionConfig` / `InteractionTrigger` / `InteractionEventType`, `MouseButton`,
`ModifierKey`, `DragMode`) and register handlers with `set_interaction()` /
`on_interaction()`. Cover the event dataclasses (`ClickEvent`, `DragEvent`,
`ScrollEvent`) and the attached `Camera` (world↔screen `project()` / `unproject()`).
Introduce the active scene objects (`ActSceneObject`, `ActPoint`) with their styles
(`ActObjectStyle`, `ActPointStyle`) as a simplified high-level API for common
drag/interaction patterns. Cover `ActPoint`'s drag lifecycle — the move-phase
`handler=` plus the `on_drag_start=` / `on_drag_end=` notification callbacks — its
`drag_mode=` constraint (`ActPoint(..., drag_mode=DragMode.XY_PLANE)` pins the
unmodified left-button drag to a single plane; when omitted, 2D visualizers default to
`XY_PLANE` and 3D keeps the four modifier-switched triggers), and its attached
`label=` (with `label_style`, `attach_to`, and `parent_id`) like any regular entity.

---

## 11. Animation ✅

**Format:** Jupyter notebook

**Abstract:** Animate geometric constructions. Drive scripted animations with the
`Visualizer.animate()` frame loop (a generator that yields once per frame, paces to a
target `fps`, and stops cleanly on exit), updating entities in place via the `content`
aspect. `animate()` no longer opens the viewer — call `show()` first (or use
`with viz:`); for per-frame `add()` calls that should not accumulate, pass
`animate(auto_clear=True)` (each frame flushes, then removes objects added after the
loop began). Use `PointPath` for connected line segments, object trails, per-point colors,
and FIFO capping with gradient utilities; keyframe tweening with `animate_to`; and the
scene-aware `Timeline` sequencer for choreographed multi-entity animations (fade-in,
move, rotate). Drive live plotting trails with `CoordinateSystem.add_plot()` /
`update_plots()` (see [Chapter 8](#8-coordinate-system-and-plotting)). For building
an interactive application around your animation, see
[Chapter 13](#13-interactive-applications-visualizerapp).

---

## 12. Split Views, Layouts, and Control Views ✅

**Format:** Jupyter notebook

**Abstract:** Compose multiple scenes and control panels into a single browser page
with the `View` hierarchy: `SplitView` (nestable horizontal/vertical splits with
draggable splitters), `StackView` (vertical/horizontal/wrap flow), `SceneView` (a
scene pane with overlays and a per-pane initial camera), `GroupView` (a titled
control group usable as a pane or a `SceneView` overlay), `SpacerView`, and the HTML
control views `SliderView` / `DropdownView` / `ButtonView` / `ValueEditView` /
`FileChooserView` and their text / color / checkbox counterparts (every panel
control has a matching `View` class — all detailed in
[Chapter 14](#14-controls-and-input)). Cover the `Size` units
(`px` / `%` / `fr` / `auto`), per-axis `min`/`max` constraints, and fixed vs. movable
splitters. Open a layout at one URL with `show(layout=...)` / `run(layout=...)`;
give a pane its own initial camera with `SceneView(scene, camera=…)` and re-aim one
pane at runtime with `set_view_camera(view, camera)`. Control handlers
(`on_change` / `on_click`) are registered automatically when the layout is set, and a
browser subscribes to every pane's scene over one WebSocket connection.

**Visual Examples:** `demo_split_view.py` (a control sidebar, nested splits, a
per-pane camera, and a runtime `set_view_camera` button).

---

## 13. Interactive Applications (VisualizerApp) ✅

**Format:** Jupyter notebook

**Abstract:** Build a complete interactive application with `VisualizerApp` — the
managed lifecycle (`init` → block → `cleanup`), the async handler contract
`(value, ControlEvent)`, and clean shutdown via `request_shutdown()` and the opt-in
browser Ctrl+Q stop key (`enable_server_stop_key`). This chapter is the **overview
hub** for everything that makes a viewer interactive: it maps out the moving parts and
points to the dedicated detail chapters — the controls
([Chapter 14](#14-controls-and-input)), banners & dialogs
([Chapter 15](#15-banners-and-dialogs)), and keeping the viewer responsive during
computation ([Chapter 16](#16-responsive-computation)). Show how to combine panel
controls with view controls inside a `SplitView` layout (overriding `run()` to open
`show(layout=...)`).

**Visual Examples:** `two_spheres_interact.py`, and the split-view app from the
library's "Layouts — Split Views & Controls" guide.

---

## 14. Controls and Input ✅

**Format:** Jupyter notebook

**Abstract:** Cover every control the viewer offers, and how to combine them into a
polished control panel. Panel controls created on the `Visualizer` / `VizSceneHandle`:
`add_slider` (`min`/`max`/`step`/`value`, `on_change`, plus the press/release events
`on_press` / `on_release`), `add_dropdown` (`options` / `value` / `on_change`),
`add_button` (`on_click`), the numeric stepper `add_value_edit` (`min`/`max`/`step`/
`digits`, up/down buttons, arrow-key / scroll-wheel stepping, `editable=`), the text
inputs `add_text_field` (single-line) and `add_text_area` (multi-line, `rows`),
`add_color_picker` (native hex color input), `add_checkbox` (boolean), and the file
chooser `add_file_chooser` (a text field + "Browse…" backed by a backend-driven,
modal file browser, `root=`, `open_file_chooser()`). Group them with
`add_control_group` (title bar, `position`, `collapsed`, `on_toggle`). Cover the
shared chrome: button icons (`icon=` with an `icon_only` mode) and the icon model
(`family:name` strings plus the `EIconMaterial` / `EIconUC` enums — Material icons
load from Google Fonts, `uc:` glyphs need no font), and `tooltip=` hover text on every
control and the group title bar. Introduce the reusable text editor `open_editor()` (a
transient multi-line overlay whose `on_close(text, event)` receives the edited text,
or `None` on discard). Cover updating a control's value in place after creation —
`set_control_value` / `set_control_view_value` (plus `VizSceneHandle.set_control_value`
and `update_control(..., value=...)`) via the lightweight `control_update` message,
which preserves the panel's collapse/drag/focus state instead of rebuilding it — and
note the 1.9 breaking rename: the control value field is `value`, not `default` (the
old `default=` keyword no longer works). Cover the layout view-control counterparts
used inside a `SplitView` pane (every panel control has a matching `View`, incl.
`ValueEditView`), scene-scoped controls, and removal (`remove_control` /
`remove_control_group` / `clear_controls`). Note that controls must be created before
any group that references them, and that every control uses the same async
`(value, event)` handler contract.

**Visual Examples:** `all_controls.py` (one of every control kind — slider, dropdown,
button with icon + icon-only, value-edit stepper, text field, text area, color
picker, checkbox, file chooser, plus `open_editor` and in-place `set_control_value`
sync), `file_chooser.py`, `two_spheres_interact.py`, and the library's "Controls"
guide.

---

## 15. Banners and Dialogs ✅

**Format:** Jupyter notebook

**Abstract:** Show transient overlays and dialogs over the viewer. Cover the banner
kinds — `alert()` (acknowledge), `show_banner()` (custom options via
`controls=[Button(…), Slider(…), …]`), `confirm()` (yes/no/cancel), and the modal
variant `show_banner(..., dismissable=False)` (dimmed backdrop, blocks the scene) —
with markdown/KaTeX text, fractional `align_x` / `align_y` placement, global vs
per-scene scope (`scene_name=` / `VizSceneHandle`), and auto-hide vs explicit removal
(`remove_banner(id)` / `clear_banners()`). Introduce `show_banner_async()` for
awaiting the push from an async handler.

**Visual Examples:** `banner_types.py` (every banner kind: acknowledge, custom
options, yes/no/cancel, modal).

---

## 16. Responsive Computation ✅

**Format:** Jupyter notebook

**Abstract:** Keep the viewer responsive while your script or handler does real work.
Explain why control handlers (which run on the server's event loop) must not block,
and the two flush tools for that: `flush_async()` (awaitable flush — guarantee pending
updates are rendered before blocking) and `flush(wait=True)` (blocking flush for plain
synchronous scripts; raises a clear `RuntimeError` on the server loop). Then cover
offloading computation to the user loop with `submit_user()` / `run_user()` /
`run_user_sync()` (and `Visualizer.run_blocking()` for scripts without
`VisualizerApp`), including the one-shot `done=` callback and the canonical pattern:
show a "Calculating…" banner, await it, run the work off-loop, then update the scene
and remove the banner in the done callback.

**Visual Examples:** `heavy_work.py` (a slider whose release shows a modal banner,
runs a 3 s computation off-loop, then updates the scene and removes the banner).

---

## 17. Export and Publishing ✅

**Format:** Jupyter notebook

**Abstract:** Export visualizations for sharing and publication. Generate
self-contained HTML files with `export_snapshot()` (with the embedded JS animation
engine), embeddable HTML / presentation figures with `export_figure()` and
`FigureStyle`, and glTF/GLB with `export_glb()` (the glTF/GLB entry point — there is no
`export_gltf`). Cover PNG screenshots (programmatic)
and MP4 video capture (still on the deprecated `SceneExporter`), the inline
`display_snapshot()` and standalone `open_snapshot()` previews, animated export via
`export_snapshot(..., animation=rec)` / `export_figure(..., animation=rec)` with
`start_animation_recording()` and the `AnimStyle` dataclass (`fps`, `loop`,
`show_controls`, `compress`), the keyboard shortcuts in exported figures (`Ctrl+S`, `r`),
and the `FigureConfig`/`export_figure()` pipeline for embedding in presentations.
Note that exports apply the full live-scene camera config (the default 2D view uses
an orthographic camera), and that animated exports capture the camera per frame —
`AnimationRecording` snapshots the scene camera each frame, so `set_camera()` inside
the animation loop is reflected in the exported animation.

---

## 18. Visualizing GA Entities and Operators ✅

**Format:** Jupyter notebook

**Abstract:** A basic bridge from visualization to geometric algebra. Show how raw
multivectors are accepted by `add()` and analyzed into entities on the way in (honoring
the algebra's `opns` flag), and how operators (`Rotor`, `Translator`, `Motor`,
`Reflection`, `Inversion`, `Dilator`) are rendered: `GeneralRotor` renders with the
same rotor visualization as `Rotor` (disc arc, torus, and axis line) displaced to its
origin, and `Motor` renders a displaced rotation (general rotor) plus a translation
arrow along the screw axis. This chapter intentionally stays
high-level: it describes *what* gets drawn and how to point it at the viewer. For the
meaning of the underlying blades, the OPNS/IPNS distinction, and how to construct
entities/operators, see
[Part II — Geometry Submodule](../algebra/tutorial_overview.md) and the individual
algebra chapters there.

---

## 19. SDF Viewer (SdfVisualizer) ✅

**Format:** Jupyter notebook

**Abstract:** Introduce the dedicated, fullscreen ray-marched viewer
`pytanga.viz.sdf.SdfVisualizer`. **Note:** this is an early-stage, experimental
rendering path — it does not yet support the full `Visualizer` feature set (WebGL2
only, 3D only), so treat it as a playground for SDF ideas; the supported,
feature-rich route for SDF objects is [Chapter 3](#3-sdf-objects-in-the-standard-viewer).
Cover the quick start (`SdfVisualizer` + `add()` + `show()`/`wait()`), the SDF
primitive library (`sphere`, `box`, `cylinder`, `capped_cylinder`, `cone`,
`capped_cone`, `torus`, `ellipsoid`, `round_box`, `capsule`, `segment`, `plane`,
`bound_box`), the `Composed` object bundling constituents with per-constituent
combine modes, per-object CSG (`combine=`/`polarity=` union/intersection/subtract
and their smooth variants with a `smoothness` knob), the automatic
entity/operator→SDF mapping (`Point`→sphere, `Line`→segment, `Rotor`→disc+ring+axis,
…), configurable lighting (`DirectionalLight`, `add_default_light`,
`set_ambient_light()`), shader-drawn `Grid`/`Axes` overlays, and the simple update
loop (`update_entity()` / `update_light()` / `flush()` / `sleep_ms()`). Note: the
1.6/1.7 per-object SDF additions (the extra viz-only entities, the
`partialDisk`/`regularPolygon` primitives, and `SdfStyle.antialias`) live in the
*standard* viewer's SDF path ([Chapter 3](#3-sdf-objects-in-the-standard-viewer));
this fullscreen viewer is unchanged.

**Visual Examples:** `entities.py` (line + sphere − sphere), `booleans.py`
(per-object combine modes), `composed.py` (primitive library + `Composed` + entity
mapping), `light_animation.py` (moving light).