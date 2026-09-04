"""Inject the pytanga version into pages carrying the ``{{ tanga_version }}`` placeholder.

The version is read from ``mkdocs.yml`` -> ``extra.tanga_version`` (the single
source of truth). It is replaced in the final rendered HTML, so the landing page
always shows the version the tutorials are built against without a second
hand-edited copy.
"""


def on_post_page(output, page, config, **kwargs):
    version = config.extra.get("tanga_version", "")
    return output.replace("{{ tanga_version }}", version)
