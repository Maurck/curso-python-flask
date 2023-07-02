# Crear una tupla
mi_tupla: tuple = (1, 2, 3, 4, 5)
print(mi_tupla)  # Output: (1, 2, 3, 4, 5)

# Acceder a elementos de una tupla
primer_elemento = mi_tupla[0]
print(primer_elemento)  # Output: 1

# Obtener la longitud de una tupla
longitud = len(mi_tupla)
print(longitud)  # Output: 5

# Desempaquetar una tupla
a, b, c, d, e = mi_tupla
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# Concatenar tuplas
otra_tupla = (6, 7, 8)
concatenacion = mi_tupla + otra_tupla
print(concatenacion)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)