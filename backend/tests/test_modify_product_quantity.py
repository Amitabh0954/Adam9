import unittest
from app import create_app
from backend.models import db, Product, Cart, CartItem

class ModifyProductQuantityTestCase(unittest.TestCase):
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

    def test_modify_product_quantity(self):
        response = self.client.patch('/cart_item/modify', json={
            'cart_id': 1,
            'product_id': 1,
            'quantity': 3
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Product quantity updated successfully')

        # Verify quantity update
        cart_item = CartItem.query.filter_by(cart_id=1, product_id=1).first()
        self.assertIsNotNone(cart_item)
        self.assertEqual(cart_item.quantity, 3)

    def test_modify_product_quantity_invalid(self):
        response = self.client.patch('/cart_item/modify', json={
            'cart_id': 1,
            'product_id': 1,
            'quantity': 0
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Quantity must be a positive number')

    def test_modify_nonexistent_product_quantity(self):
        response = self.client.patch('/cart_item/modify', json={
            'cart_id': 1,
            'product_id': 999,
            'quantity': 3
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Cart item not found')

if __name__ == '__main__':
    unittest.main()
```