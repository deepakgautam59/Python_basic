import requests
import json
url="https://v2.jokeapi.dev/joke/any"
data=requests.get(url)
if data.status_code==200:
    print(data.json())