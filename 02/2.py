import requests

response = requests.get("https://swapi.dev/api/starships/9/")


print(response.json())
print(response.json().get("name"))
