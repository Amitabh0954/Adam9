from backend.models.cart import Cart, CartItem
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CartRepository:
    """Repository for the Cart and CartItem models"""
    
    @staticmethod
    def get_cart(user_id: int = None) -> Cart:
        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart and user_id:
            cart = Cart(user_id=user_id)
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

    @staticmethod
    def remove_from_cart(item_id: int):
        cart_item = CartItem.query.get(item_id)
        if not cart_item:
            raise ValueError('Cart item not found')
        db.session.delete(cart_item)
        db.session.commit()

    @staticmethod
    def update_cart_item_quantity(item_id: int, quantity: int) -> CartItem:
        cart_item = CartItem.query.get(item_id)
        if not cart_item:
            raise ValueError('Cart item not found')
        cart_item.quantity = quantity
        db.session.commit()
        return cart_item

    @staticmethod
    def get_cart_items(user_id: int) -> list:
        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart:
            raise ValueError('No cart found for the user')
        return cart.items