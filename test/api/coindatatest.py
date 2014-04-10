'''
Created on Apr 9, 2014

@author: drmaas
'''
import unittest

from api.coindata import CoinData

class CoinDataTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetEma(self):
        coinData = CoinData()
        result = coinData.getEma('1', 'btc_usd', 1, 8)
        print result
        self.assertIsNotNone(result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()