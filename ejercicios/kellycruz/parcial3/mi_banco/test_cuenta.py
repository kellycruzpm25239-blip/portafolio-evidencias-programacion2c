import unittest
from cuenta import cuenta

class TestCuenta(unittest.Testcase):

    def setUP(self):
        """
        se ejecuta antes de cada prueba
        """
        self.cuenta = cuenta("Fulanito Perez Mengano","001")

    #-------------PRUEVAS DE CONTRUCCION-------------
#cada prueba OBLIGATORIAMENTE debe llevar TEST
    def test_valida_saldo(self):
        self.assertEqual(self, cuenta.saldo, 0, "El saldo inicial debera ser 0 por defecto")
    def test_validar_cliente(self):
        self.assertEqual(self.cuenta.cliente, "Fulanito Perez Mengano","El nomdre del cliente")

        #-----------------PRUEBAS DE DEPOSITO-----------------

        def test_depositar_dinero_valido(self):
            result = self.cuenta.deposito(500)
            self.assertTrue(result)
            self.asserEqua(self,cuenta.saldo, 500, "el saldo actual deberia ser de 500")
        
        def test_depositar_cantidad_negativa(self):
            result = self.cuenta.deposito(-200)
            self.assertFalse(result)
            self.assertEqual(self, cuenta.saldo, 0, "El saldo actual deberia ser 0")

            #TEST PARA VALIDAR DEPOSITO EN 0
        def test_depositar_dinero_cero(self):
            result = self.cuenta.deposito(0)
            self.assertFalse(result)
            self.assertEqual(self, cuenta.saldo, 0, "El saldo actual debera se 0")

        #------------------PRUEBAS DE RETIRO------------------#
        
        #----------TEST PARA VALIDAR RETIRO CON CANTIDAD 0----------#
        def test_retirar_cantidad_0(self):
            self.cuenta.deposito(500)
            result = self.cuenta.retiro(200)
            self.assertTrue(result)
            self.assertEqual(self,cuenta.saldo, 300, "El saldo actual deberia ser 300")

            #----------TEST PARA VALIDAR RETIRO COM CANTIDA NEGATIVA----------#
            def test_retirar_dinero_mayor_saldo(self):
                self.cuenta.deposito(300)
                result = self.cuenta.retiro(400)

            #----------TEST PARA VALIDAD CANTIDAD MAYOR AL SALDO----------#
            self.assertEqual(self, cuenta.saldo, 300, "Elsaldo actual deberia ser de 300")
            
            def test_retirar_dinero_mayor(self):
                self.cuenta.deposito(300)
                result = self.cuenta.retiro(400)