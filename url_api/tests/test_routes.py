def test_healthcheck(test_server):
    result = test_server.head("/healthcheck")

    assert result.status_code == 200


def test_redirect_short_url_exists(test_server, test_app):
    test_app.redis.set("this_url_does_exist", "a_real_url")
    result = test_server.get("/this_url_does_exist")
    assert result.status_code == 302
    test_app.redis.delete("this_url_does_exist")


def test_redirect_short_url_not_exists(test_server):
    result = test_server.get("/this_url_does_not_exist")
    assert result.status_code == 404


def test_short_url_lookup(test_server, test_app):
    test_app.redis.set("this_url_does_exist", "a_real_url")
    result = test_server.get("/this_url_does_exist/lookup")
    assert result.status_code == 200
    assert (
        result.json["shortened_url"]
        == f'{test_app.config["BASE_URL"]}/this_url_does_exist'
    )
    assert result.json["original_url"] == "a_real_url"
    test_app.redis.delete("this_url_does_exist")


def test_lookup_all(test_server, test_app):
    test_data = {
        "url_1": "short_1",
        "url_2": "short_3",
        "url_3": "short_3",
    }
    test_app.redis.mset(test_data)

    result = test_server.get("/lookup")
    assert result.status_code == 200
    assert result.json == list(test_data.keys())


def test_add_new_url(test_server, test_app, mock_create_short_url):
    test_data = {"long_url": "blah"}
    expected_short_url = "qwertyuiop"
    result = test_server.post("/add", json=test_data)

    assert test_app.redis.get(expected_short_url) == test_data["long_url"]
    assert result.json["original_url"] == test_data["long_url"]
    assert (
        result.json["shortened_url"]
        == f'{test_app.config["BASE_URL"]}/{expected_short_url}'
    )

    assert result.status_code == 201

    test_app.redis.delete(test_data["long_url"])
