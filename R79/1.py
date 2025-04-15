import unittest
import math
def cuadratica(a,b,c):
    t1 = (b**2) - 4 * a * c
    # Calculate the roots
    root1 = (-b - math.sqrt(t1)) / (2 * a)
    root2 = (-b + math.sqrt(t1)) / (2 * a)
    return root1, root2

class ValidarFuncionCuadratica(unittest.TestCase):
    def test_numeros_correctos(self):
        self.assertTrue(cuadratica(5, 10,15))
    
    def test_numeros_incorrectos(self):
        self.assertTrue(cuadratica(3,4,1))

    def test_numeros_invalidos(self):
        self.assertTrue(cuadratica(0,0,0))

if __name__ == '__main__':
    unittest.main()
