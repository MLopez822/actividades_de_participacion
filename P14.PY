def cal_media(numeros):
    if not numeros:
        raise ValueError("la lista esta vacia ")
    return sum(numeros)/ len(numeros)

numeros = [1,2,3,4,5,6,7,8,9,10]
media = cal_media(numeros)
print ("la media de la lista de numeros es: ",media)