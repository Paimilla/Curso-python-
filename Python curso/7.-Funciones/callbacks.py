#los callbacks son funciones que se pasan como argumentos a otras funciones 
promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7 

def es_aprobatorio(calificacion): #callback function
    return calificacion >= 90 

def mostrar_mensaje(func_promedio, func_aprobatorio, *args): #func_promedio y aprobatorio son callback functions 
    promedio = func_promedio(*args) #

    if func_aprobatorio(promedio) == True: #func_aprobatorio es una funcion callback
        print(f'Felicidades, aprobaste con {promedio}') 
    else:
        print(f'No aprobaste, tu promedio es {promedio}')

mostrar_mensaje(promedio, es_aprobatorio, 10, 10, 8, 1, 9)

