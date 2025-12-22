from flask import Blueprint, request, jsonify
from backend.services.cart.cart_item_service import CartItemService

cart_item_bp = Blueprint('cart_item', __name__)

@cart_item_bp.route('/modify', methods=['PATCH'])
def modify_product_quantity():
    data = request.get_json()
    cart_id = data.get('cart_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    try:
        CartItemService.modify_product_quantity(cart_id, product_id, quantity)
        return jsonify({"message": "Product quantity updated successfully"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400