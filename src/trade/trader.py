'''
Created on Apr 9, 2014

@author: drmaas
'''

from enum import Enum

class Trader(object):

    def __init__(self):
        pass
    
    def buy(self, exchangeId, pair):
        pass
    
    def sell(self, exchangeId, pair):
        pass

class TradeState(Enum):
    LONGABOVE,LONGEQUAL,LONGBELOW = range(3)
        
    