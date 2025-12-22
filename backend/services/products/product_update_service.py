from backend.repositories.products.product_repository import ProductRepository
from backend.models.product import Product

class ProductUpdateService:
    @staticmethod
    def update_product(product_id: int, name: str, description: str, price: float) -> Product:
        product = ProductRepository.get_product_by_id(product_id)
        if not name or price <= 0:
            raise ValueError("Product name must be unique, Price must be a numeric value, Description can be modified but not removed")
        if ProductRepository.get_product_by_name(name) and product.name != name:
            raise ValueError("Product name must be unique")
        product.name = name
        product.description = description
        product.price = price
        ProductRepository.save_product(product)
        return product