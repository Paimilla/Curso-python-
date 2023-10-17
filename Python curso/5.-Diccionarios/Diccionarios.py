elementos = {"a": 1, "b": 2, "c": 3, "a": 4} # los diccionarios no pueden tener llaves repetidas, si se repite la llave, se reemplaza el valor

"""
elementos["H"] = "Hidrogeno"
elementos[(1, 2, 3)] = "la llave es una tupla" # las llaves pueden ser tuplas o strings o numeros, booleanos, flotantes o enteros

elementos["H"] = "Helio" # si se repite la llave H, se reemplaza el valor
"""
print(elementos)
print(len(elementos))