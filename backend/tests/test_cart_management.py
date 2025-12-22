import unittest
from app import create_app
from backend.models import db, Product, Cart

class CartManagementTestCase(unittest.TestCase):
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

    def test_create_cart(self):
        response = self.client.post('/cart/create', json={
            'user_id': 1
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Cart created successfully')

    def test_add_product_to_cart(self):
        response = self.client.post('/cart/create', json={
            'user_id': 1
        })
        cart_id = response.get_json()['cart_id']
        response = self.client.post('/cart/add', json={
            'cart_id': cart_id,
            'product_id': 1,
            'quantity': 2
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Product added to cart successfully')

    def test_add_product_to_cart_invalid_quantity(self):
        response = self.client.post('/cart/create', json={
            'user_id': 1
        })
        cart_id = response.get_json()['cart_id']
        response = self.client.post('/cart/add', json={
            'cart_id': cart_id,
            'product_id': 1,
            'quantity': 0
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Quantity must be a positive number')

if __name__ == '__main__':
    unittest.main()
```