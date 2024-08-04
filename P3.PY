import random

def generar_lista(tamano):
    lista_aleatoria = [random.randint(1,100) for _ in range(tamano)]
    return lista_aleatoria

tamano = int(input("ingrese la cantidad de la lista: "))
lista_aleatoria = generar_lista(tamano)
print("lista_aleatoria: ")
print(lista_aleatoria)