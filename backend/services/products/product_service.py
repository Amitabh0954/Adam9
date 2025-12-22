from backend.repositories.products.product_repository import ProductRepository
from backend.models.product import Product

class ProductService:
    @staticmethod
    def add_product(name: str, description: str, price: float) -> Product:
        if not name or not description or price <= 0:
            raise ValueError("Product name must be unique, Product price must be a positive number, Product description cannot be empty")
        if ProductRepository.get_product_by_name(name):
            raise ValueError("Product name must be unique")
        return ProductRepository.create_product(name, description, price)