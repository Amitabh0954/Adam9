from backend.repositories.cart.cart_repository import CartRepository
from backend.models.cart import CartItem

class CartService:
    """Service class for cart-related operations"""
    
    @staticmethod
    def add_to_cart(user_id: int, product_id: int, quantity: int) -> CartItem:
        cart = CartRepository.get_cart(user_id)
        return CartRepository.add_to_cart(cart.id, product_id, quantity)

    @staticmethod
    def remove_from_cart(item_id: int) -> None:
        return CartRepository.remove_from_cart(item_id)
```