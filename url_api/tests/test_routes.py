def test_healthcheck(test_server):
    result = test_server.head("/healthcheck")

    assert result.status_code == 200


def test_redirect_short_url_exists(test_server):
    result = test_server.get("/this_url_does_exist")
    assert result.status_code == 302


def test_redirect_short_url_not_exists(test_server):
    result = test_server.get("/this_url_does_not_exist")
    assert result.status_code == 404
