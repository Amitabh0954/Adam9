from backend.models.category import Category
from backend.models import db

class CategoryRepository:
    @staticmethod
    def get_category_by_name(name: str) -> Category:
        return Category.query.filter_by(name=name).first()

    @staticmethod
    def create_category(name: str, parent_id: int = None) -> Category:
        new_category = Category(name=name, parent_id=parent_id)
        db.session.add(new_category)
        db.session.commit()
        return new_category

    @staticmethod
    def get_categories():
        return Category.query.all()