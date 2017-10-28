import unittest
from calculator import Calculator

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_sum(self):
        self.assertEqual(5, self.calculator.sum(2, 3))

    def test_sub(self):
        self.assertEqual(-1, self.calculator.sub(2, 3))

    def test_mul(self):
        self.assertEqual(6, self.calculator.mul(2, 3))

    def test_div(self):
        self.assertEqual(3, self.calculator.div(6, 2))

    def test_history(self):
        self.calculator.div(6, 2)
        self.assertEqual(1, len(self.calculator.get_history()))
        self.calculator.clear_history()
        self.assertEqual(0, len(self.calculator.get_history()))


if __name__ == '__main__':
    unittest.main()