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
        
    @staticmethod
    def get_user_by_email(email: str) -> User:
        return UserRepository.get_user_by_email(email)
        
    @staticmethod
    def update_user_profile(current_email: str, new_username: str, new_email: str) -> User:
        user = UserRepository.get_user_by_email(current_email)
        if user:
            if new_email != current_email and UserRepository.get_user_by_email(new_email):
                raise ValueError('Email already registered')
            user.username = new_username
            user.email = new_email
            db.session.commit()
            return user
        raise ValueError('User not found')