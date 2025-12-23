from backend.repositories.auth.user_repository import UserRepository
from backend.models.user import User

class ProfileService:
    """Service class for profile-related operations"""

    @staticmethod
    def get_profile(user_id: int) -> User:
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise ValueError('User not found')
        return user

    @staticmethod
    def update_profile(user_id: int, email: str = None, new_password: str = None) -> User:
        return UserRepository.update_user(user_id, email, new_password)
```