import turtle
import requests

symbols = requests.get('https://api.binance.com/api/v3/exchangeInfo').json()['symbols']

# Filtrage avec filter
data = filter( lambda elem: 'ETH' in elem['symbol'], symbols )

# Tri avec sorted
data = sorted(data, key=lambda elem: elem['symbol'])

# Transfo avec map
data = map( lambda symbol: symbol['symbol'], data)

print( list(data) )



