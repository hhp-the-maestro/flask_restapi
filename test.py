import requests
import json

base = 'http://127.0.0.1:5000/'

data = [
{'likes': 106, 'name': 'hhp', 'views': 101001}, 
{'likes': 168, 'name': 'hari', 'views': 582}, 
{'likes': 1600, 'name': 'hara', 'views': 18360}
]
'''
for i in range(len(data)):
	response = requests.put(base + 'video/' + str(i), data[i])
	try:
		print(response.json())
	except:
		print(response)
 
input()

response = requests.delete(base + 'video/0')
print(response)
input()

onse = requests.get(base + 'video/5')
print(response.json())
'''
response = requests.patch(base + 'video/2', {})
print(response.json())