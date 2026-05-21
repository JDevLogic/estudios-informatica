class Personaje:
    def __init__(self,nombre,vida,nivel):
        self.nombre  = nombre
        self.vida = vida
        self.nivel = nivel
    
    def atacar (self,objetivo,daño):
        print (f"{self.nombre} ataca a {objetivo.nombre} con {daño} de daño.")
        objetivo.recibir_daño(daño)

    def curar (self):
        print (f"{self.nombre} se cura 10 puntos.")
        self.vida += 10
        
    def recibir_daño (self,daño):
        self.vida -= daño
        if self.vida <= 0:
            print(f"{self.nombre} te quedaste sin vida. MORISTE.")

    def subir_nivel (self):
        self.nivel += 1
        self.vida += 20
        print (f"Subiste de nivel {self.nombre} y te curaste 20 puntos de vida adicionales.")

class Guerrero(Personaje):
    
    def atacar (self,objetivo):
        print (f"{self.nombre} golpea con la espada a {objetivo.nombre} con 25 de daño.")
        objetivo.recibir_daño(25)
    
    def ataque_especial(self,objetivo):
        print (f"{self.nombre} golpea con la espada de escalibur a {objetivo.nombre} con 40 de daño.")
        objetivo.recibir_daño(40)

class Mago (Personaje):
    
    def atacar (self,objetivo):
        print (f"{self.nombre} lanza un conjuro basico a {objetivo.nombre} con 20 de daño.")
        objetivo.recibir_daño(20)
    
    def conjuro_fuego(self,objetivo):
        print (f"{self.nombre} ataca a {objetivo.nombre} con 30 de daño.")
        objetivo.recibir_daño(30)
    

jonathan = Personaje("Jonathan",70,1)
lucia = Personaje("Lucia",80, 3)
paladin =Guerrero("Paladin",1000,50)
mago = Mago("Mago",500,30)

jonathan.curar()
lucia.curar()

jonathan.atacar(lucia, 25)
lucia.atacar(jonathan,10)

paladin.atacar(jonathan)
paladin.ataque_especial(jonathan)

mago.conjuro_fuego(paladin)
mago.atacar(paladin)

# mago.ataque_especial(jonathan)
# paladin.conjuro_fuego(mago)

jonathan.subir_nivel()
lucia.subir_nivel()

print(jonathan.nombre,jonathan.vida,jonathan.nivel)
print(lucia.nombre,lucia.vida,lucia.nivel)
print(paladin.nombre,paladin.vida,paladin.nivel)