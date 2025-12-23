from backend.models.user import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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