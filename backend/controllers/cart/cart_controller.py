from flask import Blueprint, request, jsonify
from backend.services.cart.cart_service import CartService

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['POST'])
def create_cart():
    user_id = request.json.get('user_id')
    cart = CartService.create_cart(user_id)
    return jsonify({
        'cart_id': cart.id,
        'user_id': cart.user_id,
        'created_at': cart.created_at.isoformat()
    }), 201

@cart_bp.route('/cart/<int:cart_id>/items', methods=['POST'])
def add_to_cart(cart_id):
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)
    try:
        CartService.add_to_cart(cart_id, product_id, quantity)
        return jsonify({'message': 'Product added to cart'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@cart_bp.route('/cart/<int:cart_id>', methods=['GET'])
def get_cart(cart_id):
    cart = CartService.get_cart(cart_id)
    if not cart:
        return jsonify({'error': 'Cart not found'}), 404

    items = [{'product_id': item.product_id, 'quantity': item.quantity} for item in cart.items]
    return jsonify({'cart_id': cart.id, 'user_id': cart.user_id, 'items': items}), 200