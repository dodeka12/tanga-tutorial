# Visualization Tutorials

Part I of the TanGA tutorial series teaches the **`pytanga.viz` viewer** from
scratch — no geometric-algebra background required. The tutorials cover building
scenes, styling, axes/grid/camera, labels, object interaction, animation,
controls, banners/dialogs, responsive computation, and export, plus the viewer's
two rendering paths: the standard mesh pipeline and an opt-in ray-marched
signed-distance-field (SDF) path.

Visualization inputs are drawn from `pytanga.geometry` dataclasses (`Point`,
`Direction`, `Line`, `Plane`, `Sphere`, `Circle`, `PointPair`, …) used as **plain
3D data**.

## Tutorials

| # | Tutorial | Topic |
|---|----------|-------|
| 01 | [Quick Tour](01_quick_tour/) | A glance at every viewer capability |
| 02 | [Getting Started](02_getting_started/) | `Visualizer`, `add()`, `show()`, run modes |
| 03 | [SDF Objects](03_sdf_objects/) | Ray-marched solids in the standard viewer |
| 04 | [Multi-Scene](04_multi_scene/) | Named scenes and `VizSceneHandle` |
| 05 | [Scene Graphs](05_scene_graphs/) | `VizGroup`, `VizObjectRef`, transforms |
| 06 | [Styles & Colors](06_styles_colors/) | Per-type style dataclasses and defaults |
| 07 | [Axes, Grid & Camera](07_axes_grid_camera/) | `Axis`/`Grid`/`Axes2D`/`Axes3D`, camera config |
| 08 | [Coordinate System](08_coordinate_system/) | Plotting with `CoordinateSystem` |
| 09 | [Labels](09_labels/) | Labels, titles, annotations, KaTeX |
| 10 | [Interaction](10_interaction/) | Pointer events and `ActPoint` |
| 11 | [Animation](11_animation/) | `animate()`, `PointPath`, `animate_to`, `Timeline` |
| 12 | [Split Views](12_split_views/) | `SplitView`/`SceneView`/`GroupView` layouts |
| 13 | [Interactive Apps](13_visualizer_app/) | The `VisualizerApp` lifecycle |
| 14 | [Controls](14_controls/) | Every control type and `open_editor()` |
| 15 | [Banners & Dialogs](15_banners_dialogs/) | `alert()`/`confirm()`/`show_banner()` |
| 16 | [Responsive Computation](16_responsive_computation/) | `flush_async()`, `submit_user()` |
| 17 | [Export](17_export/) | HTML, figures, glTF/GLB, screenshots, video |
| 18 | [GA Entities](18_ga_entities/) | Visualizing multivectors and operators |
| 19 | [SDF Viewer](19_sdf_viewer/) | The experimental `SdfVisualizer` |

## Prerequisites

- **Part II — Geometric Algebra** (`../algebra/`) is *not* required to
  follow this part; the GA-entities bridge (tutorial 18) is the only place that
  touches multivectors, and it defers the theory to Part II.
- Python 3.10+ with `pytanga` and `aiohttp` installed. Three.js, KaTeX, and
  `marked` load from a CDN in the browser — no frontend build step.

## Running the notebooks

Each folder contains a self-contained `.ipynb`. Open one in Jupyter (or the MyST
book) and run the cells top-to-bottom. In a notebook, `show()` renders the
viewer inline; use `export_snapshot()` / `display_snapshot()` for a static,
serverless preview without a browser.
