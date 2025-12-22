import unittest
from app import create_app
from backend.models import db, User

class ProfileManagementTestCase(unittest.TestCase):
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

    def test_update_profile(self):
        response = self.client.put('/auth/profile/update', json={
            'user_id': 1,
            'username': 'updateduser',
            'email': 'updated@example.com',
            'password': 'newpassword123'
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Profile updated successfully')
        self.assertEqual(data['user'], 'updateduser')

        # Verify profile update
        user = User.query.get(1)
        self.assertEqual(user.username, 'updateduser')
        self.assertEqual(user.email, 'updated@example.com')
        self.assertTrue(user.check_password('newpassword123'))

if __name__ == '__main__':
    unittest.main()
```