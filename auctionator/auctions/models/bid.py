from models import db
from sqlalchemy import Integer


class Bid(db.Model):
    __tablename__ = "bids"

    id = db.Column(db.integer, primary_key=True)
    offer_id = db.Column(
        db.integer,
        db.ForeignKey(
            "offers.id", verbose_name=_(""), on_delete=db.CASCADE, nullable=False
        )
    )
    user_id = db.Column(db.integer, db.ForeignKey("users.id", verbose_name=_(""), on_delete=db.CASCADE, nullable=False))
    custom_criteria_value_id = db.Column(db.integer, db.ForeignKey("custom_criteria_values.id", verbose_name=_(""),
                                                                   on_delete=db.CASCADE, nullable=False))

    auction_tech_file = db.Column(db.string)
    offer = db.relationship("Offer", backref=db.backref("products", lazy=True))
    user = db.relationship("User", backref=db.backref("products", lazy=True))
    custom_criteria_values = db.relationship("Custom_criteria_values",
                                             backref=db.backref('custom_criteria_values', lazy=True))
