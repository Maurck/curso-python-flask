from flask import jsonify
from models.user import User
from utils.utils import response
from apis.endpoint.endpoint_flow import EndpointFlow


class GetUsersFlow(EndpointFlow):

    def __init__(self, request):
        super().__init__(request)

    def execute(self):
        try:
            request = self.request
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

