# tanga-tutorial

Tutorials and examples for the [TanGA](https://github.com/dodeka12/tanga) geometric algebra library.

## Prerequisites

- **[uv](https://docs.astral.sh/uv/)** — the fast Python package and project manager. It also
  installs the required Python version for you (see `.python-version`).

## Compiler setup (optional)

pytanga ships precompiled bindings for the standard algebra configurations and works out of
the box on **Linux**, **macOS**, and **Windows** — no C++ compiler needed. A compiler is only
required if you need an algebra configuration not covered by the precompiled set (e.g. a
custom dimension or signature).

### Linux

Install `g++` or `clang++` via your package manager:

```bash
# Debian / Ubuntu
sudo apt install g++
```

### macOS

Install the Xcode Command Line Tools (provides `clang++`):

```bash
xcode-select --install
```

### Windows

Native Windows is fully supported. Install the **Microsoft Visual C++ (MSVC)** toolchain:

1. Download **Build Tools for Visual Studio 2022** from the
   [Visual Studio downloads page](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022)
   (scroll past the full IDE editions to the **"Tools for Visual Studio"** section).
2. Run the installer and select the **"Desktop development with C++"** workload.
3. Run all `uv` / `pip` commands from the **"Developer Command Prompt for VS 2022"**.

Alternatively, you can use **Windows Subsystem for Linux (WSL)**:

1. Install WSL from an Administrator PowerShell:
   ```powershell
   wsl --install -d Ubuntu
   ```
2. Open the Ubuntu terminal and follow the [Linux](#linux) instructions above
   (install `g++`), then continue with the setup steps below.

## Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or via your system package manager.

## Clone the repository

```bash
git clone https://github.com/dodeka12/tanga-tutorial.git
cd tanga-tutorial
```

## Setup

From the `tanga-tutorial` directory, run:

```bash
# Create a virtual environment and install all dependencies
uv sync
```

This installs:

  - **tanga-py** (pytanga) — the TanGA Python package, including its `compile` and `examples` extras
  - **jupyter**, **ipykernel**, **ipython** — for running the tutorials
  - **scipy** — for optional numeric utilities

> **Note:** with the precompiled wheels, imports are instant and no compilation happens.
> The C++ binding for your algebra is only compiled on first use if you request an algebra
> configuration not covered by the precompiled set (~5–20 s); subsequent uses load the
> cached binary (~ms).

## Running Examples

```bash
# Run a single example script
uv run python examples/basic_algebra.py
uv run python examples/pga3_intro.py
uv run python examples/pga3_visualizer.py

# Or activate the venv and run directly
source .venv/bin/activate
python examples/basic_algebra.py
```

## Running Tutorials

```bash
# Start Jupyter in the tutorials directory
uv run jupyter-notebook tutorials/    # classic Notebook
uv run jupyter-lab tutorials/         # JupyterLab
```

> **Windows note:** `uv run jupyter notebook ...` can fail with
> `program not found` if the `jupyter` dispatcher shim is missing from
> `.venv\Scripts`. Use `jupyter-notebook` / `jupyter-lab` directly (above), or
> regenerate the shim with `uv pip install --reinstall jupyter-core`.

The tutorials are split into two parts, each numbered from `01`:

- `tutorials/algebra/` — **Part II · Geometric Algebra**
  (`01_quick_tour` … `17_visualizing_algebra_entities`).
- `tutorials/visualization/` — **Part I · Visualization**
  (`01_quick_tour` … `21_sdf_viewer`).

Open a notebook (e.g. `tutorials/algebra/02_algebra_core/02_algebra_core.ipynb` or
`tutorials/visualization/01_quick_tour/01_quick_tour.ipynb`) in your browser. The
full tutorial-series plan lives in `dev/todos/`.

## Documentation (MkDocs)

The tutorials are rendered as a site with **Material for MkDocs** +
**mkdocs-jupyter**, versioned and published to GitHub Pages with **mike** (the
same setup as the sibling [`tanga`](https://github.com/dodeka12/tanga) repo).
Configuration lives in the root `mkdocs.yml`.

### Preview locally

```bash
uv sync --group dev
uv run mkdocs serve       # http://localhost:8000 with live reload
```

To produce a static build (e.g. for a CI check):

```bash
uv run mkdocs build --strict
```

The build copies `tutorials/` and `examples/` into `docs/` (via
`docs/_hooks/copy_content.py`), so the notebook/script pages render from the
root-level sources. Notebooks are rendered **as saved** (`execute: false`), so no
kernel or tanga compilation is needed to build the site.

> **Live cells.** Cells that use `viz.show()`, `start_server()`, `viz.run()`, or
> `viz.wait()` open a **live** viewer/server and can only run interactively in
> Jupyter — their output is not shown in the static site. Because the build runs
> with `execute: false`, these cells are never executed during `mkdocs build`, so
> they can't hang or block the build. Readers run those cells live (e.g. via the
> **Open in Colab** / **Launch Binder** buttons).

### Deploy to GitHub Pages

Deployment is handled by the GitHub Actions workflows in `.github/workflows/`:

- `docs.yml` — on push to `main`, bumps the version (Conventional Commits →
  semver via `tools/version-tag.sh`), tags it, and deploys the docs for that
  version via `mike deploy` + `mike set-default` (updating the `latest` alias).
  Manual `workflow_dispatch` re-deploys the current version without bumping.
- `docs-preview.yml` — manual (`workflow_dispatch`) branch preview under
  `dev-<branch>/`.

The package version is dynamic (hatch-vcs derives it from the latest git tag).
Docs versions are managed by **mike** (git tags → versioned subdirectories on
`gh-pages`).

Set **GitHub Pages → Source** to **"Deploy from a branch"**, branch **`gh-pages`**,
folder **`/ (root)`**. `mike` pushes the built site to that branch (with a
`.nojekyll` file so Jekyll is bypassed). The published URL is
`https://dodeka12.github.io/tanga-tutorial/`.

> **First deploy:** push to `main` (or run `docs.yml` manually once) — this
> creates the `gh-pages` branch — then point Pages at it.

Each notebook page has **Open in Colab** / **Launch Binder** buttons (from
`docs/overrides/main.html`). Binder builds its environment from the root
`requirements.txt`.

## Repository Structure

```
├── examples/            # Standalone Python scripts
│   ├── basic_algebra.py     # E3 Euclidean algebra basics
│   ├── pga3_intro.py        # PGA3 projective geometry intro
│   └── pga3_visualizer.py   # PGA3 viewer demo
├── tutorials/           # Jupyter notebooks
│   ├── algebra/             # Part II — Geometric Algebra
│   └── visualization/       # Part I — Visualization
├── docs/                # MkDocs site (index, overrides, hooks)
├── mkdocs.yml           # MkDocs configuration
├── .github/workflows/   # Docs deploy / preview workflows
├── tools/version-tag.sh # Conventional Commits → semver version bump
├── tanga_tutorial/      # Metadata-only package (hatch-vcs dynamic version)
├── dev/todos/           # Tutorial-series plans
├── .dep-docs/           # Upstream pytanga documentation
├── .dep-examples/       # Upstream pytanga examples
├── pyproject.toml       # Project metadata and dependencies
└── README.md
```
