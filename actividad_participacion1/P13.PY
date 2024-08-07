def calcular(numero1,numero2):

    def suma():
        return numero1 + numero2 

    def resta():
        return numero1 - numero2
      

    def multiplicacion():
        return numero1 * numero2 

    def division():
        if numero2 == 0:
             return "No se puede dividir entre cero"
        else:
            return numero1 / numero2
    
    return suma(),resta(),multiplicacion(),division()

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

try:
    suma, resta, multiplicacion, division = calcular(numero1, numero2)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
except ZeroDivisionError as error:
    print(f"Error: {error}")