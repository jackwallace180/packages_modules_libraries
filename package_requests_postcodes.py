import requests
import json

request_postcode = requests.get('http://api.postcodes.io/postcodes/' + 'DA157Jz')  #path + arguement

print(request_postcode.headers)   #headers from my path
print(request_postcode.json())    #using json function convert to a dict
print(request_postcode.json().keys())   #finding keys in my dict
print(request_postcode.json()['result']['postcode'])  #calling specific keys in results
print(request_postcode.json()['result']['longitude'])
print(request_postcode.json()['result']['latitude'])

print('my longitude and latitude are: ', request_postcode.json()['result']['longitude'], ', ', request_postcode.json()['result']['latitude'])
