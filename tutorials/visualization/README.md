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
| 02 | [Use Cases & Updating the Scene](02_use_cases/) | Which method to use when; adding/updating objects |
| 03 | [Jupyter Notebooks](03_jupyter/) | Live and static inline display, notebook workflows |
| 04 | [Getting Started](04_getting_started/) | `Visualizer`, `add()`, `show()`, run modes |
| 05 | [SDF Objects](05_sdf_objects/) | Ray-marched solids in the standard viewer |
| 06 | [Multi-Scene](06_multi_scene/) | Named scenes and `VizSceneHandle` |
| 07 | [Scene Graphs](07_scene_graphs/) | `VizGroup`, `VizObjectRef`, transforms |
| 08 | [Styles & Colors](08_styles_colors/) | Per-type style dataclasses and defaults |
| 09 | [Axes, Grid & Camera](09_axes_grid_camera/) | `Axis`/`Grid`/`Axes2D`/`Axes3D`, camera config |
| 10 | [Coordinate System](10_coordinate_system/) | Plotting with `CoordinateSystem` |
| 11 | [Labels](11_labels/) | Labels, titles, annotations, KaTeX |
| 12 | [Interaction](12_interaction/) | Pointer events and `ActPoint` |
| 13 | [Animation](13_animation/) | `animate()`, `PointPath`, `animate_to`, `Timeline` |
| 14 | [Split Views](14_split_views/) | `SplitView`/`SceneView`/`GroupView` layouts |
| 15 | [Interactive Apps](15_visualizer_app/) | The `VisualizerApp` lifecycle |
| 16 | [Controls](16_controls/) | Every control type and `open_editor()` |
| 17 | [Banners & Dialogs](17_banners_dialogs/) | `alert()`/`confirm()`/`show_banner()` |
| 18 | [Responsive Computation](18_responsive_computation/) | `flush_async()`, `submit_user()` |
| 19 | [Export](19_export/) | HTML, figures, glTF/GLB, screenshots, video |
| 20 | [GA Entities](20_ga_entities/) | Visualizing multivectors and operators |
| 21 | [SDF Viewer](21_sdf_viewer/) | The experimental `SdfVisualizer` |

## Prerequisites

- **Part II — Geometric Algebra** (`../algebra/`) is *not* required to
  follow this part; the GA-entities bridge (tutorial 20) is the only place that
  touches multivectors, and it defers the theory to Part II.
- Python 3.10+ with `pytanga` and `aiohttp` installed. Three.js, KaTeX, and
  `marked` load from a CDN in the browser — no frontend build step.

## Running the notebooks

Each folder contains a self-contained `.ipynb`. Open one in Jupyter (or the MyST
book) and run the cells top-to-bottom. In a notebook, `show()` renders the
viewer inline; use `export_snapshot()` / `display_snapshot()` for a static,
serverless preview without a browser.
