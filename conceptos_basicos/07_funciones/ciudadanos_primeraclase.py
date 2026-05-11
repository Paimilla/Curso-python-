# Las funciones son ciudadanos de primera clase en Python, se pueden guardar en variables

def centigrados_a_fahrenheit(grados):
    return grados * 1.8 + 32

mi_funcion = centigrados_a_fahrenheit

print(type(mi_funcion))

print(mi_funcion(10))