class vehiculo():
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje
    
    def imprimir(self):
        print(f"la velocidad maxima fue de {self.velocidad_maxima} km/h")
        print(f"el kilometraje fue de {self.kilometraje} km")
    
mi_vehiculo = vehiculo(200, 7000)
mi_vehiculo.imprimir()