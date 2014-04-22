'''
Created on Mar 9, 2014

@author: drmaas

Secure api calls based on https://github.com/t0pep0/btc-e.api.python/blob/master/btceapi.py
'''

from base import Base

import hashlib
import hmac
import time
import urllib

class Btce(Base):

    def __init__(self):
        super(Btce, self).__init__('https://btc-e.com')
        self.__key = 'GQRTBGP6-16YAV1WC-8O6OHQW1-DXJ6XF8H-Q5544A7O'
        self.__secret = 'cce87574971e4f906a578922f18358007c777599d87046ea689bf73c7a1f0a30'

    def __nonce(self):
        return str(time.time()).split('.')[0]

    def __signature(self, params):
        return hmac.new(self.__secret, params, digestmod=hashlib.sha512).hexdigest()

    def __api_call(self,method,params):
        self.__nonce()
        params['method'] = method
        params['nonce'] = str(self.__nonce())
        headers = {'Key'  : self.__key,
                   'Sign' : self.__signature(urllib.urlencode(params))}
        r = super(Btce, self).post('/tapi', params, headers)
        return r
 
    def getTicker(self, pair):
        r = super(Btce, self).get('/api/3/ticker/' + pair)
        return r[pair]
 
    def getInfo(self):
        return self.__api_call('getInfo', {})

    def TransHistory(self, tfrom, tcount, tfrom_id, tend_id, torder, tsince, tend):
        params = {
                  "from"    : tfrom,
                  "count"   : tcount,
                  "from_id" : tfrom_id,
                  "end_id"  : tend_id,
                  "order"   : torder,
                  "since"   : tsince,
                  "end"     : tend}
        return self.__api_call('TransHistory', params)
 
    def TradeHistory(self, tfrom, tcount, tfrom_id, tend_id, torder, tsince, tend, tpair):
        params = {
                  "from"    : tfrom,
                  "count"   : tcount,
                  "from_id" : tfrom_id,
                  "end_id"  : tend_id,
                  "order"   : torder,
                  "since"   : tsince,
                  "end"     : tend,
                  "pair"    : tpair}
        return self.__api_call('TradeHistory', params)

    def ActiveOrders(self, tpair):
        params = { "pair" : tpair }
        return self.__api_call('ActiveOrders', params)

    def Trade(self, tpair, ttype, trate, tamount):
        params = {
                  "pair"    : tpair,
                  "type"    : ttype,
                  "rate"    : trate,
                  "amount"  : tamount}
        return self.__api_call('Trade', params)
  
    def CancelOrder(self, torder_id):
        params = { "order_id" : torder_id }
        return self.__api_call('CancelOrder', params)