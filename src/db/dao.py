'''
Created on Mar 10, 2014

@author: drmaas
'''

from db.coin import Exchange
from db.coin import Coin
from db.coin import Pair

import time

class CoinDao(object):

    def __init__(self, session):
        self.session = session
        
    # Get values of pair for last x hours. days=-1 gets all data, beware!
    def getValues(self, exchangeId, pair, ageInHours=0):
        if ageInHours < 1:
            timestamp = 0
        else:
            now = int(round(time.time()))
            timestamp = now - ageInHours*60*60
            
        values = self.session.query(Coin, Pair).filter(Coin.timestamp > timestamp)\
                                               .filter(Pair.exchangeId == exchangeId)\
                                               .filter(Pair.pair == pair)\
                                               .filter(Pair.id == Coin.pairId).all()
        coins = []
        for value in values:
            coins.append(value[0])
        return coins
    
    # delete values older than maxAgeHours and return the deleted items
    def deleteOldValues(self, exchangeId, maxAgeHours):
        now = int(round(time.time()))
        timestamp = now - maxAgeHours*60*60
        
        values = self.session.query(Coin, Pair).filter(Pair.exchangeId == exchangeId)\
                                               .filter(Coin.timestamp < timestamp)\
                                               .filter(Coin.pairId == Pair.id)\
                                               .all()
        for row in values:
            self.session.delete(row[0])
            
        length = len(values)
        print length," rows deleted: ",values
        
        return values
    
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
    
class PairDao(object):

    def __init__(self, session):
        self.session = session
        
    def addPair(self, exchangeId, pair):
        existingPair = self.getPairByExchangeIdPair(exchangeId, pair)
        if existingPair == None:
            p = Pair(exchangeId=exchangeId, pair=pair)
            self.session.add(p)
        
    def getPairByExchangeIdPair(self, exchangeId, pair):
        res = self.session.query(Pair).filter(Pair.exchangeId == exchangeId)\
                                .filter(Pair.pair == pair)
        if res != None and res.count() > 0:
            retval = res.one()
        else:
            retval = None
        return retval
        
    def getPairsByExchangeId(self, exchangeId):
        return self.session.query(Pair).filter(Pair.exchangeId == exchangeId)
        