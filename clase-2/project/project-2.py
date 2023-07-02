# Registro de estudiantes

# Creación de listas vacías para almacenar los datos de los estudiantes
nombres = []
edades = []
calificaciones = []

estudiantes: list = []
estudiante: dict = {}
estudiante["name"] = "Pepito"
estudiante["edad"] = 19
estudiante.append(estudiante)

estudiantes[0]["name"]
estudiantes[0]["edad"]


# Función para registrar un estudiante
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    calificacion = float(input("Ingrese la calificación del estudiante: "))

    try:
        indice = nombres.index(nombre)
        cal_list = calificaciones[indice]
        cal_list.append(calificacion)
        calificaciones[indice] = cal_list
    except:
        cal_list = []
        cal_list.append(calificacion)
        calificaciones.append(cal_list)
        edades.append(edad)
        nombres.append(nombre)
    
    print("Estudiante registrado con éxito.\n")

# Función para calcular el promedio de calificaciones de un estudiante
def calcular_promedio(nombre: str):
    if nombre in nombres:
        indice = nombres.index(nombre)
        calificaciones_estudiante = calificaciones[indice]
        promedio = sum(calificaciones_estudiante) / len(calificaciones_estudiante)
        return (nombre, promedio)
    else:
        return ()

# Función para encontrar el estudiante con la calificación más alta
def encontrar_estudiante_con_calificacion_mas_alta():
    if calificaciones:
        max_calificacion = max(calificaciones)
        indice = calificaciones.index(max_calificacion)
        estudiante = nombres[indice]
        print(f"{estudiante} tiene la calificación más alta: {max_calificacion}\n")
    else:
        print("No hay estudiantes registrados.\n")

# Loop principal del programa
while True:
    print("Bienvenido al Registro de Estudiantes")
    print("1. Registrar/Agregar calificacion a estudiante")
    print("2. Calcular promedio de calificaciones")
    print("3. Encontrar estudiante con calificación más alta")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            registrar_estudiante()
        case "2":
            nombre_estudiante = input("Ingrese el nombre del estudiante: ")
            try:
                nombre, promedio = calcular_promedio(nombre_estudiante)
                print(f"El promedio de calificaciones de {nombre} es: {promedio}\n")
                print("El promedio de calificaciones de " + nombre + " es: " + promedio + "\n")
            except:
                print("El estudiante no está registrado.\n")
        case "3":
            encontrar_estudiante_con_calificacion_mas_alta()
        case "4":
            print("Gracias por usar el Registro de Estudiantes. ¡Hasta luego!")
            break
        case _:
            print("Opción inválida. Por favor, seleccione una opción válida.\n")