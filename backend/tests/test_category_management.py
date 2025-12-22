import unittest
from app import create_app
from backend.models import db, Category

class CategoryManagementTestCase(unittest.TestCase):
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

    def test_add_category(self):
        response = self.client.post('/categories/add', json={
            'name': 'Electronics'
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Category added successfully')
        self.assertEqual(data['category'], 'Electronics')

    def test_add_category_with_existing_name(self):
        self.client.post('/categories/add', json={
            'name': 'Electronics'
        })
        response = self.client.post('/categories/add', json={
            'name': 'Electronics'
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Category name must be unique')

    def test_get_all_categories(self):
        self.client.post('/categories/add', json={
            'name': 'Electronics'
        })
        self.client.post('/categories/add', json={
            'name': 'Computers',
            'parent_id': 1
        })
        response = self.client.get('/categories/all')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'Electronics')
        self.assertEqual(data[1]['name'], 'Computers')

if __name__ == '__main__':
    unittest.main()
```