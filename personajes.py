import random

class Personaje:
    def __init__(self, nombre: str, vida: int, daño: int):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
    
    def atacar(self) -> bool:
        acertar = random.choice([True, False])
        if acertar:
            print(f"{self.nombre} fue certero en el ataque.")
        return acertar


    def recibir_daño(self, daño_recibido: int):
        print(f"{self.nombre} ha recibido {daño_recibido} de daño")
        self.vida -= daño_recibido
        if self.vida <= 0:
            print(f"{self.nombre} ha perdido.")


def combatir(atacante: Personaje, defensor: Personaje):
    if atacante.atacar():
        defensor.recibir_daño(atacante.daño)

superman = Personaje("Superman", 1000, 100)
rompetechos = Personaje("Rompetechos", 2000, 200)

print(rompetechos.vida)

combatir(superman,rompetechos)

print(rompetechos.vida)
