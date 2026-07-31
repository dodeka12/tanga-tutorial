# tanga-tutorial

Tutorials and examples for the [TanGA](https://github.com/dodeka12/tanga) geometric algebra library.

## Prerequisites

- **Python 3.12+** (see `.python-version`)
- **C++ compiler** — TanGA compiles C++ bindings on first use. You need a working compiler toolchain:
  - **Linux:** install `g++` or `clang++` via your package manager (e.g. `sudo apt install g++` on Debian/Ubuntu)
  - **macOS:** Xcode Command Line Tools (`xcode-select --install`) will provide `clang++`
  - **Windows:** TanGA does not support native Windows builds. Use **[WSL](#windows-users-wsl)** (see below)
- **[uv](https://docs.astral.sh/uv/)** — the fast Python package and project manager
- **TanGA source** — this repo expects the `tanga` repository to be cloned at `../tanga` (sibling directory)

### Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or via your system package manager.

### Clone the repositories

```bash
git clone https://github.com/dodeka12/tanga.git
git clone https://github.com/dodeka12/tanga-tutorial.git
```

Your directory layout should look like:

```
├── tanga/            # The TanGA library
└── tanga-tutorial/   # This repository
```

### Windows users (WSL)

TanGA's C++ compilation toolchain requires a Unix-like environment. Windows users should use
**Windows Subsystem for Linux (WSL)**:

1. **Install WSL** (PowerShell as Administrator):
   ```powershell
   wsl --install
   ```
   This installs Ubuntu by default. Restart your computer if prompted.

2. **Launch Ubuntu** from the Start menu. Create your Linux user and password on first launch.

3. **Install prerequisites** inside WSL/Ubuntu:
   ```bash
   sudo apt update
   sudo apt install g++ python3 python3-pip git curl
   ```

4. **Install uv** and clone the repositories as described above — all inside the WSL terminal.

All subsequent `uv sync`, examples, and tutorials should be run from within WSL.

## Setup

From the `tanga-tutorial` directory, run:

```bash
# Create a virtual environment, install all dependencies, and link to tanga-py in editable mode
uv sync
```

This installs:

  - **tanga-py** — linked in editable mode from `../tanga`
  - **jupyter**, **ipykernel**, **ipython** — for running the tutorials
  - **scipy** — for optional numeric utilities

> **Note:** the first time you use `tanga`, the C++ binding for your algebra will be compiled (~5–20 s). Subsequent uses load the cached binary (~ms).

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
