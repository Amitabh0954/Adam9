from backend.repositories.cart.cart_item_repository import CartItemRepository

class CartItemService:
    @staticmethod
    def remove_product_from_cart(cart_id: int, product_id: int, confirmation: bool) -> None:
        if not confirmation:
            raise ValueError("Removal requires confirmation")
        cart_item = CartItemRepository.get_cart_item(cart_id, product_id)
        if not cart_item:
            raise ValueError("Cart item not found")
        CartItemRepository.delete_cart_item(cart_item)