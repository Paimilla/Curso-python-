class Circulo:
    pi = 3.14159265

    @classmethod #decorador
    def area(cls, radio): #cls es el nombre por convencion de la clase 
        return cls.pi * radio**2
    
resultado = Circulo.area(14)
print(resultado)