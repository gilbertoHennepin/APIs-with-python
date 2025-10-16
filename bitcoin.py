import requests
from pprint import pprint


coindesk_url = 'https://claraj.github.io/mock-bitcoin/currentprice.json'

response = requests.get(coindesk_url)
data = response.json()
#print(data)

dollars_exchange_rate = data['bpi']['USD']['rate_float']
print(f'Bitcoin price in USD: $ {dollars_exchange_rate}')

bitcoin = float(input('Enter the number of bitcoins: '))

bitcoin_value = bitcoin * dollars_exchange_rate

print(f'Value of {bitcoin} bitcoins is $ {bitcoin_value}')