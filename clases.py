class Mascota:
    def __init__(self, nombre: str, animal: str):
        self.nombre = nombre
        self.animal = animal
        self.raza = None
        self.edad = None
        self.edad_humana = None

    def calcular_edad_humana(self):
        self.edad_humana = self.edad * 7
    
    def dame_nombre(self):
        return self.nombre


class Personaje:
    def __init__(self, nombre: str, vida: int, daño: int):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
    
    def recibir_daño(self, daño_recibido: int):
        self.vida -= daño_recibido
        if self.vida <= 0:
            print(f"{self.nombre} ha perdido")


def combatir(atacante: Personaje, defensor: Personaje):
    defensor.recibir_daño(atacante.daño)

superman = Personaje("Superman", 1000, 100)
rompetechos = Personaje("Rompetechos", 2000, 200)

print(rompetechos.vida)

combatir(superman,rompetechos)

print(rompetechos.vida)
