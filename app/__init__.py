from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        db.create_all()  # aqui cria as tabelas

    from .routes import usuario_routes
    app.register_blueprint(usuario_routes.bp)

    return app
