# Start a local Jupyter server for Jupyter Book's in-page execution (Windows).
#
# The book's "power" button connects to this server, so it must be running
# before you press the button. It is configured to match `myst.yml`:
#   - port 8888
#   - token "tanga-local"
#   - CORS origin http://localhost:3000 (the `jupyter-book start` server)
#
# Usage (PowerShell):
#   & .\scripts\serve-local.ps1

$ErrorActionPreference = "Stop"

# Resolve the project's virtualenv, preferring it over a bare `jupyter-lab` on
# PATH so the script works when invoked directly.
$REPO_ROOT = Split-Path -Parent $PSScriptRoot
$JUPYTER = Join-Path $REPO_ROOT ".venv\Scripts\jupyter-lab.exe"
if (-not (Test-Path $JUPYTER)) {
    $JUPYTER = "jupyter-lab"
}

& $JUPYTER `
  --no-browser `
  --ServerApp.port=8888 `
  --IdentityProvider.token=tanga-local `
  --ServerApp.allow_origin=http://localhost:3000
