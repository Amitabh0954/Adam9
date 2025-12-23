from flask import Blueprint, request, jsonify
from backend.services.products.product_service import ProductService

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')

    if not name or not description or not price:
        return jsonify({'error': 'Missing required fields'}), 400

    if price <= 0:
        return jsonify({'error': 'Price must be a positive number'}), 400

    try:
        product = ProductService.add_product(name, description, price)
        return jsonify({'message': 'Product added successfully', 'product_id': product.id}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')

    if not name or not description or not price:
        return jsonify({'error': 'Missing required fields'}), 400

    if price <= 0:
        return jsonify({'error': 'Price must be a positive number'}), 400

    try:
        product = ProductService.update_product(product_id, name, description, price)
        return jsonify({'message': 'Product updated successfully', 'product_id': product.id}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Assuming there's a function to check if the user is an admin.
    if not check_if_admin():
        return jsonify({'error': 'Unauthorized access'}), 403

    try:
        ProductService.delete_product(product_id)
        return jsonify({'message': 'Product deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400