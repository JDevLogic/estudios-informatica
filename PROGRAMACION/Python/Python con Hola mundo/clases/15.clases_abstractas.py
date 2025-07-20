# Las clases abstractas son una característica poderosa de la programación orientada a objetos.
# Permiten definir una "plantilla" para otras clases, asegurando que las clases hijas
# implementen ciertos métodos que son cruciales para el funcionamiento del sistema.

# Para crear una clase abstracta en Python, importamos ABC (Abstract Base Class) y 
# el decorador abstractmethod del módulo abc.
from abc import ABC, abstractmethod

# Definimos una clase abstracta 'Model' que hereda de ABC.
# Esta clase servirá como un modelo base para otras clases que manejan datos,
# como 'Usuario', 'Producto', etc.
class Model(ABC):

    # Usamos el decorador @property junto con @abstractmethod para definir una propiedad abstracta.
    # Esto significa que cualquier clase que herede de 'Model' DEBE definir una propiedad 'tabla'.
    # La propiedad 'tabla' indicará el nombre de la tabla de la base de datos correspondiente al modelo.
    @property
    @abstractmethod
    def tabla(self):
        pass
    
    # Aquí definimos un método abstracto llamado 'guardar'.
    # Las clases hijas estarán obligadas a implementar su propia versión de este método.
    # Por ejemplo, la clase 'Usuario' tendrá una lógica específica para guardar un usuario.
    @abstractmethod
    def guardar(self):
        pass

    # También podemos tener métodos concretos (no abstractos) en una clase abstracta.
    # Estos métodos pueden ser utilizados directamente por las clases hijas.
    # 'buscar_por_id' es un método de clase que busca un registro por su ID en la tabla
    # definida por la propiedad 'tabla'.
    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id: {_id} en la tabla {self.tabla}")

# La clase 'Usuario' hereda de 'Model'.
# Al hacerlo, está obligada a implementar todos los métodos y propiedades abstractos de 'Model'.
class Usuario(Model):
    # Cumplimos con el contrato de la clase abstracta 'Model' definiendo la propiedad 'tabla'.
    tabla = "Usuario" 

    # También implementamos el método 'guardar' con la lógica específica para guardar un usuario.
    def guardar(self):
        print("guardando usuario")

# Creamos una instancia de la clase 'Usuario'.
usuario = Usuario()

# Llamamos al método 'guardar' de la instancia de 'Usuario'.
# Esto ejecutará la implementación específica de 'guardar' definida en la clase 'Usuario'.
usuario.guardar()  # Salida esperada: guardando usuario

# Llamamos al método de clase 'buscar_por_id'.
# Este método fue heredado de la clase 'Model' y utiliza la propiedad 'tabla' 
# que definimos en la clase 'Usuario'.
Usuario.buscar_por_id(123) # Salida esperada: Buscando por id: 123 en la tabla Usuario

# La siguiente línea de código generaría un error si se descomenta.
# No podemos crear una instancia de una clase abstracta como 'Model' directamente.
# Las clases abstractas están diseñadas para ser heredadas, no para ser instanciadas.
# model = Model()