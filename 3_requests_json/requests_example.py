import requests
import pprint

r = requests.get('https://api.spacexdata.com/v3/capsules')
print(r.status_code)
print('*************************************************')
print(r.headers['content-Type'])
print('*************************************************')
print(r.encoding)
print('*************************************************')
print(r.text)
print('*************************************************')
print(pprint.pprint(r.json()))
print('*************************************************')
for key, value in r.headers.items():
    print(key, '=>', value)