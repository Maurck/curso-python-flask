# Blueprint: representa una colección de rutas que pueden ser registradas luego en la aplicación, se utiliza 
# para modularizar las rutas
from flask import Blueprint
from utils.utils import response
from models.user import User
from config.database import db

# Instanciamos (creamos) un blueprint que contenga las rutas de los usuarios, 
# anteriormente estas se enlazaban a 'app' directamente, pero ahora se enlazan a 'users_bp'
# para luego enlazar este con 'app'
users_bp = Blueprint('user', __name__)

# creamos la ruta que obtiene todos los usuarios
@users_bp.route('/')
def get_users():
    # obtenemos todos los usuarios con User.query.all()
    users: User = User.query.all()

    # almacenamos el json con los datos de los usuarios en un arreglo
    users_json = []
    for user in users:
        users_json.append(user.to_dict())

    # devolvemos al cliente los usuarios obtenidos junto con un mensaje y un código de status = 200 (exitoso)
    return response("Usuarios obtenidos", users_json, 200)

# creamos la ruta para añadir usuarios
@users_bp.route('/', methods=['POST'])
def add_users():
    # 'intentamos' ejecutar el código que añade usuarios mediante un 'try'
    try:
        # obtenemos los datos del usuario a crear desde el cliente el cual los mandó en data tipo 'form'
        username = request.form['username']
        email = request.form['email']

        # creamos el objeto usuario desde su modelo
        user = User(username, email)

        # añadimos el usuario y ejecutamos la acción
        db.session.add(user)
        db.session.commit()

        # devolvemos al cliente el usuario creado junto con un mensaje y un código de status = 201 (exitoso para creacion) 
        return response("Usuario añadido", user.to_dict(), 201)
    # en caso haya una excepcion (error) al ejecutar el código
    except:
        # devolvemos al cliente el mensaje de error, el código de status 500 (error de servidor interno) y data vacia
        return response("No se pudo crear el usuario", {}, 500)

# creamos la ruta para modificar usuarios
@users_bp.route('/', methods=['PUT'])
def modify_user():
    try:
        # obtenemos los datos de los usuarios desde los parametros de query:
        # localhost:5000?user_id=10&username=usuario10&email=email10
        user_id = request.args['user_id']
        username = request.args['username']
        email = request.args['email']

        # obtenemos el usuario con su id, si no se puede devolvemos un error 404 (no se encontró)
        user: User = User.query.get_or_404(user_id)

        # establecemos los nuevos datos
        user.username = username
        user.email = email

        # ejecutamos la acción
        db.session.commit()

        # devolvemos al cliente el usuario editado junto con un mensaje y un código de status = 201 (exitoso para modificacion) 
        return response("Se actualizó el usuario", user.to_dict(), 201)
    except:
        # devolvemos al cliente el mensaje de error, el código de status 500 (error de servidor interno) y data vacia
        return response("No se pudo actualizar el usuario", {}, 500)

# creamos la ruta para borrar usuarios
@users_bp.route('/', methods=['DELETE'])
def delete_user():
    # intentamos borrar el usuario
    try:
        user_id = request.args['user_id']
        user = User.query.get_or_404(user_id)
        # borramos al usuario y ejecutamos la acción
        db.session.delete(user)
        db.session.commit()
        # devolvemos al cliente el usuario borrado junto con un mensaje y un código de status = 200 (exitoso) 
        return response("Usuario borrado", user.to_dict(), 200)
    except:
         # devolvemos al cliente el mensaje de error, el código de status 500 (error de servidor interno) y data vacia
        return response("Usuario no pudo ser borrado", {}, 500)