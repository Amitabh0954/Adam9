import unittest
from app import create_app
from backend.models import db, User
from backend.services.auth.password_reset_service import PasswordResetService

class PasswordResetTestCase(unittest.TestCase):
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

    def test_password_reset_request(self):
        response = self.client.post('/password_reset/request-reset', json={
            'email': 'test@example.com'
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', data)

    def test_password_reset(self):
        token = PasswordResetService.generate_reset_token('test@example.com')
        response = self.client.post('/password_reset/reset-password', json={
            'token': token,
            'new_password': 'newpassword123'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Password has been reset successfully')

        # Verify password change
        user = User.query.filter_by(email='test@example.com').first()
        self.assertTrue(user.check_password('newpassword123'))

if __name__ == '__main__':
    unittest.main()
```