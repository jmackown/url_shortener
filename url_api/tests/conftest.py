import pytest
import fakeredis
from flask import Flask


from url_api.app import create_app, resources

mock_redis_server = fakeredis.FakeServer()


class LocalTestingConfig:
    BASE_URL = "http://www.fakeurl.com"


redis_test_data = {
    "this_url_does_exist": "a_real_url",
    "this_url_does_exist_2": "a_real_url",
    "this_url_does_exist_3": "a_real_url",
}


@pytest.fixture(scope="session")
def test_app(*args, **kwargs):

    app = create_app(Flask, config=LocalTestingConfig)

    routes = [str(p) for p in app.url_map.iter_rules()]
    print(f"routes: {routes}")

    app.redis = fakeredis.FakeStrictRedis(charset="utf-8", decode_responses=True)

    yield app


@pytest.fixture(scope="function")
def test_server(test_app):
    return test_app.test_client()


@pytest.fixture(scope="function")
def mock_create_short_url(monkeypatch):
    def predictable_short_url():
        return "qwertyuiop"

    monkeypatch.setattr(resources, "create_short_url", predictable_short_url)
