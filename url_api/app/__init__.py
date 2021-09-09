import redis
from flask import Flask

from .config import Config
from .resources import api as api_blueprint

initial_data = {
    "OjrHZTlVDa": "https://www.lego.com/en-gb/product/nasa-space-shuttle-discovery-10283",  # noqa:
}


def create_app(flask=Flask, config=Config):
    app = flask(__name__)

    app.config.from_object(config)
    app.register_blueprint(api_blueprint)

    app.redis = redis.Redis(
        host="redis", port=6379, charset="utf-8", decode_responses=True
    )
    if initial_data:
        app.redis.mset(initial_data)

    return app
