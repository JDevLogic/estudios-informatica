# La libreria de datetime es una libreria de python que contiene funciones para trabajar con fechas y horas

import datetime

ahora = datetime.datetime.now()                                # Creamos una variable con la fecha y hora actual
print("Fecha y hora actuales: ", ahora)                        # Imprime la fecha y hora actual

print("Solo la fecha:", ahora.strftime("%d/%m/%Y"))            # Imprime solo la fecha en el formato dia/mes/año
print ("Solo la hora:", ahora.strftime("%H:%M:%S"))            # Imprime solo la hora en el formato hora:minuto:segundo