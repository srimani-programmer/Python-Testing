import unittest

def test_sample1():
    assert 3 == 3


class SampleTestClass(unittest.TestCase):


    def test_sample2(self):
        self.assertEqual(3, 3)