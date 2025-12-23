from backend.repositories.products.product_repository import ProductRepository
from backend.models.product import Product

class ProductService:
    """Service class for product-related operations"""
    
    @staticmethod
    def add_product(name: str, description: str, price: float) -> Product:
        product = ProductRepository.add_product(name, description, price)
        return product
    
    @staticmethod
    def get_all_products() -> list[Product]:
        return ProductRepository.get_all_products()
    
    @staticmethod
    def get_product_by_id(product_id: int) -> Product:
        return ProductRepository.get_product_by_id(product_id)
    
    @staticmethod
    def update_product(product_id: int, name: str, description: str, price: float) -> Product:
        product = ProductRepository.update_product(product_id, name, description, price)
        return product