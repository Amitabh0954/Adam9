from backend.models.product import Product
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProductRepository:
    """Repository for the Product model"""

    @staticmethod
    def get_product_by_name(name: str) -> Product:
        return Product.query.filter_by(name=name).first()

    @staticmethod
    def add_product(name: str, description: str, price: float) -> Product:
        if ProductRepository.get_product_by_name(name):
            raise ValueError('Product with this name already exists')
        if price <= 0:
            raise ValueError('Product price must be a positive number')

        product = Product(name=name, description=description, price=price)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update_product(product_id: int, name: str = None, description: str = None, price: float = None) -> Product:
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
        
        db.session.commit()
        return product