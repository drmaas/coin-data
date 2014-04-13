'''
Created on Mar 9, 2014

@author: drmaas
'''

from sqlalchemy import Sequence, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

from db.util import connect

# Base object
Base = declarative_base()

# orm mappings
class Exchange(Base):
    
    __tablename__ = 'exchange'
    
    id = Column(Integer, Sequence('exchange_id_seq'), primary_key=True)
    name = Column(String(50))
    
    def __repr__(self):
        return "<Exchange(id='%i', name='%s')>" % ( self.id. self.name)
    
class Pair(Base):
    
    __tablename__ = 'pair'
    
    id = Column(Integer, Sequence('pair_id_seq'), primary_key=True)
    exchangeId = Column(Integer)
    pair = Column(String(50))
    
    def __repr__(self):
        return "<Pair(id='%i', exchangeId='%i', pair='%s')>" % ( self.id, self.exchangeId, self.pair)    

class Coin(Base):
    
    __tablename__ = 'coin'
    
    id = Column(Integer, Sequence('coin_id_seq'), primary_key=True)
    high = Column(Float(50))
    low = Column(Float(50))
    average = Column(Float(50))
    bid = Column(Float(50))
    ask = Column(Float(50))
    last = Column(Float(50))
    timestamp = Column(Integer)
    pairId = Column(Integer)

    def __repr__(self):
        return "<Coin(id='%i', high='%f', low='%f', average='%f', bid='%f', ask='%f', last='%f', timestamp='%i', pairId='%i')>" % (
                                self.id, self.high, self.low, self.average, self.bid, self.ask, self.last, 
                                self.timestamp, self.pairId)
        
# create db if it doesn't exist
engine = connect()
Base.metadata.create_all(engine)