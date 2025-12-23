from typing import Optional
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    token = db.Column(db.String(256), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)

class SessionRepository:
    """Repository for the Session model"""
    
    @staticmethod
    def create_session(user_id: int, token: str, duration: int) -> Session:
        expires_at = datetime.utcnow() + timedelta(minutes=duration)
        session = Session(user_id=user_id, token=token, created_at=datetime.utcnow(), expires_at=expires_at)
        db.session.add(session)
        db.session.commit()
        return session
    
    @staticmethod
    def get_session_by_token(token: str) -> Optional[Session]:
        return Session.query.filter_by(token=token).first()
    
    @staticmethod
    def delete_session(token: str) -> None:
        Session.query.filter_by(token=token).delete()
        db.session.commit()