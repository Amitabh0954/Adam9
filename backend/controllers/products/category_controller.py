from flask import Blueprint, request, jsonify
from backend.services.products.category_service import CategoryService

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        return jsonify({'error': 'Category name is required'}), 400

    try:
        category = CategoryService.add_category(name, parent_id)
        return jsonify({'message': 'Category added successfully', 'category_id': category.id}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = CategoryService.get_all_categories()
    return jsonify([{'id': cat.id, 'name': cat.name, 'parent_id': cat.parent_id} for cat in categories]), 200