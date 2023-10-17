diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

print("a" in diccionario)# in sirve para saber si un elemento esta en el diccionario
"""      
valor = diccionario["a"]
print(valor)
"""
#get sirve para obtener un valor de un diccionario
valor = diccionario.get("z", "no existe esa llave")# si el valor no existe, devuelve el segundo parametro
print(valor) # si el valor no existe, devuelve None

#setdefault sirve para agregar un valor al diccionario
valor = diccionario.setdefault("z", 5) # si el valor no existe, lo agrega al diccionario
print(diccionario) 