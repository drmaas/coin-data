from sqlalchemy import create_engine

'''
Created on Mar 27, 2014

@author: drmaas
'''

def psql_connect():
    return create_engine('postgresql://coin:coin@localhost/coindb', echo=True)
    
def sqlite_connect():
    return create_engine('sqlite:////home/drmaas/projects/python/coin-data/coin.db', echo=True)

    