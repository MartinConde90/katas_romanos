import unittest
from romanos import *

class RomanNumberTrest(unittest.TestCase):

    def test_symbols_romans(self):
        self.assertEqual(romano_a_arabigo('I'), 1)
        self.assertEqual(romano_a_arabigo('V'), 5)
        self.assertEqual(romano_a_arabigo('X'), 10)
        self.assertEqual(romano_a_arabigo('L'), 50)
        self.assertEqual(romano_a_arabigo('C'), 100)
        self.assertEqual(romano_a_arabigo('D'), 500)
        self.assertEqual(romano_a_arabigo('M'), 1000)
        self.assertEqual(romano_a_arabigo('A'), 0)


    def test_numeros_crecientes(self):
        self.assertEqual(romano_a_arabigo('XVI'), 16)
        self.assertEqual(romano_a_arabigo('III'), 3)
        
    def test_no_mas_de_tres_repeticiones(self):
        self.assertEqual(romano_a_arabigo('LXXIII'), 73)
        self.assertEqual(romano_a_arabigo('IIII'), 0)
        self.assertEqual(romano_a_arabigo('VV'), 0)

    def test_numeros_decrecientes(self):
        self.assertEqual(romano_a_arabigo('IX'), 9)
        self.assertEqual(romano_a_arabigo('CMXCIX'), 999)

    def test_restas_no_admiten_repeticiones(self):
        self.assertEqual(romano_a_arabigo('MIIX'), 0)

    def test_restas_no_admiten_derivados_del_5(self):
        self.assertEqual(romano_a_arabigo('VC'), 0)

    def test_restas_no_admiten_mas_de_un_orden_de_diferencia(self):
        self.assertEqual(romano_a_arabigo('IC'), 0)
        self.assertEqual(romano_a_arabigo('IL'), 0)
        self.assertEqual(romano_a_arabigo('VL'), 0)

if __name__ == '__main__':
    unittest.main()