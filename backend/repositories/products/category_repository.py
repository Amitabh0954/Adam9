from backend.models.category import Category
from backend.models.product_category import product_category
from backend.models.product import Product
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CategoryRepository:
    """Repository for the Category model"""
    
    @staticmethod
    def add_category(name: str, parent_id: int = None) -> Category:
        category = Category(name=name, parent_id=parent_id)
        db.session.add(category)
        db.session.commit()
        return category
    
    @staticmethod
    def get_all_categories() -> list[Category]:
        return Category.query.all()
    
    @staticmethod
    def get_category_by_id(category_id: int) -> Category:
        return Category.query.get(category_id)
    
    @staticmethod
    def add_product_to_category(product: Product, category: Category):
        product.categories.append(category)
        db.session.commit()