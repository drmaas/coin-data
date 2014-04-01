from flask import Flask
from flask import request
from flask import jsonify

from security.auth import basicauth

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
@basicauth
def getEMA(exchangeId, pair):
    # get period in hours, and number of periods to average over
    period = int(request.args.get('period', '2'))
    if period < 1 or period > 24:
        return jsonify(error="Period must be between 1 and 24 hours")
    numperiods = int(request.args.get('numperiods', '7'))
    if numperiods < 1 or numperiods > 30:
        return jsonify(error="Averages can only be calculated on ranges from 1-30 time blocks")
    ageInHours = period*numperiods
    
    # get list of values
    session = getSession()
    coinDao = CoinDao(session)
    values = coinDao.getValues(exchangeId, pair, ageInHours)
    
    # calculate the ema of the values returned
    ema = calculateEMA(values, period)
    
    session.close()
    
    # return json
    return jsonify(exchangeId=exchangeId, pair=pair, ema=ema)