---
name: create-pr
description: Open a pull request for a feature/fix branch — build all docs and confirm no errors, finalize the branch changelog, then push and create the PR with the gh CLI. Use when the user asks to open, create, or submit a pull request (PR).
---

# Create PR

Open a pull request for a feature/fix branch: build all docs to confirm the
site is error-free, finalize the branch changelog, then push the branch and
create the PR with the `gh` CLI.

## Read the full workflow first

Read and follow `dev/workflows/pull-request.md` — it is the authoritative,
step-by-step procedure (doc-build validation, changelog finalization, PR body
temp file, and the `gh pr create` invocation).

## Procedure

1. Confirm the branch is fully committed locally.
2. Build all docs and require success: `uv run mkdocs build --strict`.
3. Rename the branch changelog (`docs/changelog/YYYY-MM-DD_<branch-name>.md`) to
   its hash-based final name and update the index link, then commit the rename.
4. Write the PR summary to a temp file, push the branch, and create the PR:
   `git push -u origin <branch>` and
   `gh pr create --title "<summary>" --body-file <temp-file>`.

## Repo conventions

- No pytest suite here — `uv run mkdocs build --strict` is the validation gate.
- Run Python/tools with `uv run ...` (never bare `python`).
- Follow `dev/workflows/changelog.md` for changelog content/naming.
