# Sirve para que manegar los errores y que el programa no crashee

try:                                                        # Try es de intentar haber si da algun error 
    numero = int(input("Introduce un numero: "))            # Aqui un mensaje de que esta bien 
    print("Numero valido: " , numero)

except:                                                     # Esto seria como un else pero except evita que se crashee 
    print("¡ESO no es un numero valido!")                   # El mensaje que imprime si no pone un numero valido 