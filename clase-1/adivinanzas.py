import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = input("Adivina el número secreto (entre 1 y 100): ")
    
    # Validar la entrada del usuario
    if not intento.isdigit():
        print("Error: Debes ingresar un número.")
        continue
    
    intento = int(intento)
    intentos += 1
    
    # Comparar el número secreto y la entrada del usuario
    if intento == numero_secreto:
        print("¡Felicitaciones! Adivinaste el número secreto en", intentos, "intentos.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor. Intenta nuevamente.")
    else:
        print("El número secreto es menor. Intenta nuevamente.")