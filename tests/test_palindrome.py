import unittest
from palindromo import es_palindromo  # Esto aún no existe

class TestPalindromos(unittest.TestCase):
    def test_palabra(self):
        self.assertTrue(es_palindromo("reconocer"))

    def test_frases(self):
        self.assertTrue(es_palindromo("hola profe Quinteros"))

    def test_no_es_palindromo(self):
        self.assertFalse(es_palindromo("hola mundo"))
    
    def test_no_es_palindromo(self):
        self.assertFalse(es_palindromo("buenos dias"))


if __name__ == '__main__':
    unittest.main()
