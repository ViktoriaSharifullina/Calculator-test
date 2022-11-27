import unittest
from Calculator import *
from Calculator import activeStr

# python -m unittest -v Test.py


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(4, 7), 11)

    def test_difference(self):
        self.assertEqual(difference(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 7), 21)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertRaises(ZeroDivisionError, lambda: division(10, 0))
        self.assertRaises(ArithmeticError, lambda: division(10, 0.00000000001))

    def test_buttons(self):
        for i in range(17):
            self.assertEqual(button[i].invoke()[0], str(button[i]['text']))
        for b in button:
            self.assertTrue(lambda: b.invoke()[1])


if __name__ == "__main__":
    unittest.main()
