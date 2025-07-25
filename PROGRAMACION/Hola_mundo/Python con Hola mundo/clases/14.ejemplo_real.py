# --- Clase Base o Clase Padre ---
# Esta clase 'Model' sirve como una plantilla o un modelo base.
# La idea es que otras clases hereden de esta para reutilizar su comportamiento.
# Es una práctica común en frameworks de desarrollo web (como Django o Flask)
# para interactuar con bases de datos.
class Model:
    
    # --- Atributo de Clase ---
    # Este es un atributo de la clase, no de una instancia.
    # Todas las instancias de 'Model' y sus clases hijas compartirán este valor
    # a menos que lo anulen (como veremos en la clase Usuario).
    tabla = False

    # --- Constructor de la Clase ---
    # El método __init__ se llama automáticamente cuando creas una nueva instancia de la clase.
    def __init__(self):
        # Comprobamos si la clase que se está instanciando ha definido el atributo 'tabla'.
        # Si 'self.tabla' sigue siendo 'False', significa que la clase hija no lo ha definido.
        if not self.tabla:
            print("Error, tienes que definir una tabla")
    
    # --- Método de Instancia ---
    # Este método 'guardar' opera sobre una instancia específica de la clase (a través de 'self').
    def guardar(self):
        # Imprime un mensaje indicando que está guardando en la base de datos.
        # Accede al atributo 'tabla' a través de 'self' para saber a qué tabla corresponde.
        print(f"Guardando {self.tabla} en BBDD")
   
    # --- Decorador de Método de Clase ---
    # El decorador '@classmethod' transforma un método para que reciba la clase como primer argumento,
    # en lugar de la instancia. Por convención, se sigue usando 'cls' o 'self' como nombre para ese primer argumento.
    @classmethod
    def buscar_por_id(self, _id):
        
        # Este método no necesita una instancia para ser llamado, puede ser llamado directamente desde la clase.
        # Por ejemplo: Model.buscar_por_id(123)
        # 'self' aquí no es una instancia, sino la clase misma (la clase 'Model' o cualquier clase hija).
        print(f"Buscando por id: {_id} en la tabla {self.tabla}")


# --- Clase Hija ---
# La clase 'Usuario' hereda de la clase 'Model'.
# Esto significa que 'Usuario' obtiene todos los atributos y métodos de 'Model'.
class Usuario(Model):
    
    # --- Anulación de Atributo de Clase ---
    # Aquí, la clase 'Usuario' anula (sobrescribe) el valor del atributo 'tabla'
    # que heredó de 'Model'. Ahora, para 'Usuario', 'tabla' es "Usuario".
    tabla = "Usuario"

# --- Creación de una Instancia ---
# Creamos un objeto llamado 'usuario' a partir de la clase 'Usuario'.
# Al hacer esto, se llama al método __init__ heredado de 'Model'.
# Como 'Usuario.tabla' es "Usuario" (y no 'False'), no se imprimirá el mensaje de error.
usuario = Usuario()

# --- Llamada a un Método de Instancia ---
# Llamamos al método 'guardar' en la instancia 'usuario'.
# Este método fue heredado de 'Model', pero cuando se ejecuta, 'self.tabla'
# se refiere al valor definido en la clase 'Usuario' ("Usuario").
usuario.guardar()

# --- Llamada a un Método de Clase ---
# Llamamos al método 'buscar_por_id' directamente desde la clase 'Usuario'.
# No necesitamos una instancia para esto.
# El método recibe la clase 'Usuario' como primer argumento y el id '123' como segundo.
Usuario.buscar_por_id(123)
