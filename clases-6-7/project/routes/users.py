# Blueprint: representa una colección de rutas que pueden ser registradas luego en la aplicación, se utiliza 
# para modularizar las rutas
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, current_user
from utils.utils import response, create_jwt, admin_required
from models.user import User
from config.database import db
from config.config import bcrypt, jwt

# Instanciamos (creamos) un blueprint que contenga las rutas de los usuarios, 
# anteriormente estas se enlazaban a 'app' directamente, pero ahora se enlazan a 'users_bp'
# para luego enlazar este con 'app'
users_bp = Blueprint('user', __name__)

# creamos la ruta que obtiene todos los usuarios
@users_bp.route('/')
@admin_required()
def get_users():
    try:
        # obtenemos todos los usuarios con User.query.all()
        users: User = User.query.all()

        # almacenamos el json con los datos de los usuarios en un arreglo
        users_json = []
        for user in users:
            users_json.append(user.to_dict())

        # devolvemos al cliente los usuarios obtenidos junto con un mensaje y un código de status = 200 (exitoso)
        return response("Usuarios obtenidos", users_json)
    except Exception as e:
        # devolvemos al cliente el mensaje de error, el código de status 500 (error de servidor interno) y data vacia
        return response("No se pudo obtener los usuario", code=500, error=e)

# creamos la ruta para registrar usuarios
@users_bp.route('/register', methods=['POST'])
def register():
    # 'intentamos' ejecutar el código que registra usuarios mediante un 'try'
    try:
        # obtenemos los datos del usuario a registrar desde el cliente el cual los mandó en data tipo 'form'
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        # creamos el objeto usuario desde su modelo
        new_user = User(
            username,
            password=bcrypt.generate_password_hash(request.form['password']).decode('utf-8'),
            email=email,
            role=role
        )

        # añadimos el usuario y ejecutamos la acción
        db.session.add(new_user)
        db.session.commit()
        user_dict = new_user.to_dict()

        access_token = create_jwt(user_dict)
        # devolvemos al cliente el usuario creado junto con un mensaje y un código de status = 201 (exitoso para creacion) 
        return response("Usuario añadido", user_dict, access_token, 201)
    # en caso haya una excepcion (error) al ejecutar el código
    except Exception as e:
        # devolvemos al cliente el mensaje de error, el código de status 500 (error de servidor interno) y data vacia
        return response("No se pudo registrar el usuario", code=500, error=e)

# creamos la ruta para loguear usuarios
@users_bp.route('/login', methods=['POST'])
def login():
    # 'intentamos' ejecutar el código que añade usuarios mediante un 'try'
    try:
        # obtenemos los datos del usuario a crear desde el cliente el cual los mandó en data tipo 'form'
        email = request.form['email']

        # obtenemos el usuario con su email
        user: User = User.query.filter_by(email=email).first()

        if user is None:
            raise Exception("El usuario no existe")

        password = request.form['password']
        user_dict = user.to_dict(with_password=True)

        if not bcrypt.check_password_hash(user_dict['password'], password):
            raise Exception("Contraseña incorrecta")

        access_token = create_jwt(user_dict)
        return response(res=user_dict, token=access_token, code=201)

    # en caso haya una excepcion (error) al ejecutar el código
    except Exception as e:
        # devolvemos al cliente el mensaje de error, el código de status 500 (error de servidor interno) y data vacia
        return response("No se pudo loguear el usuario", code=500, error=e)


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

        user_dict = current_user.to_dict();

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