from backend.repositories.auth.user_repository import UserRepository
from backend.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    """Service class for user-related operations"""

    @staticmethod
    def register_user(username: str, email: str, password: str) -> User:
        hashed_password = generate_password_hash(password, method='sha256')
        return UserRepository.add_user(username, email, hashed_password)

    @staticmethod
    def verify_user(email: str, password: str) -> bool:
        user = UserRepository.get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            return True
        return False

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def get_user_by_username(username: str) -> User:
        return UserRepository.get_user_by_username(username)