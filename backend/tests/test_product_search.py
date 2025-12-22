import unittest
from app import create_app
from backend.models import db, Product

class ProductSearchTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.create_test_products()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def create_test_products(self):
        products = [
            Product(name='Test Product 1', description='Description of test product 1', price=10.99),
            Product(name='Test Product 2', description='Description of test product 2', price=15.99),
            Product(name='Another Product', description='This is another product', price=20.99)
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()

    def test_search_products(self):
        response = self.client.get('/products/search', query_string={'query': 'Test', 'page': 1, 'per_page': 10})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['total'], 2)
        self.assertEqual(len(data['products']), 2)

    def test_search_products_no_results(self):
        response = self.client.get('/products/search', query_string={'query': 'Nonexistent', 'page': 1, 'per_page': 10})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['total'], 0)

if __name__ == '__main__':
    unittest.main()
```