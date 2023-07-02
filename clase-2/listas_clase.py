var1: int = 1
var2: int = 2
# ...
var5: int = 5
mi_lista: list = [5, 2, 20, 100, 5] # [5, 100, 20, 2, 5]

primer_elemento = mi_lista[2]
print(primer_elemento) #3

mi_lista[2] = 20
print(mi_lista)

longitud = len(mi_lista)
print(longitud)

mi_lista.append(True)
print(mi_lista)

mi_lista.insert(0, 100)
print(mi_lista)

mi_lista.remove(100)
print(mi_lista)

print(mi_lista[-1])

print(mi_lista.index(5))

mi_lista.sort()
print(mi_lista)

mi_lista.reverse()
print(mi_lista)

copia_lista: list = []
copia_lista = mi_lista.copy()
print(copia_lista)

suma_listas: list = mi_lista + copia_lista
print(suma_listas)

cantidad = mi_lista.count(5)
print(cantidad)

mi_lista.clear()
print(mi_lista)