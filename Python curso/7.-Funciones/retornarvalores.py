def suma(n1, n2):
    return n1 + n2, "la funcion retorna 2 valores"


numero_uno = int(input("ingrese el numero uno: ")) 
numero_dos = int(input("ingrese el numero dos: "))

resultado, mensaje = suma(numero_uno, numero_dos) # se puede asignar a una variable el valor de retorno de la funcion
print(resultado)
print(mensaje)