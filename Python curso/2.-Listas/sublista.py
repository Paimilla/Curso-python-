lista_Cursos = ["Python", "Django", "Flask", "C", "C++", "C#", "Java", "PHP"]
#                  0          1        2      3     4      5      6      7

#[start:end]
#[start:] -> obtenemos los ultimos elementos de la lista
#[:end] -> obtenemos los primeros elementos de la lista
#[start:end:skip] -> obtenemos los elementos de la lista con saltos

#sub_lista = lista_Cursos[1:5] obtenemos los elementos de la posicion 1 a la 5
#sub_lista = lista_Cursos[:5] obtenemos los elementos de la posicion 0 a la 5
#sub_lista = lista_Cursos[1:] obtenemos los elementos de la posicion 1 hasta el final
#sub_lista = lista_Cursos[1:7:2] obtenemos los elementos de la posicion 1 a la 7 con saltos de 2
#sub_lista = lista_Cursos[::-1] obtenemos los elementos de la lista en reversa


sub_lista = lista_Cursos[::-1] 
print(sub_lista)