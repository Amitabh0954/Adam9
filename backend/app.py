from flask import Flask
from backend.config.config import Config
from backend.models.user import db
from backend.controllers.auth.user_controller import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
```