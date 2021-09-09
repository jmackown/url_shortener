from flask import jsonify, Blueprint
from flask import current_app

api = Blueprint("api", __name__)

@api.route('/healthcheck', methods=['HEAD'])
def handle_healthcheck():
    try:
        ping = current_app.redis.ping()
        if ping:
            return jsonify("alll ok"), 200
    except:
        return jsonify("no redis"), 500
