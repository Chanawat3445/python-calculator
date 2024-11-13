import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add2(self):
        self.assertEqual(self.calc.add(1, 9), 10)
    
    def test_sub(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
    def test_sub2(self):
        self.assertEqual(self.calc.subtract(-8, 6), -14)
    
    def test_multi(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
    def test_multi2(self):
        self.assertEqual(self.calc.multiply(6, -1), -6)

    def test_div(self):
        self.assertEqual(self.calc.divide(6, 2),3)
    def test_div2(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
    def test_div3(self):
        self.assertEqual(self.calc.divide(6, -2), -3)
    def test_div4(self):
        self.assertEqual(self.calc.divide(-6, -2), 3)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(6, 2), 0)
    def test_mod2(self):
        self.assertEqual(self.calc.modulo(7, -6), -5)
    def test_mod3(self):
        self.assertEqual(self.calc.modulo(-7, 2), 1)
    def test_mod4(self):
        self.assertEqual(self.calc.modulo(-5, -2), -1)

if __name__ == '__main__':
    unittest.main()