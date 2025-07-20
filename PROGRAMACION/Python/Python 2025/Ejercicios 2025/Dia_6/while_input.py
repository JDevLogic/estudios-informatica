
while True :                                                                    # Creamos un bucle con while 
    
    numero = int (input("Introduce un numero menor que 0 o igual: "))           # Pedimos el numero le decimos que ponga un numero menor o igual a 0 
    
    if numero > 0:                                                              # Aqui creamos una condicion de que si el numero es mayor que 0 lo intente de nuevo y se le pide nuevamente el numero
        print("Intentalo de nuevo. ")                                           # El mensaje de que lo vuelva a intentar y despues se le pide el numero de nuevo 
    
    elif numero <= 0:                                                           # Aqui esta la condicion importante que es que el numero debe ser menor o igual a 0 
        print("Correcto. ¡Felicidades!")                                        # El mensaje de que lo a conseguido 
        break                                                                   # Y break para salir del bucle por haberlo conseguido
 

# Este codigo esta mas optimizado y directo. 

while True :  
   
   numero = int (input("Introduce un numero menor que 0 o igual: "))
   
   if numero <= 0:                                                             # Cuando ponga un numero menor o igual que 0 se acabara el bucle
        print("Correcto. ¡Felicidades!")                                       # El mensaje de correcto
        break                                                                  # break para acabar con el bucle
   
   else:                                                                       # else es para cuando no se cumpla la condicion 
        print("Intentelo de nuevo.")                                           # El mensaje de que lo intente de nuevo 