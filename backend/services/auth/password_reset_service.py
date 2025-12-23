from datetime import datetime, timedelta
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from flask_mail import Message
from backend.models.user import User
from backend.repositories.auth.user_repository import UserRepository
from backend.config.config import Config
from backend import mail

class PasswordResetService:
    """Service class for password reset operations"""

    @staticmethod
    def generate_reset_token(email: str) -> str:
        serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        return serializer.dumps(email, salt=Config.SECURITY_PASSWORD_SALT)

    @staticmethod
    def confirm_reset_token(token: str, expiration: int = 86400) -> str:
        serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        try:
            email = serializer.loads(
                token, salt=Config.SECURITY_PASSWORD_SALT, max_age=expiration
            )
        except (SignatureExpired, BadSignature):
            return None
        return email

    @staticmethod
    def send_reset_email(email: str) -> None:
        user = UserRepository.get_user_by_email(email)
        if not user:
            return
        
        token = PasswordResetService.generate_reset_token(email)
        reset_url = f"{Config.FRONTEND_URL}/reset-password/{token}"
        msg = Message(
            subject="Password Reset Requested",
            recipients=[email],
            body=f"Please click the link to reset your password: {reset_url}",
            sender=Config.MAIL_DEFAULT_SENDER
        )
        mail.send(msg)
    
    @staticmethod
    def reset_password(email: str, new_password: str) -> bool:
        user = UserRepository.get_user_by_email(email)
        if user:
            user.password = generate_password_hash(new_password)
            db.session.commit()
            return True
        return False