# La clase 'Producto' define un modelo para crear objetos que representan productos.
class Producto: 
    # El método '__init__' es el constructor de la clase. Se llama automáticamente cuando se crea un nuevo objeto 'Producto'.
    # 'self' se refiere al objeto que se está creando.
    # 'nombre' y 'precio' son los atributos que tendrá cada producto.
    def __init__ (self,nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # El método '__str__' define cómo se representará el objeto 'Producto' como una cadena de texto.
    # Es útil para imprimir el objeto de una manera legible para los humanos.
    def __str__ (self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"


# La clase 'Categoria' actúa como un contenedor para agrupar y gestionar objetos 'Producto'.
class Categoria:
    # 'productos' es un atributo de clase. Es una lista que será compartida por todas las instancias (objetos) de 'Categoria'.
    productos = []

    # El constructor de la clase 'Categoria'.
    # 'nombre' es el nombre de la categoría.
    # 'productos' es una lista de los productos que pertenecen a esta categoría.
    def __init__ (self,nombre,productos):
        self.nombre = nombre
        self.productos = productos

    # El método 'agregar' permite añadir un nuevo producto a la lista de productos de la categoría.
    def agregar(self,producto):
        self.productos.append(producto)
    
    # El método 'imprimir' recorre la lista de productos y los muestra en la consola.
    def imprimir(self):
        for producto in self.productos:
            print(producto)

# --- Creación y uso de los objetos ---

# Creamos instancias (objetos) de la clase 'Producto'.
kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("Surfboard", 500)

# Creamos una instancia de la clase 'Categoria', pasándole un nombre y una lista inicial de productos.
deportes = Categoria("Deportes", [kayak, bicicleta])

# Usamos el método 'agregar' del objeto 'deportes' para añadir otro producto a su lista.
deportes.agregar(surfboard)

# Usamos el método 'imprimir' para mostrar todos los productos contenidos en la categoría 'deportes'.
deportes.imprimir()