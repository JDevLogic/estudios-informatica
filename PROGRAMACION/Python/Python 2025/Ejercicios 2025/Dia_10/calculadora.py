# Creamos una calculadora + saludo + fecha y hora con funciones importadas

from utilidades import sumar, restar, saludar            # Importamos las funciones que hemos creado en el modulo utilidades.py
import datetime                                          # Importamos el modulo datetime para la fecha y hora


while True:

    print("1. Sumar")                                                  # Un mensaje de la primera opcion sumar  
    print("2. Restar")                                                 # Mensaje de la segunda opcion restar
    print("3, Saludo")                                                 # Mensaje de la tercera opcion Saludo
    print("4. Fecha y hora actual")                                    # Mensaje de la cuarta opcion Fecha y hora
    print("5. Salir")                                                  # Esta opcion es para salir del bucle

    opcion = input ("Eliga la operacion: ")                            # Para que eliga la opcion el usuario

    if opcion == "1":                                                            # Creamos unas condicion para el comportamiento de las opciones en este caso el 1 (Sumar)

        num1 = int(input("Introduce el primer numero: "))                        # Se pide el primer numero al usuario numero entero
        num2 = int(input("Introduce el segundo numero: "))                       # Se pide el segundo numero para la operacion
        
        resultado = sumar(num1, num2)                                            # Creamos la variable resultado con la funcion sumar porque es la opcion 1
        print("El resultado de la suma es: ", resultado)                         # Aqui imprimimos el mensaje con el resultado

    elif opcion == "2":                                                          # Aqui creamos la opcion 2 (Restar)
        num1 = int(input("Introduce el primer numero: "))                        # Se pide el primer numero al usuario numero entero
        num2 = int(input("Introduce el segundo numero: "))                       # Se pide el segundo numero para la operacion
        
        resultado = restar(num1,num2)                                            # Creamos la variable resultado con la funcion restar porque es la opcion 2
        print("El resultado de la resta es: ",resultado)                         # Se imprime el mensaje del resultado

    elif opcion == "3":
        nombre = input("Introduce tu nombre: ")                                  # Se pide el nombre al usuario
        saludar(nombre)                                                          # Llamamos a la funcion saludar y le pasamos el nombre
    
    elif opcion == "4": 
        ahora = datetime.datetime.now()                                          # Creamos la variable ahora con la fecha y hora actual 
        print("Fecha y hora actuales: ", ahora)                                  # Imprimimos la fecha y hora actual 

    elif opcion == "5":
        print("Saliendo de la calculadora...")                                   # Imprimimos un mensaje para que sepa el usuario que esta saliendo
        break                                                                    # Y con break se rompe el bucle y sale

    else:                                                                        # Creamos un else por si el usuario elige un numero que no esta en el menu
        print("Opcion no valida. Elige una opcion del 1 al 4.")                  # Este es el mensaje que sale para el usuario