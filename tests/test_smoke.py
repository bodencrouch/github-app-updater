"""Smoke import test."""

def test_import():
    from github_app_updater import AppUpdate, RestartStrategy
    assert AppUpdate is not None
