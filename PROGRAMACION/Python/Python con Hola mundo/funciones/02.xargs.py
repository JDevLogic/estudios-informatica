def suma (*numeros):                            # Creamos una función que recibe un número indefinido de argumentos con *args
    """
    Suma todos los números pasados como argumentos.
    """
    resultado = 0                               # Inicializamos la variable resultado en 0
    
    for numero in numeros:                      # Recorremos los argumentos la lsita de argumentos *args
        resultado += numero                     # Sumar cada número a la variable resultado
   
    print(resultado)                            # Imprimimos el resultado de la suma    

suma(2,5,7)

suma(2,5)

suma(2,8,7,45,32)