from backend.models.product import Product
from backend.models.category import Category
from sqlalchemy import or_
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProductRepository:
    """Repository for the Product model"""
    
    @staticmethod
    def get_product_by_name(name: str) -> Product:
        return Product.query.filter_by(name=name).first()

    @staticmethod
    def add_product(name: str, description: str, price: float, category_id: int) -> Product:
        if ProductRepository.get_product_by_name(name):
            raise ValueError('Product with this name already exists')
        if price <= 0:
            raise ValueError('Product price must be a positive number')

        product = Product(name=name, description=description, price=price, category_id=category_id)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update_product(product_id: int, name: str = None, description: str = None, price: float = None, category_id: int = None) -> Product:
        product = Product.query.get(product_id)
        if not product:
            raise ValueError('Product not found')

        if name:
            if ProductRepository.get_product_by_name(name) and ProductRepository.get_product_by_name(name).id != product_id:
                raise ValueError('Product with this name already exists')
            product.name = name
        if description:
            product.description = description  # Description can be modified but not removed
        if price is not None:
            if price <= 0:
                raise ValueError('Price must be a positive number')
            product.price = price
        if category_id:
            product.category_id = category_id
        
        db.session.commit()
        return product

    @staticmethod
    def delete_product(product_id: int) -> None:
        product = Product.query.get(product_id)
        if not product:
            raise ValueError('Product not found')
        db.session.delete(product)
        db.session.commit()

    @staticmethod
    def search_products(query: str, page: int = 1, per_page: int = 10):
        search = f"%{query}%"
        products_query = Product.query.filter(
            or_(Product.name.ilike(search), Product.description.ilike(search))
        )
        total = products_query.count()
        products = products_query.paginate(page, per_page, False).items
        return products, total

class CategoryRepository:
    """Repository for the Category model"""
    
    @staticmethod
    def get_category_by_name(name: str) -> Category:
        return Category.query.filter_by(name=name).first()

    @staticmethod
    def add_category(name: str, parent_id: int = None) -> Category:
        if CategoryRepository.get_category_by_name(name):
            raise ValueError('Category with this name already exists')

        category = Category(name=name, parent_id=parent_id)
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def update_category(category_id: int, name: str = None, parent_id: int = None) -> Category:
        category = Category.query.get(category_id)
        if not category:
            raise ValueError('Category not found')

        if name:
            if CategoryRepository.get_category_by_name(name) and CategoryRepository.get_category_by_name(name).id != category_id:
                raise ValueError('Category with this name already exists')
            category.name = name
        category.parent_id = parent_id
        
        db.session.commit()
        return category