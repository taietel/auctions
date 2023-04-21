from flask import Blueprint

notifications_bp = Blueprint("notifications", __name__, url_prefix="/api/notifications")

from . import routes
from .models import db, init_app

init_app(notifications_bp)
with notifications_bp.app_context():
    db.create_all()

__all__ = ["notifications_bp"]
