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