from backend.repositories.auth.user_repository import UserRepository
from backend.models.user import User

class ProfileService:
    @staticmethod
    def update_profile(user_id: int, username: str, email: str, password: Optional[str] = None) -> User:
        user = UserRepository.get_user_by_id(user_id)
        if UserRepository.get_user_by_username(username) and user.username != username:
            raise ValueError("Username must be unique")
        if UserRepository.get_user_by_email(email) and user.email != email:
            raise ValueError("Email must be unique")
        user.username = username
        user.email = email
        if password:
            user.set_password(password)
        UserRepository.save_user(user)
        return user