import requests
import json

response = requests.get('http://api.are.na/v2/channels/computer-graphics-jjpidmjvw40')

output = response.json()

print(output['title'])