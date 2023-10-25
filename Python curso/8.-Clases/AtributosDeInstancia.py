#Attrs de clase
#attrs de instancia

class Usuario: 
    username = "Username por defecto" #atributo de clase
    email = ""



#__dict__ es un diccionario que contiene los atributos de la clase
user1= Usuario()
#1.- verifica si el atributo username existe en la instancia user1
#2.- verifica si el atributo username existe en la clase Usuario
#3.- lanzar un error
print(user1.username)


print(id(user1.username)) #imprime la direccion de memoria del atributo username de la instancia user1
print(id(Usuario.username)) #imprime la direccion de memoria del atributo username de la clase Usuario 


print(user1.__dict__) #imprime los atributos de la instancia user1
