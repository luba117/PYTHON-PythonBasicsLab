# tests/test_calculator.py
import unittest
import sys
import os

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
   
    def test_divide_by_zero(self):
        with self.assertRaises(Calculator.CalculatorError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()