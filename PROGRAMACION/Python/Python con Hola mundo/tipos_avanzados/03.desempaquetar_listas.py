#numeros = [1, 2, 3]

# FEO!
# primero = numeros[0]          # Asigna el primer elemento de la lista a la variable primero
# segundo = numeros[1]          # Asigna el segundo elemento de la lista a la variable segundo
# tercero = numeros[2]          # Asigna el tercer elemento de la lista a la variable tercero

numeros = [1,2,3,4,5,6,7,8,9]                           # Crea una lista de números del 1 al 9

primero,segundo,*resto, penultimo,ultimo = numeros      # Desempaqueta la lista en las variables primero, segundo, resto, penultimo

print(segundo,penultimo,*resto)                         # Imprime el segundo, penultimo y resto de la lista