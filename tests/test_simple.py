import pytest


@pytest.mark.sphinx(
    "html",
    freshenv=True,
    confoverrides={"gitstamp_fmt": "%b %d, %Y"},
)
def test_simple(app, status, warning):
    app.warningiserror = True
    app.build()
    assert "bar.html" in app.outdir.listdir()
