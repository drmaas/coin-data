'''
Created on Mar 9, 2014

@author: drmaas
'''

from base import Base

class Btce(Base):

    def __init__(self):
        super(Btce, self).__init__('https://btc-e.com/api/3')
        
    def getTicker(self, pair):
        r = super(Btce, self).get('/ticker/' + pair)
        return r[pair]
    