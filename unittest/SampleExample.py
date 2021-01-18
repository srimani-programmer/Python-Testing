import unittest

class SampleTestClass(unittest.TestCase):

    def sample_test1(self):
        self.assertEqual('HELLO', 'hello'.upper())

    def test_sample2(self):
        self.assertEqual(3*3, 9)