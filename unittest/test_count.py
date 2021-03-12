import unittest

class SampleTestClass(unittest.TestCase):


    def test_sample1(self):
        self.assertRaises(TypeError, pow, 2, '4')

    def test_sample2(self):
        self.assertRaises(Exception, max, [7, 8, '4'])

    def test_sample3(self):
        self.assertRaises(ValueError, int, 'hello')