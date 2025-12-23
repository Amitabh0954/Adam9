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

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        ProductService.delete_product(product_id)
        return jsonify({'message': 'Product deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@product_bp.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    if not query:
        return jsonify({'error': 'Search query is required'}), 400

    products, total = ProductService.search_products(query, page, per_page)

    return jsonify({
        'products': [{'id': p.id, 'name': p.name, 'description': p.description, 'price': p.price} for p in products],
        'total': total,
        'page': page,
        'per_page': per_page
    }), 200