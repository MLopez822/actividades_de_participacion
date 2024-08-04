import math

def calculararea(radio):

    return math.pi *( radio **2)

radio = int(input("ingrese el radio del circulo: "))
area = calculararea(radio)
print("el area del circulo es:",area)