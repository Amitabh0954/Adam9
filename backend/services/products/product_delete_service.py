from backend.repositories.products.product_repository import ProductRepository
from backend.models.product import Product

class ProductDeleteService:
    @staticmethod
    def delete_product(product_id: int) -> None:
        product = ProductRepository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        ProductRepository.delete_product(product)