def test_healthcheck(test_server):
    result = test_server.head("/healthcheck")

    assert result.status_code == 200
