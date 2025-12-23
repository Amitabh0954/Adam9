from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    product = db.relationship('Product', backref=db.backref('cart_items', lazy=True))

    def __repr__(self) -> str:
        return f"CartItem('{self.product_id}', '{self.quantity}')"