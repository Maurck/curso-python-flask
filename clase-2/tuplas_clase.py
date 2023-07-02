mi_tupla: tuple = (1, 2, 3, 4, 5)
print(mi_tupla)

primer_elemento = mi_tupla[0]
print(primer_elemento)

def sum(a, b):
    return a + b

a=10
b=20
sum(a, b)

longitud = len(mi_tupla)
print(longitud)

a: int = 129381 
a,b,c,d,e = mi_tupla
a=20
a,b,c,d,e = mi_tupla
print(a,b,c,d,e)

otra_tupla = (6, 7, 8)
print(mi_tupla + otra_tupla)
