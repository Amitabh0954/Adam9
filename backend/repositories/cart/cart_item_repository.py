from backend.models.cart import CartItem
from backend.models import db

class CartItemRepository:
    @staticmethod
    def get_cart_item(cart_id: int, product_id: int) -> CartItem:
        return CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()

    @staticmethod
    def delete_cart_item(cart_item: CartItem) -> None:
        db.session.delete(cart_item)
        db.session.commit()