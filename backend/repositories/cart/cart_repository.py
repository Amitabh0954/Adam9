from backend.models.cart import Cart, CartItem
from backend.models import db

class CartRepository:
    @staticmethod
    def create_cart(user_id: int = None) -> Cart:
        new_cart = Cart(user_id=user_id)
        db.session.add(new_cart)
        db.session.commit()
        return new_cart

    @staticmethod
    def get_cart(cart_id: int) -> Cart:
        return Cart.query.get(cart_id)

    @staticmethod
    def add_item_to_cart(cart: Cart, product_id: int, quantity: int) -> CartItem:
        cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
        db.session.commit()
        return cart_item