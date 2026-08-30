"""Re-execute the tutorial notebooks in place to refresh their saved outputs.

The MkDocs site renders notebooks *as saved* (``mkdocs-jupyter`` is configured
with ``execute: false`` in ``mkdocs.yml``), so the outputs committed to each
``.ipynb`` file are exactly what the published docs display. Run this script
after changing a tutorial (or after a ``tanga-py`` update) to refresh those
outputs, then rebuild the site with ``uv run mkdocs build`` / ``serve``.

Notebooks whose top-level metadata carries ``requires_live_server: true`` open
a live viewer/server (``viz.show()``, ``start_server()``, ``viz.animate()``,
scene context managers, ``VisualizerApp`` ...). Those cells can only be run
interactively in Jupyter, so this script does **not** execute such notebooks:
it leaves them untouched and prints their paths so you can run them by hand.

Usage:
    uv run python tools/execute_notebooks.py                 # everything
    uv run python tools/execute_notebooks.py --dry-run       # preview the split
    uv run python tools/execute_notebooks.py tutorials/visualization/05_sdf_objects
    uv run python tools/execute_notebooks.py tutorials/algebra/01_quick_tour/01_quick_tour.ipynb

Options:
    --kernel NAME    Kernel to use (default: the notebook's own kernelspec).
    --timeout SECS   Per-cell timeout in seconds (default: no timeout).
    --strict         Raise on the first cell error instead of recording it.
    --dry-run        Print the manual/auto split without executing anything.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

# Key stored in a notebook's top-level ``metadata`` dict. Its presence means
# the notebook needs a running viewer/server and must be run interactively.
LIVE_TAG = "requires_live_server"

# Everything the docs render as a notebook: the tutorials plus the home page.
DEFAULT_PATHS = ("tutorials", "docs/index.ipynb")


def discover_notebooks(paths: list[str]) -> list[Path]:
    """Return the unique list of notebooks referenced by ``paths``.

    Each entry may be a directory (searched recursively for ``*.ipynb``) or a
    single notebook file. Results are sorted and de-duplicated.
    """
    notebooks: list[Path] = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            notebooks.extend(sorted(path.rglob("*.ipynb")))
        elif path.suffix == ".ipynb" and path.is_file():
            notebooks.append(path)
        else:
            print(f"warning: skipping {path} (not a notebook or directory)")

    seen: set[Path] = set()
    unique: list[Path] = []
    for path in notebooks:
        key = path.resolve()
        if key not in seen:
            seen.add(key)
            unique.append(path)
    return unique


def read_notebook(path: Path) -> "nbformat.NotebookNode":
    return nbformat.read(str(path), as_version=4)


def needs_live_server(nb: "nbformat.NotebookNode") -> bool:
    return bool(nb.metadata.get(LIVE_TAG, False))


def has_error_output(nb: "nbformat.NotebookNode") -> bool:
    """True if any code cell recorded an ``error`` output."""
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        for output in cell.get("outputs", []):
            if output.get("output_type") == "error":
                return True
    return False


def execute_notebook(
    path: Path,
    kernel_name: str,
    timeout: int | None,
    allow_errors: bool,
) -> "nbformat.NotebookNode":
    nb = read_notebook(path)
    client = NotebookClient(
        nb,
        kernel_name=kernel_name,
        timeout=timeout,
        allow_errors=allow_errors,
        store_widget_state=False,
    )
    client.execute()
    nbformat.write(nb, str(path))
    return nb


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Re-execute tutorial notebooks in place (skips live-server ones).",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=list(DEFAULT_PATHS),
        help="directories or notebook files to process "
        "(default: tutorials + docs/index.ipynb)",
    )
    parser.add_argument(
        "--kernel",
        default="",
        help="kernel name to use (default: the notebook's own kernelspec)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=None,
        help="per-cell timeout in seconds (default: no timeout)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="raise on the first cell error instead of recording and continuing",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the manual/auto split without executing anything",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    notebooks = discover_notebooks(args.paths)
    if not notebooks:
        print("No notebooks found.")
        return 1

    manual: list[Path] = []
    auto: list[Path] = []
    for path in notebooks:
        nb = read_notebook(path)
        (manual if needs_live_server(nb) else auto).append(path)

    print(
        f"Found {len(notebooks)} notebook(s): "
        f"{len(auto)} to execute, {len(manual)} to run manually.\n"
    )

    print("Run manually (need a live viewer/server):")
    if manual:
        for path in manual:
            print(f"  - {path}")
    else:
        print("  (none)")

    print("\nWill execute:")
    if auto:
        for path in auto:
            print(f"  - {path}")
    else:
        print("  (none)")

    if args.dry_run:
        return 0

    if not auto:
        print("\nNothing to execute.")
        return 0

    failed: list[Path] = []
    allow_errors = not args.strict
    for path in auto:
        print(f"\n==> {path}")
        try:
            nb = execute_notebook(path, args.kernel, args.timeout, allow_errors)
        except Exception as exc:  # noqa: BLE001 - report and keep going
            failed.append(path)
            print(f"    FAILED: {type(exc).__name__}: {exc}")
            continue
        if has_error_output(nb):
            failed.append(path)
            print("    (recorded one or more cell errors)")

    print("\n" + "=" * 60)
    print("Done.")
    print(f"  Executed: {len(auto) - len(failed)}/{len(auto)} notebook(s).")
    if failed:
        print("  With errors:")
        for path in failed:
            print(f"    - {path}")
    if manual:
        print("\n  Still need to be run by hand (live viewer/server):")
        for path in manual:
            print(f"    - {path}")
    print("=" * 60)

    return 0 if not failed else 2


if __name__ == "__main__":
    sys.exit(main())
