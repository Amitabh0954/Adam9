import unittest
from app import create_app
from backend.models import db, User

class UserLoginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.create_test_user()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def create_test_user(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()

    def test_user_login(self):
        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'password123'
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue('session_id' in data)

    def test_invalid_login_attempts(self):
        for _ in range(6):
            response = self.client.post('/auth/login', json={
                'username': 'testuser',
                'password': 'wrongpassword'
            })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Too many invalid login attempts, please try again later')

if __name__ == '__main__':
    unittest.main()
```