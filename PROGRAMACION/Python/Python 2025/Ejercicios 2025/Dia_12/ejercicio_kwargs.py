# Los **kwargs son una forma de pasar un número variable de argumentos a una función en Python.
# Se utilizan para pasar argumentos con nombre (es decir, pares clave-valor) a una función.

def mostrar_perfil (**kwargs):                                           # Creamos una funcion que recibe un numero indefinido de argumentos con nombre tipo diccionario (**kwargs)
    
    for clave,valor in kwargs.items():                                   # Recorremos los argumentos con un for y con items para que nos de la clave y el valor
        print(f"{clave} : {valor}")                                      # Imprimimos la clave y el valor

mostrar_perfil (nombre = "Jonathan", edad = 21, ciudad = "Bilbao")       # Llamamos a la funcion mostrando diferentes tipos de argumentos con nombre