import ccxt
#print (ccxt.exchanges)
exchanges = ccxt.exchanges
#print (exchanges)
for exchange in exchanges:
    if exchange == 'binance':
        currentExchange = exchange
print(currentExchange)
ethNow = ccxt.binance().fetchOrderBook('ETH/USDT')
print (ethNow['symbol'])