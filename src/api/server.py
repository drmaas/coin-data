from flask import Flask
from flask import request

from db.util import connect
from db.util import getSession

from db.dao import CoinDao 

'''
Created on Mar 30, 2014

@author: drmaas
'''

app = Flask(__name__)

@app.route('/ema/<int:exchangeId>/<pair>', methods=['GET'])
def getEMA(exchangeId, pair):
    ageInDays = int(request.args.get('age', '0'))
    coinDao = getCoinDao()
    values = coinDao.getValues(exchangeId, pair, ageInDays)
    # calculate the ema of the values returned

def getCoinDao():
    engine = connect()
    session = getSession(engine)
    return CoinDao(session)
        