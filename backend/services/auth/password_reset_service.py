from datetime import datetime, timedelta
import uuid
from backend.repositories.auth.user_repository import UserRepository
from backend.models.user import User

class PasswordResetService:
    reset_tokens = {}

    @staticmethod
    def generate_reset_token(email: str) -> str:
        user = UserRepository.get_user_by_email(email)
        if not user:
            raise ValueError("Email not found")
        token = str(uuid.uuid4())
        PasswordResetService.reset_tokens[token] = {
            'user_id': user.id,
            'expires_at': datetime.utcnow() + timedelta(hours=24)
        }
        return token

    @staticmethod
    def validate_reset_token(token: str) -> int:
        token_data = PasswordResetService.reset_tokens.get(token)
        if not token_data or token_data['expires_at'] < datetime.utcnow():
            raise ValueError("Invalid or expired token")
        return token_data['user_id']

    @staticmethod
    def reset_password(token: str, new_password: str) -> None:
        user_id = PasswordResetService.validate_reset_token(token)
        user = UserRepository.get_user_by_id(user_id)
        user.set_password(new_password)
        UserRepository.save_user(user)
        del PasswordResetService.reset_tokens[token]