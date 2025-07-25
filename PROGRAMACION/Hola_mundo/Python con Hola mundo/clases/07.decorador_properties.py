class Perro:
    def __init__(self,nombre):
        self.nombre = nombre

    @property                                   # El decorador property permite definir un método como propiedad
    
    def nombre(self):                           # El método nombre se convierte en una propiedad
        print("Pasando por getter")             # Se ejecuta al acceder a la propiedad
        return self.__nombre                    # Se accede al atributo privado __nombre
    
    @nombre.setter                              # El decorador setter permite definir un método como setter 
    
    def nombre(self,nombre):                    # El método nombre se convierte en un setter
        
        print("Pasando por el setter")

        if nombre.strip():

            self.__nombre = nombre
        return

perro = Perro("Choclo")                             # Instancia de la clase Perro

print(perro.nombre)                                 # Llama al método nombre de la instancia perro   