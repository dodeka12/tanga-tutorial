# Workflow: Update Tutorials to a New pytanga Version

How to bring the tutorials up to date with a new `tanga-py` (pytanga) release:
refresh the vendored docs/examples, read the changelogs since the last update,
write a plan describing what must change, and author this repo's changelog for
the update.

## Steps

1. **Set the target version** — switch `tanga-py` to the new version with
   `uv run python tools/switch_tanga.py release|rc`, then edit the version
   constraint inside the active block in `pyproject.toml` to the exact target
   (e.g. `>=1.18.0` or `>=1.18.0rc1`). Run `uv sync --group dev`.

2. **Refresh vendored docs + examples** — install the new pytanga's packaged
   docs and examples into the gitignored `.dep-docs/pytanga/` and
   `.dep-examples/pytanga/` directories:

   ```bash
   uv run python -c "import pytanga; pytanga.install_docs(); pytanga.install_examples()"
   ```

3. **Enumerate the changelogs since the last update** — open
   `.dep-docs/pytanga/changelog/index.md` (newest-first) and list every entry
   whose "since" version is ≥ the current `extra.tanga_version` marker. Do not
   analyze them yet — just collect the ordered list of changelog files.

4. **Create the plan first** — create `dev/todos/pytanga_sync_YYYY-MM-DD.md`
   with **one step per changelog** (read one changelog → analyze → record) plus a
   final **consolidation** step, using the "Plan template" below.

5. **Execute the plan step by step** — one changelog per step: read the changelog,
   record its per-changelog analysis (`### vX.Y.Z` section), mark the step done.
   Then run the consolidation step to merge all analyses into the **unified update
   list** ("Consolidated template"). Stop after the consolidated list is written so
   it can be reviewed **before** any notebook is edited.

6. **Update the version marker** — after the tutorial edits are approved and
   applied, set `extra.tanga_version` in `mkdocs.yml` to the new version. The
   landing page (and any other page carrying the `{{ tanga_version }}` placeholder)
   picks it up automatically at build time. Do **not** edit the landing page or any
   notebook by hand.

7. **Create the changelog** — author this repo's branch changelog at
   `docs/changelog/YYYY-MM-DD_<branch-name>.md` (create the directory if this is
   the first changelog), following `dev/workflows/changelog.md`. Headline the
   entry as the tutorial update to the new pytanga version, and fill the sections
   that apply — e.g. `New Features` for newly documented APIs, `Breaking Changes`
   for chapters rewritten to match removed/changed APIs, `Bug Fixes` for wrong
   docs or examples corrected, `Refactor` for renumbering/reorganization. The
   changelog is finalized (renamed to its hash form + indexed) at PR time — see
   `dev/workflows/pull-request.md`.

8. **Validate**:

   ```bash
   uv run mkdocs build --strict
   uv run python tools/execute_notebooks.py --dry-run
   ```

   Re-execute affected notebooks with `uv run python tools/execute_notebooks.py`
   if their saved outputs need refreshing.

## Version marker

- The pytanga version the tutorials are built against lives in a single place:
  `mkdocs.yml` → `extra.tanga_version`.
- `docs/_hooks/inject_tanga_version.py` replaces the `{{ tanga_version }}`
  placeholder in rendered pages with that value, so the landing page always
  shows the marker without a second hand-edited copy.
- When updating, change only `extra.tanga_version`; never hard-code a pytanga
  version in a notebook or elsewhere in the repo.

## Report templates

### Plan template

`dev/todos/pytanga_sync_YYYY-MM-DD.md` starts as a plan — one step per changelog
plus a final consolidation step:

```markdown
# pytanga Sync — YYYY-MM-DD (<old> → <new>)

| # | Version | Changelog file | Since | Scope |
|---|---------|----------------|-------|-------|
| 1 | <ver> | `YYYY-MM-DD_<hash>.md` | <since> | <one-line scope> |

## Steps

- [ ] 1. Read `.dep-docs/pytanga/changelog/<file>.md` (v<ver>) → record `### v<ver>`.
- [ ] … (one step per changelog)
- [ ] N. Consolidate → unified update list.

## Per-changelog analyses

(Each step appends its `### vX.Y.Z` section here.)
```

### Consolidated template

After all per-changelog steps are done, the consolidation step replaces the
per-changelog sections with a single summary. Follow the structure/level of detail
of the existing `viz_api_sync_*.md` / `tutorial_*_sync_*.md` reports:

```markdown
# pytanga Sync — YYYY-MM-DD Changelog (<version>)

Driven by the changelog(s) that postdate the last sync:

| Changelog | Version | Content |
|-----------|---------|---------|
| `YYYY-MM-DD_<hash>.md` ("Since X.Y.Z") | v<version> | one-line summary |

One-paragraph summary: core-algebra changes? breaking? viz-only? …

## Authoritative changelog deltas

| Area | Change |
|------|--------|
| New / Breaking / Changed / Fixed | concise, self-contained line |

## 1. Adapt existing chapters

| Chapter | Change |
|---------|--------|

## 2. New chapters

## 3. Renumbering

## 4. Parent overview + Part I

## 5. Validation

- Grep the plans for `#…` anchors; confirm chapter numbers are consistent.
- Confirm new API names match the installed surface.
- Note which existing notebooks need no changes.
```

## Hard rule — never guess

If a changelog, API, or example is ambiguous, stop and ask a specific question.
Do not assume or invent details.
