from flask import Blueprint, request, jsonify
from backend.services.products.category_service import CategoryService
from backend.models.product import Product
from backend.models.category import Category

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    name = data.get('name')
    parent_id = data.get('parent_id')
    
    if not name:
        return jsonify({'error': 'Category name is required'}), 400
    
    category = CategoryService.add_category(name, parent_id)
    return jsonify({'id': category.id, 'name': category.name, 'parent_id': category.parent_id})

@category_bp.route('/categories', methods=['GET'])
def get_all_categories():
    categories = CategoryService.get_all_categories()
    return jsonify([{'id': category.id, 'name': category.name, 'parent_id': category.parent_id} for category in categories])