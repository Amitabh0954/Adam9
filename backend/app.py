from flask import Flask
from flask_session import Session
from backend.config.config import Config
from backend.models.user import db
from backend.models.product import Product
from backend.models.category import Category
from backend.models.product_category import product_category
from backend.models.cart import Cart
from backend.models.cart_item import CartItem
from backend.controllers.auth.user_controller import auth_bp
from backend.controllers.auth.login_controller import login_bp
from backend.controllers.auth.password_reset_controller import reset_bp
from backend.controllers.auth.profile_controller import profile_bp
from backend.controllers.products.product_controller import product_bp
from backend.controllers.cart.cart_controller import cart_bp
from backend.controllers.products.category_controller import category_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SESSION_TYPE'] = 'filesystem'
    
    db.init_app(app)
    Session(app)
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(login_bp, url_prefix='/api/auth')
    app.register_blueprint(reset_bp, url_prefix='/api/auth')
    app.register_blueprint(profile_bp, url_prefix='/api/auth')
    app.register_blueprint(product_bp, url_prefix='/api')
    app.register_blueprint(category_bp, url_prefix='/api')
    app.register_blueprint(cart_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
```