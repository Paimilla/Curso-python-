class Animal: #clase padre
    def comer(self):
        print("Estoy comiendo")

    def dormir(self):
        print("Estoy durmiendo")
    

    pass

class Mascota(Animal): # Clase hija
    pass

class Felino:
    def cazar(self):
        print("Estoy cazando")


class Gato(Mascota, Felino): # Clase Hija
    pass

salem = Gato()
salem.comer()
salem.dormir()
salem.cazar()