"""Copy the root tutorials/ into docs/ before the build."""

import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]   # docs/_hooks -> docs -> root
DOCS_DIR = REPO_ROOT / "docs"
_CONTENT = ("tutorials",)


def on_config(config, **kwargs):
    for name in _CONTENT:
        src = REPO_ROOT / name
        dst = DOCS_DIR / name
        shutil.rmtree(dst, ignore_errors=True)    # clear stale copies
        if src.is_dir():
            shutil.copytree(
                src,
                dst,
                ignore=shutil.ignore_patterns(
                    ".ipynb_checkpoints", "__pycache__", "*.pyc", ".git",
                    "README.md",
                ),
            )
