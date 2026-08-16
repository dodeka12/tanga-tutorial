# TanGA Tutorial Series — Part II: Visualization

This plan teaches the **`pytanga.viz` viewer** from scratch — no geometric-algebra
(GA) background required. It covers everything the viewer can do: building scenes,
styling, axes/grid/camera, labels, object interaction, animation, and export.

Visualization inputs are drawn from `pytanga.geometry` dataclasses (`Point`,
`Direction`, `Line`, `Plane`, `Sphere`, `Circle`, `PointPair`, …) used as **plain 3D
data**. A reader can follow the entire part without knowing anything about
multivectors or algebras. The final chapter introduces how GA entities and operators
are visualized, but only at a basic level — it defers the GA theory to
[Part I — Geometric Algebra & Core](../algebra/tutorial_overview.md).

The companion plan is [Part I — Geometric Algebra & Core](../algebra/tutorial_overview.md),
which covers the algebra, basis classes, geometry submodule, and numerical tooling.

---

## Conventions (shared with Part I)

- Entities passed to the viewer are geometry dataclasses from `pytanga.geometry`
  (or raw multivectors, which are analyzed on the way in — see
  [Chapter 9](#9-visualizing-ga-entities-and-operators)).
- Styles are passed to `add()` as `style=...`, as a `color=`/`opacity=` shortcut, or
  configured once via `default_styles`.
- Grid and axes are explicit scene objects (`Axis`, `Grid`, `Axes2D`, `Axes3D`);
  a default set is inserted per scene unless disabled with `add_default_axes=False`
  / `add_default_grid=False`.

---

## 1. Getting Started with the Viewer

**Format:** Jupyter notebook

**Abstract:** Create a `Visualizer` (3D by default; 2D with `space_dim=2`), add a few
plain entities (`Point`, `Line`, `Sphere`) via `add()`, and open the interactive
Three.js viewer with `run()`. Cover the two run modes — blocking `run()` vs
non-blocking `start()`/`flush()`/`stop()` — plus browser tab reuse
(`reuse_existing`), `wait_for_browser`, and the `Ctrl+S` screenshot shortcut.

---

## 2. Interactive Scenes and Multi-Scene Management

**Format:** Jupyter notebook

**Abstract:** Work with scenes. Add to the main scene, create named scenes with
`viz.scene(name)`, and manage each through `VizSceneHandle`. Cover multi-scene URLs,
browser navigation (`navigate_to()`), `list_browsers()`, viewer identity
(`?viewer=` URL parameter), and side-by-side Jupyter display with `display_row()`.
Cover the scene lifecycle (`add`, `update`, `remove`, `clear`, `flush`) and the
`update_style()` method for changing style properties without rebuilding geometry.

---

## 3. Styles and Colors

**Format:** Jupyter notebook

**Abstract:** Style entities with the per-type style dataclasses (`PointStyle`,
`LineStyle`, `PlaneStyle`, `SphereStyle`, `CircleStyle`, …) and the `Color` enum.
Explain the color/opacity precedence (`add(color=...)` → `style=...` →
`default_styles`), the `default_styles` override mechanism, and how to set
`default_label_style`. Cover opacity, wireframe rendering, point size, and screen-space
line thickness.

---

## 4. Axes, Grid, and Camera

**Format:** Jupyter notebook

**Abstract:** Control scene framing and reference geometry. Cover the `Axis`, `Grid`,
`Axes2D`, and `Axes3D` scene objects (value labels, styling via `AxisStyle` /
`GridStyle` / `Axes2DStyle` / `Axes3DStyle`) and the default axes+grid behaviour
(`add_default_axes` / `add_default_grid`). Cover camera configuration in depth:
auto-fit (`flush(fit_camera=True)`), explicit `CameraConfig3d`, the `View2DConfig` /
`View3dConfig` input specs and their builders (`get_camera_view2d()`,
`get_camera_view3d()`, `get_camera()`), and runtime updates via `set_camera()`.
Explain orbit controls in 3D vs 2D mode.

---

## 5. Labels, Titles, and Annotations

**Format:** Jupyter notebook

**Abstract:** Enhance visualizations with `Label` dataclasses (local-frame
positioning, custom `LabelStyle`, dynamic `update_label()`), title overlays, and
Markdown annotation panels with LaTeX math (rendered via KaTeX). Show how to combine
clear labelling with geometric content for presentation-ready figures.

---

## 6. Object Interaction and Active Objects

**Format:** Jupyter notebook

**Abstract:** Make scenes interactive. Use the pointer-event system
(`InteractionConfig` / `InteractionTrigger` / `InteractionEventType`, `MouseButton`,
`ModifierKey`, `DragMode`) and register handlers with `set_interaction()` /
`on_interaction()`. Cover the event dataclasses (`ClickEvent`, `DragEvent`,
`ScrollEvent`) and the attached `Camera` (world↔screen `project()` / `unproject()`).
Introduce the active scene objects (`ActSceneObject`, `ActPoint`) with their styles
(`ActObjectStyle`, `ActPointStyle`) as a simplified high-level API for common
drag/interaction patterns.

---

## 7. Animation

**Format:** Jupyter notebook

**Abstract:** Animate geometric constructions. Use `PointPath` for connected line
segments, object trails, per-point colors, and FIFO capping with gradient utilities.
Use frame streaming for high-FPS animations (orbiting entities, physics simulations),
keyframe tweening with `animate_to`, and the scene-aware `Timeline` sequencer for
choreographed multi-entity animations (fade-in, move, rotate). Build an interactive
`VisualizerApp` subclass with sliders, dropdowns, buttons, and layout groups.

---

## 8. Export and Publishing

**Format:** Jupyter notebook

**Abstract:** Export visualizations for sharing and publication. Generate
self-contained HTML files (with the embedded JS animation engine), embeddable HTML for
iframes, glTF/GLB for use in other 3D tools, PNG screenshots (programmatic), MP4 video
capture, and presentation figures with `FigureStyle` and `SceneExporter`. Cover
animated HTML export with the `AnimStyle` dataclass (`fps`, `loop`, `show_controls`,
`compress`), the keyboard shortcuts in exported figures (`Ctrl+S`, `r`), and the
`FigureConfig`/`export_figure()` pipeline for embedding in presentations.

---

## 9. Visualizing GA Entities and Operators

**Format:** Jupyter notebook

**Abstract:** A basic bridge from visualization to geometric algebra. Show how raw
multivectors are accepted by `add()` and analyzed into entities on the way in (honoring
the algebra's `opns` flag), and how operators (`Rotor`, `Translator`, `Motor`,
`Reflection`, `Inversion`, `Dilator`) are rendered. This chapter intentionally stays
high-level: it describes *what* gets drawn and how to point it at the viewer. For the
meaning of the underlying blades, the OPNS/IPNS distinction, and how to construct
entities/operators, see
[Part I — Geometry Submodule](../algebra/tutorial_overview.md) and the individual
algebra chapters there.