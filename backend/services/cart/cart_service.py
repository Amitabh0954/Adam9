from backend.repositories.cart.cart_repository import CartRepository
from backend.models.cart import Cart
from backend.models.cart_item import CartItem

class CartService:
    """Service class for cart-related operations"""
    
    @staticmethod
    def create_cart(user_id: int) -> Cart:
        return CartRepository.create_cart(user_id)
    
    @staticmethod
    def get_cart_by_user_id(user_id: int) -> Cart:
        return CartRepository.get_cart_by_user_id(user_id)
    
    @staticmethod
    def add_item_to_cart(user_id: int, product_id: int, quantity: int) -> CartItem:
        cart = CartRepository.get_cart_by_user_id(user_id)
        if not cart:
            cart = CartRepository.create_cart(user_id)
        return CartRepository.add_item_to_cart(cart.id, product_id, quantity)
    
    @staticmethod
    def remove_item_from_cart(cart_item_id: int) -> bool:
        return CartRepository.remove_item_from_cart(cart_item_id)
    
    @staticmethod
    def modify_item_quantity(cart_item_id: int, quantity: int) -> CartItem:
        return CartRepository.modify_item_quantity(cart_item_id, quantity)