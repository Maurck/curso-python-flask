# variables
variable: int = 30
variable_entero = 40
variable2: str = "hola"
variable3: float = 6.3
variable4: bool = True

# condiciones
if variable == 10:
    print("es igual a 10")
elif variable == 20:
    print("no es igual a 10, es igual a 20")
else:
    print("no es igual a 10 ni 20")

match variable:
    case 10:
        print("es igual a 10")
        break
    case 10:
        print("es igual a 20")

# variable == 10 ? print() : print()
estado
es_bonito = True
estado = "Es bonito" if 10 < 5 else "No es bonito"

# bucles
for i in range(0, 10):
    print(i)

i = 0
while i < 10:
    print(i)
    i=i+1

# funciones
def sum(a: int, b: int):
    return a + b

print(sum(variable,variable_entero))

# excepciones
try:
    int("hola")
except:
    print("'hola' no se puede convertir en un numero")

# importaciones
import random

random_number = random.randint(0, 10)
print(random_number)