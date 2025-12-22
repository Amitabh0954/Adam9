from flask import Flask
from backend.config.config import Config

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    from backend.controllers.auth.user_controller import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)