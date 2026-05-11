# Ejemplo de un if ternario en Python para asignar variables rápidamente

calificacion = 10
"""
color = None

if calificacion >= 10:
    color = "verde"
    print("Felicidades, sacaste 10")
elif calificacion >= 8:
    color = "azul"
    print("Felicidades, aprobaste")
else:
    color = "rojo"
    print("Reprobaste :(")
"""

color = "verde" if calificacion >= 7 else "rojo"
print(calificacion, color)