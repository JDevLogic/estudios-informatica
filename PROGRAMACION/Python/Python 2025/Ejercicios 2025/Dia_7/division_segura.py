while True:                                                                  # Creamos un bucle infinito
            
    try:
        num1 = int(input("Introduce el primer numero: "))                    # Se pide el primer numero al usuario numero entero
        num2 = int(input("Introduce el segundo numero: "))                   # Se pide el segundo numero para la operacion
        
        resultado = num1 / num2                                              # Guardamos el resultado de la division entre num1 y num2
        print("El resultado de la division es: ", resultado)                 # Imprimimos el resultado de la division
        break                                                                # Salimos del bucle si no hay excepciones
                                                                    
    except ZeroDivisionError:                                                # Si se produce una excepcion de division por cero
        print("No se puede dividir entre cero. Intenta de nuevo.")           # Mensaje para el usuario
                   
    except ValueError:                                                       # Si se produce una excepcion de valor no valido
        print("¡Eso no es un número válido! Intenta de nuevo.")              # Mensaje para el usuario