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

# Or activate the venv and run directly
source .venv/bin/activate
python examples/basic_algebra.py
```

## Running Tutorials

```bash
# Start Jupyter in the tutorials directory
uv run jupyter notebook tutorials/
```

Then open `01_e3_basics.ipynb` in your browser.

## Repository Structure

```
├── examples/          # Standalone Python scripts
│   ├── basic_algebra.py   # E3 Euclidean algebra basics
│   └── pga3_intro.py      # PGA3 projective geometry intro
├── tutorials/         # Jupyter notebooks
│   └── 01_e3_basics.ipynb  # Interactive E3 tutorial
├── pyproject.toml     # Project metadata and dependencies
├── main.py            # Placeholder entry point
└── README.md
```

## Later: Installing tanga-py from PyPI

Once `tanga-py` is published on PyPI, you can switch from the editable path dependency to a PyPI version by editing `pyproject.toml`:

```toml
# Replace this:
[tool.uv.sources]
tanga-py = { path = "../tanga", editable = true }

# With:
dependencies = [
    "tanga-py>=0.1.0",
]
```
