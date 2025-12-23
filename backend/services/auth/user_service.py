from backend.repositories.auth.user_repository import UserRepository
from backend.models.user import User
from flask_mail import Mail, Message
from flask import current_app as app

mail = Mail()

class UserService:
    """Service class for user-related operations"""

    @staticmethod
    def register_user(email: str, password: str) -> User:
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        
        return UserRepository.add_user(email, password)

    @staticmethod
    def authenticate_user(email: str, password: str) -> User:
        user = UserRepository.get_user_by_email(email)
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def send_password_reset_email(email: str) -> None:
        user = UserRepository.get_user_by_email(email)
        if not user:
            raise ValueError('Email not found')

        token = UserRepository.create_password_reset_token(email)
        reset_url = f"{app.config['FRONTEND_URL']}/password-reset/{token}"

        msg = Message('Password Reset Request',
                      sender='noreply@yourapp.com',
                      recipients=[email])
        msg.body = f"To reset your password, follow the link: {reset_url}\n" \
                   "This link will expire in 24 hours."

        mail.send(msg)

    @staticmethod
    def reset_password(token: str, new_password: str) -> None:
        email = UserRepository.verify_password_reset_token(token)
        user = UserRepository.get_user_by_email(email)
        if not user:
            raise ValueError('Invalid token or user does not exist')

        user.set_password(new_password)
        db.session.commit()
```