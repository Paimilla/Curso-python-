#scope es el alcance que tiene una variable dentro de un programa o dentro de una funcion
#por ejemplo en este caso la variable animal tiene un alcance global y local dentro de la funcion imprimir_animal 
# y dentro de la funcion imprimir_animal la variable animal tiene un alcance local
animal = "leon" #variable global

def imprimir_animal():
    global animal #con la palabra reservada global se puede acceder a la variable global animal
    
    animal = "ballena" 
    #animal = "ballena" #variable local

    tipo = "mamifero" #variable local

    print(animal)
    print(id(animal)) #id es la direccion de memoria donde se encuentra la variable

imprimir_animal()
print (animal)
print(id(animal))

#print(tipo) #no se puede acceder a la variable tipo porque es una variable local de la funcion imprimir_animal()