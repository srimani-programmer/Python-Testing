from math_module import add, sub, multiply
import unittest

class MathModuleTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(7, 11), 18)
        self.assertEqual(add(-7, 11), 4)
        self.assertEqual(add(-5, -8), -13)

    def test_sub(self):
        self.assertEqual(sub(8, 4), 4)
        self.assertEqual(sub(8, -3), 11)
        self.assertEqual(sub(-8, -3), -5)

    def test_multiply(self):
        self.assertEqual(multiply(8, 4), 32)
        self.assertEqual(multiply(-8, -3), 24)
        self.assertEqual(multiply(-8, 2), -16)