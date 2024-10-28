import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def pertenece(self, punto):
        distancia = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia <= self.radio
    
circulo = Circulo((0, 0), 5)  # crea un círculo con centro en (0, 0) y radio 5
print(circulo.area())  # imprime el área del círculo
print(circulo.perimetro())  # imprime el perímetro del círculo
print(circulo.pertenece((3, 4)))  # imprime True si el punto (3, 4) pertenece al círculo, False en caso contrario