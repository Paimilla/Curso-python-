funcion_grados = lambda grados : grados * 1.8 + 32 #funcion lambda que recibe un parametro y retorna un valor 
#lambda <parametros> : <cuerpo de la funcion>

print(funcion_grados(10))

""" 
sin_parametros = lambda : True
parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3

asterisco = lambda *args, **kwargs : len(args) + len(kwargs) 
"""