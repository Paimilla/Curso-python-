
class Usuario:
    #__init__ es un metodo especial que se ejecuta al crear una instancia de la clase por lo tanto lo que hicimos no sirve

    def inicializar(self, username, password):#por convencion el nombre del parametro es self 
        #añadiendo atributos al objeto
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

user1.inicializar('user1','paimilla')
user2.inicializar('user2','paimilla2')
user3.inicializar('user3','paimilla3')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

