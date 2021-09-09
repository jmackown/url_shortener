import fakeredis

from url_api.tests.conftest import mock_redis_server


def test_healthcheck(test_server):
    result = test_server.head('/healthcheck')

    assert result.status_code == 200

