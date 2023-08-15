from flask import jsonify, request
from models.user import User
from utils.utils import response, create_jwt
from apis.endpoint.endpoint_flow import EndpointFlow


class RegisterFlow(EndpointFlow):

    def __init__(self, request, db, bcrypt):
        super().__init__(request)
        self.db = db
        self.bcrypt = bcrypt

    def execute(self):
        # 'intentamos' ejecutar el código que registra usuarios mediante un 'try'
        try:
            request = self.request
            db = self.db
            bcrypt = self.bcrypt

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

