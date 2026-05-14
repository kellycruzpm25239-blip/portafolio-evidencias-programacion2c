class cuenta:

    def __init__(self, cliente, cuenta, saldo):
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo

    def deposito(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad #self.saldo = self.cantidad + cantidad
            return True
        return False
    
def retirar(self, cantidad):
    if cantidad > 0 and cantidad <= self.saldo:
        self.saldo -= cantidad
        return True
    return False

def main():
    pass

if __name__=="__main__":
    main()
    """




def main():
    cuenta1 = Cuenta("Ivan", "12345", 1000)

    cuenta1.deposito(500)
    print("Saldo después del depósito:", cuenta1.saldo)

    cuenta1.retirar(300)
    print("Saldo después del retiro:", cuenta1.saldo)


if __name__ == "__main__":
    main()"""