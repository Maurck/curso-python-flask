from flask import request
from models.user import User
from utils.utils import response, create_jwt
from apis.endpoint.endpoint_flow import EndpointFlow


class LoginFlow(EndpointFlow):

    def __init__(self, request, bcrypt):
        super().__init__(request)
        self.bcrypt = bcrypt

    def execute(self):
        # 'intentamos' ejecutar el código que añade usuarios mediante un 'try'
        try:
            request = self.request
            # obtenemos los datos del usuario a crear desde el cliente el cual los mandó en data tipo 'form'
            email = request.form['email']

            # obtenemos el usuario con su email
            user: User = User.query.filter_by(email=email).first()

            if user is None:
                raise Exception("El usuario no existe")

            password = request.form['password']
            user_dict = user.to_dict(with_password=True)

            if not self.bcrypt.check_password_hash(user_dict['password'], password):
                raise Exception("Contraseña incorrecta")

            access_token = create_jwt(user_dict)
            return response(res=user_dict, token=access_token, code=201)

        # en caso haya una excepcion (error) al ejecutar el código
        except Exception as e:
            # devolvemos al cliente el mensaje de error, el código de status 500 (error de servidor interno) y data vacia
            return response("No se pudo loguear el usuario", code=500, error=e)

