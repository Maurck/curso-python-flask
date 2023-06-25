import random

NUMERO_MAXIMO = 138976
numero_secreto = random.randint(1, NUMERO_MAXIMO)
intentos = 0

ultimo_max = 0
ultimo_min = 0
esMayor=True
adivinado=False

def adivinanzas_usuario():
    while not adivinado:
        num_usuario = input("Adivina el número secreto (entre 1 y 100): ")
        # Validar la entrada del usuario
        if not num_usuario.isdigit():
            print("Error: Debes ingresar un número.")
            continue
        num_usuario = int(num_usuario)
        intentos = intentos+1
        adivinado = adivinar(num_usuario)

def adivinar(num_usuario):
    global ultimo_max
    global esMayor
    global ultimo_min
    # Comparar el número secreto y la entrada del usuario
    if num_usuario == numero_secreto:
        print("¡Felicitaciones! Adivinaste el número secreto en", intentos-1, "intentos.")
        return True
    elif num_usuario < numero_secreto:
        ultimo_min = num_usuario
        esMayor = True
        print("El número secreto es mayor. Intenta nuevamente.")
    else:
        print("El número secreto es menor. Intenta nuevamente.")
        ultimo_max = num_usuario
        esMayor = False
    return False

def adivinacion_binaria(num_actual):
    global ultimo_max
    global esMayor
    global ultimo_min
    if num_actual==NUMERO_MAXIMO:
        return NUMERO_MAXIMO/2;
    elif esMayor:
        return num_actual + (ultimo_max-num_actual)/2
    else:
        return ultimo_min + (num_actual-ultimo_min)/2

def adivinanzas_busqueda_binaria():
    global ultimo_max
    global esMayor
    global ultimo_min
    global adivinado
    global intentos
    num_actual = NUMERO_MAXIMO
    ultimo_max = NUMERO_MAXIMO
    while not adivinado:
        num_usuario = adivinacion_binaria(num_actual)
        num_actual = int(num_usuario)
        intentos = intentos+1
        print("numero secreto:", numero_secreto, " numero actual:", num_actual)
        adivinado = adivinar(num_actual)

adivinanzas_busqueda_binaria()