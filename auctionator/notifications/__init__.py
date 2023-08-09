from flask import Blueprint, jsonify, current_app


notifications_bp = Blueprint("notifications", __name__, url_prefix="/notifications")


@notifications_bp.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Hello, World!"})
