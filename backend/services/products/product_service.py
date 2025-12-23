from backend.repositories.products.product_repository import ProductRepository
from backend.models.product import Product

class ProductService:
    """Service class for product-related operations"""
    
    @staticmethod
    def add_product(name: str, description: str, price: float) -> Product:
        return ProductRepository.add_product(name, description, price)
```