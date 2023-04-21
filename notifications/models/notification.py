from . import db


class Product(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    # category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    # category = db.relationship('Category', backref=db.backref('products', lazy=True))

    def __repr__(self):
        return f"<Product {self.name}>"
