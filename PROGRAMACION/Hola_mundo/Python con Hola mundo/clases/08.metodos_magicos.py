class Perro:
   
    def __init__ (self, nombre, edad):
        
        self.nombre = nombre
        
        self.edad = edad

    # def __del__(self):                            # Método destructor
    #     print(f"Chao, perro 😞​ {self.nombre}")    # Este metodo llama cuando se destruye el objeto
    
    def __str__(self):
        return f"Clase Perro: {self.nombre}"
        

    def habla (self):
        
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Toby", 5)
 
print (perro)

texto = str(perro)      # Convierte el objeto perro a una cadena de texto

print (texto)           # Imprime el texto convertido