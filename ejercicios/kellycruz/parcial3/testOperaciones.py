import unittest
from parcial2.calculadoraBasica import suma, resta ,multi ,div

class TestOperaciones(unittest.TestCase):

    def test_suma_positiva(self):
        self.assertEqual(suma(300,3),303)

    def test_suma_negativa(self):
        self.assertEqual(suma(-4,-6), -10)

    def test_resta_basica(self):
        self.assertEqual(resta(10,5), 5)

    def test_resta_negativa(self):
        self.assertEqual(resta(10,30), -20)

    def test_resta_valorNegativos(self):
        self.assertEqual(resta(-5,-5), -10)