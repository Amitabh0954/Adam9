from datetime import datetime
from backend.config.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    items = db.relationship('CartItem', backref='cart', lazy=True)

    def __repr__(self) -> str:
        return f'<Cart {self.id}>'

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f'<CartItem {self.product_id}: {self.quantity}>'