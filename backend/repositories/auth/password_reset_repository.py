from datetime import datetime, timedelta
from typing import Optional
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PasswordReset(db.Model):
    __tablename__ = 'password_resets'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    token = db.Column(db.String(256), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)

class PasswordResetRepository:
    """Repository for the PasswordReset model"""
    
    @staticmethod
    def create_password_reset(email: str, token: str) -> PasswordReset:
        expires_at = datetime.utcnow() + timedelta(hours=24)
        password_reset = PasswordReset(email=email, token=token, expires_at=expires_at)
        db.session.add(password_reset)
        db.session.commit()
        return password_reset
    
    @staticmethod
    def get_password_reset_by_token(token: str) -> Optional[PasswordReset]:
        return PasswordReset.query.filter_by(token=token).first()
    
    @staticmethod
    def delete_password_reset(token: str) -> None:
        PasswordReset.query.filter_by(token=token).delete()
        db.session.commit()