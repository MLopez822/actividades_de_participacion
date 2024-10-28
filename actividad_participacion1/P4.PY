def par_o_impar(n):
    if n % 2 == 0:
           return True
    else: 
        return False

n = int(input("ingrese un numero: "))
print(par_o_impar(n))