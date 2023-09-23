#test file for utils.py
import unittest
from utils import utils

class testClass(unittest.TestCase):

#test reverse func with string, float and int
    def test_reversed(self):
        
        #string
        with self.assertRaises(ValueError):
            utils.reverse('string')
        #float
        with self.assertRaises(ValueError):
            utils.reverse(25.50)
        #integer
        reversed_int = utils.reverse(123)
        self.assertEqual(reversed_int, 321)
# test formatter func with string, float and int
    def test_formatter(self):
        #string
        with self.assertRaises(ValueError):
            utils.formatter('string')
        #float
        with self.assertRaises(ValueError):
            utils.formatter(25.50)
        #integer
        formatter_int = utils.formatter(10)
        self.assertEqual(formatter_int, ('0b1010','0o12'))

if __name__ == '__main__':
    test = testClass()
    test.test_reversed()
    test.test_formatter()