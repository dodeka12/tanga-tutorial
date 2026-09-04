#!/usr/bin/env python3
"""Switch the tanga-py dependency source in pyproject.toml.

The single ``pyproject.toml`` stores every supported tanga-py configuration as
tagged blocks::

    # tanga:start:<name>
    <content lines (active = uncommented, inactive = '#'-prefixed)>
    # tanga:end:<name>

Each mode maps to a set of blocks that must be active; every other block is
commented out. Exactly one tanga-py dependency line is active at a time, so the
file always stays valid TOML. Edit the version constraints inside the blocks by
hand if you need a specific version.

Modes:
    release  PyPI release (default)
    rc       TestPyPI release candidate (prerelease allowed)
    src      editable local checkout at ../tanga

Usage:
    uv run python tools/switch_tanga.py release|rc|src
    uv run python tools/switch_tanga.py --show
    uv run python tools/switch_tanga.py --no-sync rc
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PYPROJECT = ROOT / "pyproject.toml"

START = re.compile(r"^\s*#\s*tanga:start:([\w-]+)\s*$")
END = re.compile(r"^\s*#\s*tanga:end:([\w-]+)\s*$")

MODE_BLOCKS = {
    "release": {"release"},
    "rc": {"rc", "rc-extra"},
    "src": {"src", "src-extra"},
}
EXPECTED_BLOCKS = {"release", "rc", "src", "rc-extra", "src-extra"}


def read_lines() -> list[str]:
    return PYPROJECT.read_text(encoding="utf-8").splitlines()


def parse_blocks(lines: list[str]) -> dict[str, tuple[int, int]]:
    blocks: dict[str, tuple[int, int]] = {}
    stack: list[tuple[str, int]] = []
    for idx, line in enumerate(lines):
        if (m := START.match(line)):
            stack.append((m.group(1), idx))
            continue
        if (m := END.match(line)):
            name = m.group(1)
            if not stack or stack[-1][0] != name:
                sys.exit(f"error: unbalanced 'tanga:end:{name}' at line {idx + 1}")
            _, start_idx = stack.pop()
            blocks[name] = (start_idx + 1, idx - 1)
    if stack:
        sys.exit(f"error: missing 'tanga:end:{stack[-1][0]}'")
    missing = EXPECTED_BLOCKS - set(blocks)
    extra = set(blocks) - EXPECTED_BLOCKS
    if missing or extra:
        sys.exit(
            f"error: unexpected tanga blocks "
            f"(missing={sorted(missing)} extra={sorted(extra)})"
        )
    return blocks


def block_is_active(lines: list[str], start: int, end: int) -> bool:
    return any(
        line.strip() and not line.lstrip().startswith("#")
        for line in lines[start : end + 1]
    )


def set_block_state(lines: list[str], start: int, end: int, active: bool) -> None:
    for i in range(start, end + 1):
        stripped = lines[i].lstrip()
        if not stripped:
            continue
        indent = lines[i][: len(lines[i]) - len(stripped)]
        if active:
            if stripped.startswith("#"):
                lines[i] = indent + re.sub(r"^# ?", "", stripped, count=1)
        elif not stripped.startswith("#"):
            lines[i] = indent + "# " + stripped


def switch(lines: list[str], mode: str) -> list[str]:
    blocks = parse_blocks(lines)
    active = MODE_BLOCKS[mode]
    for name, (start, end) in blocks.items():
        set_block_state(lines, start, end, name in active)
    return lines


def show(lines: list[str]) -> str:
    blocks = parse_blocks(lines)
    for mode in MODE_BLOCKS:
        if block_is_active(lines, *blocks[mode]):
            return mode
    sys.exit("error: could not determine the active tanga source mode")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("mode", nargs="?", choices=list(MODE_BLOCKS))
    parser.add_argument("--show", action="store_true", help="print the active mode and exit")
    parser.add_argument("--no-sync", action="store_true", help="skip 'uv sync --group dev'")
    args = parser.parse_args()

    lines = read_lines()

    if args.show:
        print(show(lines))
        return

    if not args.mode:
        parser.error("a mode is required unless --show is given")

    switch(lines, args.mode)
    PYPROJECT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"switched tanga-py source -> {args.mode}")

    if args.no_sync:
        print("note: run 'uv sync --group dev' to apply")
        return

    print("running: uv sync --group dev")
    raise SystemExit(subprocess.run(["uv", "sync", "--group", "dev"], cwd=ROOT).returncode)


if __name__ == "__main__":
    main()
