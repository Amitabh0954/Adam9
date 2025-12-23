import uuid
from datetime import datetime
from backend.repositories.auth.session_repository import SessionRepository, Session

class SessionService:
    """Service class for session-related operations"""
    
    @staticmethod
    def create_session(user_id: int, duration: int = 30) -> Session:
        token = str(uuid.uuid4())
        session = SessionRepository.create_session(user_id, token, duration)
        return session
    
    @staticmethod
    def validate_session(token: str) -> bool:
        session = SessionRepository.get_session_by_token(token)
        if session and session.expires_at > datetime.utcnow():
            return True
        return False
    
    @staticmethod
    def delete_session(token: str) -> None:
        SessionRepository.delete_session(token)