from backend.repositories.auth.profile_repository import ProfileRepository
from backend.models.user import User

class ProfileService:
    """Service class for user profile-related operations"""
    
    @staticmethod
    def update_profile(user_id: int, username: str, email: str, image_file: str) -> User:
        user = ProfileRepository.update_profile(user_id, username, email, image_file)
        return user
    
    @staticmethod
    def get_profile(user_id: int) -> User:
        return ProfileRepository.get_profile(user_id)