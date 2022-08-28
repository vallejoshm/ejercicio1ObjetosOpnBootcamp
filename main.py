
class Vehiculo :
    color = None
    ruedas = None
    puertas = None

    def __init__(self, color, puertas, ruedas):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas

class Coche (Vehiculo) :
    velocidad = None
    cilindrada = None

    def __init__(self, velocidad, cilindrada,color, puertas):
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        super().__init__(color, puertas, 4)


miCoche = Coche(60, 1600, "Azul", 3)
print("Mi coche tiene", miCoche.puertas, "puertas.")
print("Es de color", miCoche.color, ".")
print("Su velocidad actual es", miCoche.velocidad, "k/h.")