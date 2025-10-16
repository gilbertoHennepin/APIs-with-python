import requests

data = requests.get('https://catfact.ninja/fact')
print(response.status_code)


print(response.text)
print(response.json())

data = response.json()
fact = data['fact']
print(f'A random cat fact: {fact}')