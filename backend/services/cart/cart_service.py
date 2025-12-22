from backend.repositories.cart.cart_repository import CartRepository
from backend.models.cart import Cart, CartItem
from backend.models.product import Product

class CartService:
    @staticmethod
    def create_or_get_cart(user_id: int = None) -> Cart:
        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart:
            cart = CartRepository.create_cart(user_id)
        return cart

    @staticmethod
    def add_product_to_cart(cart_id: int, product_id: int, quantity: int) -> CartItem:
        cart = CartRepository.get_cart(cart_id)
        if not cart:
            raise ValueError("Cart not found")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        product = Product.query.get(product_id)
        if not product:
            raise ValueError("Product not found")
        return CartRepository.add_item_to_cart(cart, product_id, quantity)