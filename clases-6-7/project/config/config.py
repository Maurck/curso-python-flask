from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

def config_app(name):
    app = Flask(name)
    # configuramos el string de conexión con el servidor de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost:3306/flask_db'
    app.secret_key = 'SECRET_KEY'
    return app

bcrypt = Bcrypt()
jwt = JWTManager()