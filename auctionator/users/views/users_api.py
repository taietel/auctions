from .users import users_bp
from flask import jsonify, request
from auctionator.middleware.auth_middleware import token_required
from auctionator.users.controllers import create_user, get_user_by_id, get_all_users


@users_bp.route("/api/users", methods=["GET"])
@users_bp.route("/api/users/", methods=["GET"])
@token_required
def list_users_api():
    users = get_all_users()

    if users is None:
        return jsonify({"message": "Users not found"}), 404

    return jsonify([user.get_json() for user in users])


@users_bp.route("/api/users/<int:user_id>", methods=["GET"])
@token_required
def get_user_api(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404

    return jsonify(user.get_json())


@users_bp.route("/api/users/", methods=["POST"])
def create_user_api():
    data = request.get_json()
    user = create_user(data.get("username"), data.get("password"))
    return jsonify(user.get_json())


@users_bp.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user_api(user_id):
    return jsonify({"message": f"Users Update: {user_id}"})


@users_bp.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user_api(user_id):
    return jsonify({"message": f"Users Delete: {user_id}"})