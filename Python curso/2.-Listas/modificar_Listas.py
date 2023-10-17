lista_cursos = ["Python", "Django", "Flask", "C", "C++", "Java", "PHP"]
lista_cursos2 = ["html", "css", "javascript"]

lista_cursos.append("MongoDB")#agrega el elemento al final de la lista
lista_cursos.append("SQL")

lista_cursos.insert(0, "Rust")#agrega el elemento en la posicion 0
lista_cursos.insert(3, "Go")#agrega el elemento en la posicion 3

lista_cursos.extend(lista_cursos2)#agrega los elementos de la lista2 a la lista1

print(lista_cursos)
print(lista_cursos2)
print(len(lista_cursos))

lista_cursos.remove("css")#elimina el elemento css

del lista_cursos[0]#elimina el elemento de la posicion 0

lista_cursos.clear()#elimina todos los elementos de la lista

lista_cursos.pop()#elimina el ultimo elemento de la lista

print(lista_cursos)