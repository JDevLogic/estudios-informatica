def sumar (num1:int ,num2:int )-> int:                  # Creamos la funcion del operador que queramos en este caso la de sumar 
    """
    Suma dos numeros.

    Parameters:
          num1 (int): Primer numero a sumar.
          num2 (int): Segundo numero a sumar.

    Returns:
            int: Resultado de la suma.
    """
    return num1 + num2                           # Tiene que guardar el resultado de las suma que suma el num1 con el num2  

def restar (num1:int ,num2:int )-> int:                 # Esta es la funcion de restar 
    """
    Resta dos numeros.

    Parameters:
          num1 (int): Primer numero a restar.
          num2 (int): Segundo numero a restar.
    
    Returns:
            int: Resultado de la resta.
    """
    return num1 - num2                           # Guarda el resultado de la resta entre num1 y num2 

def multiplicar (num1:int ,num2:int )-> int:            # Funcion de multiplicacion 
    """
    Multiplica dos numeros.

    Parameters:
          num1 (int): Primer numero a multiplicar.
          num2 (int): Segundo numero a multiplicar.
    
    Returns:
            int: Resultado de la multiplicacion.
    """
    return num1 * num2                                  # Guarda el resultado multiplicando num1 y num2

def division (num1:int ,num2:int )-> int:               # Funcion para dividir 2 numeros
    """
    Divide dos numeros.

    Parameters:
          num1 (int): Primer numero a dividir.
          num2 (int): Segundo numero a dividir.
    
    Returns:
            int: Resultado de la division.
    """
    if num2 != 0:                                       # Creamos una condicion que el num2 sea distinto de 0 porque da un error ZeroDivisionError 
        return num1 / num2                              # Guarda el resultado de la division 
    else:
        return "No se puede dividir entre cero"               # Si el numero es cero te dice que no se puede y te sale ese mensaje 


num1 = int(input("Introduce el primer numero: "))             # Se pide el primer numero al usuario numero entero
num2 = int(input("Introduce el segundo numero: "))            # Se pide el segundo numero para la operacion


while True:                                              # Se crea un bucle para hacer una interfaz de la operacion    
    print("1. Sumar")                                    # Un mensaje de la primera opcion sumar  
    print("2. Restar")                                   # Mensaje de la segunda opcion restar  
    print("3. Multiplicar")                              # Mensaje de la tercera opcion multiplicar 
    print("4. Dividir")                                  # Mensaje de la cuarta opcion Dividir
    print("0. Salir")                                    # Esta opcion es para salir del bucle 

    opcion = input ("Eliga la operacion: ")              # Para que eliga la opcion el usuario 

    if opcion == "1":                                                            # Creamos unas condicion para el comportamiento de las opciones en este caso el 1 (Sumar)
        resultado = sumar(num1, num2)                                            # Creamos la variable resultado con la funcion sumar porque es la opcion 1 
        print("El resultado de la suma es: ", resultado)                         # Aqui imprimimos el mensaje con el resultado 
    
    elif opcion == "2":                                                          # Aqui creamos la opcion 2 (Restar) 
        resultado = restar(num1,num2)                                            # Creamos la variable resultado con la funcion restar porque es la opcion 2 
        print("El resultado de la resta es: ",resultado)                         # Se imprime el mensaje del resultado 
    
    elif opcion == "3":                                                          # Aqui creamos la opcion 3 (Multiplicacion) 
        resultado = multiplicar(num1,num2)                                       # Creamos la variable resultado con la funcion multiplicar porque es la opcion 3  
        print("El resultado de la multiplicacion es: ", resultado)               # Se imprime el mensaje del resultado           
    
    elif opcion == "4":                                                          # Aqui creamos la opcion 4 (Division) 
        resultado = division(num1,num2)                                          # Creamos la variable resultado con la funcion division porque es la opcion 4
        print("El resultado de la division es: ", resultado)                     # Se imprime el mensaje del resultado 
    
    elif opcion == "0":                                                          # Aqui la ultima opcion que es la de salir de calculadora basica
        print("Saliendo de la calculadora...")                                   # Imprimimos un mensaje para que sepa el usuario que esta saliendo
        break                                                                    # Y con break se rompe el bucle y sale 

    else:                                                                        # Creamos un else por si el usuario elige un numero que no esta en el menu 
        print("Opcion no valida. Elige una opcion del 0 al 4.")                  # Este es el mensaje que sale para el usuario      
    
        