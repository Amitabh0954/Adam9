from datetime import datetime, timedelta
from typing import Optional

class SessionManager:
    sessions = {}

    @staticmethod
    def create_session(user_id: int) -> str:
        session_id = f"{user_id}_{datetime.utcnow().timestamp()}"
        SessionManager.sessions[session_id] = {
            'user_id': user_id, 
            'created_at': datetime.utcnow(),
            'last_active_at': datetime.utcnow()
        }
        return session_id

    @staticmethod
    def get_session(session_id: str) -> Optional[dict]:
        session = SessionManager.sessions.get(session_id)
        if session and datetime.utcnow() - session['last_active_at'] < timedelta(minutes=30):
            session['last_active_at'] = datetime.utcnow()
            return session
        return None

    @staticmethod
    def invalidate_session(session_id: str) -> None:
        if session_id in SessionManager.sessions:
            del SessionManager.sessions[session_id]