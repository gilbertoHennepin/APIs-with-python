from pprint import pprint
import requests
import os

key = os.environ.get('WEATHER_KEY')
print(key)


url = 'https://api.openweathermap.org/data/2.5/weather?'


city = input('Enter city name: ')
country = input('Enter country code: ')
location = f'{city},{country}'

query = {'q' : location, 'units': 'imperial', 'appid': key}


data = requests.get(url, params=query).json()

pprint(data)

temp = data['main']['temp']
print(f'The current temperature {temp}F')