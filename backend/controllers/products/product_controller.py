from flask import Blueprint, request, jsonify
from backend.services.products.product_service import ProductService

product_bp = Blueprint('products', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_id = data.get('category_id')

    if not name or not description or price is None or not category_id:
        return jsonify({'error': 'Product name, description, price, and category are required'}), 400

    try:
        product = ProductService.add_product(name, description, price, category_id)
        return jsonify({
            'message': 'Product added successfully',
            'product_id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category_id': product.category_id
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@product_bp.route('/products/<int:product_id>', methods=['PATCH'])
def update_product(product_id):
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_id = data.get('category_id')

    try:
        product = ProductService.update_product(product_id, name, description, price, category_id)
        return jsonify({
            'message': 'Product updated successfully',
            'product_id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category_id': product.category_id
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@product_bp.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        return jsonify({'error': 'Category name is required'}), 400

    try:
        category = ProductService.add_category(name, parent_id)
        return jsonify({
            'message': 'Category added successfully',
            'category_id': category.id,
            'name': category.name,
            'parent_id': category.parent_id
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@product_bp.route('/categories/<int:category_id>', methods=['PATCH'])
def update_category(category_id):
    data = request.json
    name = data.get('name')
    parent_id = data.get('parent_id')

    try:
        category = ProductService.update_category(category_id, name, parent_id)
        return jsonify({
            'message': 'Category updated successfully',
            'category_id': category.id,
            'name': category.name,
            'parent_id': category.parent_id
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400