def operacion(cantidad, balance, tipo= "deposito"):
    #funciones anidadas de 2 niveles
    def deposito(cantidad, balance):
        return cantidad + balance
    #por convencion se deben hacer 2 saltos de linea entre funcion y funcion

    def retiro(cantidad, balance):#balance es una variable local de la funcion retiro
        if balance >= cantidad:
            return balance - cantidad
        else:
            return None
        
    if tipo == "deposito":
        return deposito(cantidad, balance)
    elif tipo == "retiro":
        return retiro(cantidad, balance)
    else:
        return None
    
        

resultado= operacion(10, 30, "retiro")
print(resultado)