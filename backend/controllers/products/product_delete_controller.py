from flask import Blueprint, request, jsonify
from backend.services.products.product_delete_service import ProductDeleteService

product_delete_bp = Blueprint('product_delete', __name__)

@product_delete_bp.route('/delete', methods=['DELETE'])
def delete_product():
    data = request.get_json()
    product_id = data.get('product_id')
    confirmation = data.get('confirmation')
    if not confirmation:
        return jsonify({"message": "Deletion requires confirmation"}), 400
    try:
        ProductDeleteService.delete_product(product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400