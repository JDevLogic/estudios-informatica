class Mi_Perro:
    def __init__(self, nombre, edad):           # init sirve para inicializar los atributos de la clase
        self.nombre = nombre
        self.edad = edad

    def habla(self):                            # Ya no son funciones son métodos, dentro del parametro debe ir self
        print(f"{self.nombre} dice: Guau!")

mi_perro = Mi_Perro("Chanchito", 1)



mi_perro.habla()                                # Llamamos al método habla de la clase Mi_Perro


