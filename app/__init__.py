from flask import Flask
from app.config import Config
from app.db import db
from flask_login import LoginManager
from app.models.usuario import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config['SECRET_KEY'] = 'ch4v3_h1p3r_s3cr3t4'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registro dos blueprints
    from app.routes.login_routes import login_bp
    from app.routes.register_routes import register_bp
    from app.routes.home_routes import home_bp
    from app.routes.carrinho_routes import carrinho_bp
    app.register_blueprint(carrinho_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(home_bp)


    return app