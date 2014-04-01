from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

import os

'''
Created on Mar 27, 2014

@author: drmaas
'''

def connect():
    dburl = os.environ['DATABASE_URL']
    #return create_engine('sqlite:////home/drmaas/projects/python/coin-data/coin.db', echo=True)
    #localtest: postgresql://coin:coin@localhost/coindb
    return create_engine(dburl, echo=True)     

def getSession():
    engine = connect()
    DBSession = sessionmaker(bind=engine)
    return DBSession()
    