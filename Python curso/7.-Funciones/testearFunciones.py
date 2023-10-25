#docstring
#__doc__ (modulos,clases, metodos y funciones)
def suma(numero1, numero2):
    """La funcion suma dos numeros y retorna el resultado

    Args:
        numero1 (int)
        numero2 (int)

    Returns:
        se retorna la suma de parametros

    >>> suma(10, 20)
    30

    >>> suma(10, 30)
    40



    """
    return numero1 + numero2

def resta(numero1, numero2):
    """La funcion resta dos numeros y retorna el resultado # se puede usar el comando python -m doctest  testearFunciones.py para probar los test

    Args:
        numero1 (int)
        numero2 (int)

    Returns:
        se retorna la resta de parametros

    >>> resta(10, 20)
    -10

    >>> resta(10, 30)
    -20



    """
    return numero1 - numero2
