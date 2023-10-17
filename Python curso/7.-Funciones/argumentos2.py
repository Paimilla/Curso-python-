def promedio(*args): # *args: argumentos variables (tupla) (no se sabe cuantos argumentos se van a pasar)
    return sum(args) / len(args)
   #entre funcion y funcion deben haber 2 lineas de espacio

def combinacion(p1, p2, *args, p4=500): # *args: argumentos variables (tupla) (no se sabe cuantos argumentos se van a pasar)
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(10, 20, 1, 2, 3, 4, 5, 6, 7, 8, p4=1000)