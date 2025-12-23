from backend.models.product import Product
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProductRepository:
    """Repository for the Product model"""

    @staticmethod
    def add_product(name: str, description: str, price: float) -> Product:
        if ProductRepository.get_product_by_name(name):
            raise ValueError('Product with this name already exists')
        product = Product(name=name, description=description, price=price)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def get_product_by_name(name: str) -> Product:
        return Product.query.filter_by(name=name).first()