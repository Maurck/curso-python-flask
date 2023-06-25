# variables
a = 10
b: int = 20
c: float = 20

# condicionales
if a == b:
    print("a es igual a b")
elif a == 20:
    print("a no es igual a b y es 20")
else:
    print("a no es igual a b y es diferente de 20")

match a:
    case 10:
        print("a es 10")
    case 20:
        print("a es 20")

# bucles
for i in range(0, 10):
    print(i)

i = 0
while i < 10:
    print(i)
    i=i+1

# funciones
def sum(a: int, b: int) -> int:
    return a + b

print(sum(10+20))

# excepciones
try:
    int("string")
except:
    print("'string' no es un numero")

# importaciones
import random

random_number = random.randint(1, 100)
print(random_number)