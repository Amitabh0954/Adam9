from backend.models.product import Product
from sqlalchemy import or_

class ProductSearchRepository:
    @staticmethod
    def search_products(query: str, page: int, per_page: int):
        search_query = f"%{query}%"
        return Product.query.filter(
            or_(
                Product.name.ilike(search_query),
                Product.description.ilike(search_query),
            )
        ).paginate(page=page, per_page=per_page, error_out=False)