# Crear una lista
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)  # Output: [1, 2, 3, 4, 5]

# Acceder a elementos de una lista
primer_elemento: list = mi_lista[0]
print(primer_elemento)  # Output: 1

# Modificar un elemento de la lista
mi_lista[2] = 10
print(mi_lista)  # Output: [1, 2, 10, 4, 5]

# Obtener la longitud de una lista
longitud = len(mi_lista)
print(longitud)  # Output: 5

# Agregar elementos al final de una lista
mi_lista.append(6)
print(mi_lista)  # Output: [1, 2, 10, 4, 5, 6]

# Agregar un elemento en una posicion especifica de una lista
mi_lista.insert(0, 20)
print(mi_lista)

# Eliminar elementos de una lista
mi_lista.remove(2)
print(mi_lista)  # Output: [1, 10, 4, 5, 6]

# Acceder al ultimo elemento de una lista
print(mi_lista[-1])

# Obtener indice de una lista
print(mi_lista.index(5))

# Ordenar una lista
mi_lista.sort()
print(mi_lista)  # Output: [1, 2, 3, 4, 5]

# Invertir una lista
mi_lista.reverse()
print(mi_lista)  # Output: [5, 4, 3, 2, 1]

# Copiar una lista
copia_lista = mi_lista.copy()
print(copia_lista)  # Output: [5, 4, 3, 2, 1]

# Unir dos listas
print(mi_lista + copia_lista)

# Contar la cantidad de veces que aparece un elemento en la lista
cantidad = mi_lista.count(3)
print(cantidad)  # Output: 1

# Vaciar una lista
mi_lista.clear()
print(mi_lista)  # Output: []