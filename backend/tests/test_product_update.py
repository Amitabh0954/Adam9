import unittest
from app import create_app
from backend.models import db, Product

class ProductUpdateTestCase(unittest.TestCase):
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

    def test_update_product(self):
        response = self.client.put('/products/update', json={
            'product_id': 1,
            'name': 'Updated Product',
            'description': 'This is an updated test product',
            'price': 12.99
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Product updated successfully')
        self.assertEqual(data['product'], 'Updated Product')

        # Verify product update
        product = Product.query.get(1)
        self.assertEqual(product.name, 'Updated Product')
        self.assertEqual(product.description, 'This is an updated test product')
        self.assertEqual(product.price, 12.99)

    def test_update_product_with_existing_name(self):
        self.client.put('/products/update', json={
            'product_id': 1,
            'name': 'Updated Product',
            'description': 'This is an updated test product',
            'price': 12.99
        })
        response = self.client.put('/products/update', json={
            'product_id': 1,
            'name': 'Updated Product',
            'description': 'This is another updated test product',
            'price': 14.99
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Product name must be unique')

if __name__ == '__main__':
    unittest.main()
```