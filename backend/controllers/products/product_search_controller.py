from flask import Blueprint, request, jsonify
from backend.services.products.product_search_service import ProductSearchService

product_search_bp = Blueprint('product_search', __name__)

@product_search_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    try:
        pagination = ProductSearchService.search_products(query, page, per_page)
        products = [{
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price
        } for product in pagination.items]
        return jsonify({
            'products': products,
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': pagination.page
        }), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400