archivo = open ("Ejercicios 2025/Dia_8/notas.txt", "r")              # Abre el archivo en (modo lectura) (si no existe lo crea)

print(archivo.read())                                                # Lee el contenido del archivo y lo imprime en pantalla

archivo.close()                                                      # IMPORTANTE cerrar el archivo