class Usuario:
   
   # object 
   def __init__(self, username="", password=""): #el username = "" es un valor por defecto es decir si no se envia un parametro username se asigna el valor por defecto
        self.username = username
        self.password = password
    

user1 = Usuario("user1","paimilla")
user2 = Usuario("user2","paimilla2")
user3 = Usuario("user3","paimilla3")

user4 = Usuario()


print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)