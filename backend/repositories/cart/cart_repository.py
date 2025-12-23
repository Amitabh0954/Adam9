from backend.models.cart import Cart
from backend.models.cart_item import CartItem
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CartRepository:
    """Repository for the Cart model"""
    
    @staticmethod
    def create_cart(user_id: int) -> Cart:
        cart = Cart(user_id=user_id)
        db.session.add(cart)
        db.session.commit()
        return cart
    
    @staticmethod
    def get_cart_by_user_id(user_id: int) -> Cart:
        return Cart.query.filter_by(user_id=user_id).first()
    
    @staticmethod
    def add_item_to_cart(cart_id: int, product_id: int, quantity: int) -> CartItem:
        cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
        db.session.commit()
        return cart_item
    
    @staticmethod
    def remove_item_from_cart(cart_item_id: int) -> bool:
        cart_item = CartItem.query.get(cart_item_id)
        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def modify_item_quantity(cart_item_id: int, quantity: int) -> CartItem:
        cart_item = CartItem.query.get(cart_item_id)
        if cart_item:
            cart_item.quantity = quantity
            db.session.commit()
            return cart_item
        return None