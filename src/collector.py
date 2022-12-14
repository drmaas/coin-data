'''
Created on Mar 9, 2014

@author: drmaas
'''

from api.btce import Btce

from db.coin import Coin

from db.dao import ExchangeDao
from db.dao import CoinDao
from db.dao import PairDao
from db.util import getSession

from trade.trader import Trader
from trade.trader import TradeState

#from api.coindata import CoinData

from analytics.ema import Ema

from threading import Thread

import time

def run():
    # Run once every 10 minutes
    period1 = 600
    t1 = Thread(target=run_collector, args=(period1,))
    # Run once per hour
    period2 = 3600 
    maxAgeHours = 24*7
    t2 = Thread(target=run_cleanup, args=(period2,maxAgeHours))
    # Run once every 5 minutes
    period3 = 300
    t3 = Thread(target=run_trader, args=(period3,1,1,8,24))
    
    t1.start()
    t2.start()
    t3.start()

# collect data
def run_collector(period):
      
    # get btce ticker
    btce = Btce() 
    
    while True:       
        # get exchange id
        session = getSession() 
        exchangeDao = ExchangeDao(session)
        btceExchangeId = exchangeDao.getExchangeByName('btce').id
        
        # get available pairs
        pairDao = PairDao(session)
        pairs = pairDao.getPairsByExchangeId(btceExchangeId)
    
        # get btce pairs and save
        coins = []
        for pairObj in pairs:
            pair = pairObj.pair
            pairId = pairObj.id
            ticker = btce.getTicker(pair)
            coin = Coin(high=float(ticker['high']),
                        low=float(ticker['low']),
                        average=float(ticker['avg']),
                        bid=float(ticker['buy']),
                        ask=float(ticker['sell']),
                        last=float(ticker['last']),
                        timestamp=int(ticker['updated']),
                        pairId=pairId)
            coins.append(coin)
    
        # commit and close
        session.add_all(coins)
        session.commit()
        
        session.close()
        time.sleep(period)
    
# Expunge entries older than maxAgeDays    
def run_cleanup(period, maxAgeHours):

    while True:
        # get db connection
        session = getSession() 
        coinDao = CoinDao(session)
        
        exchangeDao = ExchangeDao(session)
        btceExchangeId = exchangeDao.getExchangeByName('btce').id
        
        coinDao.deleteOldValues(btceExchangeId, maxAgeHours)
        session.commit()
        
        session.close()
        time.sleep(period)
    
# Trade them coins
def run_trader(period, shortperiod, longperiod, shortnumperiods, longnumperiods):
    
    trader = Trader()
    prevstate = TradeState.NA
    
    while True:
        session = getSession() 
        exchangeDao = ExchangeDao(session)
        btceExchangeId = exchangeDao.getExchangeByName('btce').id
        
        # get available pairs
        pairDao = PairDao(session)
        pairs = pairDao.getPairsByExchangeId(btceExchangeId)
            
        ema = Ema(session)
        for pairObj in pairs:
            pair = pairObj.pair
            #shortema = coinData.getEma(btceExchangeId, pair, shortperiod, shortnumperiods)
            #longema = coinData.getEma(btceExchangeId, pair, longperiod, longnumperiods)
            shortema = ema.getEma(btceExchangeId, pair, shortperiod, shortnumperiods)
            longema = ema.getEma(btceExchangeId, pair, longperiod, longnumperiods)
            print "Short ema:"+str(shortema)+". Long ema:"+str(longema)
            print "Previous state:"+str(prevstate)
            if shortema < longema:
                if prevstate == TradeState.LONGBELOW or prevstate == TradeState.LONGEQUAL:
                    print "SELL "+pair+" IF POSSIBLE"
                    trader.sell(btceExchangeId, pair)
                else:
                    print "HOLD "+pair
                prevstate = TradeState.LONGABOVE
            else:
                if prevstate == TradeState.LONGABOVE or prevstate == TradeState.LONGEQUAL:
                    print "BUY "+pair+" IF POSSIBLE"
                    trader.buy(btceExchangeId, pair)
                else:
                    print "HOLD fiat, wait to buy "+pair
                prevstate = TradeState.LONGBELOW
        
        session.close()
        time.sleep(period)

if __name__ == '__main__': 
    run()