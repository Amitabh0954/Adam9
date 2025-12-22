from backend.repositories.products.product_search_repository import ProductSearchRepository
from backend.models.product import Product

class ProductSearchService:
    @staticmethod
    def search_products(query: str, page: int = 1, per_page: int = 10):
        if not query:
            raise ValueError("Search query cannot be empty")
        return ProductSearchRepository.search_products(query, page, per_page)