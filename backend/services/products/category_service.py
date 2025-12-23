from backend.repositories.products.category_repository import CategoryRepository
from backend.models.category import Category
from typing import List

class CategoryService:
    """Service class for category-related operations"""
    
    @staticmethod
    def add_category(name: str, parent_id: int = None) -> Category:
        return CategoryRepository.add_category(name, parent_id)

    @staticmethod
    def get_all_categories() -> List[Category]:
        return CategoryRepository.get_all_categories()
```