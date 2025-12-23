from flask import Blueprint, request, jsonify
from backend.services.products.product_service import ProductService

product_bp = Blueprint('products', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')

    if not name or not description or price is None:
        return jsonify({'error': 'Product name, description, and price are required'}), 400

    try:
        product = ProductService.add_product(name, description, price)
        return jsonify({
            'message': 'Product added successfully',
            'product_id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@product_bp.route('/products/<int:product_id>', methods=['PATCH'])
def update_product(product_id):
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')

    try:
        product = ProductService.update_product(product_id, name, description, price)
        return jsonify({
            'message': 'Product updated successfully',
            'product_id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400