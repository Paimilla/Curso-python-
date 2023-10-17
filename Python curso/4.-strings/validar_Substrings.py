titulo_curso = "Curso de Python"
#como puedo hacer que cuente las o mayusculas igual que las minusculas

#contador = titulo.curso.lower().count("o") #lower convierte todo el string en minusculas

"""
contador= titulo_curso.count("o") #cuenta cuantas veces se repite un caracter en un string

print(contador)
"""
print("python" in titulo_curso.lower()) #in permite saber si un string esta dentro de otro string y devuelve un booleano
#el .lower() permite que no importe si esta en mayuscula o minuscula ya que lo convierte todo en minuscula

print(titulo_curso.startswith("Curso")) #startswith permite saber si un string empieza con un caracter o string y devuelve un booleano
print(titulo_curso.endswith("Python")) #endswith permite saber si un string termina con un caracter o string y devuelve un booleano