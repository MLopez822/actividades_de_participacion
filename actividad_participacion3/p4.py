import math

class punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def mostrar(self):
        print(f'las coordenadas del punto es X: {self.x}, Y: {self.y}')

    def distancia_punto(self):
        distancia = math.sqrt((self.x)**2 + (self.y)**2)
        return distancia
    
class rectangulo():
    def __init__(self, punto1, punto2):
            self.punto1 = punto1
            self.punto2 = punto2

    def calcular_perimetro(self):
        ancho = abs(self.punto2.x - self.punto1.y)
        alto = abs(self.punto2.y - self.punto1.y)
        perimetro = 2 * (ancho + alto)
        return perimetro

    def calcular_area(self):
        ancho = abs(self.punto2.x - self.punto1.x)
        alto = abs(self.punto2.y - self.punto1.y)
        area = ancho * alto
        return area

    def cuadrado(self):
        ancho = abs(self.punto2.x - self.punto1.x)
        alto = abs(self.punto2.y - self.punto1.y)
        return ancho == alto

# Crear dos puntos
punto1 = punto(1, 1)
punto2 = punto(4, 4)

# Crear un rectángulo con los puntos
rectangulo = rectangulo(punto1, punto2)

# Calcular el perímetro del rectángulo
perimetro = rectangulo.calcular_perimetro()
print(f"Perímetro del rectángulo: {perimetro}")

# Calcular el área del rectángulo
area = rectangulo.calcular_area()
print(f"Área del rectángulo: {area}")

# Verificar si el rectángulo es un cuadrado
es_cuadrado = rectangulo.cuadrado()
print(f"¿Es un cuadrado?: {es_cuadrado}")
