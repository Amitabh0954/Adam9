from backend.models.category import Category
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CategoryRepository:
    """Repository for the Category model"""
    
    @staticmethod
    def add_category(name: str, parent_id: int = None) -> Category:
        if CategoryRepository.get_category_by_name(name):
            raise ValueError('Category with this name already exists')
        category = Category(name=name, parent_id=parent_id)
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def get_all_categories() -> list:
        return Category.query.all()

    @staticmethod
    def get_category_by_name(name: str) -> Category:
        return Category.query.filter_by(name=name).first()