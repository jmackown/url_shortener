import redis
from flask import Flask

from .config import Config
from .resources import api as api_blueprint

def create_app(flask=Flask, config=Config):
    app = flask(__name__)

    app.config.from_object(config)
    app.register_blueprint(api_blueprint)

    app.redis = redis.Redis(host='redis', port=6379)


    return app