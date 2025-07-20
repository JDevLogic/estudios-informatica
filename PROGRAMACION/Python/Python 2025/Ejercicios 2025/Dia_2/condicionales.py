# if -> se ejecuta si la condición es verdadera
# elif -> si la anterior es falsa, prueba esta
# else -> si ninguna es verdadera, se ejecuta esto


numero = int(input("Introduce un numero: "))        # Pedimos al usuario un numero importante ponerlo en int para que sea un numero y input para que el usuario pueda escribir

if numero > 0:                          # Creamos una condicion con if que sea mayor que 0 
    print("El numero es positivo")      # Con ello sabriamos que es positivo 

elif numero < 0:                        # Otra condicion si la otra es falsa se pone elif pero en este caso seria menor que 0 
    print("El numero es negativo")      # Y en este caso sabriamos que es negativo el numero 

else:                                    # Else ya es lo ultimo que si ninguna se cumple 
    print("El numero es cero")           # En este caso ya que no es ni negativo ni positivo pues sera 0.