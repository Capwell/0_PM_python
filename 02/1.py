import requests

response = requests.get("https://swapi.dev/api/starships/9/")

print(response)
print(response.text)
print(type(response.text))
