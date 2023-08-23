from flask import Blueprint, jsonify, current_app


notifications_bp = Blueprint("notifications", __name__)


@notifications_bp.route("/notifications/", methods=["GET"])
def test():
    return jsonify({"message": "Hello, World!"})
