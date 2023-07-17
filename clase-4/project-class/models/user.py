class User:
    name: str
    age: int
    email: str

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greet(self):
        return f'Mi nombre es {self.name}, mi edad es {self.age} y mi correo es {self.email}'

