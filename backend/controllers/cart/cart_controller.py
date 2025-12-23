from flask import Blueprint, request, jsonify
from backend.services.cart.cart_service import CartService

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    user_id = request.json.get('user_id')
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')

    if not product_id or not quantity:
        return jsonify({'error': 'Product ID and quantity are required'}), 400

    cart_item = CartService.add_to_cart(user_id, product_id, quantity)
    return jsonify({
        'message': 'Product added to cart',
        'cart_item': {
            'cart_id': cart_item.cart_id,
            'product_id': cart_item.product_id,
            'quantity': cart_item.quantity
        }
    }), 201