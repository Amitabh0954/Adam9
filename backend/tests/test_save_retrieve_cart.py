import unittest
from app import create_app
from backend.models import db, Product, Cart, CartItem

class SaveRetrieveCartTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.create_test_data()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def create_test_data(self):
        # Create a test product
        product = Product(name='Test Product', description='This is a test product', price=10.99)
        db.session.add(product)
        db.session.commit()
        
        # Create a test cart
        cart = Cart(user_id=1)
        db.session.add(cart)
        db.session.commit()

        # Add product to cart
        cart_item = CartItem(cart_id=cart.id, product_id=product.id, quantity=1)
        db.session.add(cart_item)
        db.session.commit()

    def test_save_cart_state(self):
        response = self.client.post('/cart/save', json={
            'user_id': 1,
            'cart_id': 1
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Cart state saved successfully')

    def test_retrieve_saved_cart(self):
        response = self.client.get('/cart/retrieve', query_string={'user_id': 1})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['cart_id'], 1)
        self.assertEqual(len(data['items']), 1)
        self.assertEqual(data['items'][0]['product_id'], 1)
        self.assertEqual(data['items'][0]['quantity'], 1)

    def test_retrieve_no_cart(self):
        response = self.client.get('/cart/retrieve', query_string={'user_id': 999})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'No saved cart for user')

if __name__ == '__main__':
    unittest.main()
```