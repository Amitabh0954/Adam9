import uuid
from backend.repositories.auth.password_reset_repository import PasswordResetRepository, PasswordReset
from backend.repositories.auth.user_repository import UserRepository
from backend.models.user import User

class PasswordResetService:
    """Service class for password reset operations"""
    
    @staticmethod
    def request_password_reset(email: str) -> PasswordReset:
        token = str(uuid.uuid4())
        password_reset = PasswordResetRepository.create_password_reset(email, token)
        return password_reset
    
    @staticmethod
    def reset_password(token: str, new_password: str) -> bool:
        password_reset = PasswordResetRepository.get_password_reset_by_token(token)
        if password_reset and password_reset.expires_at > datetime.utcnow():
            user = UserRepository.get_user_by_email(password_reset.email)
            if user:
                user.password = new_password
                db.session.commit()
                PasswordResetRepository.delete_password_reset(token)
                return True
        return False