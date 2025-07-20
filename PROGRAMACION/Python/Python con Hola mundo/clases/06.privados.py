class Mi_Perro:
    
    def __init__(self, nombre, edad):
    
        self.__nombre = nombre
    
        self.edad = edad
    
    def get_nombre(self):
        
        return self.__nombre

    def set_nombre(self, nombre):

        self.__nombre = nombre

    def habla(self):
        
        print(f"{self.__nombre} dice: Guau!")
    
    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)                # Retorna una instancia de la clase Mi_Perro con los valores por defecto

perro1 = Mi_Perro.factory()                             # Instancia de la clase Mi_Perro con los valores por defecto

perro1.habla()                                         # Llama al método habla de la instancia perro1

print(perro1._Mi_Perro__nombre)                            # Llama al método get_nombre de la instancia perro1