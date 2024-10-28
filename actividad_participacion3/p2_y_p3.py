import math

class punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f'las coordenadas del punto es X: {self.x}, Y: {self.y}')

    def nueva_coordenada(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def distancia_punto(self):
        distancia = math.sqrt((self.x)**2 + (self.y)**2)
        return distancia

#creamos dos puntos  
punto1 = punto(6,4)
punto2 = punto(3,5)

#mostramos las coordenadas de los puntos
punto1.mostrar()
punto2.mostrar()  

#movemos los puntos o generamos una nueva coordenada
punto1.nueva_coordenada(7, 5)
punto1.mostrar()


#calculamos la distancia entre los puntos
print(f'la distancia entre los puntos es: {punto1.distancia_punto()}')
