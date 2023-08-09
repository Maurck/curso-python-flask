import enum
from config.database import db
from config.config import jwt

class Role(enum.Enum):
    USER = 'USER'
    ADMIN = 'ADMIN'

# creamos el modelo (representacion en código de la tabla) usuario
class User(db.Model):
    # definimos sus campos (columnas)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=False)
    password = db.Column(db.String(100), unique=False)
    email = db.Column(db.String(100), unique=True)
    role = db.Column(db.Enum(Role))

    def __init__(self, username: str, password: str, email: str, role: Role):
        self.username = username
        self.password = password
        self.email = email
        self.role = role

    # establecemos un método que devuelva la informacción como un diccionario
    def to_dict(self, with_password=False):
        user_dict = {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": str(self.role)
        }

        if with_password:
            user_dict["password"] = self.password

        return user_dict

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(email=identity).one_or_none()