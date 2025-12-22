from backend.repositories.auth.user_repository import UserRepository
from backend.models.user import User

class UserService:
    @staticmethod
    def register_user(username: str, email: str, password: str) -> User:
        if UserRepository.get_user_by_email(email):
            raise ValueError("Email must be unique")
        if len(password) < 8:
            raise ValueError("Password must meet security criteria")
        return UserRepository.create_user(username, email, password)