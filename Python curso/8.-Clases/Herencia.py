class Mascota: # Clase Padre

    def comer(self):
        print("Estoy comiendo")

    def dormir(self):
        print("Estoy durmiendo")
    

class Perro(Mascota): # Clase Hija
    pass

class Gato(Mascota): # Clase Hija
    pass

salem = Gato()
salem.comer()
salem.dormir()


jose = Perro()
jose.comer()
jose.dormir()