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

@cart_bp.route('/cart/item/<int:item_id>', methods=['PATCH'])
def update_cart_item_quantity(item_id):
    quantity = request.json.get('quantity')

    if quantity is None or int(quantity) <= 0:
        return jsonify({'error': 'Quantity must be a positive integer'}), 400

    try:
        cart_item = CartService.update_cart_item_quantity(item_id, int(quantity))
        return jsonify({
            'message': 'Cart item updated',
            'cart_item': {
                'cart_id': cart_item.cart_id,
                'product_id': cart_item.product_id,
                'quantity': cart_item.quantity
            }
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400