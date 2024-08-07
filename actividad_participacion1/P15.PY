def es_palin(texto):
    texto= texto.lower()
    return texto == texto[::-1]
#esta es la funcion de palindromo

def main():
    print("ingrese una cadena de texto:")
    texto = input()
    if es_palin(texto):
        return True 
    else:
        return False
    
if __name__ == "__main__":
    print(main())