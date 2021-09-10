def test_healthcheck(test_server):
    result = test_server.head("/healthcheck")

    assert result.status_code == 200


def test_redirect_short_url_exists(test_server):
    result = test_server.get("/this_url_does_exist")
    assert result.status_code == 302


def test_redirect_short_url_not_exists(test_server):
    result = test_server.get("/this_url_does_not_exist")
    assert result.status_code == 404


def test_add_new_url(test_server, mock_create_short_url):
    test_data = {"long_url": "blah"}
    result = test_server.post("/add", json=test_data)
    assert result.json["original_url"] == test_data["long_url"]
    assert result.json["shortened_url"][-10:] == "qwertyuiop"

    assert result.status_code == 201
