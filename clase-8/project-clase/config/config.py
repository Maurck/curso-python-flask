import os
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

def config_app(name):
    load_dotenv()
    app = Flask(name)
    # configuramos el string de conexión con el servidor de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    app.secret_key = os.getenv('SECRET_KEY')
    return app

bcrypt = Bcrypt()
jwt = JWTManager()