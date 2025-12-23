from backend.repositories.cart.cart_repository import CartRepository
from backend.models.cart import Cart

class CartService:
    """Service class for cart-related operations"""

    @staticmethod
    def create_cart(user_id: int = None) -> Cart:
        return CartRepository.create_cart(user_id)

    @staticmethod
    def get_cart(cart_id: int) -> Cart:
        return CartRepository.get_cart(cart_id)

    @staticmethod
    def add_to_cart(cart_id: int, product_id: int, quantity: int = 1) -> None:
        CartRepository.add_to_cart(cart_id, product_id, quantity)
```