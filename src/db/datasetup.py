'''
Created on Apr 12, 2014

@author: drmaas
'''

from db.dao import ExchangeDao
from db.dao import PairDao

from db.coin import Coin

from db.util import getSession

def run():
    # connect and get session
    session = getSession()
    
    # setup exchange ids
    exchangeDao = ExchangeDao(session)
    exchangeDao.addExchange('btce')
    exchangeDao.addExchange('campbx')
    exchangeDao.addExchange('cryptsy')
    session.commit()
    
    # setup pairs for btce
    pairDao = PairDao(session)
    btceExchangeId = exchangeDao.getExchangeByName('btce').id
    pairs = [ 'btc_usd', 'ltc_usd', 'ltc_btc', 'nmc_usd', 'nmc_btc', 'ppc_usd', 'ppc_btc', 'xpm_btc' ]
    for pair in pairs:
        pairDao.addPair(btceExchangeId, pair)
    session.commit()
    
    # populate missing pairId for coin entries
    coins = session.query(Coin)
    tuples = { 'btc_usd':9, 'ltc_usd':10, 'ltc_btc':11, 'nmc_usd':12, 'nmc_btc':13, 'ppc_usd':14, 'ppc_btc':15, 'xpm_btc':16 }
    for coin in coins:
        coin.pairId = tuples[coin.pair]
    session.commit()

if __name__ == '__main__':
    run()

    
    
