class User:
    name: str
    age: int
    email: str

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def info(self):
        return f'Mi nombre es {self.name}, tengo {self.age} años y mi correo es {self.email}'

