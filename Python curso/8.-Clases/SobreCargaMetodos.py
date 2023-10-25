class Animal: #clase padre

    def comer(self):
        print("Estoy comiendo")

    def dormir(self):
        print("Estoy durmiendo")
    

 
class Mascota(Animal): # Clase hija
    
    def comer(self):  #Sobreescribiendo el metodo comer de la clase padre 
        print("Estoy comiendo en un plato en el piso")

class Felino:
    def cazar(self):
        print("Estoy cazando")


class Gato(Mascota, Felino): # Clase Hija

    def __init__(self, nombre): #sobreescribiendo el metodo __init__ de la clase padre
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} esta comiendo en un plato en el piso")
    
    def dormir(self):
        super().dormir() #llamando al metodo dormir de la clase padre
        print(f"{self.nombre} esta durmiendo en el sillon")
        
salem = Gato("Salem")
salem.comer()
salem.dormir()
salem.cazar()
