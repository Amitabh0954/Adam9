from backend.models.product import Product
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProductSearchRepository:
    """Repository for searching products"""
    
    @staticmethod
    def search_products(query: str, page: int, per_page: int):
        search = f"%{query}%"
        results = Product.query.filter(
            (Product.name.ilike(search)) | 
            (Product.description.ilike(search))
        ).paginate(page, per_page, error_out=False)
        
        return results.items, results.total