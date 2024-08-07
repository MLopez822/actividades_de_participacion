def sumadenum(lista):
    suma = 0

    for num in lista:
        suma += num
    return suma

ejemplolista = [1,2,3,4,5,6,7,8,9,10]
resultado = sumadenum(ejemplolista)
print("la suma de los numeros de tu lista es : ",resultado)