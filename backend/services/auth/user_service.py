from backend.repositories.auth.user_repository import UserRepository
from backend.models.user import User

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
```