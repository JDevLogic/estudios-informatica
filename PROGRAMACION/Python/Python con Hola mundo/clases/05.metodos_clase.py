class Mi_Perro:
    def __init__(self, nombre, edad):
    
        self.nombre = nombre
    
        self.edad = edad

    @classmethod
    def habla(cls):
        
        print("Guau!")
    
    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)                # Retorna una instancia de la clase Mi_Perro con los valores por defecto

Mi_Perro.habla()                                  # Llamamos al método habla de la clase Mi_Perro

perro1 = Mi_Perro("Chanchito", 2)

perro2 = Mi_Perro("Felipe", 3)

perro3 = Mi_Perro.factory()                          # Llamamos al método factory de la clase

print (perro3.nombre, perro3.edad)                            # Imprime Chanchito

 