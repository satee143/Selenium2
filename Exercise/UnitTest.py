__author__ = 'AMMA'

import unittest
from Examples import example

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        print('This will come in starting')
    @classmethod
    def tearDown(self):
        print('This will come at end')
    def test_func(self):
        res=example.sum(self,10,20)
        print(res)
        res=example.sub(self,20,10)
        print(res)
        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
