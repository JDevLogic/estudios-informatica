# Con el with no es necesario cerrar el archivo, se cierra automáticamente al salir del bloque
# Con el with se recomienda usarlo porque es más seguro y evita errores de programación
# El with se usa para abrir archivos y asegurarse de que se cierren correctamente


with open ("Ejercicios 2025/Dia_9/archivo.txt", "w") as archivo:                    # Abre el archivo en (modo escritura) (si no existe lo crea) se debe especificar la ruta completa del archivo

    archivo.write ("algo de texto\n")                                               # Escribe una línea en el archivo

