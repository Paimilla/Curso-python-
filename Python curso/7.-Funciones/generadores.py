"""
def pares():
    for numero in range(0, 100, 2):
        return numero # return corta la ejecucion de la funcion
    
        print("un mensaje despues de retunr")# no se ejecuta por el return

print(pares()) # 0 ya que el return corta la ejecucion de la funcion
"""
def pares(): #generador -> lazy iterator -> iterador perezoso 
    for numero in range(0, 100, 2):
        yield numero # yield no corta la ejecucion de la funcion
    
        #print("un mensaje despues de yield")# se ejecuta por el yield

for par in pares():# se ejecuta la funcion pares y se recorre el generador
    print(par) # se imprime el generador


