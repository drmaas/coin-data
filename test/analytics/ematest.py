'''
Created on Mar 30, 2014

@author: drmaas
'''
import unittest
import math

from analytics.ema import calculateEMA

from db.coin import Coin

class emaTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testCalculateEMA(self):
        coins = []
        # 1 days worth of values
        for i in xrange(0,96):
            coins.append(self.createCoin(i))
        
        ema = calculateEMA(coins, 2)
        
        self.assertEquals(math.floor(ema), 60, 'Invalid ema=%6.10f' % ema)

    def createCoin(self, value):
        coin = Coin(pair='btc_usd',
                    high=0.0,
                    low=0.0,
                    average=0.0,
                    bid=0.0,
                    ask=0.0,
                    last=float(value),
                    timestamp=0,
                    exchangeId=1)
        return coin

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCalculateEMA']
    unittest.main()