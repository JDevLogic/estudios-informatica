# Aqui vamos a probar las funciones que hemos creado en el modulo utilidades

from utilidades import saludar, sumar, restar                # Importamos las funciones que hemos creado en el modulo utilidades

saludar("Jonathan")                                          # Llamamos a la funcion saludar y le pasamos el argumento "Jonathan"

resultado = sumar(2, 3)                                      # Llamamos a la funcion sumar y le pasamos los argumentos 2 y 3
print("El resultado de la suma es:", resultado)              # Imprimimos el resultado de la suma

resultado_resta = restar(5, 2)                               # Llamamos a la funcion restar y le pasamos los argumentos 5 y 2

print("El resultado de la resta es:", resultado_resta)       # Imprimimos el resultado de la resta
