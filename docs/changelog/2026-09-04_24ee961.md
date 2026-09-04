# Changes since version 0.1.1

## New Features

- **Tutorials updated to pytanga 1.17.0** — the notebooks now cover the new
  `DataArray` batches and counting-axis reduction, UI menus and dialogs, themes,
  random multivector generation (`RndMV`), split views, and controls.
- **pytanga version shown on the landing page** — the version the tutorials are
  built against lives in a single `extra.tanga_version` marker in `mkdocs.yml`
  and is injected into pages at build time.
- **tanga-py source switcher** — `tools/switch_tanga.py` flips the `tanga-py`
  dependency between the release, rc, and source builds in a single
  `pyproject.toml`.

## Breaking Changes

- **Tutorials now target pytanga 1.17.0** — chapters were rewritten to match the
  removed or changed APIs (`project_onto`, `open_browser`/`host`/`port`, integer
  variable labels, batched evaluation), so the examples no longer run unchanged
  against older pytanga releases.

## Bug Fixes

- **Inline visualizations** — fixed the inline visualization rendering.
- **`DataArray` mask ordering** — corrected the docs: `masks` follow the array's
  dimension order, and the blade axis is not necessarily first.

## Refactor

- **Examples folder removed** — the standalone `examples/` scripts were dropped;
  the notebooks are the single source of truth.
- **Navigation** — "Geometric Algebra" and "Visualization" were promoted to the
  top-level nav.
