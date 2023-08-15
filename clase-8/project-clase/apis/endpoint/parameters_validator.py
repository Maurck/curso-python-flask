from utils.utils import validate_parameters

class ParametersValidator:

    def __call__(self, request, data, schema):
        return validate_parameters(data, schema)
