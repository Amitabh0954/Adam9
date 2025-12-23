from backend.models.user import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProfileRepository:
    """Repository for the User model profile updates"""
    
    @staticmethod
    def update_profile(user_id: int, username: str, email: str, image_file: str) -> User:
        user = User.query.get(user_id)
        if user:
            user.username = username
            user.email = email
            user.image_file = image_file
            db.session.commit()
        return user
    
    @staticmethod
    def get_profile(user_id: int) -> User:
        return User.query.get(user_id)