class Mi_Perro:
    patas = 4                                            # Atributo de clase, se puede acceder desde la clase o desde la instancia
    
    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad
    
    def habla(self):
        
        print(f"{self.nombre} dice: Guau!")

Mi_Perro.patas = 3                                        # Cambiamos el valor del atributo de clase

mi_perro = Mi_Perro("Chanchito", 1)

mi_perro.patas = 5 

mi_perro2 = Mi_Perro("Felipe", 1)                        # Creamos otra instancia de la clase Mi_Perro

print (Mi_Perro.patas)                                   # Imprime 3, porque el atributo de clase es 3

print (mi_perro.patas)                                   # Imprime 5, porque el atributo de instancia es 5

print (mi_perro2.patas)                                  