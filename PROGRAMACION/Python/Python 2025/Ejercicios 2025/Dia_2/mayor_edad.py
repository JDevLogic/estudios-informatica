edad = int(input("Introduce tu edad: "))        # Pedimos al usuario la edad para verificar si es o no mayor de edad

if edad >= 18:                                  # La edad que introduzca debe ser mayor o igual a 18 para que sea mayor de edad
    print ("Eres mayor de edad")                # El mensaje de la mayoria de edad

elif edad >= 0:                                 # Para saber que no es mayor de edad hay una condicion que tiene que ser mayor o igual a 0 
    print ("Eres menor de edad")                # El mensaje de que es menor de edad

else:                                           # Si ninguna de las anteriores se cumple el numero sera no valido por si escriben numeros negativos
    print ("Numero no valido")
