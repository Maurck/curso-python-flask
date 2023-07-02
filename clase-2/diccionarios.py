# Crear un diccionario
mi_diccionario: dict = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(mi_diccionario)  # Output: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}

# Acceder a valores mediante claves
print(mi_diccionario["nombre"])  # Output: Juan

# Modificar un valor en el diccionario
mi_diccionario["edad"] = 30
print(mi_diccionario)  # Output: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

# Acceder a valor mediante funcion
print(mi_diccionario.get("edad"))

# Agregar un nuevo par clave-valor al diccionario
mi_diccionario["profesion"] = "Ingeniero"
print(mi_diccionario)  # Output: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

# Eliminar un par clave-valor del diccionario
del mi_diccionario["ciudad"]
print(mi_diccionario)  # Output: {'nombre': 'Juan', 'edad': 30, 'profesion': 'Ingeniero'}

# Obtener todas las claves del diccionario
claves = mi_diccionario.keys()
print(claves)  # Output: dict_keys(['nombre', 'edad', 'profesion'])

# Obtener todos los valores del diccionario
valores = mi_diccionario.values()
print(mi_diccionario.values())

# Verificar si existe una clave en un diccionario
print("nombre" in mi_diccionario)