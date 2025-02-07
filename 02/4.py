import sqlite3

connect = sqlite3.connect("starships.sqlite")

cursor = connect.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS ships(name TEXT, passenger TEXT);"
)

connect.commit()
connect.close()
