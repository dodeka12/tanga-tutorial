#!/usr/bin/env bash
# Start a local Jupyter server for Jupyter Book's in-page execution.
#
# The book's "power" button connects to this server, so it must be running
# before you press the button. It is configured to match `myst.yml`:
#   - port 8888
#   - token "tanga-local"
#   - CORS origin http://localhost:3000 (the `jupyter book start` server)
#
# Usage:
#   uv run scripts/serve-local.sh     # or: ./scripts/serve-local.sh
set -euo pipefail

# Resolve the project's virtualenv, preferring it over a bare `jupyter` on PATH
# so the script works both with `uv run` and when invoked directly.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
JUPYTER="${REPO_ROOT}/.venv/bin/jupyter"
if [ ! -x "$JUPYTER" ]; then
  JUPYTER="jupyter"
fi

exec "$JUPYTER" lab \
  --no-browser \
  --ServerApp.port=8888 \
  --IdentityProvider.token=tanga-local \
  --ServerApp.allow_origin=http://localhost:3000