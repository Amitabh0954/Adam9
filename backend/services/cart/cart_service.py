from backend.models.cart import Cart
from backend.models import db
from backend.repositories.cart.cart_repository import CartRepository
from backend.repositories.cart.cart_item_repository import CartItemRepository

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

    @staticmethod
    def save_cart_state(user_id: int, cart_id: int) -> None:
        cart = CartRepository.get_cart(cart_id)
        if not cart or cart.user_id != user_id:
            raise ValueError("Cart not found or access denied")
        # Persist the cart with associated user id
        db.session.commit()

    @staticmethod
    def retrieve_saved_cart(user_id: int) -> Cart:
        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart:
            raise ValueError("No saved cart for user")
        return cart