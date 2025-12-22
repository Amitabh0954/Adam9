from backend.repositories.auth.user_repository import UserRepository
from backend.services.auth.session_manager.py import SessionManager
from backend.services.auth.limit_manager.py import LimitManager

class LoginService:
    @staticmethod
    def login(username: str, password: str) -> str:
        user = UserRepository.get_user_by_username(username)
        
        if not user:
            raise ValueError("Invalid username or password")
        
        if not user.check_password(password):
            LimitManager.record_login_attempt(user.id, False)
            if not LimitManager.can_attempt_login(user.id):
                raise ValueError("Too many invalid login attempts, please try again later")
            raise ValueError("Invalid username or password")
        
        LimitManager.record_login_attempt(user.id, True)
        session_id = SessionManager.create_session(user.id)
        return session_id