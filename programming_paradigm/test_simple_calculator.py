# test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    # Addition tests
    def test_add_positive(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_negative_and_positive(self):
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

    # Subtraction tests
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    # Multiplication tests
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    # Division tests
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 7/3)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    # Edge cases: floats
    def test_float_operations(self):
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.30000000000000004)
        self.assertAlmostEqual(self.calc.divide(1.5, 0.5), 3.0)

if __name__ == "__main__":
    unittest.main()
