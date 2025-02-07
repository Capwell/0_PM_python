import sqlite3

connect = sqlite3.connect("starships.sqlite")

cursor = connect.cursor()

cursor.execute(
    "SELECT * FROM ships;"
)

print(cursor)
for i in cursor:
    print(i)


connect.commit()
connect.close()
