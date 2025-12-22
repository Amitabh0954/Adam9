from flask import Blueprint, request, jsonify
from backend.services.products.product_service import ProductService

product_bp = Blueprint('products', __name__)

@product_bp.route('/add', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    try:
        product = ProductService.add_product(name, description, price)
        return jsonify({"message": "Product added successfully", "product": product.name}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400