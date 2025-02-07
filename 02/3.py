import requests

response = requests.get("https://swapi.dev/api/starships/")


# print(response.json())
# print(response.json().get("results"))
# results = response.json().get("results")

# for i in results:
#     print(i.get("name"), i.get("passengers"))

# starships = {}
# for i in results:
#     starships[i.get("name")] = i.get("passengers")

# print(starships)
