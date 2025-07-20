# Existen dos tipos de bucles en Python:

# 1. while: Se repite mientras la condición sea verdadera.
# 2. for: Se repite un número determinado de veces o sobre una secuencia (listas, rangos, etc.).

# while -> útil cuando no sabemos cuántas veces se repetirá
# for -> útil cuando sabemos las veces o iteramos sobre un rango o lista



contador = 1                                # Hacemos que el contador tenga el valor de 1 que empiece por 1 

while contador <=5:                         # Creamos el bucle con while que es menor o igual a 5 
    print("Contador: ",contador)            # El mensaje del contador aqui saldran los numeros del contador
    contador += 1                           # Para que no sea un bucle de solo unos y sea un contador al final se le suma 1 hasta que llegue hasta 5 




for numero in range (1,6):                  # Recorre el numero del 1 al 5
    print("Numero: ", numero)               # Este es el mensaje que sale al iniciar el codigo





for numero in range (0,10,2):               # Recorre desde 0 hasta 10 (sin incluir el 10) sumando de 2 en 2
    print ("Numero: ", numero)              # Este es el mensaje que saldria con los pares