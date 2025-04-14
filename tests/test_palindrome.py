import unittest
from palindromo import es_palindromo 

class TestPalindromos(unittest.TestCase):
    def test_palabra_simple(self):
        self.assertTrue(es_palindromo("reconocer"))

    def test_con_espacios(self):
        self.assertTrue(es_palindromo("buenas tardes profe quinteros"))

    def test_no_es_palindromo(self):
        self.assertFalse(es_palindromo("race a car"))

    def test_no_es_palindromo(self):
        self.assertFalse(es_palindromo("Mundo"))

if __name__ == '__main__':
    unittest.main()
