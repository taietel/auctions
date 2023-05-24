from flask import Blueprint, jsonify, current_app

# from . import routes
from .models import db, init_app

notifications_bp = Blueprint("notifications", __name__)

app = current_app._get_current_object()

# init_app(notifications_bp)
with notifications_bp.app_context():
    db.create_all()

__all__ = ["notifications_bp"]


@notifications_bp.route("get-notifications")
def get_notification(id):
    item = db.notifications.query.get(id)
    if item is None:
        return jsonify({"error": "Item not found"})
    return jsonify(item.serialize())
