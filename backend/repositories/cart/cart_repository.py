from backend.models.cart import Cart, CartItem
from backend.models.product import Product
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CartRepository:
    """Repository for the Cart and CartItem models"""

    @staticmethod
    def create_cart(user_id: int = None) -> Cart:
        cart = Cart(user_id=user_id)
        db.session.add(cart)
        db.session.commit()
        return cart

    @staticmethod
    def get_cart(cart_id: int) -> Cart:
        return Cart.query.get(cart_id)

    @staticmethod
    def get_cart_by_user_id(user_id: int) -> Cart:
        return Cart.query.filter_by(user_id=user_id).first()

    @staticmethod
    def add_to_cart(cart_id: int, product_id: int, quantity: int = 1) -> None:
        cart = CartRepository.get_cart(cart_id)
        if not cart:
            raise ValueError('Cart not found')

        product = Product.query.get(product_id)
        if not product:
            raise ValueError('Product not found')

        cart_item = CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)

        db.session.add(cart_item)
        db.session.commit()

    @staticmethod
    def remove_from_cart(cart_id: int, product_id: int) -> None:
        cart_item = CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()
        if not cart_item:
            raise ValueError('Cart item not found')

        db.session.delete(cart_item)
        db.session.commit()

    @staticmethod
    def modify_quantity(cart_id: int, product_id: int, quantity: int) -> None:
        cart_item = CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()
        if not cart_item:
            raise ValueError('Cart item not found')
        if quantity <= 0:
            raise ValueError('Quantity must be a positive integer')

        cart_item.quantity = quantity
        db.session.commit()