from flask import Blueprint, jsonify, current_app

offers_bp = Blueprint("offers", __name__, url_prefix="/offers")


@offers_bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "offers module"})

