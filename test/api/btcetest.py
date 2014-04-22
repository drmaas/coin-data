'''
Created on Apr 9, 2014

@author: drmaas
'''
import unittest

from api.btce import Btce

class BtceTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetTicker(self):
        btce = Btce()
        result = btce.getTicker('btc_usd')
        print result
        self.assertIsNotNone(result)
        
    def testGetInfo(self):
        btce = Btce()
        result = btce.getInfo()
        print result
        self.assertIsNotNone(result)
        self.assertEquals(1, result['success'])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetTicker']
    unittest.main()