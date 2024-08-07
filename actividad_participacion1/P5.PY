def farenheit(f):
    celsius = (f - 32)*5/9
    return celsius

f = float(input("ingrese los grados farenheit que quiere convertir a ceslsius: "))
celsius = farenheit(f)
print("la conversion de los grados ingresados a celsius es: ",celsius)

