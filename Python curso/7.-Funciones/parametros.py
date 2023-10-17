def area_circulo(radio, pi=3.14): # Parametros por defecto (se pone sin espacios entre el nombre y el igual por convencion de la comunidad)
    return pi * (radio**2)

resultado = area_circulo(10, 3.141592) #tambien se puede poner el valor del parametro por defecto
print(resultado)