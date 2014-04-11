'''
Created on Mar 30, 2014

@author: drmaas
'''

from db.dao import CoinDao 

class Ema(object):

    def __init__(self, session):
        self.session = session

    # Return ema as a value based on period and numperiods
    def getEma(self, exchangeId, pair, period=2, numperiods=7):
        ageInHours = period*numperiods
        
        # get list of value
        coinDao = CoinDao(self.session)
        values = coinDao.getValues(exchangeId, pair, ageInHours)
        
        # calculate the ema of the values returned
        return self.calculateEma(values, period)
        
    # Calculate exponential moving average
    # coins is list of values
    # period is amount of time in hours at which to sample
    # blocks is the number of blocks to average over
    # baseline is ema for 7 2-hour periods and 30 2-hour periods
    def calculateEma(self, coins, period):
        
        # pre-process values into list of 'period' hour averages
        values = self.aggregate(coins, period)
    
        # Step 1: Simple moving average used in first ema calculation as the previous period's value
        sma = self.calculateSMA(coins)
    
        # Step 2: Multiplier
        multiplier = self.calculateMultiplier(len(values))
    
        # Step 3: ema
        return self.calculateEMAInternal(values, sma, multiplier)
        
    def aggregate(self, coins, period):
        
        # number of 10 minute segments/block
        num = period*6
        
        start = 0
        end = num
    
        aggregates = []
        if len(coins) > 0:
            while True:
                aggregates.append(self.calculateSMA(coins[start:end]))
                if end >= len(coins):
                    break
                else:
                    start = end
                    end = start + num
        
        return aggregates
        
    # simple moving average of all values
    def calculateSMA(self, coins):
        size = len(coins)
        total = 0.0
        if (size > 0):
            for i in xrange(0, size):
                coin = coins[i]
                total = total + coin.last
        else:
            size = 1
        return float(total/float(size))
    
    # formula: (2 / (Time periods + 1) )
    def calculateMultiplier(self, periods):
        return float(2.0/(float(periods)+1.0))
    
    # formula is {Close - EMA(previous day)} x multiplier + EMA(previous day)
    def calculateEMAInternal(self, values, sma, multiplier):
        last = len(values) - 1
        if last <= 0:
            prevema = sma
        else:
            prevema = self.calculateEMAInternal(values[0:last], sma, multiplier)
        if last >= 0:
            close = values[last]
        else:
            close = 0.0
        return ((close - prevema) * multiplier) + prevema