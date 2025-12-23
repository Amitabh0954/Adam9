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

@cart_bp.route('/cart/<int:cart_id>/items/<int:product_id>', methods=['DELETE'])
def remove_from_cart(cart_id, product_id):
    try:
        CartService.remove_from_cart(cart_id, product_id)
        return jsonify({'message': 'Product removed from cart', 'cart_id': cart_id, 'product_id': product_id}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@cart_bp.route('/cart/<int:cart_id>/items/<int:product_id>', methods=['PATCH'])
def modify_quantity(cart_id, product_id):
    quantity = request.json.get('quantity')
    if quantity is None or quantity <= 0:
        return jsonify({'error': 'Quantity must be a positive integer'}), 400

    try:
        CartService.modify_quantity(cart_id, product_id, quantity)
        return jsonify({'message': 'Product quantity updated', 'cart_id': cart_id, 'product_id': product_id, 'quantity': quantity}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@cart_bp.route('/cart/<int:cart_id>', methods=['GET'])
def get_cart(cart_id):
    cart = CartService.get_cart(cart_id)
    if not cart:
        return jsonify({'error': 'Cart not found'}), 404

    items = [{'product_id': item.product_id, 'quantity': item.quantity, 'price': item.product.price, 'total': item.product.price * item.quantity} for item in cart.items]
    total_price = sum(item['total'] for item in items)
    return jsonify({'cart_id': cart.id, 'user_id': cart.user_id, 'items': items, 'total_price': total_price}), 200

@cart_bp.route('/user/<int:user_id>/cart', methods=['GET'])
def get_user_cart(user_id):
    try:
        cart = CartService.get_cart_by_user_id(user_id)
        if not cart:
            return jsonify({'error': 'Cart not found for user'}), 404

        items = [{'product_id': item.product_id, 'quantity': item.quantity, 'price': item.product.price, 'total': item.product.price * item.quantity} for item in cart.items]
        total_price = sum(item['total'] for item in items)
        return jsonify({'cart_id': cart.id, 'user_id': cart.user_id, 'items': items, 'total_price': total_price}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400