class CuentaBancaria:
    def __init__(self, numero_cuenta, propietario, balance):
        self.numero_cuenta = numero_cuenta
        self.propietario = propietario
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto
        print(f"Se ha depositado ${monto} en la cuenta {self.numero_cuenta}. Nuevo balance: ${self.balance}")

    def retirar(self, monto):
        if monto > self.balance:
            print("No hay suficiente dinero en la cuenta para realizar la transaccion.")
        else:
            self.balance -= monto
            print(f"Se ha retirado ${monto} de la cuenta {self.numero_cuenta}. Nuevo balance: ${self.balance}")

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= cuota_manejo
        print(f"Se aplicó una cuota de manejo del 2% sobre la cuenta {self.numero_cuenta}. Nuevo balance: ${self.balance}")

    def mostrar_detalles(self):
        print(f"Detalles de la cuenta {self.numero_cuenta}:")
        print(f"Propietarios: {self.propietario}")
        print(f"Balance: ${self.balance}")

cuenta = CuentaBancaria("1234567890", "Miguel Lopez", 2000)

cuenta.mostrar_detalles()
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.aplicar_cuota_manejo()
cuenta.mostrar_detalles()