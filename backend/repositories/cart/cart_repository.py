from backend.models.cart import Cart, CartItem
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CartRepository:
    """Repository for the Cart and CartItem models"""
    
    @staticmethod
    def get_cart(user_id: int = None) -> Cart:
        if user_id:
            cart = Cart.query.filter_by(user_id=user_id).first()
        else:
            cart = Cart()
            db.session.add(cart)
            db.session.commit()
        return cart

    @staticmethod
    def add_to_cart(cart_id: int, product_id: int, quantity: int) -> CartItem:
        cart_item = CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
            db.session.add(cart_item)
        db.session.commit()
        return cart_item