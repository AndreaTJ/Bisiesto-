import unittest
import bisiesto
"""La lógica de los años bisiestos:
Cómo saber si un año va a ser bisiesto
• Los años bisiestos son los divisibles entre 4 (como 2004, 2008, etc.)
• excepto si es divisible entre 100, entonces no es bisiesto (como 2100, 2200, etc.)
• excepto si es divisible entre 400, entonces sí (como 2000, 2400)"""

class BisiestoTest (unittest.TestCase):
    #El método tiene que empezar por la palabra "Test"
    def test_divisible_4 (self): 
        self.assertEqual(bisiesto.esbisiesto(2004),"Es bisiesto")
        self.assertEqual(bisiesto.esbisiesto(2009),"No es bisiesto")
    
    def test_divisible_100 (self): 
        self.assertEqual(bisiesto.esbisiesto(2100),"No es bisiesto")

    def test_divisible_400 (self): 
        self.assertEqual(bisiesto.esbisiesto(2400),"Es bisiesto")

if __name__ == "__main__": 
    unittest.main() 