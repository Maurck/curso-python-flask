from apis.endpoint.parameters_validator import ParametersValidator

class Endpoint:

    def __call__(self, flow, request, schema={}):

        try:
            validator = ParametersValidator()
            validation_errors = validator(request, request.form.copy(), schema)
            if validation_errors:
                return validation_errors

            return flow.execute()
        except Exception as e:
            # devolvemos al cliente el mensaje de error, el código de status 500 (error de servidor interno) y data vacia
            return response("No se pudo acceder al endpoint", code=500, error=e)
