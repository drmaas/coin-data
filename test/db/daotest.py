'''
Created on Mar 30, 2014

@author: drmaas
'''
import unittest

from db.coin import Coin
from db.coin import Exchange
from db.dao import CoinDao
from db.dao import ExchangeDao

from db.util import getSession

import os

class DaoTest(unittest.TestCase):

    def setUp(self):
        self.session = getSession()
        self.dao = CoinDao(self.session)

    def tearDown(self):
        pass

    def testCoinDaoGetValues(self):
        values = self.dao.getValues(1, 'btc_usd', 0)
        print values
        self.assertIsNotNone(values, 'CoinDao.getValues returned null')
        self.assertGreater(len(values), 0, 'CoinDao.getValues returned no values')

if __name__ == "__main__":
    unittest.main()