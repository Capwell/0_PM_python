import sqlite3

connect = sqlite3.connect("starships.sqlite")

cursor = connect.cursor()

cursor.execute(
    "INSERT INTO ships VALUES(?, ?);",
    ("CR900 corvette", "600")

)

connect.commit()
connect.close()
