from flask import Blueprint, request, jsonify
from backend.services.products.product_service import ProductService
from backend.services.products.category_service import CategoryService

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_ids = data.get('category_ids', [])
    
    if not name or not description or price is None or price <= 0:
        return jsonify({'error': 'Invalid product data'}), 400
    
    product = ProductService.add_product(name, description, price)
    
    for category_id in category_ids:
        category = CategoryService.get_category_by_id(category_id)
        if category:
            CategoryService.add_product_to_category(product, category)
    
    return jsonify({'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price})

@product_bp.route('/products', methods=['GET'])
def get_all_products():
    products = ProductService.get_all_products()
    return jsonify([{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price} for product in products])

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id: int):
    product = ProductService.get_product_by_id(product_id)
    if product:
        return jsonify({'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price})
    return jsonify({'error': 'Product not found'}), 404

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id: int):
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_ids = data.get('category_ids', [])
    
    if not name or not description or price is None or price <= 0:
        return jsonify({'error': 'Invalid product data'}), 400
    
    product = ProductService.update_product(product_id, name, description, price)
    
    for category_id in category_ids:
        category = CategoryService.get_category_by_id(category_id)
        if category:
            CategoryService.add_product_to_category(product, category)
    
    if product:
        return jsonify({'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price})
    return jsonify({'error': 'Product not found'}), 404

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int):
    # Note: Admin authentication and confirmation logic should be added here
    product = ProductService.delete_product(product_id)
    if product:
        return jsonify({'message': 'Product deleted successfully'})
    return jsonify({'error': 'Product not found'}), 404

@product_bp.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    products = ProductService.search_products(query, page, per_page)
    return jsonify([{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price} for product in products])