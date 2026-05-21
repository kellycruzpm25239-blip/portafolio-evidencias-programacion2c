import unittest

from cuenta import Cuenta
from banco import Banco

class TestIntegracionBanco(unittest.TestCase):
    def setUp(self):
        self.cuenta1 = Cuenta("Fulanito Perez", "001", 1000)
        self.cuenta2 = Cuenta("Perezcila Sanches", "002")

        self.banco = Banco()

    def test_transferencia_exitosa(self):
        resultado = self.banco.transferir(self.cuenta1, self.cuenta2, 350)
        self.assertTrue(resultado, "Deberia realizarse de manera correcta la transferencia")
        self.assertEqual(self.cuenta1.saldo, 650, "El saldo de la cuenta 1 deberia ser 650")
        self.assertEqual(self.cuenta2.saldo, 350, "el saldo de la cuenta deveria ")

    def test_transferencia_saldo_insuficiente(self):
        resultado = self.banco.transferir(self.cuenta1, self.cuenta2, 1200)
        self.assertFalse(resultado, "la transerencia no se deveria realizar al no disponer del saldo insuficiente")
        self.assertEqual(self.cuenta1.saldo)

    def test_transferencia_saldo_insuficienta(self):
        resultado = self.banco.transferir(self.cuenta2,)