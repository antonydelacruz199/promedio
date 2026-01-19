import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        Conjunto = Conjunto
        self.assertIsNone(Conjunto.promedio())