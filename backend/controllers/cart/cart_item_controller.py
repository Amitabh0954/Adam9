from flask import Blueprint, request, jsonify
from backend.services.cart.cart_item_service import CartItemService

cart_item_bp = Blueprint('cart_item', __name__)

@cart_item_bp.route('/remove', methods=['DELETE'])
def remove_product_from_cart():
    data = request.get_json()
    cart_id = data.get('cart_id')
    product_id = data.get('product_id')
    confirmation = data.get('confirmation')
    try:
        CartItemService.remove_product_from_cart(cart_id, product_id, confirmation)
        return jsonify({"message": "Product removed from cart successfully"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400