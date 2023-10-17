titulo_curso = "Curso profesional de Python"

for caracter in titulo_curso:
    if caracter == "P":
        break # el break se utiliza para romper el ciclo
    if caracter == "s":
        continue # el continue se utiliza para saltar una iteracion

    print(caracter)