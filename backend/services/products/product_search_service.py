from backend.repositories.products.product_search_repository import ProductSearchRepository
from typing import List, Tuple
from backend.models.product import Product

class ProductSearchService:
    """Service class for product search operations"""
    
    @staticmethod
    def search_products(query: str, page: int, per_page: int) -> Tuple[List[Product], int]:
        return ProductSearchRepository.search_products(query, page, per_page)
```