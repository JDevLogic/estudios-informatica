# Los *args son una forma de pasar un número variable de argumentos a una función en Python.
# Se utilizan para pasar una lista de argumentos no nombrados a una función.

def mostrar_argumentos(*datos):                             # Creamos una funcion que recibe un numero indefinido de argumentos (*args)

    for dato in datos:                                      # Recorremos los argumentos recibidos con un bucle for

        print("El argumento es: ",dato)                     # Imprimimos el argumento recibido con un print


mostrar_argumentos("Jonathan", 1.75, True, 99)              # Llamamos a la funcion mostrando diferentes tipos de argumentos   


def mostrar_argumentos(*datos):                                             # Creamos una funcion que recibe un numero indefinido de argumentos (*args)

    for indice,valor in enumerate (datos, start = 1):                       # Recorremos los argumentos con un for y enumerandolo con enumerat y para que comience en 1 ponemos start = 1                

        print(f"Argumento {indice} : {valor}")                              # Para cada argumento imprimimos el indice y el valor del argumento    


mostrar_argumentos("Jonathan", 1.75, True, 99)

