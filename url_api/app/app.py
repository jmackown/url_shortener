from . import create_app


if __name__ == "__main__":
    app = create_app()
    if initial_data := {
        "OjrHZTlVDa": "https://www.lego.com/en-gb/product/nasa-space-shuttle-discovery-10283",  # noqa:
    }:
        app.redis.mset(initial_data)
