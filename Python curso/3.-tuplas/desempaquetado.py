numero = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, _, tres, cuatro, *_, nueve, diez = numero # el *restonumeros almacena los demas numeros que no se han asignado a las variables
# si se agrega un *_ omite los demas numeros que no se han asignado a las variables
"""
uno = numero[0]
dos = numero[1]
tres = numero[2]
cuatro = numero[3]

"""

print(uno)
print(tres)
print(cuatro)

print(nueve)
print(diez)