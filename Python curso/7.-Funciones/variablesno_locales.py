e= "e" #variable global puede ser utilizada en cualquier funcion 

def funcion_principal():
    a= "a" #variable local de la funcion principal pero tienen un alcance mayor ya que es de la funcion principal es decir se puede utilizar en la funcion anidada
    b= "b"

    def funcion_anidada():
        c = "c" #variable local de la funcion anidada no se puede utilizar en la funcion principal 

        nonlocal b #nonlocal permite utilizar la variable b de la funcion principal en la funcion anidada
        b = "cambio de valor"
        print(a, b)
        print(id(b))
        print(e)


    funcion_anidada()
    #print(c) no se puede utilizar la variable c ya que es una variable local de la funcion anidada
    print(b) 
    print(id(b)) #tienen diferente id ya que son variables diferentes

funcion_principal()
        


