from collections import defaultdict
from datetime import datetime, timedelta

class LimitManager:
    login_attempts = defaultdict(list)

    @staticmethod
    def record_login_attempt(user_id: int, success: bool) -> None:
        now = datetime.utcnow()
        attempts = LimitManager.login_attempts[user_id]
        # Keep only attempts within last 15 minutes
        attempts = [attempt for attempt in attempts if now - attempt < timedelta(minutes=15)]
        attempts.append(now)
        LimitManager.login_attempts[user_id] = attempts
        
        if success:
            LimitManager.login_attempts[user_id] = []

    @staticmethod
    def can_attempt_login(user_id: int) -> bool:
        attempts = LimitManager.login_attempts[user_id]
        now = datetime.utcnow()
        recent_attempts = [attempt for attempt in attempts if now - attempt < timedelta(minutes=15)]
        return len(recent_attempts) < 5