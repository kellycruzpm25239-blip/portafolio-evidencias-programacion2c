from cuenta import Cuenta

class Banco:

    def transferir(self, origen, destino, cantidad):
        if origen.retirar():
            destino.deposito(cantidad)
            return True
        return False