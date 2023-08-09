from flask import jsonify
from models.user import Role
from flask_jwt_extended import create_access_token

def response(msg='', res='', token='', code=200, error=''):
    response_json = {}
    if msg != '':
        response_json["msg"] = msg
    if res != '':
        response_json["res"] = res
    if token != '':
        response_json["token"] = token
    if error != '':
        response_json["error"] = str(error)

    return jsonify(response_json), code

def create_jwt(user_dict):
    additional_claims = {
        'role': str(user_dict["role"])
    }

    access_token = create_access_token(user_dict["email"], additional_claims=additional_claims)
    return access_token

from flask_jwt_extended import get_jwt
from flask_jwt_extended import verify_jwt_in_request
from functools import wraps

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["role"] == str(Role.ADMIN):
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Se necesita ser administrador para acceder a este endpoint"), 403

        return decorator

    return wrapper