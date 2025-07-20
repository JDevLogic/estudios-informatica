class Coordenadas: 
    def __init__ (self, lat,lon):

        self.lat = lat
        self.lon = lon

    def __eq__ (self, otro):                                        # Esto lo que hace es comparar los atributos de la clase
        return self.lat == otro.lat and self.lon == otro.lon    
    
    def __ne__ (self, otro):                                        # Esto lo que hace es comparar los atributos de la clase        
        return self.lat != otro.lat or self.lon != otro.lon

    def __lt__ (self, otro):                                        # Esto lo que hace es comparar los atributos de la clase    
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__ (self, otro):                                        # Esto lo que hace es comparar los atributos de la clase
        return self.lat + self.lon <= otro.lat + otro.lon


coords = Coordenadas (45,27)

coords2 = Coordenadas (45,27)

#print (coords != coords2)                                           # False, porque compara la referencia de memoria  

print (coords >= coords2) 