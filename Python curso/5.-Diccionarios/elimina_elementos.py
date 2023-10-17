diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}
print(len(diccionario))

del diccionario["a"] # elimina el elemento con la llave "a"
valor = diccionario.pop("b") # elimina el elemento con la llave "b" y devuelve el valor

diccionario.clear() # elimina todos los elementos del diccionario

print(diccionario)
print(len(diccionario))
