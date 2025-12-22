import unittest
from app import create_app
from backend.models import db, Product

class ProductManagementTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_product(self):
        response = self.client.post('/products/add', json={
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': 10.99
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Product added successfully')
        self.assertEqual(data['product'], 'Test Product')

    def test_add_product_with_existing_name(self):
        self.client.post('/products/add', json={
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': 10.99
        })
        response = self.client.post('/products/add', json={
            'name': 'Test Product',
            'description': 'This is another test product',
            'price': 10.99
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Product name must be unique')

if __name__ == '__main__':
    unittest.main()
```