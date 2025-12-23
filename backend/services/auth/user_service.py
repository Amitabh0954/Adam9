from werkzeug.security import generate_password_hash
from backend.repositories.auth.user_repository import UserRepository
from backend.models.user import User

class UserService:
    """Service class for user-related operations"""
    
    @staticmethod
    def register_user(username: str, email: str, password: str) -> User:
        hashed_password = generate_password_hash(password)
        user = UserRepository.create_user(username, email, hashed_password)
        return user