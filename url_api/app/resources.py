from flask import jsonify, Blueprint, redirect, abort
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


@api.get("/<short_url>")
async def redirect_short_url(short_url):
    long_url = current_app.redis.get(short_url)
    if long_url:
        return redirect(long_url, 302)
    else:
        abort(404)
