from backend.repositories.products.product_repository import ProductRepository
from backend.models.product import Product

class ProductService:
    """Service class for product-related operations"""
    
    @staticmethod
    def add_product(name: str, description: str, price: float) -> Product:
        return ProductRepository.add_product(name, description, price)
    
    @staticmethod
    def get_all_products() -> list[Product]:
        return ProductRepository.get_all_products()
    
    @staticmethod
    def get_product_by_id(product_id: int) -> Product:
        return ProductRepository.get_product_by_id(product_id)
    
    @staticmethod
    def update_product(product_id: int, name: str, description: str, price: float) -> Product:
        return ProductRepository.update_product(product_id, name, description, price)
    
    @staticmethod
    def delete_product(product_id: int) -> bool:
        return ProductRepository.delete_product(product_id)
    
    @staticmethod
    def search_products(query: str, page: int, per_page: int) -> list[Product]:
        return ProductRepository.search_products(query, page, per_page)