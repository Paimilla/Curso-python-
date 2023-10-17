def promedio (*args): # *args: argumentos variables (tupla) (no se sabe cuantos argumentos se van a pasar)
    return sum(args) / len(args)

def usuarios(**kwargs): # **kwargs: argumentos variables (diccionario) (no se sabe cuantos argumentos se van a pasar)
    print(kwargs)
    print(type(kwargs))

def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)


combinacion(1, 2, 3, 4, 5, nombre="Eduardo", edad=22, promedio=10.0)
usuarios(eduardo=[4, 7, 8], felipe=[10, 9, 9], maria=[10, 10, 10]) #