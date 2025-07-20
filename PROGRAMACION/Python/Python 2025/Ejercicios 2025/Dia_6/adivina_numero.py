intentos = 0                                                                        # Creamos una variable que seran los que cuente los intentos empezara por 0 

while True:                                                                         # Creamos un bucle 
    numero_secreto = int (input("Adivina el numero secreto: "))                     # Pedimos que adine el numero al usuario

    if numero_secreto == 7:                                                         # La condicion de que el numero secreto es 7 
        print(f"¡Felicidades! Acertaste el numero en {intentos} intentos. ")        # El mensaje de que acerto con un plus de en cuantos intentos lo consiguio
        break                                                                       # Como acerto se rompe el bucle con break
    
    else:                                                                           # Hasta que no adivine el numero le saldra un mensaje 
        print("Numero incorrecto. Intentelo de nuevo ")                             # El mensaje de que no es y que lo intente de nuevo 
        intentos += 1                                                               # Esto es para que cada vez que falle se sume 1 a intentos y que cuando adivine se le muestre en cuantos lo hizo