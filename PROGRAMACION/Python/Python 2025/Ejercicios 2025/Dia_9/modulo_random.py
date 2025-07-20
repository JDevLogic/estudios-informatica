# La libreria de random es una libreria de python que contiene funciones para generar valores aleatorios

import random

numero = random.randint(1, 10)                                      # Genera un numero aleatorio con .randint y dentro de los limites que le pongas (1,10)
print ("El numero aleatorio del 1 al 10 es: ", numero)              # Imprime el numero aleatorio generado

nombres = ["Jonathan", "Lucia", "Bryan","Carlos"]                       # Crea una lista de nombres 
print ("El nombre aleatorio es: ", random.choice(nombres))              # Imprime un nombre aleatorio de la lista de nombres