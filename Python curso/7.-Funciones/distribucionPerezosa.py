def pares(): #generador -> lazy iterator -> iterador perezoso  
    for numero in range(0, 12, 2):#si se pone un numero menor al que se intenta imprimir se produce un error
        yield numero # yield no corta la ejecucion de la funcion
    
        #print("un mensaje despues de yield")# se ejecuta por el yield

generador = pares()# se ejecuta la funcion pares y se recorre el generador
"""
print(next(generador)) # se imprime el generador
print(next(generador)) # esto sirve para obtener el valor del generador dependiendo de la demanda del usuario 
print(next(generador)) #la principal ventaja es el espacio de la memoria ya que no se almacena en memoria los valores del generador
print(next(generador)) #cuando hay mucho datos en memoria se puede usar el generador para no saturar la memoria
print(next(generador)) 
print(next(generador)) 
print("ejecutamos codigo entre un llamado y otro")
print(next(generador)) 
"""
while True: # se puede usar un while para recorrer el generador
    try: # se usa un try para manejar el error de tipo StopIteration
        par = next(generador)
        print(par)
    except StopIteration: # cuando se termina el generador se produce un error de tipo StopIteration 
        print("se termino el generador")
        break
