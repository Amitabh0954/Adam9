from flask import Blueprint, request, jsonify
from backend.services.products.product_update_service import ProductUpdateService

product_update_bp = Blueprint('product_update', __name__)

@product_update_bp.route('/update', methods=['PUT'])
def update_product():
    data = request.get_json()
    product_id = data.get('product_id')
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    try:
        product = ProductUpdateService.update_product(product_id, name, description, price)
        return jsonify({"message": "Product updated successfully", "product": product.name}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400