import os
from logging.config import dictConfig

class Config:
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI: str = os.getenv('DATABASE_URI', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    
    @staticmethod
    def init_app(app):
        """Initialize application with config settings."""
        dictConfig({
            'version': 1,
            'formatters': {'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }},
            'handlers': {'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            }},
            'root': {
                'level': 'INFO',
                'handlers': ['wsgi']
            }
        })