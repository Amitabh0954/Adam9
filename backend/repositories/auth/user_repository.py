from backend.models.user import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserRepository:
    """Repository for the User model"""

    @staticmethod
    def add_user(username: str, email: str, password: str) -> User:
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_email(email: str) -> User:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()