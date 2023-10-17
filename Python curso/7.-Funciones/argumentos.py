def promedio(*args): # *args: argumentos variables (tupla) (no se sabe cuantos argumentos se van a pasar)
    print(args)
    print(type(args))

    return sum(args) / len(args)

resultado = promedio(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(resultado)