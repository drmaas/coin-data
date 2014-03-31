'''
Created on Mar 30, 2014

@author: drmaas
'''

# Calculate exponential moving average
# coins is list of values
# period is amount of time in hours at which to sample
# blocks is the number of blocks to average over
# baseline is ema for 7 2-hour periods and 30 2-hour periods
def calculateEMA(coins, period):
    
    # pre-process values into list of 'period' hour averages
    values = aggregate(coins, period)

    # Step 1: Simple moving average used in first ema calculation as the previous period's value
    sma = calculateSMA(coins)
    
    # Step 2: Multiplier
    multiplier = calculateMultiplier(len(values))
    
    # Step 3: ema
    return calculateEMAInternal(values, sma, multiplier)
    
def aggregate(coins, period):
    
    # number of 15 minute segments/block
    num = period*4
    
    start = 0
    end = num

    aggregates = []
    while True:
        aggregates.append(calculateSMA(coins[start:end]))
        if end >= len(coins):
            break
        else:
            start = end
            end = start + num
    
    return aggregates
    
# simple moving average of all values
def calculateSMA(coins):
    size = len(coins)
    total = 0.0
    for i in xrange(0, size):
        coin = coins[i]
        total = total + coin.last
    return float(total/float(size))

# formula: (2 / (Time periods + 1) )
def calculateMultiplier(periods):
    return float(2.0/(float(periods)+1.0))

# formula is {Close - EMA(previous day)} x multiplier + EMA(previous day)
def calculateEMAInternal(values, sma, multiplier):
    last = len(values) - 1
    if last == 0:
        prevema = sma
    else:
        prevema = calculateEMAInternal(values[0:last], sma, multiplier)
    
    close = values[last]
    return ((close - prevema) * multiplier) + prevema
    