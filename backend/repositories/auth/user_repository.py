from datetime import datetime, timedelta
from backend.models.user import User
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
SECRET_KEY = 'your-secret-key'
serializer = URLSafeTimedSerializer(SECRET_KEY)

class UserRepository:
    """Repository for the User model"""

    @staticmethod
    def get_user_by_email(email: str) -> User:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def add_user(email: str, password: str) -> User:
        if UserRepository.get_user_by_email(email):
            raise ValueError('Email already registered')
        
        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id: int, email: str = None, password: str = None) -> User:
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise ValueError('User not found')

        if email:
            if UserRepository.get_user_by_email(email) and UserRepository.get_user_by_email(email).id != user_id:
                raise ValueError('Email already registered')
            user.email = email
        if password:
            user.set_password(password)
        
        db.session.commit()
        return user

    @staticmethod
    def create_password_reset_token(email: str) -> str:
        return serializer.dumps(email, salt='password-reset-salt')

    @staticmethod
    def verify_password_reset_token(token: str, expiration=86400) -> str:
        try:
            email = serializer.loads(token, salt='password-reset-salt', max_age=expiration)
        except SignatureExpired:
            raise ValueError('The password reset link has expired')
        return email