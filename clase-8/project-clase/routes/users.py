# Blueprint: representa una colección de rutas que pueden ser registradas luego en la aplicación, se utiliza 
# para modularizar las rutas
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, current_user
from utils.utils import response, create_jwt, admin_required
from models.user import User
from config.database import db
from config.config import bcrypt

from apis.endpoint.endpoint import Endpoint

from apis.user.get_users.get_users_flow import GetUsersFlow

from apis.user.register.register_flow import RegisterFlow
from apis.user.register.register_query_schema import register_query_schema

from apis.user.login.login_flow import LoginFlow
from apis.user.login.login_query_schema import login_query_schema

# Instanciamos (creamos) un blueprint que contenga las rutas de los usuarios, 
# anteriormente estas se enlazaban a 'app' directamente, pero ahora se enlazan a 'users_bp'
# para luego enlazar este con 'app'
users_bp = Blueprint('user', __name__)

# creamos la ruta que obtiene todos los usuarios
@users_bp.route('/')
@admin_required()
def get_users():
    get_users = Endpoint()
    return get_users(GetUsersFlow(request), request)

# creamos la ruta para registrar usuarios
@users_bp.route('/register', methods=['POST'])
def register():
    register = Endpoint()
    return register(RegisterFlow(request, db, bcrypt), request, register_query_schema)

# creamos la ruta para loguear usuarios
@users_bp.route('/login', methods=['POST'])
def login():
    login = Endpoint()
    return login(LoginFlow(request, bcrypt), request, login_query_schema)

# creamos la ruta para modificar usuarios
@jwt_required()
@users_bp.route('/', methods=['PUT'])
def modify_user():
    try:
        # obtenemos los datos de los usuarios desde los parametros de query:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if current_user is None:
            raise Exception("El usuario no existe")

        new_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # establecemos los nuevos datos
        current_user.username = username
        current_user.password = new_password
        current_user.email = email

        # ejecutamos la acción
        db.session.commit()

        user_dict = current_user.to_dict()

        access_token = create_jwt(user_dict)
        # devolvemos al cliente el usuario editado junto con un mensaje y un código de status = 201 (exitoso para modificacion) 
        return response("Se actualizó el usuario", user_dict, token=access_token, code=201)
    except Exception as e:
        # devolvemos al cliente el mensaje de error, el código de status 500 (error de servidor interno) y data vacia
        return response("No se pudo actualizar el usuario", code=500, error=e)

# creamos la ruta para borrar usuarios
@users_bp.route('/', methods=['DELETE'])
@admin_required()
def delete_user():
    # intentamos borrar el usuario
    try:
        email = request.args['email']
        user: User = User.query.filter_by(email=email).first()

        if user is None:
            raise Exception("El usuario no existe")

        # borramos al usuario y ejecutamos la acción
        db.session.delete(user)
        db.session.commit()
        # devolvemos al cliente el usuario borrado junto con un mensaje y un código de status = 200 (exitoso) 
        return response("Usuario borrado", user.to_dict(), code=200)
    except Exception as e:
        # devolvemos al cliente el mensaje de error, el código de status 500 (error de servidor interno) y data vacia
        return response("No se pudo borrar el usuario", code=500, error=e)

# creamos una ruta protegida con el rol de administrador
@users_bp.route('/admin')
@admin_required()
def admin():
    return response(msg="Eres administrador!")