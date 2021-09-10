import random
import string

from flask import jsonify, Blueprint, redirect, abort, request
from flask import current_app

api = Blueprint("api", __name__)


@api.route("/healthcheck", methods=["HEAD"])
def handle_healthcheck():
    try:
        ping = current_app.redis.ping()
        if ping:
            return jsonify("alll ok"), 200
    except Exception:
        return jsonify("no redis"), 500


@api.route("/<short_url>/lookup", methods=["GET"])
def lookup_short_url(short_url):

    long_url = current_app.redis.get(short_url)

    if long_url:
        result = {
            "original_url": long_url,
            "shortened_url": f"{current_app.config['BASE_URL']}/{short_url}",
        }

        return jsonify(result), 200
    else:
        abort(404)


@api.route("/<short_url>", methods=["GET"])
def redirect_short_url(short_url):
    long_url = current_app.redis.get(short_url)
    if long_url:
        return redirect(long_url, 302)
    else:
        abort(404)


@api.route("/lookup", methods=["GET"])
def lookup_all_short_urls():

    all_urls = current_app.redis.keys()

    if all_urls:

        return jsonify(all_urls), 200
    else:
        abort(404)


@api.route("/add", methods=["POST"])
def add_new_short_url():
    body = request.json

    long_url = body["long_url"]

    while True:
        short_url = create_short_url()
        exists = current_app.redis.get(short_url)
        if not exists:
            current_app.redis.set(short_url, long_url)
            break

    result = {
        "original_url": long_url,
        "shortened_url": f"{current_app.config['BASE_URL']}/{short_url}",
    }

    return jsonify(result), 201


def create_short_url():
    possible_chars = string.ascii_letters
    return "".join(random.choice(possible_chars) for i in range(10))
