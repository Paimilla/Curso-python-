nombre = "Felipe"
apellido = "Paimilla"

#nombre_completo = nombre + " " + apellido + "." # concatenar

#nombre_completo = "Mr. %s %s." %(nombre, apellido) # %s es un comodin

#nombre_completo = "Mr. {} {} {}.".format(nombre, apellido, "castillo") # .format es un metodo que permite concatenar {} es un comodin
"""
nombre_completo = "Mr. {nombre} {apellido} {segundo_Apellido}.".format(  # 
    nombre = nombre,              #de esta forma se puede cambiar mas facil los valores de las variables 
    apellido = apellido,
    segundo_Apellido = "castillo"
)
"""
nombre_completo = f"Mr. {nombre} {apellido} {"Castillo"} {2*2}." # Fstring es una forma mas facil para crear nuevos strings

print(nombre_completo)