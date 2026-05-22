import urllib.request
import json

with urllib.request.urlopen('https://api.github.com/users/codewithharry') as response:
    data = response.read().decode('utf-8')
    user = json.loads(data)
    print(user)

# import requests

# r = requests.get('https://api.github.com/users/codewithharry')
# user = r.json()  # requests can parse JSON directly
# print(user)
