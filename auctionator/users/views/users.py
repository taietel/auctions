from flask import Blueprint

users_bp = Blueprint("users", __name__)


@users_bp.route("/users")
def list_users():
    return "Users Index"


@users_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return f"Users Show: {user_id}"


@users_bp.route("/users/", methods=["POST"])
def create_user():
    return "Users Create"


@users_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    return f"Users Update: {user_id}"


@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return f"Users Delete: {user_id}"
