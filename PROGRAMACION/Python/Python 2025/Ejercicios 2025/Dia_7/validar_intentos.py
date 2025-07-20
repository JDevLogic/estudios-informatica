while True:                                                                 # Creamos un bucle infinito
   
    # Pedimos un número al usuario
    try:
        numero = int(input("Introduce un número: "))
        
        if numero > 0:                                                      # El numero tiene que ser mayor que 0 
            print("Numero valido:",numero)                                  # Si el numero es mayor que 0, lo imprimimos
            break                                                           # Con break salimos del bucle
    
    except ValueError:                                                      # Si el usuario introduce un valor no valido, se lanza una excepcion   
        print("¡Eso no es un número válido! Intenta de nuevo.")             # Si el usuario introduce un valor no valido, se le pide que lo intente de nuevo