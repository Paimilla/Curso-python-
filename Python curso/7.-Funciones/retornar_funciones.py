def saludar():
    
    
    def mostrar_mensaje():
        print('Hola mundo')

    return mostrar_mensaje #retorna la funcion mostrar_mensaje

respuesta = saludar() #respuesta es una funcion 
print(respuesta) 
print(type(respuesta))
respuesta() #llama a la funcion mostrar_mensaje que es la que retorna la funcion saludar 
    