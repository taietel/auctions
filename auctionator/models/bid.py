from . import db


class Bid(db.Model):
    __tablename__ = "bids"

    id = db.Column(db.integer, primary_key=True)
    offer_id = db.Column(
        db.integer,
        db.ForeignKey(
            "offers.id", verbose_name=_(""), on_delete=db.CASCADE, nullable=False
        ),
    )
    offer = db.relationship("Offer", backref=db.backref("products", lazy=True))
