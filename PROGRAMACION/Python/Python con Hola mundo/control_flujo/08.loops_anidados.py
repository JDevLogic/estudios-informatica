# El bucle interno se ejecuta completamente antes de que el bucle externo avance a la siguiente iteración
# El bucle interno se ejecuta 2 veces por cada iteración del bucle externo
# El bucle externo se ejecuta 3 veces
# En total se ejecuta 3 * 2 = 6 veces

for j in range(3):                          # Creamos un bucle externo
    for k in range(2):                      # Creamos un bucle interno    
        print(f"i: {j}, j: {k}")            # Imprimimos el valor de i y j

   