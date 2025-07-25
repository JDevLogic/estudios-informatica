class Animal:                    # Creamos una clase base llamada Animal
    
    def comer(self):             # Creamos un método comer en la clase Animal    
        print("comiendo")        # Imprimimos el mensaje "comiendo"



class Perro(Animal):             # Creamos una clase llamada Perro que hereda de la clase Animal

    
    def pasear(self):            # Creamos un método pasear en la clase Perro
        print("paseando")        # Imprimimos el mensaje "paseando"

class Chanchito(Perro):          # Creamos una clase llamada Chanchito que hereda de la clase Perro

    def programar(self):         # Creamos un método programar en la clase Chanchito
        print("programando")     # Imprimimos el mensaje "programando"

chanchito = Chanchito() 
chanchito.pasear()               # Ahora chanchito puede llamar al metodo comer y pasear porque hereda de Perro y Animal
                                 # A eso se le llama herencia multiple, porque Chanchito hereda de Perro y Perro hereda de Animal