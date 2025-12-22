import unittest
from app import create_app
from backend.models import db, Product

class ProductDeleteTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.create_test_product()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def create_test_product(self):
        product = Product(name='Test Product', description='This is a test product', price=10.99)
        db.session.add(product)
        db.session.commit()

    def test_delete_product(self):
        response = self.client.delete('/products/delete', json={
            'product_id': 1,
            'confirmation': True
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Product deleted successfully')

        # Verify product deletion
        product = Product.query.get(1)
        self.assertIsNone(product)

    def test_delete_product_without_confirmation(self):
        response = self.client.delete('/products/delete', json={
            'product_id': 1,
            'confirmation': False
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Deletion requires confirmation')

if __name__ == '__main__':
    unittest.main()
```