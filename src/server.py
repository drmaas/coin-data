from flask import Flask
from flask import request
from flask import jsonify

from db.util import connect
from db.util import getSession

from db.dao import CoinDao 

from analytics.ema import calculateEMA

'''
Created on Mar 30, 2014

@author: drmaas
'''

app = Flask(__name__)

# Note: 7 and 30 seem good numperiods defaults
@app.route('/ema/<int:exchangeId>/<pair>', methods=['GET'])
def getEMA(exchangeId, pair):
    # get period in hours, and number of periods to average over
    period = int(request.args.get('period', '2'))
    numperiods = int(request.args.get('numperiods', '7'))
    ageInHours = period*numperiods
    
    # get list of values
    coinDao = getCoinDao()
    values = coinDao.getValues(exchangeId, pair, ageInHours)
    
    # calculate the ema of the values returned
    ema = calculateEMA(values, period)
    
    # return json
    return jsonify(exchangeId=exchangeId, pair=pair, ema=ema)

def getCoinDao():
    engine = connect()
    session = getSession(engine)
    return CoinDao(session)
        