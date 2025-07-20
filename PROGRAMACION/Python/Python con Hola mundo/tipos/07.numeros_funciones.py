# Funciones para trabajar con operaciones matemáticas
# Estos son algunos de los métodos más comunes para trabajar con números en Python

import math

print (round(1.3))                            # Redondea el número al entero más cercano
print (round(1.5))                            # Redondea el número al entero más cercano
print (round(1.7))                            # Redondea el número al entero más cercano

print (abs(-77))                              # Devuelve el valor absoluto de un número (que sera positivo)
print (abs(55))                               # Devuelve el valor absoluto de un número devuekve el mismo número por ser positivo

print (math.ceil(1.3))                        # Redondea hacia arriba al entero más cercano
print (math.floor(1.999999))                  # Redondea hacia abajo al entero más cercano

print (math.isnan(12))                        # Devuelve False porque 12 no es NaN
#print (math.isnan("23"))

print (math.pow(10, 3))                       # Devuelve 10 elevado a la 3
print (math.sqrt(16))                         # Devuelve la raíz cuadrada de 16