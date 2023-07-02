mi_diccionario: dict = {
    "nombre": "Juan",
    "edad": 23,
    "ciudad": "Lima"
}

mi_diccionario_2: dict = {
    "gusto": "soccer"
}

print(mi_diccionario)

print(mi_diccionario["edad"])

mi_diccionario["edad"] = 100
print(mi_diccionario)

print(mi_diccionario.get("edad")) # mi_diccionario["edad"]

mi_diccionario["profesion"] = "Carpintero"
print(mi_diccionario)

del mi_diccionario["edad"]
print(mi_diccionario)

claves = mi_diccionario.keys()
print(claves)

valores = mi_diccionario.values()
print(valores)

print("edad" in mi_diccionario)