'''
Created on Mar 9, 2014

@author: drmaas
'''

from api.btce import Btce

from db.coin import Coin
from db.dao import ExchangeDao
from db.util import connect

from threading import Thread

import time

from sqlalchemy.orm import sessionmaker 

def run():
    period = 300
    t1 = Thread(target=run_collector, args=(period,))
    t1.start()   

def run_collector(period):
    
    engine = connect()
        
    # get btce ticker
    btce = Btce() 
    
    pairs = [ 'btc_usd', 'ltc_usd', 'ltc_btc', 'nmc_usd', 'nmc_btc', 'ppc_usd', 'ppc_btc', 'xpm_btc' ]
    
    # get db connection
    session = getSession(engine)
    
    # get exchange id
    exchangeDao = ExchangeDao(session)
    exchangeDao.addExchange('btce')
    exchangeDao.addExchange('campbx')
    exchangeDao.addExchange('cryptsy')    
    
    session.commit()
    
    while True:

        session = getSession(engine)

        btceExchangeId = exchangeDao.getExchangeByName('btce').id
        
        # get btce pairs and save
        for pair in pairs:
            ticker = btce.getTicker(pair)
            coin = Coin(pair=pair,
                        high=float(ticker['high']),
                        low=float(ticker['low']),
                        average=float(ticker['avg']),
                        bid=float(ticker['buy']),
                        ask=float(ticker['sell']),
                        last=float(ticker['last']),
                        timestamp=int(ticker['updated']),
                        exchangeId=btceExchangeId)
            session.add(coin)
    
        # commit and close
        session.commit()
        
        time.sleep(period)

def getSession(engine):
    DBSession = sessionmaker(bind=engine)
    return DBSession()

if __name__ == '__main__':
    run()