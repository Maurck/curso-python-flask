from flask import Flask, jsonify, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
# importamos la instancia de base de datos
from config.database import db
from config.config import bcrypt, jwt
from config.config import config_app

# creamos la instancia de la aplicacion mediante la función 'config_app'
app = config_app(__name__)

# enlazamos la instancia de base de datos importada con nuestra aplicación
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# importamos el blueprint con las rutas de los usuarios
from routes.users import users_bp

# registramos el blueprint que contiene las rutas de los usuarios
app.register_blueprint(users_bp)

if __name__ == "__main__":
    # creeamos las tablas en base de datos en el contexton de la aplicación
    with app.app_context():
        db.create_all()

    # corremos el servidor de la aplicación en modo debug (recargarse cuando hayan cambios en el código)
    app.run(debug=True)