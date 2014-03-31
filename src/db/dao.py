'''
Created on Mar 10, 2014

@author: drmaas
'''

from db.coin import Exchange
from db.coin import Coin

import time

class CoinDao(object):

    def __init__(self, session):
        self.session = session
        
    # Get values of pair for last x days. days=-1 gets all data, beware!
    def getValues(self, exchangeId, pair, ageInHours=0):
        if ageInHours < 1:
            timestamp = 0
        else:
            now = int(round(time.time()))
            timestamp = now - ageInHours*60*60
            
        values = self.session.query(Coin).filter(Coin.exchangeId == exchangeId).\
                                          filter(Coin.pair == pair).\
                                          filter(Coin.timestamp > timestamp)
        return values.all()
    
class ExchangeDao(object):
    
    def __init__(self, session):
        self.session = session
        
    def addExchange(self, name):
        ex = self.getExchangeByName(name)
        if ex == None:
            ex = Exchange(name=name)
            self.session.add(ex)
        
    def getExchangeByName(self, name):
        res = self.session.query(Exchange).filter(Exchange.name == name)
        if res != None and res.count() > 0:
            ex = res.one()
        else:
            ex = None
        return ex