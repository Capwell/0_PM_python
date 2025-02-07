import sqlite3
import requests

response = requests.get("https://swapi.dev/api/starships/")
results = response.json().get("results")

starships = []
for i in results:
    starships.append((i.get("name"), i.get("passengers")))

print(starships)
connect = sqlite3.connect("starships.sqlite")

cursor = connect.cursor()

cursor.executemany(
    "INSERT INTO ships VALUES(?, ?);",
    starships

)

connect.commit()
connect.close()
