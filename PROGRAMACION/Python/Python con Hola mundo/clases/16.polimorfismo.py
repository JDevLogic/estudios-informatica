# El polimorfismo es un concepto fundamental en la programación orientada a objetos.
# La palabra "polimorfismo" significa "muchas formas", y en programación se refiere a la
# capacidad de objetos de diferentes clases de responder al mismo mensaje (llamada de método)
# de maneras específicas para cada clase.

from abc import ABC, abstractmethod

# Definimos una clase abstracta 'Model' que sirve como un contrato.
# Cualquier clase que herede de 'Model' debe implementar el método 'guardar'.
class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass

# La clase 'Usuario' hereda de 'Model' e implementa el método 'guardar'.
# Su implementación específica es guardar los datos en una base de datos.
class Usuario(Model):
    def guardar(self):
        print("Guardando en BBDD")

# La clase 'Sesion' también hereda de 'Model' e implementa 'guardar'.
# Su implementación es diferente: guarda los datos en un archivo.
class Sesion(Model):
    def guardar(self):
        print("Guardando en archivo")

# Esta función 'guardar_entidades' demuestra el polimorfismo en acción.
# Acepta una lista de objetos (que llamamos 'entidades').
# No necesita saber si un objeto es un 'Usuario' o una 'Sesion'.
# Solo necesita saber que cada objeto tiene un método 'guardar'.
def guardar_entidades(entidades):
    # Itera sobre cada entidad en la lista.
    for entidad in entidades:
        # Llama al método 'guardar()' de la entidad.
        # Python determina en tiempo de ejecución qué versión de 'guardar()' llamar.
        # Si 'entidad' es un objeto Usuario, llama a Usuario.guardar().
        # Si 'entidad' es un objeto Sesion, llama a Sesion.guardar().
        entidad.guardar()

# Creamos una instancia de Usuario y una de Sesion.
usuario = Usuario()
sesion = Sesion()

# Llamamos a la función 'guardar_entidades' con una lista que contiene ambos objetos.
# A pesar de que son de tipos diferentes, la función puede trabajar con ambos
# gracias a que comparten la misma interfaz (el método 'guardar').
guardar_entidades([sesion, usuario])

# Salida esperada:
# Guardando en archivo
# Guardando en BBDD
# (El orden puede variar dependiendo del orden en la lista)