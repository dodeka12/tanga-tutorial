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

- `tutorials/algebra/` — **Part I · Geometric Algebra & Core**
  (`01_quick_tour` … `17_visualizing_algebra_entities`).
- `tutorials/visualization/` — **Part II · Visualization**
  (`01_quick_tour` … `19_sdf_viewer`).

Open a notebook (e.g. `tutorials/algebra/02_algebra_core/02_algebra_core.ipynb` or
`tutorials/visualization/01_quick_tour/01_quick_tour.ipynb`) in your browser. The
full tutorial-series plan lives in `dev/todos/`.

## Documentation (Jupyter Book v2)

The tutorials are also rendered as a book with **Jupyter Book v2** (powered by the
MyST Document Engine — no Sphinx). Configuration lives in the root `myst.yml`.

### Preview the book locally

```bash
uv sync --group dev
uv run jupyter-book start       # serves http://localhost:3000 with live reload
```

The `start` command runs its own dev webserver; no separate static-site server is
needed. To produce a static HTML build (e.g. for CI checks):

```bash
uv run jupyter-book build --html --strict
cd _build/html 2>/dev/null || echo "see _build/ for build output"
```

### Run notebook cells live (self-contained, local by default)

Each notebook page exposes a power button for **in-page execution**. By default
`myst.yml` is configured for a **local Jupyter server** so everything runs
self-contained (no internet). The power button *connects to* an already-running
server — it does not launch one — so start the Jupyter server **first** (in a
separate terminal):

```bash
# Terminal 1 — the book (all platforms)
uv run jupyter-book start
```

**Linux / macOS** — Terminal 2 (kernel server):

```bash
uv run scripts/serve-local.sh
```

**Windows (PowerShell)** — Terminal 2 (kernel server):

```powershell
uv run jupyter-lab --no-browser --ServerApp.port=8888 --IdentityProvider.token=tanga-local --ServerApp.allow_origin=http://localhost:3000
# or, using the helper script:
# & .\scripts\serve-local.ps1
```

The helper scripts use port `8888`, token `tanga-local`, and allow CORS from
`http://localhost:3000` — matching `myst.yml` (`project.jupyter.server` and
`project.jupyter.kernelName: python3`). Without step 2, pressing the power button
will fail because there is no kernel server to connect to.

### Deploy to GitHub Pages (Binder-backed, later)

For the published site, in `myst.yml` uncomment `project.github` and the
`jupyter: true` line, and comment out the `jupyter.server` block. Then:

```bash
uv run jupyter-book init --gh-pages   # generates .github/workflows/deploy.yml
```

Enable **GitHub Pages → Source: GitHub Actions** in the repository settings. Live
execution then runs on Binder, which builds its environment from a root
`requirements.txt` (not `pyproject.toml`/`uv.lock`), so add one when enabling this.

> **Note:** in-page execution and the launch button are marked **beta** in Jupyter
> Book v2. JupyterLite (in-browser WASM) is **not** supported here because `tanga-py`
> ships compiled native extensions.

## Repository Structure

```
├── examples/            # Standalone Python scripts
│   ├── basic_algebra.py     # E3 Euclidean algebra basics
│   ├── pga3_intro.py        # PGA3 projective geometry intro
│   └── pga3_visualizer.py   # PGA3 viewer demo
├── tutorials/           # Jupyter notebooks
│   ├── algebra/             # Part I — Geometric Algebra & Core
│   └── visualization/       # Part II — Visualization
├── dev/todos/           # Tutorial-series plans
├── .dep-docs/           # Upstream pytanga documentation
├── .dep-examples/       # Upstream pytanga examples
├── myst.yml             # Jupyter Book v2 configuration
├── index.md             # Book landing page
├── pyproject.toml       # Project metadata and dependencies
└── README.md
```

## Installing tanga-py (TestPyPI → PyPI)

The project currently installs `tanga-py` (`0.11.0rc1`) from the **TestPyPI** index
via `[tool.uv.sources]`:

```toml
[project]
dependencies = [
    "tanga-py[compile,examples]==0.11.0rc1",
]

[tool.uv]
prerelease = "allow"

[tool.uv.sources]
tanga-py = { index = "testpypi" }

[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
explicit = true
```

Once `tanga-py` is published on PyPI, switch to a PyPI release by updating the
dependency and removing the `[tool.uv.sources]` entry:

```toml
[project]
dependencies = [
    "tanga-py[compile,examples]>=1.0.0",
]
```
