import pytest
import fakeredis
from flask import Flask

from url_api.app import create_app

mock_redis_server = fakeredis.FakeServer()


class LocalTestingConfig:
    BASE_URL = "http://www.fakeurl.com"


@pytest.fixture(scope="session")
def app(*args, **kwargs):

    app = create_app(Flask, config=LocalTestingConfig)

    routes = [str(p) for p in app.url_map.iter_rules()]
    print(f"routes: {routes}")

    app.redis = fakeredis.FakeStrictRedis()

    yield app


@pytest.fixture(scope="function")
def test_server(app):

    return app.test_client()
