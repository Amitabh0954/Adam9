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

@cart_bp.route('/cart/item/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    confirmed = request.args.get('confirmed', default='false').lower() == 'true'
    if not confirmed:
        return jsonify({'error': 'Confirmation required'}), 400

    try:
        CartService.remove_from_cart(item_id)
        return jsonify({'message': 'Product removed from cart'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400