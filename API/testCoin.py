
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}



session = Session()
session.headers.update(headers)




try:
  response = session.get(url, params=parameters).json()
  

  coins = response['data']

  for item in coins:
    print(item['symbol'], item['quote']['USD']['price'])
    

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)