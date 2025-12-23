from backend.repositories.products.product_repository import ProductRepository
from backend.models.product import Product

class ProductService:
    """Service class for product-related operations"""
    
    @staticmethod
    def add_product(name: str, description: str, price: float) -> Product:
        if not name or not description:
            raise ValueError('Product name and description cannot be empty')
        return ProductRepository.add_product(name, description, price)

    @staticmethod
    def update_product(product_id: int, name: str = None, description: str = None, price: float = None) -> Product:
        return ProductRepository.update_product(product_id, name, description, price)

    @staticmethod
    def delete_product(product_id: int) -> None:
        ProductRepository.delete_product(product_id)
```