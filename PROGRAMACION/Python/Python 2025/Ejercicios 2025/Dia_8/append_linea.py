archivo = open ("Ejercicios 2025/Dia_8/notas.txt", "a")                 # "Con a añadimos al final del archivo" (modo escritura) (si no existe lo crea) se debe especificar la ruta completa del archivo

archivo.write (" Linea añadida desde append. \n")                       # Escribe una línea en el archivo

archivo.close()                                                         # MUY IMPORTANTE cerrar el archivo porque si no lo cierras no se guardan los cambios