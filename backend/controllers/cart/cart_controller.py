from flask import Blueprint, request, jsonify
from backend.services.cart.cart_service import CartService

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/create', methods=['POST'])
def create_cart():
    user_id = request.json.get('user_id')
    cart = CartService.create_or_get_cart(user_id)
    return jsonify({"message": "Cart created successfully", "cart_id": cart.id}), 201

@cart_bp.route('/add', methods=['POST'])
def add_product_to_cart():
    data = request.get_json()
    cart_id = data.get('cart_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    try:
        cart_item = CartService.add_product_to_cart(cart_id, product_id, quantity)
        return jsonify({"message": "Product added to cart successfully", "cart_item_id": cart_item.id}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@cart_bp.route('/save', methods=['POST'])
def save_cart_state():
    data = request.get_json()
    user_id = data.get('user_id')
    cart_id = data.get('cart_id')
    try:
        CartService.save_cart_state(user_id, cart_id)
        return jsonify({"message": "Cart state saved successfully"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@cart_bp.route('/retrieve', methods=['GET'])
def retrieve_saved_cart():
    user_id = request.args.get('user_id')
    try:
        cart = CartService.retrieve_saved_cart(user_id)
        cart_items = [{
            'product_id': item.product_id,
            'quantity': item.quantity
        } for item in cart.items]
        return jsonify({"cart_id": cart.id, "items": cart_items}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400