# Ejemplo de cómo pedir datos por consola y convertirlos al tipo adecuado (int, float, bool)


edad = int(input("cuantos años tienes: "))


altura = float(input("cuantos centimetros mides: "))


autorizacion = input("Autorizas el uso de tus datos: (si/no) ") == "si"



print(edad)
print(type(edad))

print(altura)
print(type(altura))

print(autorizacion)
print(type(autorizacion))