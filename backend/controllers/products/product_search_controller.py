from flask import Blueprint, request, jsonify
from backend.services.products.product_search_service import ProductSearchService

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    if not query:
        return jsonify({'error': 'Search query is required'}), 400
    
    results, total = ProductSearchService.search_products(query, page, per_page)
    
    return jsonify({
        'results': results,
        'total': total,
        'page': page,
        'per_page': per_page
    }), 200