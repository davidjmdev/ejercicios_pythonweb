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

Tuna = Mascota("Tuna", "Gato")
Tuna.edad = 3

print(Tuna.edad)

print(Tuna.edad_humana)

Tuna.calcular_edad_humana()
print(Tuna.edad_humana)

print(Tuna.dame_nombre())