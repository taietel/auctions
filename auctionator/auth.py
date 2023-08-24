import functools

import jwt
from flask import (Blueprint, redirect, request, session, url_for, jsonify)
from auctionator.database import db
from auctionator.users.controllers.user import create_user, authenticate
from auctionator.config import SECRET_KEY

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/api/register', methods=['POST'])
@auth_bp.route('/api/register/', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        try:
            create_user(username, password)
        except db.IntegrityError:
            return jsonify({"message": "User already exists."}), 400

        return jsonify({"message": "User created successfully."}), 201

    except Exception as e:
        return jsonify({"message": "No data provided.", "error": str(e)}), 400


@auth_bp.route('/api/login', methods=['POST'])
@auth_bp.route('/api/login/', methods=['POST'])
def login():
    try:
        data = request.json

        if not data:
            return jsonify({"message": "No data provided."}), 400

        user = authenticate(data.get("username"), data.get("password"))

        if user:
            try:
                user["token"] = jwt.encode(
                    {"user_id": user["id"]},
                    SECRET_KEY,
                    algorithm="HS256"
                )
                return jsonify(user)

            except Exception as user_exception:
                return jsonify({"message": "Something went wrong", "error": str(user_exception)}), 500

    except Exception as e:
        return jsonify({"message": "No data provided.", "error": str(e)}), 400

    return jsonify({"message": "Invalid username or password."}), 401


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
