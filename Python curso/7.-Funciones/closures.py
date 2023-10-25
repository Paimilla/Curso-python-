#los closures son funciones que retornan funciones que a su vez pueden utilizar variables locales de la funcion que las retorna 

def saludar(username):  #de la linea 1 a la 8 es una closure function ya que la funcion mostrar_mensaje utiliza una variable local de la funcion saludar 
    mensaje = f"hola {username}" #variable local de la funcion saludar

    def mostrar_mensaje(): #funcion anidada
        print(mensaje)
    
    return mostrar_mensaje #retorna la funcion mostrar_mensaje

username = "Felipe"
respuesta = saludar(username) #respuesta es una funcion

username = "Juan" #cambia el valor de la variable username pero no cambia el valor de la variable mensaje ya que es una variable local de la funcion saludar

respuesta() #llama a la funcion mostrar_mensaje que es la que retorna la funcion saludar