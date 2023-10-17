lista = [1, 2, 3, 4, 5]

tupla = (10, 30, 20, 40, 50)

lista_2 = [100, 200, 300, 400, 500]

tupla_2 = (1000, 2000, 3000, 4000, 5000)

resultado = zip(lista, tupla, lista_2, tupla_2) # -> zip es una funcion que permite comprimir dos listas o tuplas
resultado = tuple (resultado) # -> se convierte en tupla



print(resultado)