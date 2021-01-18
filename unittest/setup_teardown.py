import unittest

class SampleTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Entering Test Class')

    @classmethod
    def tearDownClass(cls):
        print('Exiting Test Class')

    def test_sample1(self):
        self.assertEqual(3*3, 9)