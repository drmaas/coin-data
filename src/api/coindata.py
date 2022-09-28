'''
Created on Apr 9, 2014

@author: drmaas
'''

from base import Base
import os

class CoinData(Base):

    def __init__(self):
        super(CoinData, self).__init__('https://coin-data.herokuapp.com', user=os.environ['USER'], passwd=os.environ['PASSWD'])
        
    def getEma(self, exchangeId, pair, period=2, numperiods=7):
        r = super(CoinData, self).get('/ema/' + str(exchangeId) + '/' + pair, params = { 'period':str(period), 'numperiods': str(numperiods) })
        return r['ema']        
        