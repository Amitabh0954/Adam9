from backend.models.product import Product
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProductRepository:
    """Repository for the Product model"""
    
    @staticmethod
    def add_product(name: str, description: str, price: float) -> Product:
        product = Product(name=name, description=description, price=price)
        db.session.add(product)
        db.session.commit()
        return product
    
    @staticmethod
    def get_all_products() -> list[Product]:
        return Product.query.all()
    
    @staticmethod
    def get_product_by_id(product_id: int) -> Product:
        return Product.query.get(product_id)
    
    @staticmethod
    def update_product(product_id: int, name: str, description: str, price: float) -> Product:
        product = Product.query.get(product_id)
        if product:
            product.name = name
            product.description = description
            product.price = price
            db.session.commit()
        return product
    
    @staticmethod
    def delete_product(product_id: int) -> bool:
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False