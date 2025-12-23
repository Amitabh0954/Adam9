from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    items = db.relationship('CartItem', back_populates='cart', cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return f"Cart('{self.id}', '{self.user_id}')"

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cart = db.relationship('Cart', back_populates='items')
    product = db.relationship('Product')

    def __repr__(self) -> str:
        return f"CartItem('{self.cart_id}', '{self.product_id}', '{self.quantity}')"