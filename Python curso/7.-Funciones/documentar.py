#docstring
#__doc__ (modulos,clases, metodos y funciones)
def suma(numero1, numero2):
    """La funcion suma dos numeros y retorna el resultado

    Args:
        numero1 (int)
        numero2 (int)

    Returns:
        _se retorna la suma de parametros

    TODO: #EL TODO es una etiqueta que se usa para indicar que se debe hacer algo en el futuro
        *
    """
    return numero1 + numero2

print(suma.__doc__) # se imprime la documentacion de la funcion suma

#print(help(suma)) # se imprime la documentacion de la funcion suma