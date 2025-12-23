from backend.repositories.products.product_repository import ProductRepository, CategoryRepository
from backend.models.product import Product
from backend.models.category import Category

class ProductService:
    """Service class for product-related operations"""

    @staticmethod
    def add_product(name: str, description: str, price: float, category_id: int) -> Product:
        if not name or not description:
            raise ValueError('Product name and description cannot be empty')
        return ProductRepository.add_product(name, description, price, category_id)

    @staticmethod
    def update_product(product_id: int, name: str = None, description: str = None, price: float = None, category_id: int = None) -> Product:
        return ProductRepository.update_product(product_id, name, description, price, category_id)

    @staticmethod
    def delete_product(product_id: int) -> None:
        ProductRepository.delete_product(product_id)

    @staticmethod
    def search_products(query: str, page: int = 1, per_page: int = 10):
        return ProductRepository.search_products(query, page, per_page)

    @staticmethod
    def add_category(name: str, parent_id: int = None) -> Category:
        if not name:
            raise ValueError('Category name cannot be empty')
        return CategoryRepository.add_category(name, parent_id)

    @staticmethod
    def update_category(category_id: int, name: str = None, parent_id: int = None) -> Category:
        return CategoryRepository.update_category(category_id, name, parent_id)
```