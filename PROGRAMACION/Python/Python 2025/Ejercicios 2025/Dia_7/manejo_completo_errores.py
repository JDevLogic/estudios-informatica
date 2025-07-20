while True:

    try:
        num1 = int(input("Introduce el primer numero: "))                      # Se pide el primer numero al usuario numero entero
        num2 = int(input("Introduce el segundo numero: "))                     # Se pide el segundo numero para la operacion

        resultado = num1 / num2                                                # Guardamos el resultado de la division entre num1 y num2
    
    except ZeroDivisionError:                                                  # Si se produce una excepcion de division por cero
        print("No se puede dividir entre cero. Intenta de nuevo.")             # Mensaje para el usuario
        continue                                                               # Volvemos al inicio del bucle para pedir los numeros de nuevo
   
    except ValueError:                                                         # Si se produce una excepcion de valor no valido
        print("¡Eso no es un número válido! Intenta de nuevo.")                # Mensaje para el usuario
        continue                                                               # Volvemos al inicio del bucle para pedir los numeros de nuevo
    
    else:                                                                      # Si no hay excepciones
        print("El resultado de la division es:",resultado)                     # Imprimimos el resultado de la division
        break                                                                  # Salimos del bucle si no hay excepciones

    finally:                                                                   # Este bloque se ejecuta siempre, independientemente de si hay excepciones o no
        print("Fin del programa")                                              # Mensaje que indica el fin del programa