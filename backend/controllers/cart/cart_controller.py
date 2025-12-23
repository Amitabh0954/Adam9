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

@cart_bp.route('/cart/<int:cart_item_id>', methods=['DELETE'])
def remove_item_from_cart(cart_item_id: int):
    # Note: User authentication logic should be added here
    cart_item = CartService.remove_item_from_cart(cart_item_id)
    if cart_item:
        return jsonify({'message': 'Item removed successfully'})
    return jsonify({'error': 'Item not found'}), 404

@cart_bp.route('/cart/<int:cart_item_id>', methods=['PUT'])
def modify_item_quantity(cart_item_id: int):
    data = request.json
    quantity = data.get('quantity')
    
    if quantity is None or quantity <= 0:
        return jsonify({'error': 'Invalid quantity'}), 400
    
    cart_item = CartService.modify_item_quantity(cart_item_id, quantity)
    if cart_item:
        return jsonify({'id': cart_item.id, 'product_id': cart_item.product_id, 'quantity': cart_item.quantity})
    return jsonify({'error': 'Item not found'}), 404