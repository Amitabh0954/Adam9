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