from flask import Blueprint, request, jsonify
from backend.services.products.category_service import CategoryService

category_bp = Blueprint('categories', __name__)

@category_bp.route('/add', methods=['POST'])
def add_category():
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')
    try:
        category = CategoryService.add_category(name, parent_id)
        return jsonify({"message": "Category added successfully", "category": category.name}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@category_bp.route('/all', methods=['GET'])
def get_all_categories():
    categories = CategoryService.get_all_categories()
    return jsonify([{'id': category.id, 'name': category.name, 'parent_id': category.parent_id} for category in categories]), 200