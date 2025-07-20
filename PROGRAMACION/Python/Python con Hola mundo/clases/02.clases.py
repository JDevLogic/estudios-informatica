class Mi_Perro:
    def habla(self):                         # Ya no son funciones son métodos, dentro del parametro debe ir self
        print("Guau!")

mi_perro = Mi_Perro()

print (type(mi_perro))                       # <class '__main__.Mi_Perro'>

mi_perro.habla()                             # Llamamos al método habla de la clase Mi_Perro

print (isinstance(mi_perro, Mi_Perro))       # Verifica si mi_perro es una instancia de la clase Mi_Perro

print (isinstance(mi_perro, object))         # Verifica si mi_perro es una instancia de la clase object es True porque todas las clases heredan de object

print (isinstance(mi_perro, str))            # Verifica si mi_perro es una instancia de la clase str es False porque no es  cadena de texto