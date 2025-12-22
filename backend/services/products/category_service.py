from backend.repositories.products.category_repository import CategoryRepository
from backend.models.category import Category

class CategoryService:
    @staticmethod
    def add_category(name: str, parent_id: int = None) -> Category:
        if not name:
            raise ValueError("Category name cannot be empty")
        if CategoryRepository.get_category_by_name(name):
            raise ValueError("Category name must be unique")
        return CategoryRepository.create_category(name, parent_id)

    @staticmethod
    def get_all_categories():
        return CategoryRepository.get_categories()