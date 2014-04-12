'''
Created on Apr 12, 2014

@author: drmaas
'''

from db.dao import ExchangeDao
from db.dao import PairDao

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

if __name__ == '__main__':
    run()

    
    
