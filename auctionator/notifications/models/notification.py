# from . import db
from datetime import datetime

from models import db


class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String)
    status = db.Column(db.String)  # active, read, sent,
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Notification {self.name}>"
