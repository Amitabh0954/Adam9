from backend.repositories.products.category_repository import CategoryRepository
from backend.models.category import Category
from backend.models.product import Product

class CategoryService:
    """Service class for category-related operations"""
    
    @staticmethod
    def add_category(name: str, parent_id: int = None) -> Category:
        return CategoryRepository.add_category(name, parent_id)
    
    @staticmethod
    def get_all_categories() -> list[Category]:
        return CategoryRepository.get_all_categories()
    
    @staticmethod
    def get_category_by_id(category_id: int) -> Category:
        return CategoryRepository.get_category_by_id(category_id)
    
    @staticmethod
    def add_product_to_category(product: Product, category: Category):
        CategoryRepository.add_product_to_category(product, category)