from flask import Blueprint, request, jsonify
from backend.services.cart.cart_service import CartService

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['POST'])
def add_item_to_cart():
    data = request.json
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    
    if not user_id or not product_id or not quantity or quantity <= 0:
        return jsonify({'error': 'Invalid cart item data'}), 400
    
    cart_item = CartService.add_item_to_cart(user_id, product_id, quantity)
    return jsonify({'id': cart_item.id, 'product_id': cart_item.product_id, 'quantity': cart_item.quantity})