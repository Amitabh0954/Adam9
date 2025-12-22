from backend.repositories.cart.cart_item_repository import CartItemRepository

class CartItemService:
    @staticmethod
    def modify_product_quantity(cart_id: int, product_id: int, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        cart_item = CartItemRepository.get_cart_item(cart_id, product_id)
        if not cart_item:
            raise ValueError("Cart item not found")
        cart_item.quantity = quantity
        CartItemRepository.update_cart_item(cart_item)