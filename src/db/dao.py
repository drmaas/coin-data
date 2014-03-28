'''
Created on Mar 10, 2014

@author: drmaas
'''

from db.coin import Exchange

class CoinDao(object):

    def __init__(self, session):
        self.session = session
    
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