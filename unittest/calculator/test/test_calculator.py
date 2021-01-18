from src.calc_operations import add, sub, multiply
import unittest

def test_sample1():
    assert 3 == 3

class MathModuleTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(7, 11), 18)
        self.assertEqual(add(-7, 11), 4)
        self.assertEqual(add(-5, -8), -13)
        self.assertRaises(TypeError, add, 'hello', 5)

    def test_sub(self):
        self.assertEqual(sub(8, 4), 4)
        self.assertEqual(sub(8, -3), 11)
        self.assertEqual(sub(-8, -3), -5)

    def test_multiply(self):
        self.assertEqual(multiply(8, 4), 32)
        self.assertEqual(multiply(-8, -3), 24)
        self.assertEqual(multiply(-8, 2), -16)

    def test_sample1(self):
        with self.assertRaises(TypeError) as e:
            r = add(3, 'hello')
            self.assertEqual(str(e.exception), "unsupported operand type(s) for +: 'int' and 'str'")

    def test_sample2(self):
        self.assertEqual(3, 3)

if __name__ == '__main__':
    unittest.main()