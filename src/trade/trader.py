'''
Created on Apr 9, 2014

@author: drmaas
'''

from enum import Enum

class Trader(object):

    def __init__(self):
        pass
    
    def buy(self, exchangeId, pair):
        #0. Check if active orders exist for this pair - if so cancel.
        #1. get account balance for the 2nd portion of the pair. If > 0 we will attempt a buy.
        #2. get latest ask price for pair, that will be target price to buy at.
        #3. the quantity to buy is balance/(buy price)
        #4. Execute trade
        #5. Add entry to trade table about what was decided
        pass
    
    def sell(self, exchangeId, pair):
        #0. Check if active orders exist for this pair - if so cancel.
        #1. get account balance for the 1st portion of the pair. If > 0 we will attempt a sell.
        #2. get latest bid price for pair, that will be target price to sell at.
        #3. the quantity to sell is balance
        #4. Execute trade
        #5. Add entry to trade table about what was decided        
        pass

class TradeState(Enum):
    LONGABOVE,LONGEQUAL,LONGBELOW,NA = range(4)
    
    