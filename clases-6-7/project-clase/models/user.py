from config.database import db

# creamos el modelo (representacion en código de la tabla) usuario
class User(db.Model):
    # definimos sus campos (columnas)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=False)
    email = db.Column(db.String(100), unique=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    # establecemos un método que devuelva la informacción como un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }