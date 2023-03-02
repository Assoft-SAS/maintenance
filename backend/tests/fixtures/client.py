import pytest

from app.main import app as localApp


@pytest.fixture()
def app():
    localApp.config.update({
        "TESTING": True,
    })

    yield localApp


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()