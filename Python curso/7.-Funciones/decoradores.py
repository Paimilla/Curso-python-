""" 

a-> la funcion principal (Decorador)
b-> la funcion de decorar
c-> la funcion decorada

a(b) -> c

el decorador tiene como objetivo agregar funcionalidades a una funcion sin modificarla 
"""

def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print("<<<Antes del llamado")

        resultado = funcion_b(*args,**kwargs) 

        print("<<<Despues del llamado")

        return resultado
        
    return funcion_c

@funcion_a
def suma(numero1, numero2):
    return numero1 + numero2

resultado = suma(15,60) #llama a la funcion_c que es la que retorna la funcion_a que a su vez recibe como parametro la funcion_b que es la funcion suma
print(resultado)