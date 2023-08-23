from .notifications import *


@notifications_bp.route("/api/notifications/", methods=["GET"])
@notifications_bp.route("/api/notifications", methods=["GET"])
def index():
    return jsonify({"message": "notifications api!"})
