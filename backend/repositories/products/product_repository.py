from backend.models.product import Product
from backend.models import db

class ProductRepository:
    @staticmethod
    def get_product_by_name(name: str) -> Product:
        return Product.query.filter_by(name=name).first()

    @staticmethod
    def create_product(name: str, description: str, price: float) -> Product:
        new_product = Product(name=name, description=description, price=price)
        db.session.add(new_product)
        db.session.commit()
        return new_product